---
source: notebooklm_export
file_id: "068"
filename: "068_airis_rc_part_3.txt.txt"
doc_type: "reference_card"
product: "AIRIS"
content_type: "txt"
language: "en"
guide_summary: "This comprehensive documentation details the functionalities and integrations of AIRIS, an Intelligent Customer Data Platform. A core theme is the ability to connect AIRIS with various external services—such as **Google Ads, Meta Ads, BigQuery, HubSpot, and Salesforce**—to centralize and enrich customer data. The platform heavily utilizes **Automations**, including real-time **Triggers** based on user events and **Scheduled Batches** that run at set intervals for actions like report exports and "
guide_keywords: "Integrations, Scheduled Batches, Retargeting, Report Sharing, Data Discrepancies"
---

# 068 airis rc part 3

Google Ads [1]

https://docs.airis.appier.com/docs/retargeting-google-ads



Goal and action optimization: Select the Goal category for this action.

Conversion name: Input a name for the conversion event.

After completing the settings, click the Use Google Tag Manager tab. Copy the Conversion ID and Conversion label for the conversion event you just created. These details will be required to create the AIRIS trigger in the next step.

Create a trigger on the AIRIS console. Navigate to the Automate section and go to Triggers, then click + New Trigger.

Click Add Target and select Remarket to your users.

Under Conversion ID and Conversion Label, input the details for the Google Ads conversion action you created in the previous step. After completing all the trigger settings, click Create.

In Google Ads, go to Tools > Shared library > Audience manager. Click + to add an audience segment, then select + Website visitors.

Next, complete the following settings:

Segment name: Enter a name for the segment.

Segment members: Select Visitors of a page with specific tags.

Tags: Select the AIRIS conversion action you created.

Click Create segment.

Updated 23 days ago



Scheduled Batches [0]

https://docs.airis.appier.com/docs/scheduled-batches



Scheduled batches allow you to create automations based on your reports. While scheduled batches are similar to triggers in functionality, scheduled batches run on set time intervals rather than being triggered by a user event.

For example, you can use scheduled batches to automate the following actions on a set schedule:

Export a profile report to Google Sheets.

Bulk subscribe users in a profile report to a MailChimp mailing list.

Export an activity report to Amazon S3.

📘NoteEach project can contain a maximum of 50 scheduled batches. If you need more than 50 scheduled batches, please contact Appier Support (ess_support@appier.com).

📘Beta featureScheduled batches for activity reports is a beta feature. Contact your customer success manager to learn more.

Scheduled batches update data incrementally. Each batch only includes new data that was added after the previous batch completed.

Timeframe settings:

Setting your report timeframe's ending date to Today will ensure new data is exported by the scheduled batch every day.

Up to 100 million records can be included in a single batch. Note that if you're creating a scheduled batch for an activity report for the first time, all report records will be new, so you may need to decrease the report's timeframe for the first batch to avoid exceeding this limit.

Create a report to use in the scheduled batch. The following report types are supported:

Profile reports

Activity reports

From the navigation bar, click Automate, then go to Scheduled Batches and click + New Scheduled Batch.

Complete the following settings:

Report: Select the source report.

Frequency: Select the run frequency. For profile reports, consider the timeframe of the report and the interval for the scheduled batch—for example, if your report uses a relative timeframe of one week, you'll want the scheduled batch to run weekly.



Scheduled Batches [1]

https://docs.airis.appier.com/docs/scheduled-batches



Limit: Set the maximum number of records to use in a single batch. For example, if you're using a profile report to create an AIQUA segment, a limit of 30 will ensure the segment won't exceed 30 users.

Add one or more target actions to execute every time the scheduled batch runs.

Ensure that all target actions are toggled on, then click Create to finish creating the scheduled batch.

Updated 23 days ago



Sharing Reports

https://docs.airis.appier.com/docs/sharing-reports



Once you create your report, it's not going to be very useful if the right people don't see it. That's why it's important to always share your report to the correct groups. Reports can be shared via:

Tags

Snapshots

You can tag reports to organize them for easy access. Tags can be shared with groups, so everyone in that group has access to all the reports with that tag.

To create a tag, navigate to Analyze, and in the left menu, scroll to the My Tags section and click the + button.

Once you've created a tag, add it to your reports by opening the report, clicking on the three vertical dots, then clicking Tag from the dropdown menu.

To share a tag with a group, go to the tag's details page, click the three vertical dots, then click Share. Check the boxes next to the groups you'd like to share this tag with.

A snapshot is a view of the report at the time when the snapshot was created. Snapshots can be shared via public URL, allowing you to easily share reports with anyone—including external teams that aren't using AIRIS. The snapshot URL will link to a snapshot of the report at the time the snapshot was created.

📘NoteEditing the report won't change previously-created snapshots.

To retrieve the snapshot URL, open a report, click the three vertical dots, and click Snapshot to copy the URL.

Updated 23 days ago



Report Subscriptions

https://docs.airis.appier.com/docs/subscribing-to-reports



In AIRIS, subscriptions allow you to receive emailed reports directly to your inbox. You can easily subscribe to any report type and select how often you'd like to receive it.

When you are viewing a report, click the Subscribe button on the top right, then select the interval at which you'd like to receive the report by email: Daily, Weekly, or Monthly.

Click View Subscriptions to see a list of all your active subscriptions.

Updated 23 days ago Sharing ReportsReport URL VariablesTable of Contents

Overview

How to subscribe



Report URL Variables [0]

https://docs.airis.appier.com/docs/url-variables



Create URL links to reports that include custom variables to inject into report filters.If you use an external CRM or you would like to create links to reports, you can create custom variables in the report URLs to inject into the report constraints. For example, say you want to dynamically create links for your sales team to show the history of a particular user who does a particular action.

First, we need to create a report and use it as a template. Here we created a new Activity Report and saved the report. The Performed by, Events, and Columns are set up based on what we want in the report, but specific constraints or filters are not configured yet.

Next, copy the report link. Now you can edit the URL and add the custom variables to be used in the filtering of the report. In this example, let's create a link with two variables: var.email and var.category. The link will look something like this:

https://airis.appier.com/project/myshop.com/activity/njsino4cl0?var.email=&var.category=

The part added to the link is ?var.email=&var.category=. You must name the variables in this format: var.name= where the var. is needed before the variable name. Once you're done editing the URL, go to the URL you've created in your browser. You can now select the variables in your report filters.

In the Performed by filter, we can select the created variable for var.email.

Click the event and add an event constraint to include the other created variable var.category. This allows us to filter results based on the product category.

Save the report. Now you can inject any values into those links and the report will automatically filter on the variables. We can dynamically create links in the CRM for the sales team so they don't have to manually configure the report.

In the example below, we added values for the two variables to create a report link that only includes product_added_to_cart events where the email is "jane@example.com" and the product category is "beauty".



Report URL Variables [1]

https://docs.airis.appier.com/docs/url-variables



https://airis.appier.com/project/myshop.com/activity/njsino4cl0?var.email=jane@example.com&var.category=beauty

Now, using this link, the report is filtered based on the values for the custom variables.

Updated 23 days ago



Integrations [0]

https://docs.airis.appier.com/docs/integrations



Many companies have snippets of customer interaction information scattered all over the place. From email automation and live chat to CRMs and support platforms, companies interact with and engage their customers in many ways from many different sources. To get a full picture of customer engagement across all of these different tools, teams spend much of their time looking at siloed snapshots and piecing them together into a full picture of their users.

AIRIS Integrations solves this industry-wide problem by instantly connecting AIRIS to other tools in a matter of seconds. This greatly enriches the data from tracking custom events and identifying customers on the website or application with AIRIS’s SDKs.

Integrations’ tight connections with CRMs, help desks, email automation systems, live chat tools, and more, allow you to take control of your data, centralizing it in a single platform.

AIRIS’s Integrations are set up in two parts:

Snippets give you multiple SDKs to install on the website or app so the user can start tracking events with AIRIS. Snippets include SDKs for Javascript, Android, iOS, Node.js, Python, Java, and PHP.

Integrations – Integrations are the external Apps that you can connect to AIRIS in just a few clicks.

Integrations are super easy to set up; most of them can be installed with just a few clicks. You can find Integrations under the Configure tab on the dashboard. Once installed and authorized (where necessary), the different apps instantly sync events from within the given tool to AIRIS. You will be able to use these events immediately throughout AIRIS.

For example, one can leverage Integrations’ events as a segmentation filter option in the Profile Reports. In addition, you can use them to set up a step in the Journey report.

In addition to bringing data into AIRIS, some apps also enable you to trigger actions in other tools to create more personalized and relevant customer experiences.



Integrations [1]

https://docs.airis.appier.com/docs/integrations



Other apps allow automated scheduling of important reports to different tools so that all teams can easily access important reports from a single location without requiring different authorizations or permissions in the different products.

First, go to the Configure section in AIRIS’s navigation bar. Select the Integrations icon from the sidebar to access the applications. Click on the app of interest to set it up. Click the Connect or Install tab and follow the instructions to authorize the app according to the permissions of the tool.

Once installed and authorized, select the Setup page to ensure that the tracking of interest is selected. Different apps will allow for enabling or disabling certain features from this page, so be certain to check for more information.

After installation, any application events automatically sent or defined by the setup will instantly become available in segmentation filters and Segments throughout AIRIS’s reports as well as event filters in Journeys, Trends, and Retention reports.

To use Integrations Trigger actions, go to the Automate section, and select Triggers on the sidebar. Configure the conditions that you wish to trigger the action for, select an App Action from the Add Target options, and define the conditions appropriately. Click Create to save your setup.

To schedule report uploads to the tool of interest, choose to upload your Analytics reports to the app target by selecting the tool name from the scheduled tasks options. Configure the specific destination you want to send the reports to and the format that you’d like the report to be sent in. Click Create to save your setup.

Integrations are unique in their ability to bring all of the data together into a single hub, where you can then analyze events and automate actions based on a comprehensive picture of their customer interactions, responses to email campaigns, onsite surveys, chat efforts, and so on.



Integrations [2]

https://docs.airis.appier.com/docs/integrations



Let’s consider a few examples; Using the Zendesk App, a SaaS company may set up a trigger to upgrade ticket status when a customer experiences any kind of error. The recently submitted ticket of a high-profile customer could be automatically upgraded to urgent, allowing for faster response times.

Another example might be an online game company, whose support team closely monitors player activity for any potential abuse. They might make good use of the HipChat app, which installs a trigger action that allows the user to post custom messages to the HipChat channels when a given event occurs. This company might set up a trigger to alert the moderators immediately when there may be questionable activity.

In another example, a sales representative might schedule an upload for a weekly report on new signups, which is automatically shared with product and sales teams, or upload a monthly report on Google Ads performance, to be shared with the marketing team and an outside agency.Updated 23 days ago



Log in | AIRIS

https://airis.appier.com/project/~/configure/integrations



Password



AIQUA

https://docs.airis.appier.com/docs/integration-aiqua



Integrating your AIQUA account allows you to:

Export profile reports to create AIQUA segments

Trigger AIQUA web push campaigns

Before adding the connection to your AIRIS account, retrieve the following details for your AIQUA app ID and API token from the AIQUA dashboard. These details are required for a later step.

From the AIQUA dashboard, click your account name in the bottom-left corner, go to Account Settings, then look under General Settings.

In the top menu, go to Configuration, then from the left menu, go to Install > Integrations.

From the list of services, click AIQUA. Click Connect, then click + New connection.

In the configuration panel, enter the following details:

The name of the connection

Your AIQUA app ID and API token

Click Connect to AIQUA to complete the connection process.

Updated 23 days ago



BotBonnie

https://docs.airis.appier.com/docs/integration-botbonnie



Integrate with BotBonnie to:

Export profile reports to BotBonnie segments

Create triggers that open WebChat modules to automatically start conversations with site visitors

Work with your customer success manager to integrate your website with the BotBonnie WebChat SDK.

Retrieve your BotBonnie bot's API token. From the BotBonnie console, go to Settings > Advanced. Your API token will be visible under API Credentials > API TOKEN.

In the top menu, go to Configuration, then from the left menu, go to Install > Integrations.

From the list of services, click BotBonnie. Click Connect, then click + New connection.

In the configuration panel, enter a name for the connection and your BotBonnie bot's API token.

Click Connect to BotBonnie to complete the setup process.

Updated 23 days ago



BigQuery [0]

https://docs.airis.appier.com/docs/bigquery



Google BigQuery is a powerful data warehouse service offered by Google Cloud Platform (GCP). It's designed to handle large amounts of data quickly and efficiently, making it a popular choice for businesses looking to store and analyze their data.

AIRIS's BigQuery integration allows you to seamlessly combine data from BigQuery with real-time data from web, mobile, and other sources. This integration helps you create a holistic view of your customers, enabling more informed decision-making and personalized marketing strategies. The AIRIS BigQuery integration allows you to:

Merge data from other sources

Unify the data to have a holistic view

Activate users in paid ads or using marketing automation tools to deliver personalized campaigns

In this guide, we'll walk you through the process of connecting BigQuery with AIRIS. You'll learn how to:

Set up the connection

Map data between the two platforms

Ensure your BigQuery data is continuously updated in AIRIS

👍Best practices and guidelinesSee BigQuery Integration Best Practices for guidelines on setting up and organizing your data to get the most out of this integration.

Before integrating Google BigQuery with AIRIS, you'll need to complete a some prerequisite steps to obtain a BigQuery Dataset ID and GCP Service Account Key before adding the BigQuery connection to your AIRIS project.

Here are the steps you need to complete to obtain the GCP Service Account Key and BigQuery Dataset ID:

Create a project and enable BigQuery

Create a GCP service account for AIRIS

Create a GCP service account key

Upload data to the service account

Retrieve the dataset ID

If your data team has already completed these steps, please obtain the BigQuery Dataset ID and Service Account Key from them. Alternatively, you can reach out to Appier Support (ess_support@appier.com) for assistance.



BigQuery [1]

https://docs.airis.appier.com/docs/bigquery



If you haven't done so already, create a project in Google Cloud Platform and enable the BigQuery service. This is where your data will be stored and analyzed. Complete the following steps to create a project and enable the BigQuery API.

Open the Google Cloud Console and create a new project or select an existing one.

Enable the BigQuery API for your project.

Go to the API & Services page

Click + Enable APIs and Services

Search for "BigQuery API".

Click on BigQuery API and then select Enable.

The service account will allow AIRIS to access your BigQuery data securely.

In the Google Cloud Console, navigate to the IAM & Admin, then go to Service Accounts.

Click + Create Service Account, fill in the service account details, then click Create and Continue. In the next screen, click Done to complete the creation process.

Verify that the account was successfully created. You should now see your new service account listed in the Service Accounts section.

This key will be used to authenticate your service account with AIRIS.

On the Google Cloud Console, click on the service account you just created.

Go to the Keys tab, click Add Key, and select Create New Key.

For the Key Type, choose JSON. Click Create to finish the process.

A JSON file containing your private key will be downloaded. Keep this file secure, as it will be used to connect BigQuery to AIRIS.

Upload your data to the service account you've created for AIRIS. This data will be used by AIRIS for analysis and insights.

Go to your BigQuery project in the Google Cloud BigQuery console.

Under the Explorer section, + Add. Add your dataset to the project. If you're unsure about how to prepare the right dataset, please reach out to your data team or Appier Support for guidance.

Obtain the dataset ID from your BigQuery project. This ID is essential for connecting your BigQuery data to AIRIS. After your data has been uploaded, you can retrieve the dataset ID.

Click on the dataset you've uploaded in the BigQuery console.



BigQuery [2]

https://docs.airis.appier.com/docs/bigquery



Click on the dataset you've uploaded in the BigQuery console.

Under the Dataset info section, look for Dataset ID. Save this ID, as it will be used later to establish the connection with AIRIS.

You've successfully set up your BigQuery project, created a service account for AIRIS, and retrieved the dataset ID. Now, it's time to connect AIRIS with BigQuery.

Log in to the AIRIS console, navigate to Configure > Connections, then click + New Connection.

Enter the following connection details.

Connection Name: Choose a name for your connection. This can be anything that helps you identify the connection later.

Dataset ID: Enter the dataset ID you retrieved earlier.

Service Account Key: Enter the Service Account Key you created earlier.

Under the Configure section, go to Tasks, then click + New Task.

In the Source Configuration, under Table, click Select a connection and select your BigQuery connection. Next, click Select a table dropdown and choose the BigQuery table that you want to sync with AIRIS.

Configure the task settings based on your specific data set. For detailed instructions on configuring tasks, refer to the e-commerce transaction table example or the connections guide .

📘Selecting the data typeWhen creating the task, ensure that you select the correct data type depending on what information the BigQuery table contains. The following options are available:

Identify (user properties): Identifying information such as company names, emails, first and last names, locations.

Track (event data): Anything a user does that contains a timestamp. These can be events like payments, signups, or subscription updates.

Data Store: Data that will be used to enrich existing data in user profiles.

Once the task is configured, the data from the selected BigQuery table will begin mapping to the corresponding data table in AIRIS.



BigQuery [3]

https://docs.airis.appier.com/docs/bigquery



In this example, we'll create a task to map the transaction.transaction_table, which contains information about customer transactions on an e-commerce website. The following table provides a description of each column:

Column nameDescriptionorder_timeA timestamp indicating when the order was completed.user_idThe unique identifier of the user who placed the order.order_idThe order's unique identifier.total_product_countThe total number of products included in the order. This is the sum of the product_count field of each item in the order.total_amountThe total amount of money spent on the order. This is the sum of the amount field for each item in the order.

Since this table contains event data, select Track for the data type. In addition, complete the following settings under Map User Events:

Select & Map User ID: Select the order_time column, since this is the table's unique identifier.

Event Name: Enter the event name "checkout_completed".

Timestamp: Select order_time, since this is the column containing the event's timestamp.

Event properties: Map order_id, total_product_count and total_amount to the corresponding event properties of the checkout_completed event.

After the settings have been completed and task is activated, data from the selected BigQuery table will begin mapping to the corresponding data table in AIRIS.Updated 23 days ago



BigQuery Integration Best Practices [0]

https://docs.airis.appier.com/docs/bigquery-integration-best-practices



As an Intelligent Customer Data Platform, AIRIS has the capabilities to ingest and unify different kinds of data. Before ingesting data into AIRIS, it's important to follow these best practices.

Create a dedicated service account for AIRIS.

Follow BigQuery table naming guidelines.

Design your data architecture and data tables on BigQuery to ensure that data onboarded to AIRIS is ready for unification and further analysis.

For a streamlined connection with BigQuery, we advise setting up a dedicated service account for AIRIS. For detailed instructions, see Create a GCP service account for AIRIS.

By following these guidelines, your data will be organized efficiently in BigQuery, allowing for smooth integration and the full utilization of AIRIS's analytics and personalization features for your marketing campaigns.

🚧ImportantIf BigQuery table names don't conform to the following guidelines, the AIRIS BigQuery integration won't function.

Ensure that your BigQuery tables adhere to the following naming guidelines:

Don't use uppercase letters.

Don't use hyphens ("-").

Exclude the word "order" to prevent SQL command conflicts.

For optimal analysis of customer data in AIRIS, we recommend organizing your data into a flat format rather than relying on on-the-fly joins of different tables to enhance user experience and efficiency. In this section, we'll share the best practices of table design for the e-commerce or retail industry.

Typically, an e-commerce or retail data set comprises the following tables:

Customer table

Transaction table

Transaction details table

Product table

The customer table provides a snapshot of each customer. When configuring the task, specify the Data Type as Identify.



BigQuery Integration Best Practices [1]

https://docs.airis.appier.com/docs/bigquery-integration-best-practices



The customer table provides a snapshot of each customer. When configuring the task, specify the Data Type as Identify.

ColumnDescriptionData typeRequiredcustomer_idA unique identifier assigned to each customer. This is used to distinguish individual customers in the data set.stringYesfull_nameThe customer's complete, including both first and last names.stringNofirst_nameThe customer's first name or given name.stringNolast_nameThe customer's surname or family name.stringNoemailThe customer's email address.stringNocityThe city where the customer resides. This can be useful for regional analysis or marketing.stringNobirthdayThe customer's birth date, typically in the format YYYY-MM-DD. This can be used to calculate age or for birthday-related promotions.timestampNophone_noThe customer's telephone number, used as a contact point for communication or customer service.stringNojoin_dateThe date when the user first signed up or became a customer. It is typically recorded in a YYYY-MM-DD format. This information is crucial for analyzing customer lifecycle, tenure, and understanding trends in customer acquisition over time.timestampNo

The transaction table records each customer transaction. When creating a task, specify the Data Type as Track.

ColumnDescriptionData typeRequiredorder_timeThe exact date and time when the transaction was completed.timestampYescustomer_idA unique identifier assigned to each customer. This is used to distinguish individual customers in the data set.stringYesorder_idThe order's unique identifier.stringYestotal_product_countAn aggregate count of all products included in a single order. Note that this represents the sum of all products, including multiples of the same type.integerNototal_amountThe cumulative monetary value of all items in a particular order.floatNo

The transaction details table contains specific details about each transaction. When configuring the task, specify the Data Type as Track.



BigQuery Integration Best Practices [2]

https://docs.airis.appier.com/docs/bigquery-integration-best-practices



ColumnDefinitionData typeRequiredorder_timeThe exact date and time when the transaction was completed.timestampYescustomer_idA unique identifier assigned to each customer. This is used to distinguish individual customers in the data set.stringYesorder_idThe order's unique identifier.stringYesproduct_idThe product's unique identifier. This ID is used to reference and distinguish individual products in the dataset.stringYesitem_sequenceA numerical value indicating the order in which products appear within a transaction. This sequence can be used to track the order of product selection in a customer’s purchase process.stringNoproduct_countThe quantity of a particular product ordered within a single transaction. This count reflects how many units of product_id were purchased.integerNoamountThis represents the total cost associated with the product_count of a single product_id in a transaction. It is typically a numeric value that can include decimals to represent cents.integer, floatNo

The product table lists details for each product. When configuring the task, specify the Data Type as Data Store.



BigQuery Integration Best Practices [3]

https://docs.airis.appier.com/docs/bigquery-integration-best-practices



The product table lists details for each product. When configuring the task, specify the Data Type as Data Store.

ColumnDescriptionData typeRequiredproduct_idThe product's unique identifier. This ID is used to reference and distinguish individual products in the dataset.stringYesproduct_categoryThe classification or grouping that the product belongs to, based on its type or function. This helps in organizing products into hierarchical groups and is often used for analysis of product performance by category.stringNoproduct_nameThe official name of the product, which is used for identification and marketing purposes. It’s the name that customers would see on a website or in a catalog.stringNobrandThe name of the manufacturer or company that owns the product. The brand serves as a trademark and can be a determinant of quality and customer loyalty.stringNopriceThe cost at which the product is sold to the customer. This is often a numeric value that can vary depending on the market and is crucial for sales analysis and price optimization studies.integer, floatNodescriptionA detailed explanation of the product, including features, specifications, and potential uses. This descriptive text provides insight into what the product is and can be used to match product offerings with customer needs.stringNoUpdated 23 days ago



AdWords Auto-Tagging [0]

https://docs.airis.appier.com/docs/adwords-auto-tagging



Letting AdWords and AIRIS work together on campaign reporting with utm data.Google AdWord's auto-tagging makes tracking your AdWords campaigns very easy! But in order to allow it to work with analytics solutions other than Google Analytics, you will have to do a few extra steps. Luckily, doing these steps will also give you some extra power and customizability in how you define and report on your campaigns.

Some concepts here may require some familiarity with how urls work and specifically, the query part of the url.

AdWords has a section in its interface called the "Shared Library." This tab contains account-level settings and defaults that can be used in multiple campaigns. To set up UTM Auto-Tagging to work with AIRIS, you need to tell AdWords to send the campaign data in the universal utm_ format, rather than encoded in the gclid that only Google Analytics can read. Here's how:

Navigate to the Shared Library, and then to the "URL options." Note the URL options are not available from manager accounts, only on an individual ad account level.

Turn on Auto-Tagging by clicking the edit button, and selecting the check box. This will tell AdWords to include query parameters to help identify campaigns, etc. with each pageview.

Create your tracking template. This is creating a template for the urls to which AdWords directs people who click your add. Each campaign may have its own url that a clicked ad will lead to, and using this template will allow AdWords to automatically add other information to the query part of the URL.

The concept here is that you are going to tell AdWords that when creating the url for the link in one of your adds, put it through this template on a per-ad-view basis so that each click gets the right metadata or campaign information in the query.



AdWords Auto-Tagging [1]

https://docs.airis.appier.com/docs/adwords-auto-tagging



So the template will look something like: {base url you provided} ?(begin query)utm_campaign={campagin name}&utm_medium={campaign medium} and will form a recipe for AdWords to add in the data. When creating the url, the parts in the {} braces (called Value Track Parameters, more here) will be exchanged for actual values, while the parts outside will be included literally. A full list of available Value Track parameters is available here.

Here is an actual functional example. You can start with copying this into the template in AdWords, and then you can adjust it as necessary after testing to meet your goals:

{lpurl}?utm_campaign={campaignid}&utm_source=AdWords&utm_medium={network}&utm_content={creative}&utm_term={keyword}

Note that {lpurl} means the target url for the ad, which you provide to google when building a particular ad--so this will be replaced with the actual page on your site where you want people to go.

You can click "test" and it will run the template and create a test url that you can click to go to one of your pages--usually it will just use the homepage. If you click the test link and load your page, you should see the utm parameters in the url address bar, and you should also see a new pageview action in your profile in AIRIS, with campaign data associated with it right there in the interface. AdWords will also note any errors it detects, and you can use this to make sure you are getting all the right campaign data and utm parameters you want.

📘Pro Tip:You can create custom ValueTrack tags to carry things like human-readable campaign name. For more info on this, see this AdWords Article.Updated 23 days ago



Meta Ads

https://docs.airis.appier.com/docs/retargeting-meta-ads



日本語ホーム한국어홈中文首頁



Meta Ads (Pixel) [0]

https://docs.airis.appier.com/docs/meta-ads-pixel



The following guide describes how to set up retargeting on Meta Ads Manager by creating a trigger that sends your website users' events to Meta. This trigger works for unidentified users without emails, but the event must be triggered by a client-side tracking event such as a page view.

Retrieve your Meta Pixel ID

Create an AIRIS trigger

Create an audience in Meta ads

(Optional) Create a lookalike audience in Meta ads

The pixel ID will be required to create the AIRIS trigger.

In Meta Ads Manager, navigate to Events Manager, then go to Data Sources.

Copy the ID of the pixel you'd like to use.

Create a trigger on the AIRIS console. Navigate to the Automate section and go to Triggers, then click + New Trigger.

Click Any Event to select when to trigger the event to Meta. If you want the event to be sent to Meta when the users do any event, select Any Event.

Click Add Target and select Track Custom Events in Facebook.

Under Pixel ID, input the pixel ID you retrieved in the previous step.

Under Event Name, add an event name. This is the event name you will see on Meta. After completing all the trigger settings, click Create.

To see if the event is being sent to Meta successfully, go to Meta Events Manager, navigate to Data Sources, and click the pixel you used. Trigger the event and you should see the event listed under the Events section on Meta.

In Meta Ads Manager, navigate to Audiences. Click the Create audience dropdown and select Custom audience.

In the settings window, under Your sources, select Website.

Next, select the custom event you'd like to use, name the Meta ads audience, and then click Create audience.

The newly created audience will be visible in the Audiences page, and its ID can be found under the Audience ID column.

In Meta Ads Manager, navigate to Audiences. Click the Create audience dropdown and select Lookalike audience.

Under Select your lookalike source, input the name of the custom segment you created. Complete the remaining settings, then click Create audience.



Meta Ads (Pixel) [1]

https://docs.airis.appier.com/docs/meta-ads-pixel



The newly created audience will be visible in the Audiences page, and its ID can be found under the Audience ID column.

Updated 23 days ago



Meta Ads (Conversions API) [0]

https://docs.airis.appier.com/docs/meta-ads-conversions-api



📘Beta featureThe Meta Conversion API integration is a beta feature. Contact your customer success manager to learn more.

AIRIS's Meta Conversions API integration allows you to send web, app, and offline events directly to Meta using server-to-server tracking, offering more flexibility and better data accuracy without being impacted by browser tracking restrictions. Use AIRIS triggers to send events to Meta based on user actions, and then create custom audiences and lookalike audiences in Meta based on those user events to deliver relevant ads to users.

Complete the following steps to set up the Meta integration:

Add Appier as a business partner in Meta Ads Manager

Retrieve your Meta Pixel ID

Create an AIRIS trigger

Check that events are successfully sent via Conversions API

Monitor Conversions API events

Create an audience in Meta ads

(Optional) Create a lookalike audience in Meta ads

Grant Appier (business ID1546643532281115) access to the following asset types.

Datasets

Apps (only required if you'll be sending app data)

After giving Appier access to your business assets, contact Appier Support to complete the setup process.

The pixel ID will be required to create the AIRIS trigger.

In Meta Ads Manager, navigate to Events Manager, then go to Data Sources.

Copy the ID of the pixel you'd like to use.

Create a trigger on the AIRIS console. Go to Triggers and click + New Trigger.

Click Any Event to select when to trigger the event to Meta. If you want the event to be sent to Meta when the users do any event, select Any Event.

Click Add Target and select Track Custom Events in Meta (Conversions API).

Under Pixel ID, input your pixel ID.

Under Event Name, add an event name. This is the event name you will see on Meta. After completing all the trigger settings, click Create.

Under Event Properties, User Information, and Other Parameters, map Meta Custom Data parameters to AIRIS parameters by selecting a Meta parameter from the dropdown and providing the name of the corresponding AIRIS parameter.



Meta Ads (Conversions API) [1]

https://docs.airis.appier.com/docs/meta-ads-conversions-api



Event Properties: Map Meta Custom Data parameters to AIRIS event parameters.

User Information: Map Meta Customer Information parameters to AIRIS user attributes. Meta requires at least one type of user information to match users.

Other Parameters: Map additional parameters as required. Note that AIRIS automatically includes event_time, action_source, and the required app data parameters, so you don't need to manually add mappings for these parameters.

👍Tip

If you'd like to add Meta parameters, you can refer to the Meta Conversions API server event reference for detailed descriptions of each parameter.

See Meta’s best practices for increasing matching quality when configuring Meta parameter mappings.

Click Create to save the trigger.

After completing the setup steps and creating an AIRIS trigger, check that events are being correctly sent.

Go to Meta Events Manager, navigate to Data Sources, and click the pixel you used.

Trigger the event and you should see the event listed under the Events section on Meta.

In Meta Events Manager, monitor your Event Match Quality Score—we recommend aiming for a score of at least 6/10.

To improve a low score, you can:

Import first-party data to AIRIS, like ClickID and the _fbc and _fpc parameters.

Send additional parameters recommended by Meta to see additional conversions reported.

In Meta Ads Manager, navigate to Audiences. Click the Create audience dropdown and select Custom audience.

In the settings window, under Your sources, select Website.

Next, select the custom event you'd like to use, name the Meta ads audience, and then click Create audience.

The newly created audience will be visible in the Audiences page, and its ID can be found under the Audience ID column.

In Meta Ads Manager, navigate to Audiences. Click the Create audience dropdown and select Lookalike audience.

Under Select your lookalike source, input the name of the custom segment you created. Complete the remaining settings, then click Create audience.



Meta Ads (Conversions API) [2]

https://docs.airis.appier.com/docs/meta-ads-conversions-api



The newly created audience will be visible in the Audiences page, and its ID can be found under the Audience ID column.

Updated 23 days ago



Amazon S3

https://docs.airis.appier.com/docs/integration-amazon-s3



The AIRIS + Amazon S3 integration enables you to securely transfer your customer data and analytics to and from the Amazon S3 cloud storage solution. With this integration, you can automate the process of exporting and importing your data to and from your S3 bucket in a secure and reliable way.

For example, you can use this integration to:

Transfer your customer analytics to your company's data warehouse for further analysis

Back up your data to a secure offsite storage solution

Share data with partners or other departments within your organization

This integration provides you with flexibility and control over your data, enabling you to manage it according to your specific needs and requirements.

Please note the following behaviors and limitations for S3 tasks.

Batch size (Advanced settings)

Cursor (Map User Events)

Task failure retry timeout

Maximum of 300,000 records per batch: If you set a batch size larger than 300,000 records, only the first 300,000 records will be imported in a single batch, and the subsequent batch will begin importing from where the previous batch ended.

Maximum total size of 153 MB per batch: If the size of the batch exceeds 153 MB, only the first 153 MB of data will be imported in a single batch, and the subsequent batch will begin importing from where the previous batch ended.

The S3 connector doesn't support cursors. Configuring this setting will not affect the task.

The retry timeout for Amazon S3 task failures is 30 minutes. If a task encounters a failure before completing a batch the task will retry again after 30 minutes. The import will begin from the last point of failure, ensuring that no data is missed.Updated 23 days ago



Clearbit [0]

https://docs.airis.appier.com/docs/clearbit



Pointers for setting up and using the Clearbit AppConnect IntegrationsClearbit is a data enrichment partner. Clearbit can enrich your profiles based on email, and IP address. The Clearbit functionality is separated into two apps. Basic email address-based enrichment is available to all AIRIS and Clearbit customers, while the ip-address-based enrichment from Clearbit's Reveal product, is a separate premium integration, and is only available to enterprise AIRIS users.

Clearbit Reveal is quite simply, a game changer. The prototypical use case is more or less the following: A brand new user comes to your website. You send their IP address to Clearbit Reveal. Clearbit responds with company information. You score the company as a lead, and determine a specific personalized experience, or even personalized chat pop-up to show the brand new user to your site. For example, a Drift Message saying: "Hello! I see you work at AIRIS! Because you are a B2B SAAS company, I think My Product would be a great fit for you. How about a personal product tour?" Similarly, you could trigger Optimizely to show a given experiment, or tell Zendesk to prioritize all support and information request tickets from this user.

Here are the steps to create the example trigger from above, using Clearbit data to inform a Personalized Drift live chat message to new anonymous users to your marketing site.

Pre-requisites:

Make sure Drift and Clearbit Reveal are both installed and authorized in AIRIS.

Make sure Drift is properly installed on your website. See their docs for help.

Create your trigger: In AIRIS, go to Automations > Triggers and create a new trigger.

Define Your trigger:

Define the user segment (the criteria a person must meet to cause this trigger to fire.) In this case, the user segment will be something like: "People who DID: "clearbit.identified_by_ip" AND who ARE: "clearbit_company.name exists, AND clearbit_company.customer_model is 'B2B' AND clearbit_company.model is 'SAAS' "



Clearbit [1]

https://docs.airis.appier.com/docs/clearbit



Determine when this trigger should fire for people who match the above criteria. We want this to fire on a pageview event, because on your website is where using a tool like Drift makes sense. (We couldn't fire a drift message based on, say, and "email received" event, can we?) So we will set up the trigger to "Fire When: 'pageview' "

Determine the frequency: We probably don't want this to fire constantly on every pageview event, because that would be annoying. Let's say "once per visit" so that once they dismiss the chat bubble or leave the page, they will not be shown the same chat again immediately, but rather on their next session (the next time they visit our site.)

Click "save" to make sure all these settings are saved

Set up your Trigger Action:

Find the Drift Trigger Action called Show the Welcome or Away Message in the menu.

Customize your message in the trigger actions settings. You can use AIRIS templates in the message content as well. In this case, our message will look like:

"Hello! I see you work at ${visitor.clearbit_company.name}. Because you are a B2B SAAS company, I think My Product would be a great fit for you. How about a personal product tour?"

Click "save" again to save the trigger action settings.

Updated 23 days ago



HubSpot [0]

https://docs.airis.appier.com/docs/hubspot



Using HubSpot to host your website? Getting started with website tracking is easy!

1) You'll need to install the AIRIS Javascript Tracking Snippet to the Site Header HTML. You can find HubSpot's instructions here for adding to individual landing pages and where to locate the advanced tracking feature.

2) For the integration to function properly, you'll need AIRIS's basic Javascript tracking for tracking page views and you'll need to add AIRIS's identify tracking to identify the users on your site. This allows AIRIS to generate one customer profile for each individual and populate that profile with all the various behavioral data points you're collecting.







This a two-part process to successfully track HubSpot forms in AIRIS.

###1. Data Loader Method

Using the Data Loader will allow you to bring in historical data and will not require any coding. You can create the connection under the Connections in the Data Loader section. Once you create the connection, you can create the Tasks to pull in the data.

Follow the below example of how to set up the Task. Use the 'submittedAt' or 'createdAt' field for the Timestamp.



HubSpot [1]

https://docs.airis.appier.com/docs/hubspot



Follow the below example of how to set up the Task. Use the 'submittedAt' or 'createdAt' field for the Timestamp.

📘Event NameBe sure to add the formName field as one of the Action Properties and label the event name something generic like 'import data loader HubSpot form'. Doing this will allow you to create other tasks for other HubSpot forms using the same event name, thus allowing all form events to be track under the same event name instead of creating a new event for every form.

Limitations

Due to limitations with HubSpot API, we can only pull in one form per task. If you have multiple different forms on your site, you'll need to create a new task for each form and use the same event name for each of the Tasks.

Another limitation is linking anonymous users and identifying them after they submit a form. When an anonymous user comes to your site, then submits a HubSpot form, this can create two separate profiles if you do not identify them using woopra.identify. This is because there is no way to link the two profiles together since HubSpot doesn't pass the AIRIS cookie with the HubSpot form. There is a solution but will require changes to the HubSpot form embed code. See the next section for details.

You can customize the embed code in HubSpot to send track requests when the form is submitted.

Below is an example of the code you can use to link the anonymous profiles with the form submissions from the Data Loader import. You can also edit this code to track all the form fields and not use the Data Loader.



HubSpot [2]

https://docs.airis.appier.com/docs/hubspot



However, we suggest using both methods together for two reasons. For one, client-side tracking is not foolproof, and anyone using a blocker or certain browsers can block these events. Using the Data Loader will ensure 100% of the forms being submitted will be tracked in AIRIS. Secondly, sending a woopra.identify() call on the client-side will allow you to link anonymous users and identify them so their anonymous browsing history is merged with the profile made from the Data Loader 'HubSpot form submit' event.





❗️Example Code OnlyThe above code is an example that worked during our testing. This may not necessarily work in every case and may need modification.

This is one example of how you can identify users when they submit the HubSpot form when you're using the HubSpot embed form code.Updated 23 days ago



Salesforce [0]

https://docs.airis.appier.com/docs/salesforce



Follow the below steps to successfully install the AIRIS and Salesforce integration, map fields between the two tools, and set up the AIRIS embedded profile feature in Salesforce.

Note: You must have both AIRIS and Salesforce accounts to access the integration. You must have the AIRIS Javascript tracking code on your website, and it must be identifying users via email address for the integration to work. If you have not set up AIRIS accordingly, please follow steps one and two of the setup tutorial or contact us.

Navigate to the “Configure” section of your AIRIS instance.

Click on the “Integrations” button on the sidebar.

Search for the Salesforce integration and click on the app.

Click the “Connect” tab on the top and create a new connection.

With our Data Loader connection made, we can pull in any data from your Salesforce Objects. In the following section, we have some examples of how to set up the Tasks to pull in specific data. If you have any questions, please reach out to our support and we can help set up these tasks.

Once the connection is made, navigate to the "Task" tab under the Data Loader section on the left pane.

Click in the upper right corner to set up a new Task. Here, we'll configure the Task to pull in Leads when they are created using the Lead Object.

First, we'll configure the Source Configuration as follows:

We are using a "Track" data type since we are pulling in an event when the leads are created.

Next, we'll configure the mapping, User properties, and Event properties.

Select and Map

First, we'll map the lead email to the email in AIRIS. This is to tell AIRIS what profiles to send the data to. Typically email is the most common mapping.

User Properties

The User Properties can be any data you want to import from the Lead to enrich Lead profiles

Event Name

In our example, we used 'sf created lead'.

Event Properties

It's ok to duplicate what you selected in the User Properties here or simply add properties for the event that are important. We suggest adding at least status as one property.



Salesforce [1]

https://docs.airis.appier.com/docs/salesforce



This is an example setup of the Lead Import Task. You can follow this, or tweak the imported fields to suit your needs.

Timestamp and Cursor

Select CreatedDate for the timestamp and Cursor

Save and Activate

Lastly, you can save, preview and activate the task. The task might take some time for the import to complete. The Task will automatically check for new updates at set sync intervals.

📘Double Check Your FieldsIt's important to make sure you have all the fields you want to import selected. It's always a good idea to bring in more data than less because you can always hide fields in AIRIS but it's difficult to go back and re-import the data if you need to add a field later.If you need to add a field later, you'd have to pause and reset the cursor which will remove all the imported data, and you will need to start the task over.

Click in the upper right corner to set up a new Task. Here, we'll configure the Task to pull in updates to Leads using the LeadHistory and Lead Objects.

First, we'll configure the Source Configuration as follows:

We will need to join the Leadhistory object with the Lead object to make sure we have the lead email field available to us to map.

Next, we'll configure the mapping, User properties, and Event properties.

Select and Map

First, we'll map the lead email to the email in AIRIS. This is to tell AIRIS what profiles to send the data to. Typically email is the most common mapping.

User Properties

We'll leave these blank for this Task.

Event Name

In our example, we used 'lead ${Field} update'. This will create multiple different events for the types of updates. These include Lead updates for leadmerged, leadconverted, owner, created, status, ownerassignment, title company, and other history updates.

Event Properties

Select from the LeadHistory Object the following: Field, OldValue, and NewValue.

Timestamp and Cursor

Select CreatedDate for the timestamp and Cursor

Save and Activate



Salesforce [2]

https://docs.airis.appier.com/docs/salesforce



Timestamp and Cursor

Select CreatedDate for the timestamp and Cursor

Save and Activate

Lastly, you can save, preview and activate the task. The task might take some time for the import to complete. The Task will automatically check for new updates at set sync intervals.

Since the Opportunity Object can be connected to multiple emails, we can only map Opportunity history events to the main contact. To do this, we will need to create several joins using the OpportunityHistory, OpportunityContactRole, Contact, and Opportunity Objects.

Please configure the joins in this exact way:

Select and Map

First, we'll map the Contact email to the email in AIRIS. This is to tell AIRIS what profiles to send the data to. Typically email is the most common mapping.

User Properties

We'll leave these blank for this Task.

Event Name

In our example, we used 'opportunity history update' as the Event Name.

Event Properties

You can customize what you want to bring in, but we recommend at least opportunityid, stagename, closedate as standard fields. If you add more, remember it's better to bring in more than fewer fields. Bring in anything you think you might need.

Timestamp and Cursor

Select CreatedDate for the timestamp and SytemModstamp for the cursor.

Save and Activate

Lastly, you can save, preview and activate the task. The task might take some time for the import to complete. The Task will automatically check for new updates at set sync intervals.

Start by Installing the AIRIS package for Salesforce.

Log in to Salesforce as an administrator and select “Setup” in the top navigation.

Under “Build” select the “Leads” dropdown.

Select “Page Layout” to customize the page layout for your leads.

Click on “Edit Layout”

Under VisualForce Pages, add a Section and set the Section Properties so that the layout is 1-Column. Name your section.

Next, drag the “WoopraLeadProfile” to the section you just created.

Scroll to the added AIRIS Profile, click on the configuration button and add the following settings for width and height.



Salesforce [3]

https://docs.airis.appier.com/docs/salesforce



Scroll to the added AIRIS Profile, click on the configuration button and add the following settings for width and height.

Hit “Save” and you’re all set. Follow the same instructions to add the AIRIS profile to the Contact layout and save!

You'll need to provide AIRIS access keys for Salesforce Visualforce pages. If the access keys are not provided, the Visualforce page will rely on the current user being logged into AIRIS and you may not see the profiles populate.

To fix this, the following configuration needs to be edited in Salesforce:

Go to Settings > App Setup > Develop > Custom Settings

Click on Manage next to “WoopraSettings”

Click on Edit

Note: AIRIS needs to map by email address at the lead and contact level to embed the live AIRIS profile. Be sure that you've set up to map by email address in your AIRIS configuration.Updated 23 days ago



WordPress [0]

https://docs.airis.appier.com/docs/wordpress



Guide to installing AIRIS on a Wordpress site

The WordPress app seamlessly tracks all WordPress events, such as when a visitor performs a search on your website, which articles (AIRIS considers blog posts as articles) they read, pageviews, and more. This integration makes it extremely simple for you to access a comprehensive WordPress-customized analytics suite within minutes.

With the WordPress app, you will have access to reports detailing top authors, top categories, reader retention, and more.

Note: This plugin automatically adapts to the WooCommerce WordPress plugin so that you can seamlessly track e-commerce transactions as well.

If your site is powered by WordPress, there are two ways to install the Woopra plugin:

Sign in to your WordPress Dashboard at yourdomain.com/wp-admin

Click on the “PlugIns” in the menu on the left

Below “PlugIns” in the menu on the left, click “Add New”

Search for Woopra

Click “Install Now” underneath the Woopra plugin

You can view your site’s stats by visiting https://airis.appier.com/

Download the Woopra WordPress Plugin from http://wordpress.org/plugins/woopra/

Extract the Woopra.zip file to a location on your local machine

Upload the Woopra folder and all contents into the /plugins/ directory

You can view your site’s stats by visiting https://airis.appier.com/

After installation, you will need to configure the events that you wish to track within your WordPress dashboard. You can find these options by selecting Settings, then select Woopra from the list.

We recommend using the Contact Forms 7 or Gravity Forms plugin.

In the following example, we are using Contact Forms 7: https://wordpress.org/plugins/contact-form-7/.

Once you have installed the Wordpress Plugin and Contact Forms 7 you can add the following code to the header.php file found under the theme settings. You will insert the code after the 



After you save the file, you can test to see if your forms are being correctly tracked in AIRIS. To test, you can find your profile before you submit the form, then refresh the list of users in the people profiles and see if your profile has been updated with the information you submitted.

add_action("gform_after_submission_1", "woopra_contact_form", 10, 2);

function woopra_contact_form($entry, $form) {

$data = array(

"fullname" => $entry[1],

"email" => $entry[2],

"phone" => $entry[3],

"website" => $entry[4],

"subject" => $entry[5] 

);

$user_data = array (

"name" => $entry[1],

"email" => $entry[2]

);

do_action("woopra_identify", $user_data);

do_action("woopra_track", "contact form", $data, true);

}

?>Updated 23 days ago



Drupal

https://docs.airis.appier.com/docs/drupal



Login to your site.

Click Administer -> Site Building -> Blocks -> Add Block.

Give the new block a Block Description of AIRIS. Leave the title blank.

Copy the JavaScript snippet provided in the JavaScript app in AppConnect.

Just below the Block Body, click the Input Format, and set it to PHP code.

📘NoteIf this option is not available, cancel and make sure you have the PHP filter enabled in your modules section and then start again.

Scroll down and click Save Block.

In the list of Blocks you should now see AIRIS and the Region set to None.

Set the Region to be whatever is closest to the header. Some themes have a left/right/center/header/footer. Any placement should work but the closer to the header, the better.

Scroll down and click Save Blocks.

Once the code is installed, you can view your site’s stats by visiting from an up-to-date browser. AIRIS works best in Chrome and Safari but FireFox works as well.

Updated 23 days ago



Zapier [0]

https://docs.airis.appier.com/docs/zapier



You can use our AIRIS Zapier connection to send events to AIRIS from other applications.

❗️Zapier IssuesWhile Zapier is good to send some events to AIRIS, there are some pitfalls to be aware of. Unless the user is identified on your site first, before the Zapier event is sent, there may be issues linking anonymous profiles with the data you are sending from Zapier. We will merge profiles based on a hierarchy of IDs. The issue is that without one of the IDs to merge on, this can cause split profiles. As long as you set one of these ID's using the identity function on your site, you could then set that ID to send with the Zapier event so AIRIS will know which profile to put the event on.For example, if a user comes to your site and is required to register on your site with an email, you would first have them register and send their email address from your site directly to AIRIS using the woopra.identify function. Then, let's say you are using some 3rd party app on your site where they can request demos. Let's assume that you have connected this app to Zapier and you then want to send Zaps to AIRIS. When you send this Zap to AIRIS, you would send their email with the demo request info. Since it is being sent with their email, AIRIS will know to automatically merge these profiles (previous browsing history profile and the new demo request profile) because they share the same email. This way you will have all the previous browsing history along with the demo request data you sent from Zapier all in the same profile.Taking the same example, if the user does not enter their email (or some other unique identifier) on your site first, they will have an anonymous profile in AIRIS. Then, when you send the registration event through Zapier with an email, AIRIS will not know which profile to attach this to. It will create a new profile. To remedy this, you would need to identify the user first on your site, then send the registration info.

Enter your project name (e.g. yoursite.com).



Zapier [1]

https://docs.airis.appier.com/docs/zapier



Enter your project name (e.g. yoursite.com).

Connect any data from your trigger to the AIRIS fields (e.g. email, custom event, etc.).

Test. Send some test events and check them in AIRIS to make sure the events are being sent correctly.

Save and activate your Zap.

Updated 23 days ago



Pardot [0]

https://docs.airis.appier.com/docs/pardot



Add to List - Add this user to a Pardot email list

Remove from List - Remove this user from a Pardot email list

Fetch Visitor Email - Hidden Trigger to find prospect by id and fetch email from pardot if it's missing from the AIRIS profile.

Fetch Pardot Events - Automatically fetch user events from Pardot on a regular basis.

Pardot Opened Email - A user opened an email sent via Pardot.

Pardot View - A user performed the Pardot view action. This could be a number of different view types.

Pardot Success - User completed Pardot Success. This is usually a defined conversion event in your Pardot instance.

Pardot Email Bounced - An Email sent to this user via Pardot was Bounced.

Pardot Unsubscribed - The user went to the unsubscribe page.

Pardot Custom Url Click - The user clicked a custom URL in an email sent via Pardot.

Pardot Click - The user clicked in an email sent via Pardot.

Pardot Opportunity Lost - The opportunity associated with this user in Pardot was marked as lost.

Pardot Opportunity Linked - The Opportunity in Pardot associated with this user was linked.

Pardot Email Sent - An email was sent to this user via Pardot.

Pardot Viewed Email Preferences Page - The user went to the email preferences page in Pardot.

Pardot Error - The user had an error in Pardot.

Pardot New Opportunity - The user became a new opportunity in Pardot.

Submitted Pardot Spam Complaint - The user reported an email sent via Pardot as spam.

Pardot Resubscribed - The user re-subscribed to Pardot emails.

Pardot Opportunity Won - The opportunity associated with this user in Pardot was marked as won.

Pardot Opportunity Reopened - The opportunity associated with this user in Pardot was re-opened.

Pardot Prospect ID - This Field is the person's prospect ID in Pardot. Do not change it!

Pardot Visitor ID - This Field is the person's user ID in Pardot. Do not change it!

Last Pardot Inbound Sync At - Timestamp of last Pardot sync event for this user. Do not change it!



Pardot [1]

https://docs.airis.appier.com/docs/pardot



Last Pardot Inbound Sync At - Timestamp of last Pardot sync event for this user. Do not change it!

Click install and authorize with your Pardot admin email, password, and API user key.

Configure the integration by setting your property mapping and sync settings.

Select the Pardot events you'd like to track in AIRIS.

Select "Apply Configuration" and you're done!

The integration will also automatically install triggers in the Triggers section that you can use to add and remove users to email lists, dynamically update contact data and more!Updated 23 days ago



SFTP

https://docs.airis.appier.com/docs/integrations-sftp



The SSH File Transfer Protocol (SFTP) is a network protocol used for transferring files securely. SFTP can be used to host files of any format or size, and requires a client that supports the SFTP protocol to transfer files. AIRIS supports the ingestion of CSV-formatted files hosted on an SFTP server.

Only CSV files are supported for SFTP connection imports.

To ensure efficient processing, we advise keeping each CSV file under 100,000 rows.

From the top menu, go to Configure, then from the left menu, go to Install > Integrations.

Go to the Connect tab, then click + New Connection.

In the settings panel that opens on the right, enter a name for the connection, then complete the following settings.

SettingDescriptionHostnameThe SFTP hostname.PortThe SFTP host port number.PathThe file path of the directory where files will be uploaded to or from which they will be downloaded.UsernameThe SFTP account's username.Authentication Type: PasswordThe SFTP account's password.Authentication Type: Private KeyThe SFTP account's SSH private key.• Only PEM keys are supported (ssh-keygen -m PEM -t rsa).

• Enter the entire private key, including the header and footer, i.e. -----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY-----

Click Connect to SFTP to finish creating the connection.

Updated 23 days ago



Shopify [0]

https://docs.airis.appier.com/docs/shopify



📘For some guided help connecting Shopify, please contact us and we'll gladly hop a call to walk you through the process.

The AIRIS + Shopify Integration enables you to import order data for use in your customer analytics.

Since this integration uses our Dataloader connection, this means you can import historical data from Shopify. This also means that we have access to certain tables in Shopify where you can customize what data you want to import to AIRIS.

This integration makes it easy to do reporting on revenue and sales. With the right setup, it’s possible to see your customer’s complete journey from marketing campaigns all the way to checking out.

There are two parts to setting up Shopify tracking:

Connect Shopify through our Data Loader to import historical and real-time order data. This data is pulled directly from Shopify's API.

Edit the Shopify code to tie website browsing data with the imported order data. Since the order data is imported directly from Shopify's API, this creates a separate AIRIS profile from a user's website tracked data profile(i.e a profile that includes events that include pageviews, button clicks, scroll depth, etc.) unless this "website profile" is identified. We can assure these two profiles will merge correctly by editing the code on your shop page to identify users when they check out. This way you'll have a complete journey for your user, from site behavior to completed order.

Navigate to the integration section and search for Shopify. Click the connect tab and create a new connection. You'll be prompted to enter your connection details.

Shopify and Shopify Plus will have different methods of editing the code to successfully identify users on the client-side.

There will be two places to update the code--the main website tracking and the tracking checkout pages.

To do this, you'll need to edit the Shopify 'header.liquid' and 'checkout.liquid' files. This will allow the orders to be tracked correctly in AIRIS.



Shopify [1]

https://docs.airis.appier.com/docs/shopify



From your Shopify admin page, first find the 'header.liquid' file. Typically this should be under Online Store > Themes.

Find the theme you want to edit, and then click Actions > Edit code.

Add the following code inside of the .

🚧Make sure you replace "domain.com" with your project name.







Track the checkout pages. Insert the tracking snippet below to your 'checkout.liquid' file. This tracking code will identify logged in customers and customers who are checking out as guests.







Since the checkout.liquid is only available in Shopify Plus accounts, the following instructions will need to be used for non-Shopify Plus accounts.

❗️Section In ProgressThe following section is incomplete. We are currently doing testing for non-Shopify Plus accounts and refining the code. Please reach out to our support team for assistance.

To add code, you can add additional scripts to the order status page.

Navigate to Shopify > Admin Settings and edit the Order Status Page code with the following:

The Task is used to pull in selected data from Shopify. You can create a new Task if one wasn't added by navigating to the Task section under Data Loader.

From there configure the Task by selecting the Order table. You will also select the data type as 'Track'.

Add any additional conditions if you want to limit the orders to a specific timeframe. Use the created_at timestamp to filter the data.



Shopify [3]

https://docs.airis.appier.com/docs/shopify



Map User Events. First Map the order.email to "email" in AIRIS.

Name your Event and add Event Properties. Important fields would be total_price, order_id, checkout_id. Also, add any additional fields that are important to you.

Tag User Properties. This is data about the user that you want to import. You can select any User properties you'd like but be sure to add email.

Select the Timestamp as created_at.

Save, Preview, and Activate. The import will start to bring in records. This may take some time to complete depending on the amount of data.

Updated 23 days ago



LiveChat

https://docs.airis.appier.com/docs/livechat



To use our LiveChat integration, you must set up trigger events in AIRIS. These triggers will inject AIRIS code on your page to send us LiveChat events.

With this integration we can track the following: Post-chat survey submitted, rating submitted, end chat, chat msg received, chat message sent, pre-chat survey submitted, minimize window, start chat, show window, and hide window events.

From the Integrations page for LiveChat, then click on the "+ New Trigger" button.

Configure the trigger event to match the below settings. Name the trigger, set the trigger to a page view event, and set the frequency to "always."

Configure the Target. Click "Add Target" at the bottom and select what events you want to track in AIRIS. Search for "livechat" to see the available trigger events.

You can add multiple targets for the different events as shown below.

Save the trigger. After you save and set the trigger live, you will start to see the events come in.

Updated 23 days ago



Consent Management Platform [0]

https://docs.airis.appier.com/docs/consent-management



Consent management platforms (CMP) are tools that help you collect and manage the cookie consent of your website visitors. Some common consent management platforms include OneTrust, TrustArc, CookieYes, and Osano.

If you are using a CMP, you can pass the consent status of your users to AIRIS. Using AIRIS, you can then use these data to create segments and engage with your users based on the consent granted.

Follow the instructions below to set up CMP with your website and AIRIS.

Part I: Set up cookie categories on CMP

Part II: Integrate CMP with the website and AIRIS

Part III: Create user schemas on AIRIS

Verify integration

📘DisclaimerThis guide uses OneTrust as an example to show how to integrate a CMP with AIRIS. The actual setup steps may be different depending on the CMP you are using. We are not endorsing any CMP and make no guarantee regarding the consent data tracked by the CMP.

On your CMP, you need to set up the different types of cookie consent you want to collect.

You should have a category for necessary cookies, which are cookies required for the website to operate. Depending on your website functionalities and business needs, you might also need to create other non-essential cookie categories. Below is an example of the cookie categories you might have.

Necessary cookies

Performance cookies

Functional cookies

Targeting cookies (or advertising cookies)

Social media cookies

Here we'll show the interface of OneTrust as an example. Note that each category comes with a Category ID. You will need these IDs in later steps.

The Category Name and Description of each cookie category will be visible to your website visitor.

Refer to the documentation of your CMP for instructions on how to integrate CMP with your website. In most cases, a code snippet will be provided and you need to add the snippet to your website. You will then need to use the woopra.identify() function to send the consent data to AIRIS.



Consent Management Platform [1]

https://docs.airis.appier.com/docs/consent-management



We will use OneTrust as an example. For OneTrust, the easiest way to integrate is to use Google Tag Manager (GTM).

To add CMP code snippet to your website, create a variable and create a tag that includes the code snippet on GTM.

Log into your GTM account and go to the container of your website.

In the left menu, click Variables and click New.

Name the variable, set the Variable Type to Data Layer Variable, and enter OnetrustActiveGroups under Data Layer Variable Name.

📘NoteThe data layer variable name OnetrustActiveGroups is embedded in the OneTrust script and cannot be changed.

Click Save.

In the left menu, click Tags and click New to add the OneTrust code snippet.

Name the tag, set the Tag Type to Custom HTML, and paste the OneTrust code snippet.

Under Triggering, select All Pages. Click Save.

To send consent data to AIRIS, create a trigger that fires whenever users' consent status is updated and create a tag for woopra.identify() to send the data to AIRIS.

In the left menu of GTM, click Triggers and click New.

Name the trigger and set the Trigger type to Custom Event.

Set the Event name to OneTrustGroupsUpdated, select Use regex matching and select All Custom Events.

📘NoteThe event name OneTrustGroupsUpdated is embedded in the OneTrust script and cannot be changed.

In the left menu, click Tags and click New to create the tag to send consent data to AIRIS.

Name the tag, set the Tag Type to Custom HTML, and add the AIRIS code snippet in the HTML field.



Under Triggering, select the trigger created above and click Save.

On AIRIS, create the following user schemas.



Consent Management Platform [2]

https://docs.airis.appier.com/docs/consent-management





Under Triggering, select the trigger created above and click Save.

On AIRIS, create the following user schemas.

A user schema called cookie_consent that shows the category ID of all consented cookie categories (e.g. cookie consent: ,C0001,C0002,).

A separate user schema for each cookie category that shows whether the consent status is true or false (e.g. Necessary cookies: true).

Follow the steps below.

On AIRIS console, go to Configure > User Schema and click New User Schema.

Name the user schema, set the Key name to cookie_consent, set Data Type to Text, and click Create. The key name cookie_consent must be identical to the user property name used in the woopra.identify() function.

Click New User Schema to create another schema. Now you need to create a user schema for each category to show the consent status of each category in the user profile.

Type a user schema name that identifies the cookie category, type a Key name, set Property Type to Formula, and set up the formula like this:

Select CONTAINS. The CONTAINS operation returns true if the left parameter contains the right parameter.

For left parameter, select the user schema of the cookie consent.

For right parameter, type the category ID for the cookie category with a comma before and after the ID (e.g. ,C0001,).

Set Data Type to Boolean and click Create.

Repeat steps 3 to 5 for each cookie category.

After setup is complete, follow the steps below to check if everything works as expected.

Visit your website and accept the cookie consent.

On AIRIS console, go to Profiles and click on your own user profile. The cookie consent status should be consistent which what you have selected.

The user's latest consent status can be found under the Unassigned Properties section.

Changes in cookie consent status can be found in the behavioral feed section.

📘NoteIf the consent status is not updated yet, try refreshing the AIRIS console.



Consent Management Platform [3]

https://docs.airis.appier.com/docs/consent-management



📘NoteIf the consent status is not updated yet, try refreshing the AIRIS console.

This is an optional step. You can organize the consent-related properties into their own section. Start by clicking Edit Profile Layout.

Click New Section, type a section name such as "🍪 Cookie consent", drag all consent-related properties to that section and click Save Layout.

You can go to Configure > Segments to create segments based on users' consent status. Below is an example of how to create a segment to include users whose consent status for targeting cookies is true.

The segments can be further exported to AIQUA, allowing you to run campaigns according to the consent granted.Updated 23 days ago



Calendly Tracking Guide [0]

https://docs.airis.appier.com/docs/calendly-tracking-guide



AIRIS does not have a direct integration with Calendly. However, you can use the following code with Zapier to track Calendly events in AIRIS.

To track Calendly events, we need to add additional code to the page that contains the Calendly iframe code on your site. This code will send a webhook to Zapier that contains a Calendly inviteeUrl and eventUrl that we will use to retrieve the user's email. This is done by first catching the hook in Zapier, which contains the necessary data that we'll then use to send a GET request to Calenedly to retrieve the email and event details. We'll finally capture the GET request response and then send that data as a track event to AIRIS.

In Zapier, create a new Zap with a Catch Hook.

Under Test, there will be a webhook URL. Copy this URL and paste it into the following code in step 2.

The following code needs to be added to the page that contains the Calendly iframe code on your site.

function calendlyHandler(e) {

if (e.data.event && e.data.event.indexOf('calendly') !== 0) {

return;

}

switch (e.data.event) {

/* Start Zapier Augmentation */

case 'calendly.event_scheduled':

fetch('Replace this with Zappier Webhook URL', {

method: 'POST',

body: JSON.stringify({

cookie: window.woopra.cookie,

eventUrl: e.data.payload.event.uri,

inviteeUrl: e.data.payload.invitee.uri

})

});

/* End Zapier Augmentation */

default:

woopra.track(e.data.event, e.data.payload);

break;

}

}

window.addEventListener('message', calendlyHandler);

Once you have added the code on your site, schedule a test meeting so a webhook gets sent to the catch hook in Zapier.

Go to Zapier, click the Test section in the Catch Hook, and select the webhook that was sent from the Calendly test. You may need to click the dropdown of the request and click Load more to select the most recent test.

When you receive the event, you'll have the necessary data to configure the rest of the webhooks.

Next, add a new action, "Webhook", and select the event as a GET request.



Calendly Tracking Guide [1]

https://docs.airis.appier.com/docs/calendly-tracking-guide



Next, add a new action, "Webhook", and select the event as a GET request.

Under the URL field, you'll now have the Invitee URL from the previous Catch Hook that you can add. The rest of the settings should be the following:

Follow this link to create an API Token. Select Personal access token and name it. Once you have the token, copy it and enter it under the Header section, as shown above. You'll need to add the text "Authorization" in the first box and "Bearer" followed by the copied token in the second box. Click Continue.

Finally, add another action and search for "Woopra" (use the latest version). Select a track action and enter your project name.

Next, configure the action as follows:

Save the Zap and you're done!Updated 23 days ago



Glossary [0]

https://docs.airis.appier.com/docs/glossary



An ever-growing list of words with special meanings in AIRISAction: An action is an automated trigger or other AIRIS engagement tool that can be or has been run for a user.

Automations: Automations are part of AIRIS's engagement layer. They are set up ahead of time and then run either in real-time on a user by user basis--like sms triggers--or they run on a schedule and perform some action on a number of users at once--like adding people to an email marketing list.

Dynamic Fields: Special kind of user data that is defined as a formula rather than a static value. The value is calculated each time data about a user is queried. These allow you to have constantly changing information about a user in their profile. For example, the number of visits to your website in the past week can be a dynamic field, but would not work as a static one. See User Properties.

Engagement Layer: AIRIS's engagement layer is the part of the AIRIS system that allows AIRIS users to actually interact with their users and user data. Real-time triggers and scheduled batches are examples of Automations. There are also non-automated parts of the engagement layer such as exports.

Event (proposed differentiate from action): An event is a specific instance of tracked activity of a user. For instance, a pageview is an event that AIRIS commonly tracks. Events are one of AIRIS's three main data scopes.

Identify: The concept of identification in AIRIS refers to setting properties in the user data scope, that is, on a user's profile. There are methods in the tracking SDKs to accomplish this, and they are usually called identify(). This term can also be used to specifically refer to sending woopra.identify() in your track requests in order to make sure you don't get split profiles.

Scheduled Batch: A scheduled batch is an automation that runs at an interval and makes a query to find a list of people. It then performs some engagement layer action on these people, such as Syncing them to an external contact list.



Glossary [1]

https://docs.airis.appier.com/docs/glossary



Scheduled Report: A scheduled report is an AIRIS report that is run at an interval and sent to an email address or perhaps uploaded to Dropbox or Google Drive. EX: daily signups report, weekly page views, etc.

Scope: Data scopes are essentially kinds of data. AIRIS has three data scopes: User (visitor), visit (session), and event (action).

Split Profiles: Refers to a situation in which a single person is tracked in an AIRIS account on multiple occasions, and has more than one profile in AIRIS. Split profiles are generally caused by lack of identify calls in the tracking code.

Static Fields: A static field is a user property that has a value that does not change unless changed. See User Properties.

Trigger: A trigger is an action in the AIRIS engagement layer that runs in real-time for one user at a time. EX: you can set up a trigger to show a particular web survey to anyone who engages with a given feature on your website.

Visit: A visit is also known as a session. It represents a group of events that have happened in a given amount of time, usually on the same device and ideally, in one "sitting" on the part of the user. By default, a web session will time out after the user has been idle for 5 minutes.

User: A user is a person who is tracked in AIRIS. Other systems call them visitors, people, contacts, etc.Updated 23 days ago



AIRIS Templates [0]

https://docs.airis.appier.com/docs/woopra-templates



Templates are used to dynamically insert content into text placeholders. These are used in our Schemas and in our Automation and Triggers.

There are two main uses for AIRIS templates:

Determining how an event looks in the user profile (i.e: "Viewed Page /docs" instead of "Did pageview").

Using event and user properties in the configuration of an automation like a trigger, for instance when sending a text message or transactional email in which you want to include a visitor property like the person's name, or an event property like the url of their abandoned cart.

AIRIS templates use the ${ and } format for template expressions. In general the format will be:

${(user|event|visit).}.

The available scopes are user, event, and visit. The user scope means user properties like a user's first_name. The event scope means action/event properties, like the url of a pageview event. The visit scope has session-level properties such as browser or ip.

The SCOPE part allows you to declare if you are referring to a session/visit property, a user property, or to an event property of the current action (in the case of a trigger, this would be the action that is selected in the "trigger when" section when you define your trigger.)

To see what event properties are available for a given action, it is best to go check out your event schemas in the AIRIS interface: Configure > Event Schemas. Similarly, you can see what properties/fields you have defined in your schemas for users in Configure > User Schemas.



AIRIS Templates [1]

https://docs.airis.appier.com/docs/woopra-templates



A visit scope allows you to use a visit property that actually applies to many events. For instance, things like: ip address, referer/source, Operating system, browser, etc. are all visit properties and can be accessed in templates using, e.g.: ${visit.browser} For more on the visit scope and properties, see User Properties, and finally Generated Visit Properties which discusses a few properties like browser that are generated automatically when possible, and generally available in any templating situation. They are not always present, however. For example, you wouldn't expect to have a visit.browser on a session that only includes a serverside event like "email bounced" in which the user never actively used a browser to interact with your system.

AIRIS also supports escaping values that are injected into a Javascript context. For example, you can use ${user.name | json} to escape the text into "First Last".Updated 23 days ago



Regular Expressions (RegEx) [0]

https://docs.airis.appier.com/docs/regular-expressions-regex



Using Regex in AIRIS segmentationAIRIS's segmentation allows you to use regular expressions to match very specific patterns in AIRIS user and event property values. The regex is compiled and run using Oracle's regular expressions, the documentation for which can be found here: https://docs.oracle.com/javase/tutorial/essential/regex/

This document is not designed to be a full introduction to regex, but rather to serve as a reference for common patterns and usages you might want to use in AIRIS segmentation.

One of the most common reasons that an AIRIS user who is not already familiar with regex might want to use regex, is to match any of multiple values. For example, let us imagine we are attempting to build a segment in AIRIS of people whose company field is "appier" OR "oracle." The best way to do this would be to create a segment of people who "ARE" company contains "appier" or "oracle". While you can do this in AIRIS without using regular expressions, it can become quite tedious to build a separate filter for each possible value you are looking for, and then to combine all of these "OR'ed" conditions with some other "AND'ed" ones. The way to express "OR" in a regular expression is with the bar: |. So to find people whose company field is either "appier" or "oracle", use this regular expression:

📘Having trouble getting your regex to work?Try putting '(?i)' or '.*' before the expression (without quotes).

In Oracle regex, you can make a group or character class case insensitive by using the (?i) pattern. It will apply to the next group or class you have in the regex, so to only allow the "A" in Appier to be case insensitive: (?i)Appier. However, if you want the entire word to be case insensitive, you can group the word by using parentheses, and the case insensitivity will apply to all the characters in the match group (within parentheses) that follows the (?i). So to put it all together:

That pattern will match all of these: "appier", "appier, inc.", and "Appier, Inc."



Regular Expressions (RegEx) [1]

https://docs.airis.appier.com/docs/regular-expressions-regex



That pattern will match all of these: "appier", "appier, inc.", and "Appier, Inc."

Going one step further, if you want to find multiple companies, like with the example above using OR, you may do it all together like this:

(?i)(.*appier.*|.*oracle.*)

A Regex matches the entire length of the value that is being checked. So the above regex, appier will only match values that are exactly "appier" with no other spaces or characters in the value, and also, with no capital letters. To match "Appier Inc.", you would need to do two things: make your regex case insensitive, and alter the regex to allow for other characters to be present, as long as "appier" is in the value somewhere.

One of the most useful patterns in regex is .* (dot star). The dot, in regex, means match ANY character at all (including spaces, and non-alphanumeric characters). The star is what's known as a quantifier, it means "match 0 or more of the preceding character or group. (A group could be a character class in square brackets, or it could be anything in parentheses).

So to match "Appier, Inc." as well as "Appier Incorporated" along with any other potential names for the same company, what you essentially want to say is "match any company that includes the word 'appier'". You would do this by surrounding your appier regex with .*s like this:

Updated 23 days ago



Why Referer Tracking can be Inaccurate

https://docs.airis.appier.com/docs/why-referer-tracking-can-be-inaccurate



While Referrer (originally misspelled referer: https://en.wikipedia.org/wiki/HTTP_referer#Etymology) data can be a great tool to analyze where users came from, it's important to understand the possible pitfalls. Referrer data can sometimes be inaccurate when using this as a filter when analyzing traffic or marketing campaigns. Because this field is an optional part of the HTTP request, there can be several reasons why using this filter can produce inaccurate results.

One such reason is due to referrer hiding. With the increase in privacy concerns, many servers and browsers will not send the referrer data, or can even send false data. Additionally, browsers will not send the referrer field when they are redirected using the “Refresh” field.

Another reason is due to Secure (HTTPS) access. If the user connects from HTTPS to HTTP, this will also cause the referrer to not be sent. This is implemented to increase security for end users.

Also, some pages that use HTML5 can add attributes (rel=”noreferrer”) which will instruct the user agent to not send a referrer.

These are just some of the reasons why using referrer can be inaccurate. While they can be useful to see a general or overall view of where you're traffic is coming from, they might not be entirely correct.

When using the "referrer type" fields in AIRIS, some traffic could be marked as "internal," which can occur when:

A page on your site that isn't integrated with the Appier SDK.

A user goes idle and returns to a tab, and then visits another page on your site. The referrer data could be replaced with your own site's referrer URL, thus marking the new visit as "internal."

In AIRIS, we recommend the use of UTM tags when linking traffic to your site. If you are running a campaign, AIRIS can use these UTM tags to automatically track campaigns and allow you to filter more accurately on the traffic to your site.

See Campaign and Referrer Data: What's the difference? for more details.Updated 23 days ago



Campaign and Referrer Data: What's the difference? [0]

https://docs.airis.appier.com/docs/campaign-and-referrer-data-whats-the-difference



Understand the difference between campaign and referrer data, and when to use them.There are different ways to analyze where a user came from and how they landed on your site. In this document, we'll break down some scenarios and explain when to use certain AIRIS system properties such as campaign source or referrer type.

Wikipedia states:

"In HTTP, 'referrer' is the name of an optional HTTP header field that identifies the address of the web page (i.e., the URI or IRI), which is linked to the resource being requested. By checking the referrer, the server providing the new web page can see where the request originated.

In the most common situation, this means that when a user clicks a hyperlink in a web browser, causing the browser to send a request to the server holding the destination web page, the request may include the Referer field, which indicates the last page the user was on (the one where they clicked the link)."

AIRIS will attempt to pull this referrer data that's stored in the user's browser (if available) and we'll use that referrer URI to determine the AIRIS fields Referrer URL and Referrer type. There is logic on our backend that determines the referrer type based on rules such as: if the referrer URI contains "google.com" then the referrer type is "Search."

You can read more on Why Referrer Tracking Can Be Inaccurate, but the main point is that tracking applications are not always able to pull referrer data from the user's browser. Typically, this field should be used to get a general sense of where users are coming from and not a definitive answer.

👍What is the difference between URL and URI in AIRIS?URL and URI can differ depending on the platform you're using. However, in AIRIS, we define URL as anything after the domain name. For example, if you visit the page the URL field in AIRIS would be /blog. The URI in AIRIS is the complete address including the https.



Campaign and Referrer Data: What's the difference? [1]

https://docs.airis.appier.com/docs/campaign-and-referrer-data-whats-the-difference



The Campaign Properties in AIRIS are based on UTM data extracted from the URIs of pageviews on your site. You can use a URL builder tool to add UTM tags to external links that direct to your website.

We recommend using UTM tags in all external links to your website (paid or not) when possible. This way, when a user lands on your page containing UTM tags, they'll land on a page that looks like: "http://www.yourwebsite.com/?utm_campaign=promo&utm_source=facebook&utm_medium=web_paid_ppc&utm_content=banner"

Campaign data will always be more accurate because it does not rely on referrer data (which may or may not exist) and the URI is always recorded on pageview events in AIRIS. When a URI is recorded on a pageview event, AIRIS will automatically extract the UTM data into separate fields under Campaign Properties.

All of these "campaign" fields are extracted from utm_campaign, utm_source, etc.

Not all external links contain UTM data. For example, UTM data is not available for organic traffic from search engines.

Usually, paid campaigns will contain UTM tags, so AIRIS's campaign-related fields should be used to analyze paid campaign performance. Since there are several UTM tags you can define such as utm_medium, you can specify whether the link was paid or not (e.g. utm_medium=web_paid_ppc). This makes it easy to analyze specific campaigns and differentiate between paid and non-paid traffic.

Referrer fields should be used to analyze general traffic trends if UTM data isn't available. Since many new browsers might block referrer data, you'll often see a lot of "direct" referrer type traffic. This can mean there was no referrer data for the pageview visit.

👍You can also create Custom Event Schema Properties that can combine campaign data and referrer data using Formulas. For example, we could create a formula that says, if campaign data exists for a recorded pageview event, use 'campaign source' and if not, use the 'referrer type'.



Campaign and Referrer Data: What's the difference? [2]

https://docs.airis.appier.com/docs/campaign-and-referrer-data-whats-the-difference



AIRIS FieldDescriptionExampleReferrer TypeUses the most recent referrer for an event. Uses the referrer URL to determine the "type".direct, internal, search, backlink, social, email, PPCFirst Referrer TypeSaves the first referrer type recorded for the user.direct, internal, search, backlink, social, email, PPCReferrer URLUses the most recent referrer URL for an event if available.https://www.somepage.comCampaign NameExtracts utm_campaign= from the pageview URI that AIRIS records. The name of the campaign.campaign xyzCampaign SourceExtracts utm_source= from the pageview URI that AIRIS records. Typically where the ad was displayed.google, facebook, instagram, etc.Campaign MediumExtracts utm_medium= from the pageview URI that AIRIS records. Typically the type of ad.web, paid, email, tweet, etc.Campaign ContentExtracts utm_content= from the pageview URI that AIRIS records. Typically used if running similar ads.topbanner, rightsidebanner, specific_location, temporarysale, etc.Campaign TermExtracts utm_term= from the pageview URI that AIRIS records. Typically associated with Google Adwords or search/keyword terms.running+shoes, journey+analytics, coffee+cups, etc.Campaign IDExtracts utm_id= from the pageview URI that AIRIS records. Some campaigns might have an ID.id_xyzFirst Campaign Name, Source, Medium, etc.Saves the first recorded visit that contained UTM tags. Note that the first visit from a user might not have UTM tags, but this will still record the first instance if there is one later on.See examples above

📘NotesCampaign data can also be associated with other events other than pageview events such as some email events or other custom events. This will depend on how you're sending these events to AIRIS.Updated 23 days ago



Why are my stats different on AIRIS than on Google Analytics? [0]

https://docs.airis.appier.com/docs/why-are-my-stats-different-on-woopra-than-on-google-analytics



Some AIRIS users see a discrepancy between their AIRIS and Google Analytics stats. The primary reasons for this discrepancy are each service’s reporting and tracking methods. AIRIS is committed to providing the most accurate data by showing you individual users and exactly how they're engaging across the omnichannel touchpoints you're tracking.

AIRIS shows you exactly who is on your site or application, what they’re doing, and when they leave. AIRIS’s reporting is accurate to the second. We use "beacons," which accurately record when a user enters, exits, switches tabs, or closes a browser.

Google Analytics reports time on page based on timestamps. They calculate this by subtracting the time of the initial event from the subsequent event. This can lead to inaccurate durations because the exit page will not have a next page to calculate, so the time on page for an exit page will be 0 seconds.

Another scenario is if a user goes idle for under 30 minutes. In GA, if a user visits a page at 12:00, stays on a page for 3 minutes, then goes idle for 29 minutes, and later visits another page at 12:29 -- GA will show that they stayed on the first page for 29 minutes. Using beacons, AIRIS can accurately tell when the user navigated away from the page and will give you the 3-minute duration.

Another cause of this discrepancy is Google Analytics’ use of sampling, which means using a subset of data. Google Analytics often uses sampling for both collecting data and generating reports based on your data. That means that Google Analytics may only be collecting data on some of your users and/or only using a portion of that collected data when generating your reports.

AIRIS never uses any kind of sampling. Since we report at the individual level, rather than simply aggregating, we always collect your full data set. AIRIS’s analytics reports are generated using this full set of data.



Why are my stats different on AIRIS than on Google Analytics? [1]

https://docs.airis.appier.com/docs/why-are-my-stats-different-on-woopra-than-on-google-analytics



Lastly, some discrepancies exist between AIRIS and Google Analytics due to the growing tendency for each person to have multiple devices (e.g., mobile, tablet, home computer, work computer, etc.) from which they access the same online services.

Traditional web analytics, like Google Analytics, cannot track a user across multiple devices or browsers, so a user returning to the site from another device or browser is identified as a new user rather than a returning user. This can lead to skewed numbers because some of their users might be the same person.

Since AIRIS focuses on individual-level profiles rather than device-based tracking, our numbers are much more accurate. For example, you might sign up for service X from your home computer, use the service’s app on your iPad, and upgrade your account from your work computer. AIRIS will track this as one person because we merge profiles based on a common identifier like an email address. Whereas GA doesn't allow for any personal information to be tracked and would count this user as three separate people.

Lastly, when comparing numbers between AIRIS and GA, it's important to get as close to comparing apples to apples as we can. While our tracking method is different, keep in mind that our reporting is also different. For example, when running a Trend report on a specific page, the filtering can vary on both platforms.

For example, if we're running a report in GA for 'www.site.com/page1', does that count include variations on the page like 'www.site.com/page1?utm_campaign=email'?

In AIRIS, we have several constraint modifiers like 'is, contains, exists, is not, etc.' so to get more accurate results when comparing numbers, try to match the filtering as closely as possible on both platforms.



Why are my stats different on AIRIS than on Google Analytics? [2]

https://docs.airis.appier.com/docs/why-are-my-stats-different-on-woopra-than-on-google-analytics



Another important point is that our reports use different metrics such as "User, Visits, and Events." The numbers that are most similar to GA would be "Events." The Event count is the number of times the tracked event occurred. Visits are the number of sessions that the event occurred in. User is the number of unique people that did the event. GA tracks sessions and people very differently, so using the event count would be the closest to what they track.Updated 23 days ago



Why Do I See Discrepancies between AIRIS and AIQUA Reports?

https://docs.airis.appier.com/docs/faq-airis-aiqua-data-discrepancies



At times, you may notice slight data differences between AIRIS reports and AIQUA Analytics Studio reports. The discrepancies are primarily due to inherent differences in how each system processes data and structures its reports.

Here are the three main factors that may cause data discrepancies.

AIRIS and AIQUA both utilize Appier SDK to capture user events but have different data ingestion frequencies. AIRIS focuses on real-time tracking and sends user events to the server instantaneously. AIQUA, on the other hand, sends and aggregates user events in small batches in order to optimize data transmission. The different data processing frequencies can result in small data inconsistencies.

Starting from July 2023, we have removed the batching behavior in AIQUA accounts that are connected with an AIRIS account. After the change, we observed that the data discrepancies have been reduced to under 0.5%.

The data collected by Appier SDK goes through two different data pipelines, one catering to AIRIS and the other to AIQUA. Consequently, even a minor network disturbance can result in small data discrepancies between the two systems.

AIRIS reports are user-centric while AIQUA reports are device-based. If the same person visits your website or app from multiple devices (for example, two iOS devices or multiple web browsers), AIRIS uses a user unification process to merge multiple devices based on the identifiers and ID hierarchy defined in AIRIS. AIQUA, on the other hand, treats each device as a different user. As a result, you might see different results if you compare the user-centric reports (such as Journey, Attribution, and Cohorts) in AIRIS with AIQUA reports.Updated 23 days ago



Queued Events

https://docs.airis.appier.com/docs/queued-events



When sending events to AIRIS, you may see a response code of "queued" which can affect some functionality such as our automation Inject Script.

Inject Script is a trigger action that will inject script on the user's browser, based on their events. We return the script that you wrote in the response from our servers after a track event is sent from the client-side. If a run script isn't working, you may be receiving a "queued" response. If the event is queued, then we'll still receive the tracking request, but the run script may not fire.

When a run script is set up, there are several factors that may affect performance which could cause the event to be queued instead of returning the script.

Depending on the complexity of your setup, AIRIS needs to check several data points before we return a response with the inject script code. Things such as Segmentation Filters and segment join/leave events, Schema Formulas, User Schema - Profile Metrics, and other Triggers and automation.

Additionally, large profiles with a lot of events, and calculated "lifetime" fields such as custom User Schema - Profile Metrics that are counting some lifetime metric such as total spent or counts of total events all must be checked before a inject script returns a response.

All these factors contribute to the time it takes to successfully return a response from our servers. If the time it takes is too long, we'll return the "queued" response.

To speed up the processing of these triggers, there are several variables to consider.

Limit the number of segment join/leave events

Limit lifetime fields such as lifetime counts and sums that must scan complete profile histories

Limit the number of inject script triggers

Make sure there are no infinite loops that may be causing profiles to be too large. i.e. profiles with too many events or duplicate events

Limit triggers that update user properties

Updated 23 days ago



Copy and Paste Files Within or Between Projects

https://docs.airis.appier.com/docs/copy-and-paste-files-within-or-between-projects



How to copy and paste reports, schemas, and lists from one project to another.

Any reports, schemas, or lists such as annotations or segments can be copied and pasted. You can paste copied files into the same project or a different project.

Dashboards, tags, and triggers are not currently supported.

From the ellipsis (three dots) dropdown, you will see the option to copy a file.

Once the file is copied, you can paste the file while you're on any AIRIS screen using Command+v on Mac or Ctrl+v on Windows. AIRIS will automatically detect the pasted file.

Once pasted, you'll have a new copy of the report, schema, or list in the currently selected project.Updated 23 days ago
