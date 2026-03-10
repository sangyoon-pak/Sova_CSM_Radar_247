---
source: notebooklm_export
file_id: "038"
filename: "038_Recommendation update of AIQUA.txt.txt"
doc_type: "product_overview"
product: "AIQUA"
content_type: "txt"
language: "en"
guide_summary: "This document serves as a comprehensive technical manual detailing the implementation and performance analysis of AIQUA’s **AI recommendation models**. It thoroughly explains core operational concepts, including how models are trained using event data and the process for generating **fallback results** when data is scarce or unavailable. The text provides practical direction by listing **suggested models** appropriate for various web and app placements, like product pages or shopping carts, base"
guide_keywords: "Recommendation Models, Core Concepts, Performance Metrics, Conversion Attribution, Model Training Data"
---

# 038 Recommendation update of AIQUA

﻿Recommendation Models

Deep dive into AIQUA's recommendation models.

* To learn the basics of recommendation models, see Core concepts.

* For details and specifications about each model, see Model reference.

* For advice on picking a model, see Suggested models.

________________





Core concepts

The following concepts form the basis of the recommendation feature, and are important to understand to get best results from AIQUA recommendations.

* What are recommendation models?

* How are models trained?

* What is a selected product?

* How are fallback results generated?

What are recommendation models?

When creating a recommendation scenario, you'll need to select a model to determine how recommendations are generated. These AI models train on event data and information in your product data feed to generate the most relevant product recommendation for your target audience.

👍

For details about each model, including the type of results generated and required data, see Model reference.

How are models trained?

For models to complete training successfully, you'll need:

* Required data present in your account. This data includes event data (only the product ID parameter is used for training) and fields in your product data feed. For specific requirements, see Model reference.

* Time to complete training. It can take several days to complete training, depending on the size of your product data feed and the specific model your scenario is using.

If any required data is unavailable:

* If the scenario has never completed training before: The first model training will fail and no recommendation results will be available.

* If the scenario has completed training at least once before: Subsequent model training will fail and fallback rules will be used to generate recommendation results instead of the selected model.

What is a selected product?

Some models generate results based on a product your specify—the "selected product". A selected product is required for models that generate results based on a specific product's attributes or user interactions, such as product-based models. Results are determined by the selected product, for example:

* For scenarios using the Similar Product Title model with the selected product "Sneaker A", recommendation results will be products with titles similar to "Sneaker A".

* For scenarios using the Similar Product Attributes model with the selected product "Shirt B", recommendation results will be products with attributes that are similar to "Shirt B".

* For scenarios using the Complementary Products model with the selected product "Jacket C", recommendation results will be products that are typically purchased together with "Jacket C".

To specify a selected product in a recommendation request, pass that product's product ID (as specified in your product data feed) in the API request.

👍

Default selected product for websites

When setting up recommendations on your website, we recommend setting a default selected product on each page that contains product data to guarantee that all recommendation requests include the product ID parameter.

How are fallback results generated?

When creating a scenario, you can choose to return fallback results if a scenario is unable to successfully generate enough results using the selected model, for example, due to insufficient data. Fallback results can either be a static list of products you choose, or they can be generated using AIQUA's default fallback rules.





If you choose to use the default fallback rules, they'll be applied in the following order:

1. If a product category filter is specified in the recommendation scenario or API requests, the most-viewed product from the last 49 days that satisfies the filter conditions will be returned. If no product category filter is specified, the next fallback rule will be used instead.

2. The most-viewed product from the last 49 days that is in the same category as the selected product will be returned. If the productId for the selected product isn't provided, the next fallback rule will be used instead.

3. The most-viewed product from the last seven days will be returned. If no products were viewed in the last seven days, the next fallback rule will be used instead.

4. A random product from the product data feed will be returned.









________________





Model reference

Your scenario can use one of following models to generate product recommendations. Refer to the sections below to learn more about each model and the data it requires to generate optimal results.





Autopilot

Adjust the model dynamically to optimize performance.





User-based

Personalize suggestions by recent user activity.





Product-based

Suggest similar or related products.





Popularity

Showcase what's popular and currently trending.





Advanced

Personalize results based on user preference.





Custom

Set custom recommendation rules.

Autopilot

When Autopilot is selected, the scenario will start using several models (based on the scenario’s placement) and periodically optimize traffic distribution for each one to improve recommendation performance.

You'll need to have at least one of the following events to use Autopilot:

* product_viewed

* product_added_to_cart

* product_purchased

For optimal results, we recommend including the following data as well:

Source

Recommended data

Product data feed

• image

• title

• category

• description

API request parameter

• productId

User-based models

User-based recommendation models generate product recommendations based on individual user preferences and behaviors. These models are suitable for scenarios placed in locations that aren't product-specific, such as your home page.

Model name

Description

Required data

Shuffle results by default

Recommended for You

Deliver a personalized experience by recommending products frequently viewed by similar shoppers.

Event: At least one of product_viewed , product_added_to_cart , product_purchased

Yes

Similar to Your Recently Browsed Products

Enhance product discovery by recommending products similar to the items the user recently viewed.

• Event: At least one of product_viewed, product_added_to_cart, product_purchased

• Product data feed: Must include title. For the best results, include category and description as well.

Yes

Recently Viewed

Re-engage browsing shoppers by recommending products they recently viewed.

Event: product_viewed

No

Recently Added to Cart

Convert cart abandoners by recommending products they recently added to their cart.

Event: product_added_to_cart

No

Recently Purchased

Encourage repurchases by recommending products the user recently purchased.

Event: product_purchased

No

Product-based models

Product-based recommendation models generate results based on a specific product, called the selected product; for example, you can use these models to recommend products that are purchased together with or share similar attributes with the selected product.

These models require you to include the product ID of the selected product in the recommendation API request.

🚧

Important

The product ID you pass into the API request must match the product ID specified in your product data feed.

Model name

Description

Required data

Shuffle results by default

Similar Product Images (Premium)

Help shoppers discover new products that match their taste by recommending items with a similar appearance to a selected product.



Suitable for large product catalogs or catalogs with many new products with limited page view data.



Contact your customer success manager to enable this model.

* Product data feed: image, title, category

* API request parameter: productId

No

Similar Product Attributes

Enhance product discovery by recommending items similar to a selected product based on key details, like product name and category.



This model is suitable for:

• Large product catalogs or catalogs with many new products with limited page view data.

• Scenario placements where users have shown strong intent for the content, for example, a product category page.



Model training is limited to the first 700,000 items in the product data feed.

* Product data feed: Must include title and category. For the best results, include description as well.

* API request parameter: productId

Yes

Similar Product Title

Enhance product discovery by recommending items similar to a selected item based on title.



This model is suitable for large product catalogs or catalogs with many new products with limited page view data.



Model training is limited to the first 2 million items in the product data feed.

* Product data feed: Must include title. For the best results, include category and description as well.

* API request parameter: productId

Yes

People Also Viewed

Enhance product discovery by recommending what other shoppers viewed after viewing a selected item.

* Event: product_viewed

* API request parameter: productId

Yes

People Also Bought

Boost cross-sells by recommending items that owners of a selected product also purchase.

* Event: product_purchased

* API request parameter: productId

Yes

Related Products that You Can't Miss

Boost cross-sells by recommending what other shoppers typically purchased after adding a selected product to their cart.

* Events: product_added_to_cart, product_purchased

* API request parameter: productId

Yes

Related High-Converting Products

Boost cross-sells by recommending what other shoppers typically purchased after viewing a selected product.

* Events: product_viewed, product_purchased

* API request parameter: productId

Yes

Shopping Cart Inspiration

Boost cross-sells by recommending products that are frequently added to shopping carts together.

* Event: product_added_to_cart

* API request parameter: productId

Yes

Post-Purchase Upsell

Boost cross-sells by recommending what other shoppers purchase after purchasing a selected product.

* Event: product_purchased

* API request parameter: productId

Yes

Complementary Products

Boost cross-sells by recommending complementary products that customers often purchase together.

* Events: product_viewed, product_purchased

* API request parameter: productId

Yes

Popularity models

Popularity recommendation models generate results from products that are considered popular among your site and app users; for example, you can use these models to recommend the most-viewed or most-purchased products on your website. Popularity models are re-trained once a day using the event data available at the time. Recent data may not be considered until the next time the model re-trains the following day.

Some models use recency weighting, such as Trending Popular Products in Last 7 days. Recency weighting means that more recent events have a greater influence on the recommendation results than older events.

👍

For more flexibility with popularity models, such as having the ability to choose the event and time period used to determine popularity, see the Popular Products model from the Custom category.

Model name

Description

Required data

Shuffle results by default

Popular Products in Last 7 Days

Capitalize on shopper interest by recommending the most-viewed products from the past week.

Event: product_viewed

No

Trending Popular Products in Last 7 Days

Capitalize on shopper interest by recommending the most-viewed products from the past week with the strongest recent traffic.

Event: product_viewed

No

Bestsellers in Last 30 Days

Capitalize on sales momentum by recommending bestsellers from the past month.

Event: product_purchased

No

Trending Bestsellers in Last 30 Days

Capitalize on sales momentum by recommending bestsellers from the past month with the strongest recent performance

Event: product_purchased

No

Category Hot Items in Last 7 Days

Capitalize on shopper interest by recommending category bestsellers from the past week.

Event: product_purchased, product_added_to_cart

No

Category Hot Items in Last 30 Days

Capitalize on shopper interest by recommending category bestsellers from the past month.

Event: product_purchased, product_added_to_cart

No

Advanced models

Advanced models aren't just based on a single dimension, such as product attributes or user preference; instead, these models use multiple dimensions or are customized by Appier Professional Service.

🚧

Important

The product ID you pass into the API request must match the product ID specified in your product data feed.

Model name

Description

Required data

Shuffle results by default

Recommended for You (Advanced)

Deliver a personalized experience by recommending products tailored to the user's preferences.

• Event: Must include product_viewed. For the best results, include product_added_to_cart and product_purchased as well.

• Product data feed: category

Yes

Related Products You May Like

Enhance product discovery by recommending items frequently viewed by shoppers who also viewed the selected product, with results tailored to the user's preferences.

• Event: At least one of product_viewed, product_added_to_cart, product_purchased

• API request parameter: productId

Yes

Similar Products You May Like

Enhance product discovery by recommending items similar to a selected product, with results tailored to the user's preferences.

• Event: At least one of product_viewed, product_added_to_cart, product_purchased

• Product data feed: Must include title. For the best results, include category and description as well.

• API request parameter: productId

Yes

Professional Service - Custom Model (Premium)

Partner with our experts to design a custom recommendation model tailored to your business goals.

Contact your customer success manager for details.

Required data depends on the customizations you request.

Dependent on requested customizations

Custom models

These models allow you to customize the parameters and events used to generate recommendation results.

🚧

Important

The product ID you pass into the API request must match the product ID specified in your product data feed.

Model name

Description

Required data

Shuffle results by default

Event to Event Model

Recommend products based on a sequence of events you define

For example, you can find users added the selected product to their cart (product_added_to_cart) and recommend products that were then purchased (product_purchased) by those same users.

• Events: Selected events

• API request parameter: productId

Yes

Event also Event Model

Recommend products based on the occurrence of two user events you define.

For example, you can find users who viewed (product_viewed) the selected product and recommend products that were also purchased (product_purchased) by those same users.

• Events: Selected events

• API request parameter: productId

Yes

Popular Products

Showcase the most popular products based on the specific customer event and time frame you select.

Specify which event should be used to determine popularity as well as a time period. You can choose whether to apply a time-decay, which means that more recent events have a greater influence on the recommendation results than older events.

For example, you can tailor recommendation results based on items the user added to their cart (product_added_to_cart) from the last 7 days.

Event: Selected event

No

The following events can be used in custom models if they contain the product_id parameter:

* product_added_to_wishlist

* product_added_to_cart

* product_purchased

* content_viewed

* content_downloaded

* content_scrolldepth_25

* content_scrolldepth_50

* content_scrolldepth_75

* content_scrolldepth_100

* content_playtime_25

* content_playtime_50

* content_playtime_75

* content_playtime_100

* content_faved

* content_shared

* content_commented

________________





Suggested models

Use the following table as a starting point to help you in deciding which recommendation model to use in your scenario for the specific type of page you'll be placing it in:

* Scenarios in a website or app

* Scenarios in a creative's dynamic content

Website or app

Placement

Suggested models

Home page

• Recommended for You

• Recommended for You (Advanced)

• Trending Popular Products in Last 7 Days

Product page

• People Also Viewed

• Related Products You May Like

• Similar Product Title

Product category page

• Recommended for You

• Similar to Your Recently Browsed Products

• Trending Bestsellers in Last 30 Days

We recommend including filter rules to provide more relevant results.

Search results page

• Popular Products in Last 7 days

• Recommended for You

• Similar to Your Recently Browsed Products

Shopping cart page

• Complementary Products

• Related Products that You Can't Miss

• Shopping Cart Inspiration

Checkout page

• Complementary Products

• People Also Bought

• Trending Bestsellers in Last 30 Days

Order confirmation page

• Complementary Products

• Post-Purchase Upsell

• Recommended for You

404 error page

• Recommended for You

• Recommended for You (Advanced)

• Trending Popular Products in Last 7 Days

Other

• Recommended for You

• Recommended for You (Advanced)

• Trending Popular Products in Last 7 Days

Dynamic content in creatives

For scenarios placed in dynamic content, such as in a push or email campaigns, we recommend using the following models:

1. Recommended for You

2. Recommended for You (Advanced)

3. Trending Bestsellers in Last 30 Days









































































Recommendation Analytics

Understand the performance of your recommendation scenarios.

To view the performance of your recommendations scenarios, go to the AIQUA dashboard, and in the left menu, click Recommendation > Scenario List.





📘

Note

Performance analytics aren't available for recommendation scenarios placed in campaign creatives as dynamic content.

________________





Requirements

Performance data for recommendation scenarios is calculated based on the following required settings.

1. Tracking recommendation clicks and impressions

2. Setting the attribution model and window

3. Setting conversion events

For details on metrics definition and downloading reports, see Performance metrics.

Requirement 1: Tracking recommendation clicks and impressions

AIQUA needs to be tracking clicks and impressions that are attributed to Recommendation 2.0. See the details for each platform below.

Platforms

Requirements

Web SDK

Make sure the product url returned in the response is used when rendering recommendation results.

Once Recommendation 2.0 is integrated, Appier Web SDK automatically tracks clicks and impressions, but the user needs to be clicking on the product url returned in the response mentioned above.

Android SDK

• Android SDK 6.5.1 or above is required. • You need to track the clicks on recommended items using this

method

.

iOS SDK

• iOS SDK 7.4.0 or above is required. • You need to track the clicks on recommended items using this

method

.

React Native SDK

• React Native SDK 1.5.0 or above is required. • You need to track the clicks on recommended items using this

method

.

For guidelines on tracking scenario clicks and impressions via REST API, see the Recommendation 2.0 REST API docs.

Requirement 2: Setting the attribution model and window

To set the attribution model and attribution window, go to Recommendation > Settings in the left menu.





* Attribution Model: The default attribution model is Last-click model.

* Last-click model: If the user clicks on multiple recommendation items before conversion, the conversion is attributed to the last clicked recommendation item (if within the attribution window).

* First-click model: If the user clicks on multiple recommendation items before conversion, the conversion is attributed to the first clicked recommendation item (if within the attribution window).

* Attribution Window: The default attribution window is 1 day. For conversions to be attributed to the recommendation item, the user needs to complete the conversion within the attribution window after clicking on the recommendation item.

Requirement 3: Setting conversion events

There are two ways to calculate how conversions are attributed to your recommendation scenarios: Item Conversion and Event Conversion.

* Item Conversion: Under this mode, for a conversion to be attributed to the scenario, the conversion item needs to be the same recommended item that the user clicks on within the attribution window. The conversion item needs to have the same product_id as the recommended item clicked.

* Event Conversion: Under this mode, conversion events that happen within the attribution window after the user clicks on any recommended item from this scenario will be attributed to the recommendation scenario.

For example, an e-commerce selected product_purchased for item conversion, and selected checkout_completed for event conversion.

Scenario 1: A user clicks on products X and Y, which are products recommended by scenario A. The user purchases product Q within the attribution window.

* Under Item Conversion mode, no conversion is attributed to scenario A, because the product purchased does not have the same product_id as the recommended product clicked.

* Under Event Conversion mode, 1 conversion (checkout_completed) is attributed to scenario A.





Scenario 2: A user clicks on products X and Y, which are products recommended by scenario A. The user purchases product X, Y, and Q in one order within the attribution window.

* Under Item Conversion mode, 2 conversions (product_purchased for products X and Y) are attributed to scenario A.

* Under Event Conversion mode, 1 conversion (checkout_completed) is attributed to scenario A.





Setting conversion events

To select the events that represent conversions for your business, go to the left menu and click Recommendation > Settings.





* You can set one or multiple events for Item Conversion mode and Event Conversion mode.

* See the table below for the list of events that can be set as conversion events for the item Conversion mode and the Event Conversion mode.

* If the event you want to use is not included in the list below, you can use custom_goal_x and custom_item_conversion_x to define your own custom events.

🚧

Important:

Make sure the events selected are properly collected by the Appier SDK, and the events used for item conversion need to have a product_id parameter.

For example, let's say you have selected product_purchased for Item Conversion and checkout_completed for Event Conversion. If the user purchases 3 items in a single order, make sure that Appier SDK is collecting 1 checkout_completed event and 3 product_purchased events. Each product_purchased event is required to include the product_id.

Item Conversion

Event Conversion

product_added_to_wishlist

product_added_to_cart

product_purchased

content_viewed

content_downloaded

content_scrolldepth_25

content_scrolldepth_50

content_scrolldepth_75

content_scrolldepth_100

content_playtime_25

content_playtime_50

content_playtime_75

content_playtime_100

content_faved

content_shared

content_commented

custom_item_conversion_1

custom_item_conversion_2

custom_item_conversion_3

added_to_cart

added_to_wishlist

cart_viewed

wishlist_viewed

checkout_initiated

checkout_step_viewed

checkout_payment_added

checkout_completed

registration_initiated

registration_completed

login_completed

subscription_initiated

subscription_completed

trial_started

trial_ended

location_searched

lead_submitted

application_submitted

search

custom_goal_1

custom_goal_2

custom_goal_3

In the recommendation scenario list, you can switch between these two modes and see the conversion performance under each type of conversion calculation.





________________





Performance metrics

To look at performance in the recommendation scenario list, select the performance date range and choose between Item Conversion and Event Conversion mode. The performance data shown on the scenario list is automatically updated every three hours.

* Performance date range: Set the date range of the performance data you want to view. The start date and end date need to be within 180 days of the current date.





* Conversion mode: Choose whether to display performance data calculated using the Item Conversion or Event Conversion setting.

The following metrics are shown:

* Requests: The number of recommendation requests made to this scenario by your website, mobile app, and campaigns. Includes failed requests, requests made by campaign dynamic content, and requests from the Recommendation REST API.

* Impressions: The total count of recommendation_impression events for the scenario. This is the number of times the scenario is viewed by your users. For example, if a user lands on a page embedded with a scenario that returns 5 recommended items, 1 impression would be counted, since all the items originated from a single scenario.

* Clicks: The total count of recommendation_clicked events for the scenario. This is the number of times the recommended items are clicked.

* For web, only clicks on the product URL returned in the response will be tracked.

* For app, make sure you have set up event tracking for clicks on recommended items.

* CTR (Click-through rate): This is calculated by CLICK / IMP.

* Conversions: The total number of conversions attributed to the recommendation scenario.

* CVR: This is calculated by CONV / CLICKS.

* Conversion value: If your conversion events contain valueToSum to track the monetary value associated with the event, the total value attributed to the recommendation scenario will be displayed here.

📘

Note:

The performance date range and the date in the downloaded report are based on the timezone set in the Account Settings.

________________





Performance page

In the scenario list, click the scenario name to view its performance summary. On this page, you can select the conversion mode (Item conversion or Event conversion) and date range you'd like to view data for.





The scenario performance page consists of the following sections:

* Performance overview

* Performance trend

* Performance lift (only available for scenarios using Autopilot)

* Model performance (only available for scenarios using Autopilot)

* Model distribution (only available for scenarios using Autopilot)

* CTR trend by model (only available for scenarios using Autopilot)

Performance overview

The performance overview chart summarizes the overall performance of the scenario.





Performance trend

Use the performance trend chart to visualize how performance changes over time. You can select two different metrics to visualize.





You can select the following metrics from the dropdown menus:

* Impressions

* Clicks

* CTR

* Conversions

* CVR

* IMP CVR

* Conversion value





Performance lift (Autopilot scenarios)

📘

Performance lift data is only available for scenarios using Autopilot for the recommendation model setting.

The performance lift, or CTR lift, is defined by the percentage increase in the CTR compared to the benchmark CTR. The benchmark CTR is the estimated CTR if traffic was evenly distributed across all models, without applying Autopilot's daily traffic redistribution.





Model performance (Autopilot scenarios)

📘

Model performance data is only available for scenarios using Autopilot for the recommendation model setting.

The model performance table summarizes scenario performance metrics broken down by recommendation model.





Model distribution (Autopilot scenarios)

The model distribution chart allows you to compare the traffic distribution between each recommendation model.





CTR trend by model (Autopilot scenarios)

The CTR trend by model chart allows you to visualize the CTR trend for each model.





________________





Performance report

To receive performance reports via email, click Export report, specify a date range, and click Export.

📘

Conversion definition

Performance data is calculated based on your conversion definition.





After clicking Export, you'll receive an email that includes download links for two CSV files, a total performance report and a daily performance report:

1. Total performance report: Contains the total performance accumulated during the specified date range for each scenario.





2. Daily performance report: Contains daily impressions, clicks, CTR, conversion count, CVR, and conversion value for each scenario.





The metrics are counted based on the date of occurrence. In the example illustrated below, two clicks and one conversion are counted under March 8, and one conversion is counted under March 9. Since Clicks is 0 on March 9, and CVR is calculated using Conversions / Clicks, the CVR will be listed as "-" in the report.
