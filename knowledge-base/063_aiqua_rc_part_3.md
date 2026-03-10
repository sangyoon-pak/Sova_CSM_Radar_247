---
source: notebooklm_export
file_id: "063"
filename: "063_aiqua_rc_part_3.txt.txt"
doc_type: "reference_card"
product: "AIQUA"
content_type: "txt"
language: "en"
guide_summary: "This comprehensive guide outlines the functionalities for building, customizing, and analyzing campaigns within the AIQUA platform, focusing heavily on **Recommendation 2.0** and **Analytics Studio**. The source details various creative templates—like *Recommendation*, *Slider surveys*, and *Story*—and explains how to tailor their elements such as buttons, images, and input fields using *Creative Studio* for a seamless user experience. A significant portion is dedicated to campaign performance m"
guide_keywords: "Creative Templates, Campaign Performance, Recommendation Models, Attribution Settings, Analytics Reporting"
---

# 063 aiqua rc part 3

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



Default Templates [0]

https://docs.aiqua.appier.com/docs/prebuilt-templates



Creative Studio offers a variety of prebuilt templates to simplify your campaign creation process. Each template is tailored to different use cases, allowing you to quickly design personalized and engaging creatives for your users without starting from scratch. 

Below is an introduction to each template category with an example of how to customize the template:

Recommendation 

Slider surveys

Lucky wheel 

Limited-time sales 

Story 

Promotions 

👍TipsBefore applying creatives to your promotional campaign, ensure all relevant configurations are valid, and use the Preview button to review your creatives for a seamless user experience.

📘NoteTo learn how AIQUA's Recommendation 2.0 can boost user engagement, see Recommendation 2.0.

The recommendation template is ideal for personalized product suggestions in your campaigns. In this guide, we'll use the Multi-tab recommendation (Desktop) as an example to demonstrate how to customize the settings in Creative Studio to meet your campaign requirements.

To get started with a recommendation template, first obtain a Scenario ID from your Recommendation scenario. For more details, see how to implement the scenario in your creative.

Choose Multi-tab Recommendation (Desktop) from the Creative Studio template list.

In the top left, click the template's name and select Variables and formulas:

Configure the key fields, such as

scenario_id

currency

title_length_limit

product_number: The number of products to display. Set to a fixed system value of 15. The number of displayed products won't change even if you edit the field's value. To change the value of product_number, contact your customer success manager.

Fallback values: Set the following values to ensure the recommendation campaign continues to work normally if any primary data is missing.

category for the category name shown at the top.

title for the product title.

price 

rec_url_item for the image URL.

click_url_1 to click_url_15 for the product page URL.



Default Templates [1]

https://docs.aiqua.appier.com/docs/prebuilt-templates



title for the product title.

price 

rec_url_item for the image URL.

click_url_1 to click_url_15 for the product page URL.

Update the text and URL for the "Check website" button. For more information on modifying elements and optimizing designs, see Designing Creatives.

Once your modifications are complete, save and apply the template to your campaign to display personalized product recommendations based on your configurations.

Use the slider surveys template to engage users through interactive surveys, and leverage their responses for targeted segmentation.

We'll use the Emoji Slider - 4 products as an example to demonstrate how to customize the settings in Creative Studio to align with your product information and segment users based on their responses.

Choose Emoji Slider - 4 products from the template list.

In the top left, click the template's name and select Variables and formulas. Update product names in the Value column.

Customize the text and image elements to fit your campaign's needs. See Creative Elements to learn more about how elements can be customized.

Save and apply the survey to your campaign. You'll be able to gather feedback and create segments based on user preferences.

The system automatically adds survey results to the user segment. To create a segment based on survey responses, navigate to the Audience > Create segment and click Segment by Condition. 

For the template Emoji Slider - 1 product, set the attribute as preference_for_[productName] and the value can be one of the 4 satisfaction levels based on your creative.

For template Emoji Slider - 4 products, set the attribute as PreferenceProduct and the value can be one of the 4 products based on your creative.

Survey results may take several minutes to appear in the segment after users completed the surveys.



Default Templates [2]

https://docs.aiqua.appier.com/docs/prebuilt-templates



Survey results may take several minutes to appear in the segment after users completed the surveys. 

Drives engagement with fun, reward-based interactions with the Lucky wheel template. We'll use the Lucky Wheel (Desktop) as an example to demonstrate how to customize the template, so users can spin the wheel for a chance to win prizes or offers.

Choose Lucky Wheel (Desktop) from the template list.

Customize the following settings:

Styles tab: Adjust your wheel appearance styles to match your brand and campaign.

Settings tab: Set the spin duration and the number of wheel sections to complete your design.

Actions tab: Set the Check and Action conditions to configure outcomes based on the spinner result.

Example for setting Actions for a "You win!": 

Select + Check, choose Spinner result from the first dropdown menu, then select the section that corresponds with the desired outcome, such as "You win," from the second dropdown menu to trigger actions for that specific result.

In the Actions tab, select Change view to display a message like "Congratulations! You won the prize!".

After customizing the template, save and apply the template to your campaign. Users can then spin the wheel, and actions will execute based on the spinner result.

Use the limited-time sales template with a countdown timer to create time-sensitive promotions that encourage quick purchase decisions. 

We'll use the Countdown Timer Blue (Mobile) as an example to demonstrate how to customize the settings in Creative Studio to encourage a quicker purchase. 

Choose Countdown Timer Blue (Mobile) from the template list.

In the top left, click the template's name and select Variables and formulas.

Set the end_date_time to specify countdown end date and time.

Set timezone_UTC to define the time zone in UTC.

Update the text and URL for the "Shop now" button. For more information about modifying elements and optimizing designs, see Designing Creatives. 

Save and apply the template to your campaign.



Default Templates [3]

https://docs.aiqua.appier.com/docs/prebuilt-templates



Save and apply the template to your campaign.

Use the story template to showcase multiple products or highlights in an engaging sequence. Similar to social media stories, you can effectively combine images with calls-to-action.

We'll use the Story - Promote Products as an example to demonstrate how to customize the settings in Creative Studio, highlighting product features and driving engagement through linked views.

Choose Story - Promote Products from the template list.

Configure the main view (View 0).

Upload preview images. Click on the circle to access the Settings tab.

Under the Actions tab, set the destination URL and link to the story view.

Repeat these steps to set up the remaining story images and Actions.

Configure Views 1 through 5 to customize each individual product you want to feature.

Select the view you’re customizing and click the image and upload the product image on the Settings tab.

Update the text and URL for the "Check product details" button. For more information on modifying elements and optimizing designs, see Designing Creatives.

Repeat steps above for all views to feature each product in sequence.

Save and apply the template to your campaign.

Use the promotions template to create coupon-based campaigns with promo codes, discounts, or special deals to drive conversions.

We'll use the Coupon Code (Brown) as an example to demonstrate how to customize the settings in Creative Studio and simplify promotional campaigns using unique coupon codes.

Choose Coupon Code (Brown) from the template list.

In the top left, click the template's name and select Variables and formulas. Set the coupon variable with your coupon code to make it easily accessible for users.

📘NoteCheck the coupon code's validity and redemption settings before launching the campaign.

Update the text and URL for the "Copy & shop" button. For more information on modifying elements and optimizing designs, see Designing Creatives.



Default Templates [4]

https://docs.aiqua.appier.com/docs/prebuilt-templates



Customize the text and image elements to fit your campaign's needs. For more information, see Creative Elements to learn more about how elements can be customized.

Save and apply the template to your campaign.

Updated about 2 months ago Table of Contents

Overview

Recommendation

Slider surveys

Lucky wheel

Limited-time sales

Story

Promotions



Creative Elements [0]

https://docs.aiqua.appier.com/docs/creative-elements



This guide introduces creative elements available in Creative Studio, including images, videos, and more. Each element is explained with its relevant settings, styles, and actions, to help you customize it to fit your campaign.

Button

Checkbox

Input fields

Radio

Drop-down list

Text element

Image

Video

Custom content

Wheel of fortune 

Add clickable buttons that trigger actions in your creative.

Button: Settings

SettingDescriptionElement nameA unique identifier for the button within your creative.Button textThe text displayed on the button.Accessibility labelA short description of the button for users relying on assistive technology.PlacementControls for position, size, offset, and rotation of the button.AnimationConfigure entrance animation and delay options.

Button: Styles

StyleDescriptionOpacityAdjust the transparency of the entire button element.CharacterFont type, size, color, and alignment settings for button text.BackgroundOptions for fill color or background image of the button.BordersControls for border radius, color, and thickness of the button.Rounded cornersSet the curvature for the button corners.ShadowCustomization for shadow color, offset, blur, and spread.Hover stylesAppearance when the user hovers over the button.Active stylesLook of the button when clicked.Disabled stylesAppearance when the button is inactive.

Button: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

📘NoteSee best practices for setting up an interactive button element.

Use checkboxes to select multiple options or indicate true/false choices.

Checkbox: Settings



Creative Elements [1]

https://docs.aiqua.appier.com/docs/creative-elements



Use checkboxes to select multiple options or indicate true/false choices.

Checkbox: Settings

SettingDescriptionElement nameA unique identifier for the checkbox within your creative.Checkbox textThe text displayed next to the checkbox.Accessibility labelA short description of the checkbox for users relying on assistive technology.PlacementControls for position, size, offset, and rotation of the checkbox.AnimationConfigure entrance animation and delay options.

Checkbox: Styles

StyleDescriptionOpacityAdjust the transparency of the checkbox element.CharacterFont type, size, color, and alignment settings for checkbox labels.BackgroundOptions for fill color or background image of the checkbox area.BordersControls for border radius, color, and thickness of the checkbox.ShadowCustomization for shadow color, offset, blur, and spread.Mark stylesCustomize the appearance of selected and unselected states.

Checkbox: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

Allow users to input text or other types of data.

Input fields: Settings

SettingDescriptionElement nameA unique identifier for the input field within your creative.PlaceholderText displayed before the user enters any input.Initial valueFill the field with a default value.Input typeSpecify the input type (text, email, phone, password, and others).Input requiredOption to make the field mandatory.Accessibility labelA short description of the input field for users relying on assistive technology.PlacementControls for position, size, offset, and rotation of the input field.AnimationConfigure entrance animation and delay options.



Creative Elements [2]

https://docs.aiqua.appier.com/docs/creative-elements



📘NoteSee best practices for highlighting the required input fields.

Input fields: Styles

StyleDescriptionOpacityAdjust the transparency of the entire element.CharacterFont type, size, color, and alignment settings for input text.BackgroundOptions for fill color or background image of the input field.BordersControls for border radius, color, and thickness of the input field.Rounded cornersSet the curvature for the input field corners.ShadowCustomization for shadow color, offset, blur, and spread.Validation stylesCustomize the appearance during input validation.

Input fields: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

Radio buttons allow users to select a single option from a list.

Radio: Settings

SettingDescriptionElement nameA unique identifier for the radio button group within your creative.ColumnsArrange options in multiple columns if desired.OptionsConfigure the selectable options.Initial valueSet a pre-selected option.Input requiredOption to make the field mandatory.Accessibility labelA short description of the radio button group for users relying on assistive technology.PlacementControls for position, size, offset, and rotation of the radio button group.AnimationConfigure entrance animation and delay options.

Radio: Styles

StyleDescriptionOpacityAdjust the transparency of the entire text element.CharacterFont type, size, color, and alignment settings for option labels.Mark stylesCustomize the appearance of selected and unselected states.ValidationCustomize the appearance during validation.

Radio: Actions



Creative Elements [3]

https://docs.aiqua.appier.com/docs/creative-elements



Radio: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

📘NoteSee best practices for highlighting required radio required options.

Use drop-down lists to allow users to select from a predefined set of options.

Drop-down list: Settings

SettingDescriptionElement nameA unique identifier for the drop-down list within your creative.PlaceholderEnter the text displayed when no option is selected.OptionsConfigure the selectable items.Initial valueSet a pre-selected option or show the placeholder.Input requiredMark the field as mandatory.Accessibility labelA short description of the drop-down list for users relying on assistive technology.PlacementControls for position, size, offset, and rotation of the drop-down list.AnimationConfigure entrance animation and delay options.

Drop-down list: Styles

StyleDescriptionOpacityAdjust the transparency of the entire text element.CharacterFont type, size, color, and alignment settings for drop-down text.BackgroundOptions for fill color or background image of the drop-down list.BordersControls for border radius, color, and thickness of the drop-down list.Rounded cornersSet the curvature for the drop-down list corners.ShadowCustomization for shadow color, offset, blur, and spread.Validation stylesCustomize the appearance during validation.

Drop-down list: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form



Creative Elements [4]

https://docs.aiqua.appier.com/docs/creative-elements



• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

Display written content to inform or guide users within your creative.

Text element: Settings

SettingDescriptionElement nameA unique identifier for the text element within your creative.PlacementControls for position, size, offset, and rotation of the text element.AnimationConfigure entrance animation and delay options.

Text elements: Styles

StyleDescriptionOpacityAdjust the transparency of the entire text element.Text settingsFont type, size, color, and alignment settings for the text.HyperlinkInsert hyperlinks within the text.BackgroundOptions for fill color or background image behind the text.BordersControls for border radius, color, and thickness around the text area.ShadowCustomization for shadow color, offset, blur, and spread.

Text elements: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

Image elements let you add static images to enhance visuals.

Image: Settings

SettingDescriptionElement nameA unique identifier for the image within your creative.Image uploadClick to add an image. Supported formats include PNG, JPEG, GIF, and SVG.Size optionsChoose how the image fits in the available space (Fit, Fill, Stretch, Original).Accessibility labelA short description of the image for users relying on assistive technology.PlacementControls for position, size, offset, and rotation of the image.AnimationConfigure entrance animation and delay options.

Image: Styles



Creative Elements [5]

https://docs.aiqua.appier.com/docs/creative-elements



Image: Styles

StyleDescriptionOpacityAdjust the transparency of the entire image element.BackgroundOptions for fill color or background image behind the main image.BordersControls for border radius, color, and thickness around the image.Rounded cornersSet the curvature for the image corners.ShadowCustomization for shadow color, offset, blur, and spread.

Image: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

Video elements allow you to embed video content to engage your audience within your creative.

Video: Settings

SettingDescriptionElement nameA unique identifier for the video within your creative.Video URLEnter the URL of your video file. Supports YouTube, Vimeo, and video files.Media playback optionsCustomize how your media behaves, including autoplay, control visibility, looping, muted playback, and tracking preferencesAccessibility labelA short description of the video for users relying on assistive technology.PlacementControls for position, size, offset, and rotation of the video element.AnimationConfigure entrance animation and delay options.

Video: Styles

StyleDescriptionOpacityAdjust the transparency of the entire video element.BackgroundOptions for fill color or background image behind the video player.BordersControls for border radius, color, and thickness around the video player.Rounded cornersSet the curvature for the video corners.ShadowCustomization for shadow color, offset, blur, and spread.

Video: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals



Creative Elements [6]

https://docs.aiqua.appier.com/docs/creative-elements



• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

Embed external content or custom code for flexible or unique additions.

Custom content: Settings

SettingDescriptionElement nameA unique identifier for the custom content within your creative.Custom contentEnter valid custom HTML or a URL to display external content.PlacementControls for position, size, offset, and rotation of the custom content.AnimationConfigure entrance animation and delay options.

Custom content: Styles

StyleDescriptionOpacityAdjust the transparency of the entire custom content element.BackgroundOptions for fill color or background image behind the custom content.BordersControls for border radius, color, and thickness around the custom content area.Rounded cornersSet the curvature for the custom field corners.ShadowCustomization for shadow color, offset, blur, and spread.

Custom content: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data field not equals

• Have value

• Value equals

• Value not equals

• Input is validActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

Add interactive spinning elements for gamified experiences in your creative.

Wheel of fortune: Settings



Creative Elements [7]

https://docs.aiqua.appier.com/docs/creative-elements



• Change variable

Add interactive spinning elements for gamified experiences in your creative.

Wheel of fortune: Settings

SettingDescriptionElement nameA unique identifier for the wheel within your creative.Number of spins allowedSet the allowed number of spins per user.Spin durationAdjust the length of the spin animation.ButtonEnter the text for the spin button and adjust its size.SectionsConfigure the number of wheel sections, including labels, probabilities, and image URLs.Accessibility labelA short description of the wheel for users relying on assistive technology.PlacementControls for position, size, offset, and rotation of the wheel.AnimationConfigure entrance animation and delay options.

Wheel of fortune: Styles

StyleDescriptionSection stylesAdjust typeface, color, and placement of each section labels.Section label placementSet the angle and distance for label placement.BordersControls for border radius, color, and thickness of the wheel and button.ShadowCustomization for shadow color, offset, blur, and spread.Button labelOptions to set typeface, style (bold/italic/underline), alignment, font size, and opacity.Button and pointer stylesModify colors, borders, or use custom images for the button and pointer.

Wheel of fortune: Actions

TabDescriptionSupported conditionsCheckConditions that must be met before an action is performed.• View inputs are valid

• Custom data field equals

• Custom data does not equal

• Have value

• Value equals

• Value not equals

• Input is valid

• Spinner result

• Spins countActionOperations that occur after check conditions are met.• Change view

• Exit

• Submit form

• URL redirect

• Run JavaScript

• Show/hide element

• Delay

• Run workflow

• Change variable

📘NoteSee best practices for limiting the number of spins allowed.

Updated 5 months ago Table of Contents

Overview

Button

Checkbox

Input fields

Radio

Drop-down list

Text element

Image

Video

Custom content

Wheel of fortune



Performance and Reports

https://docs.aiqua.appier.com/docs/performance-creative-studio



For campaigns created with Creative Studio, you can view the interaction report and download the submitted form data.

To view the interaction report, navigate to the campaign list, click the View performance icon of the campaign, and then click View report under interaction report.

In the interaction report, you will see the metrics of each creative view. 

The metrics are calculated based on unique sessions. This is different from how metrics are calculated in the rest of the campaign performance page and in downloaded reports.

For in-web campaigns created with Creative Studio, a unique session is defined as below.

A session starts when a user triggers an in-web campaign. 

A session ends when the user does not perform any actions on your website for over 30 minutes. 

Actions taken by the same user in the same browser tab are counted once per session. 

For in-app campaigns created with Creative Studio, a unique session is defined as below.

A session starts when a user triggers an in-app campaign. 

The session expires when: 

The user does not perform any actions inside the in-app campaign for over 30 minutes.

The in-app campaign is closed or a new in-app campaign is triggered.

Repeated actions taken by the same user inside the in-app campaign are only counted once during the same session.

In addition:

Overall usage shows interaction data for the specified time period.

Actions taken shows interaction data for the selected version during the specified time period.

For campaigns that include Submit form actions, such as a lead generation form or a survey, you can download the form data submitted by the users.

To download form data, navigate to the campaign list, click the menu icon of the campaign, and select Download form data. You will need to select a date range and click the Get download link button. The download link will be sent to the email address associated with your login account.

Here's an example of the downloaded form data.

Updated 4 months ago Table of Contents

View interaction reports

Download form data



FAQs [0]

https://docs.aiqua.appier.com/docs/creative-studio-faqs



Why can't videos autoplay when the user views the campaign, even if the "Autoplay" setting is enabled?

Why can't I see the destination page when I click a link in the creative preview?

How do I control the position of the creative on my website or app?

In the interaction report, why are the numbers different in the Stats panel?

Some browsers block videos from autoplaying when they're not muted. To avoid this issue, select both the Autoplay and Play muted boxes to allow autoplay to work more consistently.

📘NoteIn some mobile environments, YouTube videos won't autoplay until the user interacts with the video, regardless of the settings you've chosen. For details, see YouTube's IFrame API documentation.

When previewing the creative in the campaign setup page, you might click on a redirect URL in the creative preview. For example, you might click on a "Shop Now" button that redirects to your product page.

If the destination page blocks iframes, the redirect URL will not display in the preview window. Users will not encounter this issue when they click on the actual creative, but in the preview, you will see an error like this:

For in-web campaigns, if you want to return to the creative preview again from an error page or a destination page, you can click the Desktop or Mobile tab. For in-app campaigns, you can refresh the page.

To control the position of the creative on your website or app, go to Settings > Placement in the creative view.

First, click the creative view at the bottom of the page, then select the view name under the Elements tab. 

Under the Settings > Placement section of the creative view, you can use the following settings to control the position of the creative.

Anchored: Click on one of the nine boxes to set the position of the creative on the website or app.

Offset: Set the creative's distance from the website edge.

If you have multiple views in a creative, you will have to repeat the same steps for each view.



FAQs [1]

https://docs.aiqua.appier.com/docs/creative-studio-faqs



If you have multiple views in a creative, you will have to repeat the same steps for each view.

In the interaction report, the numbers in the interaction flow shows the performance of the current creative version.

If you have made different versions of your creative, you might see different performance numbers in the Stats panel on the right. In the Stats panel, the numbers include the combined overall performance of all creative versions.

To view the performance of a previous creative version in the interaction flow, select the drop-down list in the top-left corner and choose a version.

Updated 5 months ago Creative StudioTable of Contents

Why can't videos autoplay when the user views the campaign, even if the "Autoplay" setting is enabled?

Why can't I see the destination page when I click a link in the creative preview?

How do I control the position of the creative on my website or app?

In the interaction report, why are the numbers different in the statistics panel?



Campaign Performance

https://docs.aiqua.appier.com/docs/campaign-performance-overview



There are several ways to see how your AIQUA campaigns are performing. See the corresponding pages for more details.

View performance 

Export campaign performance reports

Export campaign user reports

Export form data 

The view performance page contains campaign performance data.

For regular, in-app, and in-web campaigns, you can see the performance page of individual campaigns by clicking the campaign name.

For trigger campaigns, you can see the performance page of individual campaigns by clicking the View performance icon.

You can also view performance in the campaign list

Export campaign performance reports of all campaigns under that campaign type in an XLSX file from the AIQUA Dashboard, or export reports to CSV via API.

Export campaign user report: Export a list of users who have been sent or shown a particular campaign from the AIQUA Dashboard or via API.

Export form data (In-web/in-app): Export the form data submitted by the users for in-web and in-app campaigns, such as a lead generation campaign.

Updated about 2 months ago Table of Contents

View performance

Export campaign performance reports

Export campaign user reports

Export form data



View Performance [0]

https://docs.aiqua.appier.com/docs/campaign-performance-page



For regular, in-app, and in-web campaigns, go to the campaign list, then click the campaign's name.

For other campaign types, click the View Performance icon.

The performance overview summarizes the campaign's performance metrics by date range.

📘Regular push campaignsFor regular push campaigns, you can access the performance overview by clicking the Performance tab.

In addition to adjusting the date range of the performance overview, you can also adjust the following metric display settings:

Metric settingDescriptionEvent count• Total event: Each event is counted once.

• Unique event: If a user completes the same event multiple times, the event is only counted once. The number of unique events is an approximation with a <1% margin of error. Unique event count is not supported for offline events.Online attribution settingSelect the attribution model for online events, that is, events logged via Appier SDK. The online conversions and attributed event data on this page will be based on this attribution rule.Offline attribution settingSelect the attribution model for offline events uploaded via API. The offline conversions on this page will be based on this attribution rule.

📘Note

The attribution model and event count settings selected here do not affect the campaign reports or the metrics in the campaign list. See Setting attribution model for details.

For campaigns created before February 2021, the online event count calculated using Unique Event is only available if the Last-View & Last-Click attribution model is selected.

Legacy journey maps have a different campaign performance page. Refer to Managing Journey Maps.

Refer to the sections below for the definitions of each metric. For metrics based on the count of an event, the event is listed under the Events column.

Total sent

Sent

Impressions and clicks

Conversions 

Total sent is the number of times the notification is sent by AIQUA during the entire campaign duration. This number is available in regular campaigns and trigger campaigns.



View Performance [1]

https://docs.aiqua.appier.com/docs/campaign-performance-page



The following limitations about the Total sent count apply to all channels in regular campaigns and trigger campaigns. 

The date range selected is not applied to Total sent. The count is the notifications sent during the entire campaign duration.

The Total sent count based on unique events is not provided. In other words, the Total sent count remains the same even when Event count is set to Unique event.

📘NoteThis number is only available in regular and trigger campaigns created after April 18, 2023 (00:00 UTC).

MetricsDescriptionEventsSentThe number of times a notification is sent by AIQUA.notification_sent

📘NoteIf you use shortened URLs in your campaigns, clicks and click-based attributions will not be tracked. To work around this limitation, see how to track clicks and attribution with shortened URLs.

MetricsDescriptionEventsImpressionsThe number of users who received the push notification on their devices.notification_receivedClicksThe number of times users clicked on an URL in the push.

In Android push, this is the sum of notification_clicked and actionClicked. actionClicked is tracked when the user clicks on a customized button in the Android push.Web and iOS Push:notification_clicked

Android Push:notification_clickedactionClickedCTRThe click-through rate of the campaign. CTR is defined as (Clicks / Impressions) x 100%.--

MetricsDescriptionEventsDeliveredThe number of users to whom the email campaign is successfully delivered by the email service provider.notification_deliveredOpensThe number of times the email was opened.qg_email_openedOpen RateThe open rate of the email campaign is defined as (Opens / Delivered) x 100%.--ClicksThe number of times users clicked on an URL in the email.notification_clickedCTRThe click-through rate of the campaign. CTR is defined as (Clicks / Opens) x 100%.--UnsubscribedThe number of times the users clicked on the unsubscription links in the email campaign.qg_email_unsubed

📘Note

Impressions are not supported for SMS campaigns.



View Performance [2]

https://docs.aiqua.appier.com/docs/campaign-performance-page



📘Note

Impressions are not supported for SMS campaigns.

Clicks and CTR are only supported for SMS campaigns containing an AIQUA short URL.

MetricsDescriptionEventsClicksThe number of times users clicked on an AIQUA short URL.notification_clickedCTRThe click-through rate of the campaign. CTR is defined as (Clicks / Sent) x 100%.--DeliveredThe number of times the SMS campaign is successfully delivered by the SMS service provider.notification_delivered

📘Note

Impressions are not supported for Kakao campaigns.

Clicks and CTR are only supported for Kakao campaigns containing an AIQUA short URL.

MetricsDescriptionEventsClicksThe number of times users clicked on an AIQUA short URLnotification_clickedCTRThe click-through rate of the campaign. CTR is defined as (Clicks / Sent) x 100%.--DeliveredThe number of times the Kakao campaign is successfully delivered by the Kakao service provider.notification_delivered

📘Note

Impressions count is not supported for LINE campaigns.

Tracking LINE clicks that direct to an SDK-integrated app is only supported in: 

Android SDK 7.12.0 or later

iOS SDK 7.20.0 or later

MetricsDescriptionEventsClicksThe number of times users clicked on any valid links in carousel or rich message creative that directs the user to a webpage or app embedded with Appier SDK.notification_clickedCTRThe click-through rate of the campaign. CTR is defined as (Clicks / Sent) x 100%.--

MetricsDescriptionEventsImpressionsThe number of times the campaign is shown on the website.



View Performance [3]

https://docs.aiqua.appier.com/docs/campaign-performance-page



MetricsDescriptionEventsImpressionsThe number of times the campaign is shown on the website.

If you have enabled the Experiment feature, note that the impression count of the control group is not included.qg_inweb_displayedClicksSubscription Boost: When the user clicks to allow push notifications.Fixed Banner: When the user clicks on the Action Button.Multiple Images: When the user clicks on an Image or Action Button.Multiple Actions: When the user clicks on an Action Button, where the button's "Click Action" is set to Open URL.Lead Generation: When the user submits a lead generation form.Creative Studio: When the user clicks on a creative element where element's "Action" is set to URL.

When the user submits a form by clicking on a creative element where the element's "Action" is set to Submit form.qg_inweb_clickedqg_inweb_lead_genCTRThe click-through rate of the campaign. CTR is defined as (Clicks / Impressions) x 100%.--SubmissionsLead Generation: When the user submits a lead generation form.Creative Studio: When the user submits a form by clicking on a creative element where the element's "Action" is set to Submit form.qg_inweb_lead_genSubmission RateLead Generation and Creative Studio: The submission rate of forms. Submission rate is defined as (Submissions / Impressions) x 100%.--

In-app pop-up campaigns: Performance data is automatically tracked by the SDK.

In-app inbox campaigns: Performance data is only available if you manually log inbox notification events. Refer to the following pages for details on how to log events for inbox notifications:

iOS in-app inbox notifications

Android in-app inbox notifications

MetricsDescriptionEventsImpressionsThe number of times the campaign is shown on the app.

If you have enabled the Experiment feature, note that the impression count of the control group is not included.qg_inapp_displayedClicksWhen the users click on any valid links in the creative.



View Performance [4]

https://docs.aiqua.appier.com/docs/campaign-performance-page



When the users submit a form by clicking on a creative element in Creative Studio where the element's "Action" is set to Submit form. qg_inapp_clickedqg_inapp_lead_genCTRThe click-through rate of the campaign. CTR is defined as (Clicks / Impressions) x 100%.--SubmissionsAvailable in Creative Studio only. When the users submit a form by clicking on a creative element where the element's "Action" is set to Submit form.qg_inapp_lead_genSubmission RateThe submission rate of forms. Submission rate is defined as (Submissions / Impressions) x 100%.--

📘Note

If you use shortened URLs in your campaigns, clicks and click-based attributions will not be tracked. To work around this limitation, see how to track clicks and attribution with shortened URLs.

Offline Conv is a metric that needs to be enabled by Appier Support. 

To see the channels that support offline conversion attribution, see Attribution models by channels.

Offline conversion events need to be uploaded through the Offline Event API V2.

AIQUA calculates the offline conversion count once a day using offline events with a timestamp within 90 days.

MetricsDescriptionConversionsThis is the number of online conversion events (or goal events) that happen after the users interact with the campaign.

This is based on the attribution model, attribution window, and the conversion events you have set.Offline conv.This is the number of offline conversion events that happen after the users interact with the campaign.

This is based on the attribution model, attribution window, and the conversion events you have set.CVRConversion Rate is defined by (Online conversions / Clicks) x 100%.Conv. valueIf monetary value is being tracked for the conversion events (or goal events) via valueToSum, the total value of all online conversion events (or goal events) will be displayed here.



View Performance [5]

https://docs.aiqua.appier.com/docs/campaign-performance-page



For example, if the conversion event is checkout_completed, the CONV VALUE will represent the total value associated with all checkout_completed events attributed to the campaign during the selected date range.

See the Experiment Report section below.

MetricsDefinitionAttributed EventsThis is the number of events attributed to the campaign, based on the attribution model and attribution window you have set.

Attributed events highlighted in bold are the conversion events you have selected.

Some system events such as notification_received are excluded and do not count toward Attributed Events.

Click View Details to see the event count for each attributed event.Attributed ValueIf attributed events contain valueToSum to track the monetary value associated with the event, the total value attributed to the campaign will be displayed here.

Click View Details to see the attributed value for each attributed event.

The experiment report section is available in campaigns using the following features:

Experiment feature

A/B Test in regular campaigns

In addition to the metrics listed above, the Imp. CVR and Imp. CVR Lift columns are available for some campaign types.

MetricsDefinitionSupported CampaignsImp. CVRImp-based conversion rate is defined by (Conversions / Impressions) x 100%.

A Imp-based CVR helps analyze the conversion rate of a variant over the control group. Control Group does not have click data.In-web and in-app (pop-up)Imp. CVR liftThe percent increase in the average imp-based CVR of the variants compared to the imp-based CVR of the control group.In-web and in-app (pop-up): Experiments with control group

📘Note:

For the control group, an impression is counted when the user meets the trigger rule of the campaign. 

When Event Count is set to Unique Event, the data (e.g. impression count) for each variant might not add up to the data of the Variant Total. This is because the number of unique events is an approximation with a <1% margin of error.



View Performance [6]

https://docs.aiqua.appier.com/docs/campaign-performance-page



👍Tip:For each variant, you can click the Preview icon to see what the Creative looks like.

For campaigns using A/B Test, you will see the performance data of creative A and B. 

In A/B Test campaigns, the numbers do NOT include the performance data from creatives that are sent to the remaining users after the winning creative is decided.

The winner of A/B Test is determined based on CTR. 

In push, in-web, and in-app (pop-up) campaigns, CTR is calculated by (Clicks / Impressions) x 100%.

In email campaigns using A/B Test, CTR is calculated by (Clicks / Delivered) x 100%.

(1) Use the drop-down list to select the metrics you want to see in the graphs.

(2) Hover over the graphs to see the actual value. For campaigns not using Experiment and AB Testing, there will be only 1 line graph named "Variant Total". 

(3) For campaigns using Experiment and AB Testing, use the checkboxes on the right if you only want to see the graphs for some variants only.

Updated 3 months ago Table of Contents

Opening the campaign performance page

Performance overview

Total sent

Sent

Impressions and clicks

Conversions

IMP. CVR and CVR lift

Event attributions

Experiment report

Experiment campaigns

A/B Test campaigns

Performance trend



Performance in the Campaign List

https://docs.aiqua.appier.com/docs/campaign-list-performance



In the campaign list, you can see the status and the performance of the campaign listed in the table.

The performance metrics in the campaign list are calculated based on the attribution model selected in the account setting.

For the definitions of performance metrics, refer to View Performance.

Updated about 2 months ago



Export Campaign Performance Reports [0]

https://docs.aiqua.appier.com/docs/downloading-campaign-reports



Campaign performance reports contain performance data about a single campaign type within a date range. Campaign performance reports can be exported in two ways:

Export via AIQUA dashboard (campaign list page)

Export via Report API

The campaign performance report is available for the following campaign types:

Regular campaigns: The report includes data for all campaigns that ran during the specified date range

Trigger campaigns: The report includes data for all campaigns that were toggled on during the specified date range

In-web and in-app campaigns: The report includes data for all campaigns that were active during the specified date range

Go to Campaigns and then select the campaign type.

Click Export report.

In the pop-up that appears, select the date range of the report.

Click Export. The download link for the report will be sent to the email of your login account. This report is available in XLSX format.

In addition to exporting campaign performance reports from the AIQUA dashboard, you can also programmatically export reports using the Report API. To export campaign performance reports via API, you'll need to provide the following details:

The type of campaign you'd like to export the report for (regular, trigger, in-app, or in-web)

The method to include campaigns in the report—select only one of the following:

Include campaigns by campaign ID: Specify a list of up to 5000 campaign IDs, or

Include campaigns by campaign run date: Specify a date range from which campaigns have run in, and the report will contain data for all campaigns that ran in the specified date range

Please note the following differences between the campaign performance report exported via AIQUA dashboard and via API:

Exported via AIQUA dashboard: Contains two sheets (sheet 1 and sheet 2, "Regular Campaigns Performance" and "Datewise Regular Campaigns Perf")

Exported via API: Only contains sheet 2 ("Datewise Regular Campaigns Perf")



Export Campaign Performance Reports [1]

https://docs.aiqua.appier.com/docs/downloading-campaign-reports



Exported via API: Only contains sheet 2 ("Datewise Regular Campaigns Perf")

On the AIQUA dashboard, go to the campaign list page corresponding to the type of campaign you're retrieving the ID for, i.e. regular, trigger, in-web, or in-app.

Click the pencil icon to open the campaign's edit screen.

The campaign ID can be found at the end of this page's URL, following the last /. For example, in the following URL, the campaign ID is 12345: https://aiqua.appier.com/regular_campaigns/edit/12345

There are two sheets in the downloaded report:

Sheet 1 (e.g. Regular Campaigns Performance): Provides the performance for each campaign across a date range, specified by the Report Start Date and Report End Date. Each row in the sheet represents a different campaign. 

Sheet 1

Sheet 2 (e.g. Datewise Regular Campaigns Perf): In the second sheet, the campaign's daily performance for each day is listed. Each campaign will have multiple rows with each row representing a different date, as specified in the Performance on (yyyy-mm-dd) column.

Sheet 2

Data in the reports is based on the following settings.

The date and time in the report are based on the timezone set in the Account Settings.

Performance metrics are calculated based on the following settings:

Attribution Model: Performance metrics are calculated based on the attribution models set in Account Settings.

Attribution Window: If you have changed the default attribution window, the custom attribution window will be applied. The metrics are calculated based on the attribution window you are using at the time when the data was collected.

Conversion Events:

Online conversion events: Conversion events are the events you specified under the "Conversion and Attribution > Conversion Events" setting in Account Settings. If campaign-level goal events are set, goal events will override the account-level conversion events for that campaign.



Export Campaign Performance Reports [2]

https://docs.aiqua.appier.com/docs/downloading-campaign-reports



Offline conversion events: Offline conversion events are the events you specified under the "Offline Conversion and Attribution" section in Account Settings. 

For campaigns with the Experiment or A/B Test feature enabled, the downloaded report only shows the combined performance data of all variants. Performance data of each variant is not provided.

For In-App Inbox Campaigns, data related to clicks and impressions are not available by default. To have these data, the events qg_inapp_displayed and qg_inapp_clicked need to be manually logged in the SDK. The SDK doesn't log these events by default.

The following campaign details are available. 

Column nameReport sheetDescriptionReport Start Date

Report End DateSheet 1This is the date range you selected for the report. Campaign IdSheet 1

Sheet 2The ID of the campaign. You can look up the campaign ID by clicking the Edit icon of the campaign in the Campaign List. The campaign ID can be found at the end of the url.Campaign NameSheet 1

Sheet 2The name of the campaign.Last Campaign Run Date (yyyy-mm-dd)

Last Campaign Run Time (hh:mm)Sheet 1This is the date and time when the campaign is last executed.Performance on (yyyy-mm-dd)Sheet 2The performance data of this row is based on this date.Campaign Run Time (hh:mm)Sheet 2This is the time when the campaign is last executed on that day.Last Used PlatformSheet 1

Sheet 2This is the Target Device you have selected when creating in-web campaigns. Available values are android, ios, others, where others is equivalent of "PC and other devices".ChannelSheet 1

Sheet 2This is the channel of the campaign: web_push, android_push, ios_push, email, sms, line, kakao, inweb, android_inapp, ios_inapp.Campaign TypeSheet 1

Sheet 2Available campaign types are regular, trigger, inapp, and inweb.Last Used Segment Id

Last Used Segment NameSheet 1Shows the "Include" segment last used during the date range.Last Excluded Segment Id



Export Campaign Performance Reports [3]

https://docs.aiqua.appier.com/docs/downloading-campaign-reports



Last Used Segment NameSheet 1Shows the "Include" segment last used during the date range.Last Excluded Segment Id

Last Excluded Segment NameSheet 1Shows the "Exclude" segment last used during the date range.Last Used Creative FormatSheet 1The creative format last used during the date range.Last Execution TypeSheet 1The execution type last used during the date range.

• manual: "Send Now" and "Send Manually"

• scheduled: "Set Schedule"

• scheduled_recurring: "Send Periodically"All Used Segment Id

All Used Segment Name Sheet 1Shows all include and exclude segments used in the campaign during the date range.

This number is only available in campaigns created after April 18, 2023 (UTC 00:00).

The definitions for the performance metrics in the report are listed below. 

👍Unique countA unique count column is provided for these metrics: Unique Impressions, Unique Opens, Unique Open Rate, Unique Clicks, Unique CTR, Unique Conversions, Unique CVR, Unique Soft Bounced, Unique Hard Bounced, Unique Spammed, Unique Unsubscribed, Unique Conversion: "{conversion_event_x}" Count.If a user completes the same event multiple times, the event is only counted once. The number of unique events is an approximation with a <1% margin of error.

The following columns are shown in the report for the campaign types listed under Fixed Column. The columns are listed in the table below based on the order they appear in the reports.

Column nameFixed columnDescriptionTotal SentRegular

TriggerPush / SMS / Email / LINE / Kakao: The total number of users AIQUA sends the campaign to during the entire campaign duration. The date range selected is not applied.SentRegular

TriggerPush / SMS / Email / LINE / Kakao: The number of users AIQUA sends the campaign to during the date range you have selected. This number is based on the notification_sent event.

For campaigns created before April 18, 2023 (00:00 UTC), a "--" will be displayed.DeliveredRegular



Export Campaign Performance Reports [4]

https://docs.aiqua.appier.com/docs/downloading-campaign-reports



For campaigns created before April 18, 2023 (00:00 UTC), a "--" will be displayed.DeliveredRegular

TriggerEmail / SMS / Kakao: The number of campaigns successfully delivered to the user by the Email / SMS / Kakao vendor. This number is based on the notification_delivered event.Push / LINE: This column will be empty.ImpressionsRegular

Trigger

In-web

In-appPush: The number of users who received the push notification on their devices based on notification_received.In-web: The number of times the campaign is shown on the website based on the qg_inweb_displayed event.In-app: The number of times the campaign is shown on the app based on the qg_inapp_displayed event.SMS / Email / LINE / Kakao: This column will be empty.OpensRegular

TriggerEmail: The number of times the email sent by AIQUA is opened.Push / SMS / LINE / Kakao: This column will be empty.Open RateRegular

TriggerEmail: Open Rate is defined by (Opens / Delivered) x 100%.Push / SMS / LINE / Kakao: This column will be empty.ClicksRegular

Trigger

In-web

In-appPush: The number of clicks on any valid links in the creative. In Web push and iOS push, this is based on the notification_clicked event. In Android push, this is the sum of notification_clicked event and actionClicked event.Email: The number of clicks on any valid links in the creative.LINE: The number of clicks on any valid links in carousel or rich message creative that directs the user to a webpage or app embedded with Appier SDK. This is based on the notification_clicked event.In-web: The number of clicks on any valid links in the creative, based on the qg_inweb_clicked event or the number of forms submitted based on qg_inweb_lead_gen event.In-app: The number of clicks on any valid links in the creative, based on the qg_inapp_clicked event or the number of forms submitted based on qg_inapp_lead_gen event.SMS: This column will be empty for SMS campaigns without an AIQUA short URL.Kakao: This column will be empty for Kakao campaigns without an AIQUA short URL.CTRRegular

Trigger

In-web



Export Campaign Performance Reports [5]

https://docs.aiqua.appier.com/docs/downloading-campaign-reports



Trigger

In-web

In-appPush / In-app / In-web: The click-through rate is defined as (Clicks / Impressions) x 100%.Email: The click-through rate is defined as (Clicks / Opens) x 100%.LINE: The click-through rate is defined as (Clicks / Sent) x 100%.SMS: This column will be empty for SMS campaigns without an AIQUA short URL.Kakao: This column will be empty for Kakao campaigns without an AIQUA short URL.SubmissionsIn-web

In-appIn-web: This is the number of times the user submits a form based on the qg_inweb_lead_gen event.In-app: This is the number of times the user submits a form based on the qg_inapp_lead_gen event.Campaigns without forms: This column will be empty.Submission RateIn-web

In-appThe submission rate of forms in in-web campaigns and in-app campaigns. Submission rate is defined as (Submissions / Impressions) x 100%.Campaigns without forms: This column will be empty.ConversionsRegular

Trigger

In-web

In-appPush / SMS / Kakao / Email / LINE / In-web / In-app: This is the total number of conversion events or goal events that happen within the attribution window after the users interact with the campaign. In downloaded reports, conversion is based on the attribution models selected in Account Settings page.

Refer to Understanding Event Attribution to read more about attribution window and the attribution models.CVRRegular

Trigger

In-web

In-appPush / SMS / Kakao / Email / LINE / In-web / In-app: The conversion rate is defined as (Conversion / Clicks) x 100%.Conversion ValueRegular

Trigger

In-web

In-appPush / SMS / Kakao / Email / LINE / In-web / In-app: If your conversion events or goal events contain vts to track the monetary value associated with the event, the total value attributed to the campaign will be displayed here.Offline ConversionRegular



Export Campaign Performance Reports [6]

https://docs.aiqua.appier.com/docs/downloading-campaign-reports



TriggerPush / Email / LINE / SMS / Kakao: This is the total number of offline conversion events that happen within the attribution window after the users interact with the campaign. In downloaded reports, conversion is based on the offline attribution settings in Account Settings page.

AIQUA calculates the offline conversion count once a day using offline events with a timestamp within 90 days.Offline Conversion ValueRegular

TriggerPush / Email / LINE / SMS / Kakao: If your offline conversion events contain the vts parameter to track the monetary value associated with the event, the total value attributed to the campaign will be displayed here.Soft BouncedRegular

TriggerEmail: The number of soft-bounced emails based on the qg_email_soft_bounced event.Push / SMS / LINE / Kakao: This column will be empty.Hard BouncedRegular

TriggerEmail: The number of hard-bounced emails based on the qg_email_hard_bounced event.Push / SMS / LINE / Kakao: This column will be empty.SpammedRegular

TriggerEmail: The number of emails sent that was reported as spam based on the qg_email_spammed event.Push / SMS / LINE / Kakao: This column will be empty.UnsubscribedRegular

TriggerEmail: The number of clicks on the unsubscription links in the email campaign, based on the qg_email_unsubed event.Push / SMS / LINE / Kakao: This column will be empty.ArchivedRegular

Trigger

In-web

In-appArchived campaigns are labeled as 1 and unarchived campaigns are labeled as 0.VariantsRegular

Trigger

In-web

In-appData for the Variants column is currently not available yet.

This column will be empty.

The following columns only appear in the report under the specified conditions.

To read about when an event is attributed to a campaign, see Understanding Event Attribution.

Column nameDescriptionConversion: "{conversion_event_x}" CountThe number of "conversion_event_x" attributed to the campaign.



Export Campaign Performance Reports [7]

https://docs.aiqua.appier.com/docs/downloading-campaign-reports



Column nameDescriptionConversion: "{conversion_event_x}" CountThe number of "conversion_event_x" attributed to the campaign.

If you have set up conversion events in the account settings, this column will be shown in the report for each type of conversion event, even if the count is 0.Conversions Values: "{conversion_event_x}" ValuesThe monetary value associated with "conversion_event_x" attributed to the campaign. See valueToSum.

If you have set up conversion events in the account settings, this column will be shown in the report for each type of conversion event, even if the value is 0."{attributed_event_x}" CountThe number of "attributed_event_x" attributed to the campaign.

This column will be shown in the report for each type of non-conversion event attributed to the campaigns in the report, if the count is not 0 for at least one campaign."{attributed_event_x}" ValueThe monetary value associated with attributed_event_x attributed to the campaign. See valueToSum.

This column will be shown in the report for each type of non-conversion event attributed to the campaigns in the report, if the value is not 0 for at least one campaign.Updated about 2 months ago Table of Contents

Overview

Exporting via AIQUA dashboard

Exporting via Report API

Retrieving campaign IDs

Reading the report

Limitations

Report columns

Campaign details

Campaign performance metrics



Export Campaign User Reports [0]

https://docs.aiqua.appier.com/docs/exporting-user-reports-via-dashboard



Campaign user reports contain details about users who interacted with a campaign in a certain date range. Campaign user reports can be exported in two ways:

Export via AIQUA dashboard (campaign list page)

Export via Report API

The campaign user report is supported by the following campaign types:

Regular campaigns

Trigger campaigns

In-web campaigns

In-app campaigns

Pop-up: The report is supported under default settings.

Inbox: Under default settings, the report for inbox campaigns will not include any user data.

Data is only available if the events qg_inapp_displayed and qg_inapp_clicked are manually logged. The SDK doesn't log these events by default.

📘User Report buttonThe User Report button is only available for campaigns that meet the following criteria.

Campaigns that are created after May 31, 2022.

Campaigns that have run in the past 60 days.

For Regular Campaigns, this includes campaigns that have been sent manually or sent after reaching the scheduled time.

For Trigger Campaigns, In-Web Campaigns, and In-App Campaigns, this includes campaigns that have been toggled on. The campaign's scheduled time is not considered.

After the campaign runs for the first time, it can take up to 10 minutes for the User Report button to become available. When toggling off trigger campaigns, the User Report button can be temporarily unavailable for a couple of minutes.

Go to Campaigns and then select the campaign type.

Click User Report.

In the pop-up that appears. specify the date range for the campaign report. Only data from the past 60 days can be selected.

Click Export. When the report is ready, an email containing the download link for the report will be sent to the email address associated with your login account. This report is available in CSV format.

In addition to exporting campaign user reports from the AIQUA Dashboard, you can also programmatically export reports using the Report API. To export the campaign user report via API, you'll need to specify the following details:



Export Campaign User Reports [1]

https://docs.aiqua.appier.com/docs/exporting-user-reports-via-dashboard



The campaign ID of the campaign you'd like to export the report for

The attribution model (Last-View & Last-Click, Last-View, or Last-Click) you want to use to calculate conversion-related metrics

On the AIQUA Dashboard, go to the campaign list page corresponding to the type of campaign you're retrieving the ID for, i.e. regular, trigger, in-web, or in-app.

Click Edit to open the campaign's edit screen.

The campaign ID can be found at the end of this page's URL, following the last /. For example, in the following URL, the campaign ID is 12345: https://aiqua.appier.com/regular_campaigns/edit/12345

Each row in the sheet represents a user who has been sent this campaign or has interacted with this campaign during the export time range. An interaction can include campaign delivery, impressions, opens, clicks, conversions, and email unsubscription.

If the campaign is sent to the user multiple times during the export time range, each campaign sent is a separate row in the report for that user. 

If the user has interacted with the campaign during the export time range, but the sent time is outside of the export time range, the user will be listed in report, but the Sent Time field will be empty. 

A user might complete the same type of interaction multiple times during the export time range, such as multiple clicks or multiple email opens. The report shows the time of the first interaction within the export time range in the following columns: First Delivered Time, First Impression Time, First Open Time, First Click Time, First Conversion Time.

In some scenarios, the first interaction time can be earlier than the campaign sent time.

In the example below, the user's First Open Time is from an email campaign that was sent before the export time range. As a result, the First Open Time is earlier than the Sent Time in the report.

The date and time in the report are based on the timezone set in the Account Settings.

Conversion-related data is based on the attribution model set in the Account Settings.



Export Campaign User Reports [2]

https://docs.aiqua.appier.com/docs/exporting-user-reports-via-dashboard



Conversion-related data is based on the attribution model set in the Account Settings.

If a LINE user clicks on a link in the LINE campaign that directs to a website embedded with Appier Web SDK, the click will be listed under a separate LINE user in the report. 

If the user also completes a conversion after clicking, both the click and the conversion will be listed under the second LINE user as shown in the illustration below. In the example below, you can see two LINE users with the same LINE UID but with different User IDs. The click and the conversion are listed under the second user with an empty Sent Time field.

The columns included in the report are different based on the campaign type and channel. 

The following columns in the report are related to information about the user.

Column nameCampaign typeChannelDescriptionVariantsRegular

In-web

In-appEmail

Push

In-web

In-appThis column is only available if you have enabled the Experiment feature for this campaign.

This is the name of the variant that the user was assigned to.User IDRegular

Trigger

In-web

In-appAllThis is the unique ID AIQUA assigns to users. AIQUA stores this ID using the userId parameter.Customer IDRegular

Trigger

In-web

In-appAllThis is the custom user ID used by your company (e.g. member ID from your CRM system). The data needs to be stored using the parameter name user_id.EmailRegular

TriggerEmailThis is the user's email address. The data needs to be stored using the parameter name email.Phone NoRegular

TriggerSMS

LINE

KakaoThis is the user's phone number. The data needs to be stored using the parameter name phoneNo.LINE UIDRegular

TriggerLINEThis is the user's LINE UID.IDFARegular

Trigger

In-web

In-appPush (iOS)

In-app (iOS)This is the Identifier for Advertisers of the user's iOS device.AAIDRegular

Trigger

In-web

In-appPush (Android)

In-app (Android)This is the Android Advertising ID of the user's Android device.

The following columns in the report are related to campaign delivery and performance.



Export Campaign User Reports [3]

https://docs.aiqua.appier.com/docs/exporting-user-reports-via-dashboard



The following columns in the report are related to campaign delivery and performance.

👍TipRefer to Campaign Performance for detailed definitions of the metrics for each channel.

Column nameCampaign typeChannelDescriptionDeliveredRegular

TriggerEmail

SMS

KakaoA Y value indicates that the campaign was delivered to the user during the export time range.ImpressionRegular

Trigger

In-web

In-appPush

In-web

In-appA Y value indicates that the campaign was received by the user during the export time range.OpensRegular

TriggerEmailA Y value indicates that the user opened the campaign during the export time range.ClicksRegular

Trigger

In-web

In-appEmail

LINE

Push

In-web

In-app

SMS

KakaoA Y value indicates that the user clicked on the campaign during the export time range.

See the limitations on click data for LINE users.ConversionsRegular

Trigger

In-web

In-appEmail

LINE

Push

In-web

In-app

SMS

KakaoA Y value indicates that the user completed a conversion that is attributed to this campaign during the export time range.

See the limitations on conversion data for LINE users.UnsubscribedRegular

TriggerEmailA Y value indicates that the user has clicked on an unsubscribe link in the email campaign during the export time range.

This status is based on the event qg_email_unsubed.Sent TimeRegular

TriggerEmail

SMS

LINE

Push

KakaoThis is the time when the campaign is sent to the user. This field may be empty if the sent time is outside of the export time range.First Delivered TimeRegular

TriggerEmail

SMS

KakaoThis is based on the first time the campaign is delivered to the user during the export time range.First Impression TimeRegular

Trigger

In-web

In-appPush

In-web

In-appThis is based on the first time the user received the campaign during the export time range.First Open TimeRegular

TriggerEmailThis is based on the first time the user opened the email campaign during the export time range.First Click TimeRegular

Trigger

In-web

In-appEmail

LINE

Push

In-web

In-app

SMS



Export Campaign User Reports [4]

https://docs.aiqua.appier.com/docs/exporting-user-reports-via-dashboard



Trigger

In-web

In-appEmail

LINE

Push

In-web

In-app

SMS

KakaoThis is based on the first time the user clicked the campaign during the export time range.First Conversion TimeRegular

Trigger

In-web

In-appEmail

LINE

Push

In-web

In-app

SMS

KakaoThis is based on the first time the user completes a conversion that is attributed to this campaign during the export time range.Unsubscribed TimeRegular

TriggerEmailThis is the time when the email user clicked on an unsubscribe link in the email campaign during the export time range.Updated over 1 year ago Table of Contents

Overview

Exporting via AIQUA dashboard

Exporting via Report API

Retrieving campaign IDs

How to read the report

Report columns



Download Form Data (In-Web / In-App)

https://docs.aiqua.appier.com/docs/download-form-data



For in-web and in-app campaigns that collect information from users, such as a lead generation campaign or a survey, you can download the form data submitted by the users. Form data can be downloaded for the following types of campaigns:

In-web campaigns using Lead Generation basic creatives

In-web campaigns using Creative Studio that include Submit Form actions

In-app campaigns using Creative Studio that include Submit Form actions

Go to Campaigns > In-web campaigns or Campaigns > In-app campaigns, click the vertical dots next to the campaign name, and select Export form data.

In the pop-up that appears, specify the data range and click Export. An email containing the download link for the report will be sent to the email address associated with your login account. This report is available in XSLX format.

Each row represents a form submission through this campaign. 

If you have enabled the Experiment feature for this campaign, the information collected from each variant will be a separate tab in the report.

The submitTime of the form is based on the timezone set in the Account Settings.

Here's an example of the form data from a basic lead generation campaign.

Here's an example of the form data from a Creative Studio campaign.

Updated 3 months ago Table of Contents

Overview

Downloading form data

Downloaded file



Understanding Event Attribution [0]

https://docs.aiqua.appier.com/docs/understanding-event-attribution



Attribution is the way AIQUA determines how to give credit to campaigns for the actions taken by the users. This allows you to evaluate how effective your campaigns are. For example, you can see how much your campaigns have contributed to the purchases completed on the website.

On the AIQUA dashboard, if the user interacts with a campaign and then proceeds to complete some events, these events are listed as Attributed Events. 

In addition, you can define some events as conversion events, such as checkout_completed or registration_completed, and AIQUA can show the conversions that are attributed to the campaign.

For an event to be attributed to a campaign: 

The user must have clicked or viewed the campaign before completing the event. AIQUA provides different attribution models to let you control when to attribute an event to a campaign. 

See Understanding attribution models.

See Setting attribution models.

The event must happen within the attribution window after clicking or viewing the campaign. The default attribution window is 24 hours for click-through attribution and 1 hour for view-through attribution for online events collected via Appier SDK. See Setting attribution window.

For a conversion to be attributed to a campaign, you need to define which events are conversion events and the same rules as above apply. See Setting conversion events.

AIQUA supports the following types of events for event attribution. 

Online events tracked by Appier SDK: Any user events tracked by Appier SDK except default events that are triggered by an AIQUA campaign. Campaign-related default events such as notification_clicked, qg_inapp_received, and qg_inweb_closed will not count toward attributed events.

Offline event uploaded through Offline Event API v2: The Offline conversion events you selected in Account Settings can be attributed to AIQUA campaigns. The offline events need to be uploaded through API. See Offline Event API v2.



Understanding Event Attribution [1]

https://docs.aiqua.appier.com/docs/understanding-event-attribution



Refer to the table below for the attribution models supported by different channels. Note that web push, in-web, email, and LINE campaigns share the same attribution window settings.

ChannelsOnline eventsOffline eventsPush

(web and app)Last-view model

Last-click model

Last-view & last-click model• Last-view model

• Last-click model

• Last-view & last-click model

• Click model

• View modelEmailLast-click model• Last-view model

• Last-click model

• Last-view & last-click model

• Click model

• View modelLINELast-click model • Last-click model

• Click model SMS, KakaoLast-click model

Click-based attribution is only supported for campaigns containing an AIQUA short URL (SMS, Kakao).• Last-click model

• Click modelMMS N/AN/AIn-webLast-view model

Last-click model

Last-view & last-click model

Click model (Beta)

View model (Beta)N/AIn-appLast-view model

Last-click model

Last-view & last-click modelN/A

📘Limitations

LINE, email campaigns (online data): View-through attribution is not available because impression data is not available.

Regarding the use of shortened URLs:

If you're creating your own shortened URLs, clicks and click-based attributions will not be tracked. To work around this limitation, see how to track clicks and attribution with shortened URLs.

To track clicks for SMS and Kakao campaigns, you can add an AIQUA short URL to your SMS or Kakao campaign creative on the AIQUA dashboard.

There are 5 types of attribution models.

Last-Click: An event is attributed to the campaign last clicked by the user within the attribution window.

Last-View: An event is attributed to the campaign last viewed by the user within the attribution window.

Last-View + Last-Click: An event is attributed to the campaign last viewed and the campaign last clicked by the user within the attribution window.

Click: An event is attributed to all campaigns the user clicked within the attribution window.

View: An event is attributed to all campaigns the user viewed within the attribution window.



Understanding Event Attribution [2]

https://docs.aiqua.appier.com/docs/understanding-event-attribution



View: An event is attributed to all campaigns the user viewed within the attribution window.

📘NoteThe Click model and View model are Beta features that need to be enabled by Appier Support and are currently only supported for in-web campaigns.Performance data for in-web campaigns is available starting from the following dates:

Click model, View model: Data related to attribution and conversion is available from February 15, 2022.

Last-Click model, Last-View model, Last-View + Last-Click model: Performance data is available from January 1, 2021 if the Click model and View model are enabled.

Under the Last-Click model, if the user clicks on multiple AIQUA campaigns before completing the events, the events will be attributed to the campaign the user last clicked on, as long as the events happen within the attribution window. 

In the example below, if you have selected the Last-Click model, the added_to_cart and checkout_completed events will be attributed to Campaign B.

Under the Last-View model, if the user views multiple AIQUA campaigns before completing the events, the events will be attributed to the campaign the user last viewed, as long as the events happen within the attribution window.

In the example below, if you have selected the Last-View model, the added_to_cart and checkout_completed events will be attributed to Campaign C.

Under the Last-View + Last-Click model, both clicks and views can count toward Attributed Events, but if the last-click campaign and the last-view campaign are the same campaign, the same event will only be counted as an attributed event once (not double-counted). 

In the example below, Campaign A is the last-view and last-click campaign before the user added a product to the cart. The added_to_cart event will only be attributed to Campaign A once.

If the last-click campaign and last-view campaign are different campaigns, the same event will be separately attributed once to each campaign.



Understanding Event Attribution [3]

https://docs.aiqua.appier.com/docs/understanding-event-attribution



For example, if the last-click campaign is Campaign A and the last-view campaign is Campaign B, the added_to_cart event will be attributed to campaign A once and then to campaign B once.

With the Click model, if the user clicks on AIQUA campaigns before completing the events, the events will be attributed to all campaigns the user clicked on within the attribution window. 

In the example below, if you have selected the Click model, the added_to_cart and checkout_completed events will be attributed to both Campaign A and Campaign B.

With the View model, if the user views AIQUA campaigns before completing the events, the events will be attributed to all campaigns the user viewed within the attribution window. 

In the example below, if you have selected the View model, the added_to_cart and checkout_completed events will be attributed to both Campaign B and Campaign C.

Updated 7 months ago Campaign Performance PageTable of Contents

Overview

How does AIQUA give attribution to campaigns?

Supported event types and channels

Understanding attribution models



Setting Attribution [0]

https://docs.aiqua.appier.com/docs/setting-attribution



See the below sections on how to set the attribution models, attribution window, and the conversion events. 

Setting the attribution model

Setting the attribution window

Setting conversion events

On the AIQUA dashboard, there are two places where you can adjust the attribution model for online events and offline events.

Account Settings page 

Campaign Performance page 

📘Supported models and limitationsFor details about the attribution models supported for each channel and their limitations, see Understanding Event Attribution.

In the Account Settings page, you can set the attribution model and conversion events for:

Online events: Go to the Conversion and attribution section

Offline events: Go to the Offline conversion and attribution section

Online events

Offline events

The attribution models selected in account settings affect the following:

(A) Campaign list

Online events: Conv. count and Conv value 

Offline events: Offline Conv. count and Offline Conv. value

(B) Campaign reports downloaded from the campaign list

(C) Campaign performance reports downloaded via Campaign Report API

Campaign List

📘Note:If someone changes the attribution model from the Account Settings page using your company's AIQUA account while you are on the AIQUA dashboard, the new attribution model will be reflected in the Campaign List on your browser after:

you reload the AIQUA dashboard, or

you visit the Account Settings page

On the Campaign Performance page, you can use the Metric Settings drop-down list to see how the metrics change under different attribution models. The model selected here affects the metrics related to conversions and attributed events shown on the campaign performance page for this campaign only.

Campaign Performance Page

For an event to be attributed to a campaign, the user needs to complete the event within a certain time period after viewing or clicking the campaign.



Setting Attribution [1]

https://docs.aiqua.appier.com/docs/setting-attribution



In the example below, the click-through attribution window is 24 hours while the view-through attribution window is 1 hour. The checkout_completed event is only attributed to campaign A because the user completed the event within the 24-hour click-through attribution window. Since the event happened more than one hour after the user views Campaign B, it is not attributed to campaign B.

You can adjust the attribution window for online and offline events. See the sections below.

📘NoteWeb push, in-web, email, and LINE campaigns share the same attribution window settings.

The maximum attribution window size is 30 days.

Changes to attribution window settings will only be applied to campaigns sent after the change was saved.

Channel typeDefault windowHow to adjustWeb push, in-webClick-through: 24 hr

View-through: 1 hrAdjustable via Appier SupportLINE, emailClick-through: 24 hrAdjustable via Appier SupportSMSClick-through: 24 hr

View-through: Not supported

Click-through attribution is only supported for SMS campaigns containing an AIQUA short URL.Adjustable via Appier SupportKakaoClick-through: 24 hr

View-through: Not supported

Click-through attribution is supported for Kakao campaigns containing an AIQUA short URL.Adjustable via Appier SupportAndroid push, Android in-appClick-through: 24 hr

View-through: 1 hrAdjustable via Android SDKiOS push, iOS in-appClick-through: 24 hr

View-through: 1 hrAdjustable via iOS SDK

The attribution window can be between 1 - 30 days.

The same attribution window is applied to both view-through and click-through attribution.

If you change the attribution window, the new settings will only be applied to offline events uploaded after the change. 

You can set the attribution window for offline event attribution on AIQUA dashboard. Go to Account settings > Offline conversion and attribution.

Channel TypeDefault WindowHow to adjustAll channels that support offline conversion eventsN/AAdjustable via AIQUA dashboard



Setting Attribution [2]

https://docs.aiqua.appier.com/docs/setting-attribution



Channel TypeDefault WindowHow to adjustAll channels that support offline conversion eventsN/AAdjustable via AIQUA dashboard

On the AIQUA dashboard, you can select the events you want to define as conversion at the account level and at the campaign level.

Conversion Events (Account Level): You can set one or more events as Conversion Events in the Account Settings page. The account-level conversion events selected here will be applied to all campaigns. 

Conversion-related metrics will be calculated based on the conversion events.

In the attributed event list, the conversion events are shown in bold.

Account Setting > Conversion Events

Goal Events (Campaign Level): When creating regular and trigger campaigns, you can optionally set one or more events as Goal Events for a particular campaign. If goal events are set, goal events will override the account-level conversion events for that campaign.

Conversion-related metrics will be calculated based on goal events instead of the conversion events.

In the attributed event list, the goal events are shown in bold instead of the conversion events.

Create New Campaign > Advanced

📘Note:After you set the conversion events, the new settings will be applied to the conversion-related metrics immediately.

In the Account Settings page, you can select the events you want to define as offline conversion, You can select up to five offline conversion events. The events need to be uploaded through API. See Offline Event API V2.

Updated about 2 months ago Table of Contents

Setting the attribution model

Setting the attribution window

Online events

Offline events

Setting conversion events

Online events

Offline events



Recommendation Analytics [0]

https://docs.aiqua.appier.com/docs/recommendations-20-analytics



To view the performance of your recommendations scenarios, go to the AIQUA dashboard, and in the left menu, click Recommendation > Scenario List.

📘NotePerformance analytics aren't available for recommendation scenarios placed in campaign creatives as dynamic content.

Performance data for recommendation scenarios is calculated based on the following required settings. 

Tracking recommendation clicks and impressions

Setting the attribution model and window

Setting conversion events

For details on metrics definition and downloading reports, see Performance metrics.

AIQUA needs to be tracking clicks and impressions that are attributed to Recommendation 2.0. See the details for each platform below.

PlatformsRequirementsWeb SDKMake sure the product url returned in the response is used when rendering recommendation results.

Once Recommendation 2.0 is integrated, Appier Web SDK automatically tracks clicks and impressions, but the user needs to be clicking on the product url returned in the response mentioned above.Android SDK• Android SDK 6.5.1 or above is required.

• You need to track the clicks on recommended items using this method.iOS SDK• iOS SDK 7.4.0 or above is required.

• You need to track the clicks on recommended items using this method.React Native SDK• React Native SDK 1.5.0 or above is required.

• You need to track the clicks on recommended items using this method.

For guidelines on tracking scenario clicks and impressions via REST API, see the Recommendation 2.0 REST API docs.

To set the attribution model and attribution window, go to Recommendation > Settings in the left menu.

Attribution Model: The default attribution model is Last-click model.

Last-click model: If the user clicks on multiple recommendation items before conversion, the conversion is attributed to the last clicked recommendation item (if within the attribution window).



Recommendation Analytics [1]

https://docs.aiqua.appier.com/docs/recommendations-20-analytics



First-click model: If the user clicks on multiple recommendation items before conversion, the conversion is attributed to the first clicked recommendation item (if within the attribution window).

Attribution Window: The default attribution window is 1 day. For conversions to be attributed to the recommendation item, the user needs to complete the conversion within the attribution window after clicking on the recommendation item. 

There are two ways to calculate how conversions are attributed to your recommendation scenarios: Item Conversion and Event Conversion. 

Item Conversion: Under this mode, for a conversion to be attributed to the scenario, the conversion item needs to be the same recommended item that the user clicks on within the attribution window. The conversion item needs to have the same product_id as the recommended item clicked.

Event Conversion: Under this mode, conversion events that happen within the attribution window after the user clicks on any recommended item from this scenario will be attributed to the recommendation scenario.

For example, an e-commerce selected product_purchased for item conversion, and selected checkout_completed for event conversion. 

Scenario 1: A user clicks on products X and Y, which are products recommended by scenario A. The user purchases product Q within the attribution window.

Under Item Conversion mode, no conversion is attributed to scenario A, because the product purchased does not have the same product_id as the recommended product clicked.

Under Event Conversion mode, 1 conversion (checkout_completed) is attributed to scenario A.

Scenario 2: A user clicks on products X and Y, which are products recommended by scenario A. The user purchases product X, Y, and Q in one order within the attribution window.

Under Item Conversion mode, 2 conversions (product_purchased for products X and Y) are attributed to scenario A.

Under Event Conversion mode, 1 conversion (checkout_completed) is attributed to scenario A.



Recommendation Analytics [2]

https://docs.aiqua.appier.com/docs/recommendations-20-analytics



Under Event Conversion mode, 1 conversion (checkout_completed) is attributed to scenario A.

To select the events that represent conversions for your business, go to the left menu and click Recommendation > Settings. 

You can set one or multiple events for Item Conversion mode and Event Conversion mode. 

See the table below for the list of events that can be set as conversion events for the item Conversion mode and the Event Conversion mode. 

If the event you want to use is not included in the list below, you can use custom_goal_x and custom_item_conversion_x to define your own custom events.

🚧Important:Make sure the events selected are properly collected by the Appier SDK, and the events used for item conversion need to have a product_id parameter.For example, let's say you have selected product_purchased for Item Conversion and checkout_completed for Event Conversion. If the user purchases 3 items in a single order, make sure that Appier SDK is collecting 1 checkout_completed event and 3 product_purchased events. Each product_purchased event is required to include the product_id.

Item ConversionEvent Conversionproduct_added_to_wishlistproduct_added_to_cartproduct_purchasedcontent_viewedcontent_downloadedcontent_scrolldepth_25content_scrolldepth_50content_scrolldepth_75content_scrolldepth_100content_playtime_25content_playtime_50content_playtime_75content_playtime_100content_favedcontent_sharedcontent_commentedcustom_item_conversion_1custom_item_conversion_2custom_item_conversion_3added_to_cartadded_to_wishlistcart_viewedwishlist_viewedcheckout_initiatedcheckout_step_viewedcheckout_payment_addedcheckout_completedregistration_initiatedregistration_completedlogin_completedsubscription_initiatedsubscription_completedtrial_startedtrial_endedlocation_searchedlead_submittedapplication_submittedsearchcustom_goal_1custom_goal_2custom_goal_3

In the recommendation scenario list, you can switch between these two modes and see the conversion performance under each type of conversion calculation.



Recommendation Analytics [3]

https://docs.aiqua.appier.com/docs/recommendations-20-analytics



To look at performance in the recommendation scenario list, select the performance date range and choose between Item Conversion and Event Conversion mode. The performance data shown on the scenario list is automatically updated every three hours.

Performance date range: Set the date range of the performance data you want to view. The start date and end date need to be within 180 days of the current date.

Conversion mode: Choose whether to display performance data calculated using the Item Conversion or Event Conversion setting.

The following metrics are shown:

Requests: The number of recommendation requests made to this scenario by your website, mobile app, and campaigns. Includes failed requests, requests made by campaign dynamic content, and requests from the Recommendation REST API.

Impressions: The total count of recommendation_impression events for the scenario. This is the number of times the scenario is viewed by your users. For example, if a user lands on a page embedded with a scenario that returns 5 recommended items, 1 impression would be counted, since all the items originated from a single scenario.

Clicks: The total count of recommendation_clicked events for the scenario. This is the number of times the recommended items are clicked.

For web, only clicks on the product URL returned in the response will be tracked.

For app, make sure you have set up event tracking for clicks on recommended items.

CTR (Click-through rate): This is calculated by CLICK / IMP.

Conversions: The total number of conversions attributed to the recommendation scenario. 

CVR: This is calculated by CONV / CLICKS.

Conversion value: If your conversion events contain valueToSum to track the monetary value associated with the event, the total value attributed to the recommendation scenario will be displayed here.

📘Note:The performance date range and the date in the downloaded report are based on the timezone set in the Account Settings.



Recommendation Analytics [4]

https://docs.aiqua.appier.com/docs/recommendations-20-analytics



📘Note:The performance date range and the date in the downloaded report are based on the timezone set in the Account Settings.

In the scenario list, click the scenario name to view its performance summary. On this page, you can select the conversion mode (Item conversion or Event conversion) and date range you'd like to view data for.

The scenario performance page consists of the following sections:

Performance overview 

Performance trend 

Performance lift (only available for scenarios using Autopilot) 

Model performance (only available for scenarios using Autopilot) 

Model distribution (only available for scenarios using Autopilot) 

CTR trend by model (only available for scenarios using Autopilot) 

The performance overview chart summarizes the overall performance of the scenario.

Use the performance trend chart to visualize how performance changes over time. You can select two different metrics to visualize.

You can select the following metrics from the dropdown menus:

Impressions

Clicks

CTR

Conversions

CVR

IMP CVR

Conversion value

📘Performance lift data is only available for scenarios using Autopilot for the recommendation model setting.

The performance lift, or CTR lift, is defined by the percentage increase in the CTR compared to the benchmark CTR. The benchmark CTR is the estimated CTR if traffic was evenly distributed across all models, without applying Autopilot's daily traffic redistribution.

📘Model performance data is only available for scenarios using Autopilot for the recommendation model setting.

The model performance table summarizes scenario performance metrics broken down by recommendation model.

The model distribution chart allows you to compare the traffic distribution between each recommendation model.

The CTR trend by model chart allows you to visualize the CTR trend for each model.



Recommendation Analytics [5]

https://docs.aiqua.appier.com/docs/recommendations-20-analytics



The CTR trend by model chart allows you to visualize the CTR trend for each model.

To receive performance reports via email, click Export report, specify a date range, and enter the email addresses. Performance data in reports is calculated based on whether you have selected Item Conversion or Event Conversion.

You will receive an email that includes download links for two CSV files: 

Total performance report: Shows the total performance accumulated during the specified date range for each scenario. 

Daily performance report: Shows the daily impressions, clicks, CTR, conversion count, CVR, and conversion value for each scenario. 

The metrics are counted based on the date of occurrence. In the example illustrated below, you will see two clicks and one conversion counted under March 8, and one conversion counted under March 9 in the report. Since CLICKS is 0 on March 9, and CVR is calculated by CONV / CLICKS, you will see CVR listed as "-" in the report.

Updated 5 months ago Table of Contents

Overview

Requirements

Requirement 1: Tracking recommendation clicks and impressions

Requirement 2: Setting the attribution model and window

Requirement 3: Setting conversion events

Performance metrics

Performance page

Performance overview

Performance trend

Performance lift (Autopilot scenarios)

Model performance (Autopilot scenarios)

Model distribution (Autopilot scenarios)

CTR trend by model (Autopilot scenarios)

Performance report



Analytics Studio

https://docs.aiqua.appier.com/docs/analytics-studio



📘BetaAnalytics Studio is a beta feature. Please contact your customer success manager for more details.

Analytics Studio is a powerful and intuitive tool that allows you to visualize your AIQUA data. Use Analytics Studio to easily create reports using the drag-and-drop interface to add, customize, and reposition chart widgets, allowing you to quickly turn data into actionable, data-driven insights.

Refer to the following guides to learn how to start using Analytics Studio reports:

Viewing a Report: Learn how to view an existing Analytics Studio report

Creating a Report: Learn how to create a new Analytics Studio report

Managing Reports: Learn about the operations available for Analytics Studio reports, such as pinning, renaming, and editing

👍Use the following reference guides when building your reports to learn more about the different components available in Analytics Studio reports.

Refer to the following guides for detailed descriptions about different reports components:

Chart Types: Learn about the chart types available for report widgets

Widget Templates: Learn about the prebuilt widget templates Analytics Studio provides

Data Sources: See the complete list of dimensions and metrics included in each data source

Updated 5 months ago Table of Contents

Overview

Getting started with Analytics Studio reports

Analytics Studio reference guides



Creating a Report [0]

https://docs.aiqua.appier.com/docs/analytics-studio-creating-a-report



Begin using Analytics Studio by creating a report. Go to the AIQUA Dashboard, and from the left-hand menu, go to Analytics Studio > All Reports, then follow the steps listed below:

Add a report

Add a widget to your report

Edit the widget

Preview and save the widget

Adjust the report layout

Once you've completed these steps, you'll be able to view the report at any time on the AIQUA Dashboard.

A report consists of a collection of customizable widgets, where each widget represents a single data visualization. To add a new report, go to the All Reports page and click Add Report.

Widgets are the building blocks of your report, and a single report can contain up to 20 widgets. When adding a widget into your report, you can choose from a widget template or start with a blank widget.

Use a prebuilt widget template: Use a prebuilt widget to visualize data instantly without needing to manually configure settings from scratch

Start from scratch: Start with a blank widget with no preconfigured settings

Use Analytics Studio's prebuilt widget templates to create data visualizations instantly—without needing to manually configure widget settings. Although settings are automatically populated in widget templates, you can still edit the widget for further customization.

👍To learn more about each widget template, see Widget Templates.

In the empty report you just created, drag a chart widget from the right-hand panel under Widget templates and drop it into your report.

Start with a blank widget for the most flexibility in creating your data visualization. In the empty report you just created, drag a chart widget from the right-hand panel under Chart widgets and drop it into your report.

Next, edit the widget to begin creating your custom data visualization.

After placing a new widget in your report, the widget settings panel will open on the right.

To edit an existing widget in your report, click the edit button in the top right corner of the widget, then click Edit widget.



Creating a Report [1]

https://docs.aiqua.appier.com/docs/analytics-studio-creating-a-report



To edit an existing widget in your report, click the edit button in the top right corner of the widget, then click Edit widget.

Next, configure the widget settings to fit your data visualization needs. The configurable widget settings are listed in the following sections.

The chart type determines how data will be visualized in your report. Different chart types have different required and supported settings.

To learn more about each chart type and its required settings, see Chart Types.

The data source you select for your chart determines which dimensions, date range, date range dimensions, metrics, and filters are available. 

For a full list of the fields and details about each data source, see Data Sources.

📘Supported chart typesThe date range dimension setting is only available for time series charts.

Time series charts use a date range dimension, which is a combination of the date range and dimension fields. The date range dimension is displayed on the X-axis of the chart, and is used to group data by time.

For details on setting the date range dimension's time period, see the instructions for setting the date range

Once you've selected a date range dimension, you can enable Compare to (comparisons with previous time periods)

📘Supported chart typesThe date range setting isn't available for time series charts. Time series charts use date range dimension instead.

The date range specifies the time period of the data displayed on the chart and is based on time-related data. For instance, time-related data from a data set using the Campaign performance data source includes Campaign last execution time and Performance time.

Select the time-related data you want to use, then set time period for the date range:

Click the dropdown under Date range and select which time-related field you want to use

Click Select date range and select a predefined date range (e.g. Today, Yesterday, Last 7 Days) or select a custom date range using the date picker

Click Apply.



Creating a Report [2]

https://docs.aiqua.appier.com/docs/analytics-studio-creating-a-report



Click Apply.

Once you've selected a date range, you can enable Compare to to show comparisons with previous time periods (supported chart types only).

📘Supported chart typesComparisons with previous time periods are supported for the following chart types:

Table

Scorecard

Time series

After setting a date range or date range dimension in supported chart types, you can enable Compare to to display the change in metric value between the original time period and a previous time period. The duration of the previous time period is equivalent to the duration of the date range or date range dimension you selected.

After enabling Compare to, you'll be able to select the previous time period that you'd like to compare with.

Comparison optionDescriptionExamplePrevious periodCompare the most recent time period with the preceding time period.For example, if you selected Last 7 Days for the date range or date range dimension, the comparison period will be the preceding seven-day period.

Given the following settings:

• Current date: Nov 11, 2022

• Original date range or date range dimension: Last 7 days (Nov 04, 2022 - Nov 10, 2022)

The comparison time period would be the following seven-day period: Oct 28, 2022 - Nov 03, 2022Custom start dateUse the date picker to select a custom start date for the previous time period.For example, if you selected Last 7 Days for the date range or date range dimension, the comparison period will be seven days, starting from the custom start date you select.

Given the following settings:

• Current date: Nov 11, 2022

• Original date range or date range dimension: Last 7 days (Nov 04, 2022 - Nov 10, 2022)

• Custom start date: Jul 1, 2022

The comparison time period would be the following seven-day period: Jul 1, 2022 - Jul 7, 2022



Creating a Report [3]

https://docs.aiqua.appier.com/docs/analytics-studio-creating-a-report



• Custom start date: Jul 1, 2022

The comparison time period would be the following seven-day period: Jul 1, 2022 - Jul 7, 2022

The dimension you select determines what values are used to group data in your chart. For instance, a data set from the Campaign performance data source includes dimensions such as Campaign channel, Campaign type, and Campaign name—these dimensions can be used to group data points in your chart.

For example, if you want to see the CTR for each campaign channel, select Campaign channel for the dimension and CTR for the metric.

A metric is a numerical, quantitative measurement, such a sum or percentage.

For example, if you want to see the CTR for each campaign channel, select Campaign channel for the dimension and CTR for the metric.

In addition:

You can set the display notation and decimal precision to customize how metrics are displayed in the widget

For certain chart types, metric switching and metric comparisons in the widget is available

You can set advanced settings to adjust the display notation and decimal precision of the metric displayed in the widget. To access advanced settings, click the settings icon next to the Metrics dropdown. 

SettingDescriptionDisplay notationSelecting Abbreviated for the display notation option will shorten large numbers displayed on the chart. For example:

• "1000" will be displayed as "1K" (one thousand)

• "1,000,000" will be displayed as "1M" (one million)

• "1,000,000,000" will be displayed as "1B" (one billion)Decimal placesSelect the decimal precision of the displayed metric values.

📘Supported chart typesThe options to Enable metric switching in widget and Compare 2 metrics in widget are only available for time series charts without any dimensions added.

For supported chart types, the following options for switching and comparing metrics inside a widget are available under Metric.



Creating a Report [4]

https://docs.aiqua.appier.com/docs/analytics-studio-creating-a-report



SettingDescriptionEnable metric switching in widgetAllows you to select a freely switch the metric displayed in the chart via a dropdown menu in the widget, without requiring you to edit and save the widget's settings.Compare 2 metrics in widgetOnly available if Enable metric switching in widget is select.

Allows you to select two metrics to display in the chart, which can also be selected via dropdown menu from directly within the widget, without requiring you to edit and save the widget's settings.

Add filter rules with conditions to exclude unwanted data from being displayed in a widget. To add a filter, click + Filter, then create the filtering rules you'd like to use.

Specify the maximum number of dimensions that can be displayed in a single chart to reduce clutter. For example, this option can be used to limit the number of lines in a time series chart or number of bars in a bar chart.

The default and maximum value of Display items is 20

Dimensions beyond the value set for Display items (based on the sorting order specified by the Sort by setting) won't be shown in the widget

Use a dimension or metric you selected to sort items in your chart.

Depending on the chart type being used, applying a different sorting order changes the sequence of the chart elements or the chart legend

The sorting order also determines which dimensions are excluded from the chart if the number of chart elements exceeds the maximum specified by Display items

After completing the widget settings, click Preview to see what the widget looks like with the new settings.

When you're satisfied with the settings you've chosen, save the widget with the currently configured settings by clicking Save.

Create your desired report layout by resizing and repositioning the widgets inside your report.

To reposition a widget: Click the widget, then drag and drop it to the desired position in the report

To resize a widget: Hover over the widget, then click and drag on the arrows that appear on its edges



Creating a Report [5]

https://docs.aiqua.appier.com/docs/analytics-studio-creating-a-report



To resize a widget: Hover over the widget, then click and drag on the arrows that appear on its edges

👍All changes to widget size and position are autosaved.

Reposition a widget by clicking on it, then dragging and dropping it

Resize a widget by hovering over it, then clicking and dragging on the arrows that appear on its edgesUpdated 5 months ago Managing ReportsTable of Contents

Overview

1. Add a report

2. Add a widget

Using a widget template

Starting from scratch

3. Edit the widget

Chart type

Data source

Date range dimension

Date range

Dimension

Metric

Filter

Display items

Sort by

4. Preview and save the widget

5. Adjust the report layout



Viewing a Report [0]

https://docs.aiqua.appier.com/docs/analytics-studio-viewing-a-report



You can view Analytics Studio reports at any time on the AIQUA Dashboard. In addition, you can export a report PDF for offline access. The following sections describe how to view your reports:

Opening a report

Reading report widgets

Downloading the report PDF

Reports can be accessed from the AIQUA Dashboard in two ways:

Navigating to the All Reports page

(Pinned reports only) Clicking the report name in the left-hand menu

From the left-hand menu, go to Analytics Studio > All Reports. From here, you'll be able see a list of all of your existing reports. Click on the name of the report you want to view.

👍TipSort the report list by report name, creation date, or last edited date by clicking the column you'd like to sort by.

In addition to viewing a list of all your reports in Analytics Studio from the All Reports page, you can pin up to five reports to your navigation bar for quick access.

👍TipTo learn how to pin and unpin reports from the navigation bar, see Managing Reports.

To open a pinned report, expand Analytics Studio in the left-hand menu, then click on the name of the report you'd like to view.

Analytics Studio reports consists of one or more widgets. Each widget is an independent component in the report and has various settings that determine how data is visualized, such as the data source, the chart type, dimensions, and metrics.

The following details are visible in each report widget:

The name of the widget

The date range of the displayed data

The last time the displayed data was updated

For widgets with comparisons enabled, the data for the comparison time period

In addition, for widgets using certain chart types, hovering over a data point will reveal a tooltip containing specific details.

You can download the PDF file of your report once the report has finished loading. From the All reports page, open the report you want to download, then click Download PDF to begin the download.

🚧After clicking Download PDF, please keep the report page open to avoid issues with the file download.



Viewing a Report [1]

https://docs.aiqua.appier.com/docs/analytics-studio-viewing-a-report



🚧After clicking Download PDF, please keep the report page open to avoid issues with the file download.

In addition to the report widgets, the PDF report file contains:

The name of the report

The date and time of export

A direct link to the report on the AIQUA Dashboard

Updated 5 months ago Creating a ReportTable of Contents

Overview

Opening a report

Viewing reports from the All Reports page

Viewing pinned reports

Reading report widgets

Downloading the report PDF



Managing Reports [0]

https://docs.aiqua.appier.com/docs/analytics-studio-managing-reports



To manage your reports in Analytics Studio, go to the left-hand menu on the AIQUA Dashboard, then click Analytics Studio > All Reports. The following report operations are available from the All reports page:

Add new reports

Edit and rename reports

Pin and unpin reports

Duplicate reports

Delete reports

To add a new report, go to the All reports page, click Add report, then follow the steps listed in the Creating a Report to configure report widgets and format your report.

To edit or rename a report, open the report by clicking its name from the All reports page. If the report is pinned, you can also open the report by clicking its name in the left-hand navigation bar.

Once the report is opened, you'll be able to add, delete, and edit report widgets. For details about configuring widgets, see Creating a Report.

Open the report and click on its title to activate the input field. You can directly edit the report's title and all changes will be autosaved.

For quick access, you can pin up to five reports to the left-hand menu. To identify which reports are pinned from the All reports page, look for the pin icon beside the report name. Reports can be pinned and unpinned at any time.

To pin your report and display it in the left menu, click the three vertical dots next to the unpinned report's name, and click Pin to navigation.

To unpin your report from the left menu, click the three vertical dots next to the pinned report's name, and click Unpin from navigation.

To duplicate a report, click the three vertical dots next to the report name and click Duplicate.

The duplicated report's name will have "-Copy" appended to it. For example, if your source report is named "Campaign overview", the duplicated report's name will be "Campaign overview-Copy".

To delete a report, go to the Analytics Studio > All Reports, click the three vertical dots next to the report name, and click Delete.

Updated 5 months ago Viewing a ReportTable of Contents

Overview

Adding a new report

Editing a report

Renaming a report



Managing Reports [1]

https://docs.aiqua.appier.com/docs/analytics-studio-managing-reports



Updated 5 months ago Viewing a ReportTable of Contents

Overview

Adding a new report

Editing a report

Renaming a report

Pinning and unpinning reports

Pinning a report

Unpinning a report

Duplicating a report

Deleting reports



Chart Types [0]

https://docs.aiqua.appier.com/docs/analytics-studio-chart-types



When creating a report widget, you can select a chart type based on the type of data visualization or analytics you want to achieve. Learn more about Analytics Studio's chart types in the following sections:

100% stacked area

Bar

Column

Scorecard

Table

Time series

Use a 100% stacked area chart to visualize how the contributions of different dimensions to a single metric change over time.

Each colored region corresponds to a single dimension

The area of a single dimension represents the percentage of the total metric value that the dimension contributes

The Y-axis is always scaled to 100%

Data source

Date range dimension

Metric

100% stacked area charts don't support comparisons between different time periods.

Data source

Metric

Bar charts don't support comparisons between different time periods.

Data source

Metric

Column charts don't support comparisons between different time periods.

Data source

Metric

When the Compare to option is enabled (comparison with previous time period), the change in percentage from the comparison time period is displayed underneath the score for each dimension.

For example, the following scorecard chart with comparisons enabled displays the percentage change in conversion value for each channel compared to the previous seven-day period.

Data source

Date range

Either Dimension or Metric

When the Compare to option is enabled (comparison with a previous time period), an additional column, labeled Comparison, is added to the right of the original metric. This column will display the change in percentage between the current time period and the comparison time period. 

For example, the following table chart with comparisons enabled displays the percentage change in the number clicks and CTR compared to a previous 30-day period.

A table chart with comparisons enabled

The Grand total row calculated by aggregating all the row values, e.g. total clicks, total impressions, total conversions, etc.



Chart Types [1]

https://docs.aiqua.appier.com/docs/analytics-studio-chart-types



The Grand total row calculated by aggregating all the row values, e.g. total clicks, total impressions, total conversions, etc.

For example, the grand total for the CTR metric is calculated by Total clicks / Total impressions, where:

A time series chart is useful for tracking trends over time. The X-axis represents the time interval (date range dimension) and the height of the line represents the value for each time interval (metric).

For time series charts without any dimensions added, comparisons and adding multiple metrics are supported

Adding dimensions isn't supported for time series charts with comparisons enabled

A time series chart with multiple dimensions

Data source

Date range dimension

Metric

🚧Note

Time series charts with added dimensions don't support comparisons with a previous time period (Compare to)

When Compare to is enabled in a time series chart, adding dimensions isn't supported

When the Compare to option is enabled (comparison with a previous time period), an additional dotted line of the same color is displayed on the chart to represent the comparison time period.

For example, the following time series chart shows a comparison between the total conversion value between the last seven days and a previous seven-day period.

The solid blue line represents the total conversion value for the most recent seven-day period

The dotted blue line represents the total conversion value for the preceding seven-day period

A time series chart with comparisons enabled

Where other chart types use the date range setting, time series charts use the date range dimension setting, which is a combination of the date range and dimension fields.

The date range dimension is displayed on the X-axis of the chart, and is used to group data by time

Only time-related dimensions can be selected for the date range dimension, e.g. Performance time

The steps for selecting the date range dimension's time period is identical to that of the date range setting

Updated 5 months ago Creating a ReportTable of Contents

Overview



Chart Types [2]

https://docs.aiqua.appier.com/docs/analytics-studio-chart-types



Updated 5 months ago Creating a ReportTable of Contents

Overview

100% stacked area

100% stacked area chart required settings

100% stacked area chart comparison

Bar

Bar chart required settings

Bar chart comparison

Column chart required settings

Column chart comparison

Scorecard chart required settings

Scorecard chart comparison

Table chart required settings

Table chart comparison

Table chart grand total row

Time series

Time series chart required settings

Time series chart comparison

Date range dimension



Widget Templates

https://docs.aiqua.appier.com/docs/analytics-studio-widget-templates



Use Analytics Studio's prebuilt chart templates to start visualizing data instantly without needing to manually configure chart settings. Widget templates can be added into your report and edited to fit your data visualization and reporting needs.

👍TipUse the Total conversion value template to visualize how much conversion value your campaigns generate overall.

This scorecard chart uses the Campaign performance data source to display the total conversion value of all of your AIQUA account's campaigns over the last 30 days, excluding experiment control groups. Campaign attribution is based on the last-view + last-click attribution model.

👍TipUse the Conversion value trend by campaign type to visualize how conversion values change over time across different campaign types.

This time series chart uses the Campaign performance data source to display the conversion value trend overtime by campaign type.

👍TipUse the CTR distribution by channel template to visualize how clickthrough rates (CTR) differ by campaign channel.

This bar chart uses the Campaign performance data source to compare clickthrough rates (CTR) across campaign channels.

Updated 5 months ago Creating a ReportTable of Contents

Overview

Total conversion value

Conversion value trend by campaign type

CTR distribution by channel



Data Sources [0]

https://docs.aiqua.appier.com/docs/analytics-studio-data-sources



The data source provides data for your widget and determines the available options for chart configuration settings, such as dimensions and metrics. The following data sources are available for use in Analytics Studio reports:

Campaign performance

Recommendation performance

Recommendation product analysis

Use this data source to analyze your AIQUA campaign performance.

Data retention period: This data source contains 180 days of historical data. Data older than 180 days isn't available for use.

Data refresh rate: It can take several hours for data that has been collected by AIQUA to display in your charts.

The following fields from the Campaign performance data source can be selected as a dimension in your charts:

Field nameDescriptionExample valueCampaign channel The channel of the campaign."Android Push"

"iOS Push"

"Web Push"

"Email"

"Line"Campaign ID The ID of the campaign."1234"Campaign last execution timeThe last time the campaign was run.

Only available as a dimension in table charts."2022-10-24"Campaign name The name of the campaign."My iOS push campaign"Campaign type The AIQUA campaign type."Regular"

"Trigger"

"InApp"

"InWeb"Experiment control group A boolean flag indicating whether the experiment variant is the control group.Either "true" or "false".

• "true": The experiment variant is the control group.

• "false": The experiment variant isn't the control group.Experiment variant ID The ID of the experiment variant."1234"Experiment variant name The name of the experiment variant."Variant 1"Performance timeThe time that AIQUA received the performance data.

Only available as a dimension in table charts."2022-11-02"

The following fields from the Campaign performance data source can be selected for the date range dimension or date range in your charts:

Field nameDescriptionCampaign last execution timeThe last time the campaign was run.Performance timeThe time that AIQUA received the performance data.

The following fields from the Campaign performance data source can be selected as a metric in your charts:



Data Sources [1]

https://docs.aiqua.appier.com/docs/analytics-studio-data-sources



The following fields from the Campaign performance data source can be selected as a metric in your charts:

Field nameDescriptionCampaign countThe total number of AIQUA campaigns.Clicks• Push campaigns: The number of clicks on any valid links in the creative.

• In-web campaigns: The number of clicks on any valid links in the creative, including form submissions.

• In-app campaigns: The number of clicks on any valid links in the creative.

• Email campaigns: The number of clicks on any valid links in the creative.

• LINE campaigns: The number of clicks on any valid links in carousel or rich message creatives that direct the user to an Appier SDK-integrated web page.

• SMS and Kakao campaigns: Unavailable.Conversion value

• Conversion value (last-click)

• Conversion value (last-click & last-view)

• Conversion value (last-view)• Push, email, LINE, in-web, and in-app campaigns: The total value attributed to the campaign based on the last-click attribution model.

• SMS and Kakao campaigns: Unavailable.

Conversions are based on the attribution models you selected.Conversions

• Conversions (last-click)

• Conversions (last-click & last-view)

• Conversions (last-view)• Push, email, LINE, in-web, and in-app campaigns: The total number of conversion events or goal events that occur within the attribution window after the users interact with the campaign.

• SMS and Kakao campaigns: Unavailable.

Conversions are based on the attribution models you selected. Refer to Understanding Event Attribution to learn more about the attribution window and the attribution models.CTR• Push, in-app, and in-web campaigns: The click-through rate is defined as (Clicks / Impressions) x 100%.

• Email campaign: The click-through rate is defined as (Clicks / Opens) x 100%.

• LINE campaigns: The click-through rate is defined as (Clicks / Sent) x 100%.

• SMS and Kakao campaigns: Unavailable.CVR

• CVR (last-click)

• CVR (last-click & last-view)



Data Sources [2]

https://docs.aiqua.appier.com/docs/analytics-studio-data-sources



• SMS and Kakao campaigns: Unavailable.CVR

• CVR (last-click)

• CVR (last-click & last-view)

• CVR (last-view)• Email, LINE, push, in-app, and in-web campaigns: The conversion rate is defined as (Conversion / Clicks) x 100%.

• SMS and Kakao campaigns: Unavailable.

Conversions are based on the attribution models you selected. Refer to Understanding Event Attribution to learn more about the attribution window and the attribution models.Delivered• SMS and Kakao campaigns: The number of campaigns successfully delivered to the user by the SMS/Kakao vendor.

• Email campaigns: The number of campaigns successfully delivered to the user by the email vendor.

• Push and LINE campaigns: This column will be empty.IMP CVR

• IMP CVR (last-click)

• IMP CVR (last-click & last-view)

• IMP CVR (last-view)The impression conversion rate is defined by the following calculation: (Conversions / Impressions) x 100%.

Conversions are based on the attribution models you selected. Refer to Understanding Event Attribution to learn more about the attribution window and the attribution models.Impressions• Push campaigns: The number of times users receive the push notification on their devices.

• In-web campaigns: The number of times the campaign is displayed on the website.

• In-app campaigns: The number of times the campaign is displayed in the app.

• SMS, Email, LINE, and Kakao campaigns: This column will be empty.Open rate• Email campaigns: Open rate is defined by (Opens / Delivered) x 100%.

• Push, SMS, LINE, and Kakao campaigns: This column will be empty.Opens• Email campaigns: The number of times the email sent by AIQUA is opened.



Data Sources [3]

https://docs.aiqua.appier.com/docs/analytics-studio-data-sources



• Push, SMS, LINE, and Kakao campaigns: This column will be empty.SentOnly available for push, SMS, Email, LINE, and Kakao campaigns. The total number of notifications AIQUA sent during the selected date range.Submission rateThe submission rate for in-web campaign forms. Submission rate is defined as (Submissions / Impressions) x 100%.SubmissionsThe number of times a form in an in-web campaign has been submitted. This column will be empty for in-web campaigns without forms.

AIQUA provides separate user-unique counts for certain metrics. A "unique" metric is counted once per user; even if the user completes the event multiple times, it's only counted once towards the metric total. For example, if the same user clicked a notification five times, Clicks would equal 5 and Unique clicks would equal 1.

📘For the definitions of each unique metric, see the corresponding metric in the previous table.

The following unique metrics are available for the Campaign performance data source:

Unique clicks

Unique conversions (last-click)

Unique conversions (last-view & last-click)

Unique conversions (last-view)

Unique CTR

Unique CVR

Unique CVR (last-click)

Unique CVR (last-view & last-click)

Unique CVR (last-view)

Unique delivered

Unique IMP CVR (last-click)

Unique IMP CVR (last-view & last-click)

Unique IMP CVR (last-view)

Unique impressions

Unique open rate

Unique opens

Unique sent

Unique submission rate

Unique submissions

Use this data source to analyze the performance of your AIQUA recommendation scenarios.

Data retention period: This data source contains 180 days of historical data. Data older than 180 days isn't available for use.

Data refresh rate: It takes least one day for data that has been collected by AIQUA to display in your charts.

The following fields from the Recommendation performance data source can be selected as a dimension in your charts:



Data Sources [4]

https://docs.aiqua.appier.com/docs/analytics-studio-data-sources



The following fields from the Recommendation performance data source can be selected as a dimension in your charts:

Field nameDescriptionExample valueScenario ID The ID of the recommendation scenario."2FZ3rpsKCnbYs2Z49nB6Jp"Scenario name The name of the recommendation scenario."AB_202201250044"Placement The placement of the recommendation scenario."Website or app - Cart page"Model type The recommendation model used by the scenario."Recommended for You"Performance timeThe time that AIQUA received the performance data.

Only available as a dimension in table charts."2022-11-02"

The following fields from the Recommendation performance data source can be selected for the date range dimension or date range in your charts:

Field nameDescriptionPerformance timeThe time that AIQUA received the performance data.

The following fields from the Recommendation performance data source can be selected as a metric in your charts:

Field nameDescriptionClicks The total count of recommendation_clicked events for the scenario. This is the number of times the recommended products are clicked.

• Websites: Only clicks on the product URL returned in the response will be tracked

• Mobile apps: You must implement event tracking for clicks on recommended productsConversion value (event conversion) The total conversion value attributed to the recommendation scenario based on event conversions.

Your conversion events must contain the valueToSum parameter to track the monetary value associated with the event.Conversion value (item conversion) The total conversion value attributed to the recommendation scenario based on item conversions.

Your conversion events must contain the valueToSum parameter to track the monetary value associated with the event.Conversion value per impression (event conversion) Conversion value (event conversion) / Impressions



Data Sources [5]

https://docs.aiqua.appier.com/docs/analytics-studio-data-sources



The total conversion value is based on event conversions. Your conversion events must contain the valueToSum parameter to track the monetary value associated with the event.Conversion value per impression (item conversion) Conversion value (item conversion) / Impressions

The total conversion value is based on item conversions

Your conversion events must contain the valueToSum parameter to track the monetary value associated with the eventConversions (event conversion) The total number of event conversions attributed to the recommendation scenario.Conversions (item conversion) The total number of item conversions attributed to the recommendation scenario.CTR Clicks / ImpressionsCVR (event conversion) Conversions (event conversion) / Clicks

Conversion counts are based on event conversions.CVR (item conversion) Conversions (item conversion) / Clicks

Conversion counts are based on item conversions.IMP CVR (event conversion)(Conversions (event conversion) / Impressions) x 100%

Conversion counts are based on event conversions.IMP CVR (item conversion)(Conversions (item conversion) / Impressions) x 100%

Conversion counts are based on item conversions.Impressions The total count of recommendation_impression events for the scenario. This is the number of requests made to the recommendation scenario.

For example, if a user views a page displaying 5 recommended products returned by the same request, only 1 impression is counted.

Use this data source to analyze the products recommended by your recommendation scenarios.

Data retention period: This data source contains 90 days of historical data. Data older than 90 days isn't available for use.

Data refresh rate: It can take at least one day for data that has been collected by AIQUA to display in your charts.



Data Sources [6]

https://docs.aiqua.appier.com/docs/analytics-studio-data-sources



Data refresh rate: It can take at least one day for data that has been collected by AIQUA to display in your charts.

Field NameDescriptionExample valueScenario nameThe name of the recommendation scenario."Scenario A"Scenario IDThe ID of the recommendation scenario."2FZ3rpsKCnbYs2Z49nB6Jp"PlacementThe placement of the recommendation scenario."Website or app - Cart page"Model typeThe recommendation model used by the scenario."Recommended for You"Product IDThe ID of the product from the product data feed."BB550LY1"Product titleThe title of the product from the product data feed."Brand A sneakers"Performance timeThe time that AIQUA received the performance data.

Only available as a dimension in table charts."2022-11-02"

The following fields from the Recommendation product analysis data source can be selected for the date range dimension or date range in your charts:

Field nameDescriptionPerformance timeThe time that AIQUA received the performance data.

Field NameDescriptionPerformance timeThe time that AIQUA received the performance data.ImpressionsThe number of times the recommended product was viewed.ClicksThe number of times users clicked on the recommended product.CTRClicks / ImpressionsConversions (item conversion)The total number of conversions attributed to the recommended product based on item conversions.Conversion value (item conversion)The total conversion value attributed to the recommended product based on item conversions.CVR (item conversion)Conversions (item conversion) / Clicks

Conversion counts are based on item conversions.IMP CVR (item conversion)(Conversions (item conversion) / Impressions) x 100%

Conversion counts are based on item conversions.Conversion value per impressions (item conversion)The total conversion value attributed to the recommendation scenario based on item conversions.Updated 5 months ago Creating a ReportTable of Contents

Overview

Campaign performance

Data retention and refresh rate

Dimension

Date range dimension and date range

Metric

Recommendation performance



Data Sources [7]

https://docs.aiqua.appier.com/docs/analytics-studio-data-sources



Data retention and refresh rate

Dimension

Date range dimension and date range

Metric

Recommendation performance

Data retention and refresh rate

Dimension

Date range dimension and date range

Metric

Recommendation product analysis

Data retention and refresh rate

Dimension

Date range dimension and date range

Metric



Analytics Pages

https://docs.aiqua.appier.com/docs/analytics-tab



To see how your users interact with your apps and websites, click Analytics on AIQUA dashboard to access the following options. 

Overview

User Analytics

Uninstall Analytics

Analytics about your website users is only available on the Overview page. User Analytics and Uninstall Analytics only include data about your Android and iOS app users.

Updated about 1 month ago Data SourcesOverviewDid this page help you?



Overview [0]

https://docs.aiqua.appier.com/docs/using-overview-analytics



To access Overview Analytics, go to Analytics > Overview, and choose a platform.

📘Note:

The data on this page is updated once a day. 

The time required to calculate analytics data varies depending on the data size. It may require up to 24 hours after the end of a day for data of that day to be updated.

For iOS, token validity may last up to 6 days from the uninstall date. This extended validity may impact chart data.

Select the Web tab to access the following data.

Current Subscribers: The number of Web users who are currently subscribed to Web push. Subscribed users who were unreachable during previous push campaign runs are NOT included in the count.

1 / 7 / 30 Day Active Subscribers: The number of Web subscribers who were active during the past 1, 7, or 30 days. Active is defined as users who had at least 1 event (excluding some system events such as notification_received) during the time period. 

The date range selected only applies to the Web Analytics By Users section. The Start Date and End Date must be within the past 30 days.

A. You can filter the results using the Device Type and Browser Name drop-down list. 

B. The graph shows the number of Blocked, New Users, and Subscribed on each day. 

Blocked: Users who first visited your site within the last 90 days and blocked push notifications within the Start Date and End Date.

New Users: Users who first visited your site within the Start Date and End Date.

Subscribed: Users who first visited your site within the last 90 days and subscribed to push notifications within the Start Date and End Date.

If a user subscribes to Web push and then later blocks Web push, this user is counted once for Subscribed and once for Blocked. If this user re-subscribes to Web push, the original subscription and the re-subscription only count as 1 subscribed user in the graph and will be counted under the re-subscribed date.



Overview [1]

https://docs.aiqua.appier.com/docs/using-overview-analytics



This section shows the top 10 URLS with the most page_viewed count in the past 7 days. Note that URL parameters are excluded when calculating the count, which means that https://abc.shop/?utm_source=facebook will be counted as https://abc.shop/ when calculating count.

Select the Android, iOS Production, or iOS Development tab to access the following data.

Current Users: The number of Android or iOS app users with a valid gcmId. Those who have uninstalled the app are not included.

1 / 7 / 30 Day Active Users: The number of Android or iOS app users who were active during the past 1, 7, or 30 days. Active is defined as users who had a valid gcmId and at least 1 event (excluding some system events such as notification_received) during the time period. The number may include those who have uninstalled the app, but were active users during the time period.

The Event Analytics graph shows the number of events completed by Android or iOS app users on each day.

A. Use the drop-down list to switch between event Count and Value. You can also select the data of All Events or the data of a specific event type. 

Event count data is calculated based on Total Count (instead of Unique Count).

To have event value data, the event needs to be associated with monetary value via a "valueToSum" parameter during event tracking. See how to track "valueToSum" in Android and iOS.

B. Use the drop-down list to see data breakdown by Channels or by Events.

Events: Breaks down the event count by event types. 

Channels: Breaks down the event count based on the channel that the event is attributed to. The data is calculated using the Last-View + Last-Click attribution model and the attribution window you have set. If attribution window is not set, the default click-through attribution window is 24 hours while the view-through attribution window is 1 hour.

Organic: The event is not attributed to any AIQUA campaign. 

Push: The event is attributed to an AIQUA app push campaign or in-app campaign.



Overview [2]

https://docs.aiqua.appier.com/docs/using-overview-analytics



Push: The event is attributed to an AIQUA app push campaign or in-app campaign.

Email: Currently, data is not available for this channel.

SMS: Currently, data is not available for this channel.

The User Analytics graph shows the number of Android or iOS app users on each day.

A. Use the drop-down list above the graph to select: 

Uninstalls: The number of users who uninstalled the app.

Installs: The number of users who installed the app, including re-installs.

Active Users: The number of active users. Active is defined as users who had a valid gcmId and at least 1 event (excluding some system events such as notification_received) during that day. 

B. Use the drop-down list to see data breakdown based on the following info:

Language: Breaks down data based on the language setting of the user's mobile device.

OS version: Breaks down data based on the OS version of the user's mobile device.

Install Type: Breaks down data based on whether this is the user's first install or a reinstall. Note that reinstall data is based on the user's IDFA or Advertiser ID, and therefore only available for users who allow IDFA or Advertiser ID to be tracked. See more about Apple's App Tracking Transparency policies here.

Sources: Breaks down data based on the install source (e.g. organic, Google Ads). This data requires integration with AppsFlyer or Adjust.

App Version: Breaks down data based on the app version used by the user.

The Users By Date graph shows the number of users who installed or uninstalled the app on each day.

Updated 6 months ago Table of Contents

Web

Web Analytics by Users

Top 10 Urls of Past 7 Days

Android and iOS

Event Analytics

User Analytics

Users by Date



User Analytics [0]

https://docs.aiqua.appier.com/docs/using-user-analytics



The User Analytics page shows the number and proportion of current users and uninstalled users of your Android or iOS apps.

To access User Analytics, go to Analytics > User Analytics, and choose a platform.

📘Note:

The data on this page is updated once a day. 

The time required to calculate analytics data varies depending on the data size. It may require up to 24 hours after the end of a day for data of that day to be updated.

For iOS, token validity may last up to 6 days from the uninstall date. This extended validity may impact chart data.

The first column in the table is based on the user attributes selected on the right. Use the drop-down list to further break down the Current Users and Uninstalled Users data based on different user attributes. 

Install Type: Breaks down data based on whether this is the user's first install or a reinstall. Note that reinstall data is based on the user's IDFA or Advertiser ID, and therefore only available for users who allow IDFA or Advertiser ID to be tracked. See more about Apple's App Tracking Transparency policies here.

Install Source: Breaks down data based on the install source (e.g. organic, Google Ads). This data requires integration with AppsFlyer or Adjust.

Lifecycle Stage: This feature has been deprecated.

App Version: Breaks down data based on the app version used by the user.

OS version: Breaks down data based on the OS version of the user's mobile device.

Language: Breaks down data based on the language setting of the user's mobile device.

Custom User Attributes: This feature has been deprecated.

Device Brand: Breaks down data based on the brand of the user's mobile device. (e.g. Xiaomi, Samsung)

Device Model: Breaks down data based on the model of the user's mobile device. (e.g. Pixel 5, iPhone 8)

The second and third columns in the table show the numbers and percentages of CURRENT USERS and UNINSTALLED USERS based on different attributes.



User Analytics [1]

https://docs.aiqua.appier.com/docs/using-user-analytics



Current Users: Users who have installed your Android or iOS app and have a valid gcmId. Those who have uninstalled the app are not included.

Uninstalled Users: Users who have uninstalled your Android or iOS app. 

The percentage is calculated using the the total number of users who have installed and uninstalled as the denominator.

In the example below, the Uninstalled Users who are Reinstalls are listed as "31,222 (9.81%)" . This means that 31,222 Android users have uninstalled after reinstalling your app. This number takes up 9.81% of all the Android users who have installed and uninstalled the app, regardless of First Install or Reinstall.

Updated over 1 year ago Table of Contents

Data by User Attribute

Current Users and Uninstalled Users



Uninstall Analytics [0]

https://docs.aiqua.appier.com/docs/using-uninstall-analytics



Uninstall Analytics gives you insights on your new app users by showing what percentage of them uninstall your app within 24 hours or within 30 days of app installation. Uninstall analytics is only available for your Android and iOS users.

During the first 24 hours: AIQUA checks the uninstall rate (hourly) for Android app users.

After the first 24 hours: For the next 29 days, AIQUA checks the uninstall rate (daily) for Android and iOS users.

The uninstall data is determined by the time that AIQUA detects that the user's token (gcmId) has been invalidated by FCM or APNs, which may not necessarily correspond with the user's actual uninstall time.

📘Note:

The data on this page is updated once a day. 

The time required to calculate analytics data varies depending on the data size. It may require up to 24 hours after the end of a day for data of that day to be updated.

For iOS

Token validity may continue to persist for several days after the uninstall date. This extended validity may impact chart data.

Uninstall rates are only supported after the first 24 hours. Displaying hourly uninstall rates during the first 24 hours of app installation is not supported.

To access Uninstall Analytics, go to Analytics > Uninstall Analytics, and choose a platform. 

This table shows the cumulative percentage of uninstalled users on each day during the 30 days after the user installed the app.

The following columns are available:

First Seen: The date when the users installed the app. 

New Users: The number of users who installed the app on this day. Both first installs and reinstalls are included.

1 - 30: The cumulative percentage of uninstalled users on each day during the 30 days after the First Seen date. If the column heading is 7, it corresponds to the 7th day after the user installed the app.

Let's use the image below as an example. 

On May 17, there are 5701 new users who installed the app. 

On day 1 of installing the app, 26% of these new users uninstalled the app.



Uninstall Analytics [1]

https://docs.aiqua.appier.com/docs/using-uninstall-analytics



On day 1 of installing the app, 26% of these new users uninstalled the app. 

On day 2, an additional 3% of users uninstalled, making the total percentage of uninstalled users 29%.

By day 3, 32% of these new users have uninstalled since the First Seen date.

📘Hourly uninstalls in the first 24 hours is only supported for Android.

This table shows the hourly uninstall rate during the first 24 hours after the user installed the app, as well as the total percentage of uninstalled users on that day.

The following columns are available:

Date: The date when the users installed the app. 

New Users: The number of users who installed the app on this day. Both first installs and reinstalls are included.

1 - 24: The hourly uninstall rate during the 24 hours after the user installed the app. If the column heading is 7, it corresponds to the 7th hour after the user installed the app.

Total Uninstalls: The overall uninstall rate during the first 24 hours of the users who installed the app on that date. 

Let's use the image below as an example. 

On March 17, there are 2658 new users who installed the app. 

11.3% of these new users uninstalled the app within the first hour after installing the app.

During the 2nd hour, an additional 3.2% of these new users uninstalled the app.

Updated 11 months ago Table of Contents

Overview

Uninstall Cohort Analysis by First Seen Date

Hourly Uninstalls in the First 24 Hours



Recommendation 2.0 [0]

https://docs.aiqua.appier.com/docs/recommendations-v2



📘NoteContact your customer success manager to enable this feature.

Recommendation 2.0 is AIQUA's AI-powered recommendation service. Product recommendations are generated by training AI models with user event data, user attribute data, and product data, allowing you to boost conversion rates by showing users relevant, personalized recommendations in your mobile app, website, and campaign creatives.

You can use AIQUA recommendations with one or both of the following methods:

Using the Appier SDK API: Only available for platforms supported by the Appier SDK.

Using the REST API: Available for any platform.

You can integrate with the Appier SDK to gather user event data and display product recommendations:

On your website or app: Show products recommended for each user on your website or app.

In campaign creatives: Embed personalized recommendations in your creative's dynamic content.

The Recommendation 2.0 REST API allows you to use recommendations without having to integrate the Appier SDK, giving you maximum flexibility to use recommendations in ways that best suit your needs. For example, the Recommendation 2.0 REST API on platforms without a supported Appier SDK, such as apps for smart TVs or your physical store's point-of-sale system.

📘NoteUsing recommendations in campaign creatives (via dynamic content) is not supported for REST API-enabled recommendation scenarios. To use recommendations in creatives, use the Appier SDK API to upload event data and retrieve recommendations.

By default, scenarios are only compatible with the Appier SDK API methods. Contact your customer success manager to enable the Recommendation 2.0 REST API for your scenario. REST API-enabled scenarios have the following limitations:

Appier SDK API methods for retrieving recommendations are not supported. Use the Get Recommendations endpoint instead.



Recommendation 2.0 [1]

https://docs.aiqua.appier.com/docs/recommendations-v2



Appier SDK API methods for retrieving recommendations are not supported. Use the Get Recommendations endpoint instead.

Appier SDK API methods for logging user events are not supported for collecting recommendation model training data. Use the Upload Event Data endpoint to upload an event file containing user event data.

Analytics and performance data are not natively supported for REST API-enabled scenarios. To track performance data for REST API-enabled scenarios, use the Appier SDK's event logging methods.

Before you can use Recommendation 2.0, you need to onboard your product data feed. A product data feed is a CSV file containing data about all of your products. For recommendation results to be correct, ensure that your data feed includes the fields as described in Recommendation model reference.

Upload user event data to train the recommendation model using either the SDK logging methods or the REST API.

📘Notes

Include the product ID parameter when uploading events required by recommendation models . Events without the product ID parameter won't be used to train recommendation models.

If you're using the Web SDK, we recommend setting a default designated product on every page that contains product data.

First, create a recommendation scenario to obtain a scenario ID. The scenario ID is required to use Recommendation 2.0 via SDK API or REST API.

Once your scenario has been created and the recommendation model has completed training, retrieve recommendations using either the SDK API or the REST API.

View performance and analytics data for all of your scenarios on the AIQUA Dashboard.

Updated 5 months ago Table of Contents

Overview

Using the Appier SDK API

Using the REST API

Using Recommendation 2.0

Prerequisites

1. Upload user event data

2. Create a recommendation scenario

3. Retrieve recommendations

4. View performance data



Web SDK: Recommendation 2.0 [0]

https://docs.aiqua.appier.com/docs/web-sdk-getting-recommendations-v2



Use the Web SDK's appier('getRecommendationByScenario') method to retrieve product recommendations generated by Recommendation 2.0:

appier('getRecommendationByScenario', options, callback)

ParameterTypeDescriptionoptions.scenarioIdNumberRequired. The ID of the recommendation scenario created on the AIQUA dashboard.options.user_idStringRequired if filtering out purchased products by user_id. The value that allows AIQUA to filter out purchased products across platforms based on user_id. See Filtering Recommendation Results for details.options.productIdStringRequired for some recommendation models. The product ID of the designated product, as specified in your product data feed. We recommend setting a default designated product for each page on your website that contains product data.

If a default designated product is not set, then productId must be explicitly passed in the request for valid results to be returned.options.filterObjectOptional. Contains filters based on product attributes in the data feed. Only products that match the filter conditions will be returned. See Defining API filter rules for details.options.numNumberOptional. The number of results to return, from 1-50. Default: 20.

The number of products returned may be less than the number specified if not enough products are generated.callbackFunctionOptional. The callback method.

appier(

'getRecommendationByScenario', {

scenarioId: 'j8z2LnxNHuJUFYvd637rgg',

user_id: '9afdf84f-1d55', // Required if filtering purchased product based on user_id

productId: 'p456',

filter: {

"version": 2,

"filterRule": {

"operator": "OR",

"ruleList": [{

"operator": "OR",

"conditionList": [{

"key": "price",

"operator": "lt",

"value": ["200"]

}]

}]

}

},

num: 20

},

function(err, RecommendationData, RecommendationMeta) {

// Use recommendation here

}

);

{

"items": [

{

"productId": "TEST_SKU_12",

"position": 1,

"image": "",

"title": "Mobile_12",

"description": "Phone",

"customLabel00": "Foo’s bar",

"customLabel01": "false",



Web SDK: Recommendation 2.0 [1]

https://docs.aiqua.appier.com/docs/web-sdk-getting-recommendations-v2



"title": "Mobile_12",

"description": "Phone",

"customLabel00": "Foo’s bar",

"customLabel01": "false",

"customLabel02": "100",

"customLabel03": "180.7",

"url": "",

"category": "Life , 3C > Mobile",

"currency": "TWD",

"price": "4999",

"originalPrice": "4999",

"order": "PRIMARY"

},

{

"productId": "TEST_SKU_15",

"position": 2,

"image": "",

"title": "Mobile_15",

"description": "Phone",

"customLabel00": "B&Q",

"customLabel01": "false",

"customLabel02": "50",

"customLabel03": "399.0",

"url": "",

"category": "3C , Life",

"currency": "TWD",

"price": "10999",

"originalPrice": "10999",

"order": "PINNED"

}

],

"recId": "1c1626d6-5dc7-442b-bab6-b34491d0d2f9",

"scenarioId": "",

"modelId": "39",

"debug": [],

"usedFilter": {

"version": 2,

"allowOverride": true,

"exclude": [],

"filterRule": {

"operator": "OR",

"ruleList": [

{

"operator": "OR",

"conditionList": [

{

"key": "category",

"operator": "in",

"value": [

"3C",

"Life"

],

"isCaseSensitive": false

}

]

}

]

},

"mergedFilterRules": []

},

"expType": "normal",

"respCode": "1000"

}

NameTypeDescriptionitemsObject[]A list of the recommended product results and their details.items.orderstringCan be one of the following values:

• PRIMARY: This result was generated by the scenario's specified AI model.

• FALLBACK: This result was generated by a fallback rule.

• PINNED: This result is a pinned product.

• DESIGNATED_FALLBACK: This fallback result was specified in the scenario settings under Select fallback products.modelIdstringUsed to track recommendation scenario analytics on the AIQUA dashboard.recIdstringUsed to track recommendation scenario analytics on the AIQUA dashboard.scenarioIdstringUsed to track recommendation scenario analytics on the AIQUA dashboard.usedFilterObject[]Contains the filtering rules used for this request.usedFilter.filterRuleObject[]Contains the rules specified in the API request (in the filter parameter).



Web SDK: Recommendation 2.0 [2]

https://docs.aiqua.appier.com/docs/web-sdk-getting-recommendations-v2



If no filter is provided in the API request, the rules specified in the scenario settings will be used.usedFilter.mergedFilterRuleslist• If the Append filter rules option is selected in the scenario settings: Consists of an array containing two objects representing filter rules. One object contains rules specified in the scenario settings (AIQUA dashboard) and one object contains rules specified in the API request.

• If the Append filter rules option is not selected in the scenario settings: Consists of an empty array.respCodestringCan be one of the following values:

• 1000: At least one results returned was generated by the scenario's AI model is returned.

• 1100: At least one result was returned, but results were generated from fallback rules, pinned products, or designated fallback products.

• 2000: No results returned, potentially due to filter conditions or an A/B test with no results.

To set a default designated product, define the appierRecommendationGetDefaultProductId() global function. Setting a default designed product allows you to dynamically set the product ID for all recommendation requests in that page. Completing this process will automatically injects appierRecommendationGetDefaultProductId() into options.productId if a value isn't explicitly provided in the recommendation request.

👍TipWe recommend setting a default designated product on every page that contains product data, even if the page isn't displaying a recommendation scenario currently.

Note that appierRecommendationGetDefaultProductId() must be defined before you call appier('getRecommendationByScenario'):

// Implement the global function appierRecommendationGetProductId(). This function should

// return the product ID of the default designated product.

window.appierRecommendationGetDefaultProductId = function(){

var productId

...

// Logic to assign the product ID of the default designated product to `productId`

...

return productId

}

...

// When retrieving product recommendations, appierRecommendationGetProductId() is



Web SDK: Recommendation 2.0 [3]

https://docs.aiqua.appier.com/docs/web-sdk-getting-recommendations-v2



...

return productId

}

...

// When retrieving product recommendations, appierRecommendationGetProductId() is

// automatically injected into the `options.productId` parameter if no value

// is provided

appier('getRecommendationByScenario', {}, callback)

The URL returned in the response contains parameters for click tracking. As long as users click on the URL returned by the appier('getRecommendationByScenario'), the click event will be tracked by AIQUA.

The Web SDK automatically logs a recommendation_impression event for each product whenever a non-empty recommendation response is successfully received, regardless of the number of recommended products contained in the response.

Error MessagesTroubleshootingInvalid parameter: "scenarioId" parameter is missingEnsure that options.scenarioId is present.Invalid v2 filter parameter: "filter.filterRule.ruleList" should be arrayEnsure that options.filter.filterRule.ruleList is passed as an array.Failed to serialize filter parametersEnsure that options.filter has the correct format. See Defining API filter rules for details.Wrong ParametersEnsure that you've included the correct parameters in the function call.Scenario not foundCheck that the scenario ID is correct and that the scenario is unarchived.Internal server errorPlease contact Appier Support.Strategy V2 not readyTry again later. If the same error keeps happening, please contact Appier Support.Failed to get recommendationTry again later. If the same error keeps happening, please contact Appier Support.Invalid filter parameter: "exclude" should be string arrayCheck the exclude format of filter passed in the SDK function. It should be a string array.Invalid parameter: "user_id" should be string or numberEnsure that user_id is passed as a String or Number.Updated about 1 year ago Table of Contents

Overview

Sample request

Sample response

(Recommended) Setting a default designated product

Tracking clicks and impressions

Tracking clicks

Tracking impressions

Troubleshooting



Android SDK: Recommendation 2.0 [0]

https://docs.aiqua.appier.com/docs/android-sdk-recommendation-20



The Android SDK provides several API methods to retrieve product recommendations generated by Recommendation 2.0. 

Before using the API methods to fetch product recommendations, complete the following:

Complete the required setup for the Appier Android SDK

Create a recommendation scenario

Retrieve the scenarioId for the recommendation scenario

In addition, the status of the scenario must be Ready, indicating that the recommendation model has completed training, before recommendation results can be retrieved.

📘Note

The product ID you pass into the request must match the product ID specified in your product data feed

getRecommendationWithScenarioId() with the productId parameter is only supported in Android SDK 6.5.1 or later

/**

* Recommendation v2

* Get Recommendation data using a Scenario created in your dashboard

* and using some optional query parameters. If the ScenarioId is null

* or invalid, the response of the Completion callback will be null.

*

* @param scenarioId ScenarioId for the scenario created

* @param productId productId for the query

* @param queryParameters filter condition or other query parameters

* @param completion Completion callback with the recommendation data

*/

public void getRecommendationWithScenarioId(String scenarioId,

String productId,

JSONObject queryParameters,

CompletionHandler completion)

📘NotegetRecommendationWithScenarioId() without the productId parameters is only supported in Android SDK 6.5.0 or later.

/**

* Recommendation v2

* Get Recommendation data using a Scenario created in your dashboard

* and using some optional query parameters. If the ScenarioId is null

* or invalid, the response of the Completion callback will be null.

*

* @param scenarioId ScenarioId for the scenario created

* @param queryParameters productId as pid or filter condition or other query parameters

* @param completion Completion callback with the recommendation data

*/

public void getRecommendationWithScenarioId(String scenarioId,

JSONObject queryParameters,

CompletionHandler completion)



Android SDK: Recommendation 2.0 [1]

https://docs.aiqua.appier.com/docs/android-sdk-recommendation-20



*/

public void getRecommendationWithScenarioId(String scenarioId,

JSONObject queryParameters,

CompletionHandler completion)

🚧DeprecatedThis method is deprecated—we recommend using getRecomendationWithScenarioId() with the productId parameter.

This method returns a single JSONArray containing the recommended products. Fields required for tracking click events (scenarioId, modelId, and recId) on recommended products aren't included in the response.

📘NoteThis version of getRecommendationWithScenarioId() is only supported in Android SDK 6.1.0 or later.

/**

* Recommendation v2

* Get Recommendation data using a Scenario created in your dashboard

* and using some optional query parameters. If the ScenarioId is null

* or invalid, the response of the Completion callback will be null.

*

* @param scenarioId ScenarioId for the scenario created

* @param queryParameters product Id as pid or filter condition or other query parameters

* @param completion Completion callback with the recommendation data

*

* @deprecated reason this method is deprecated 



* use {@link #getRecommendationWithScenarioId(String, JSONObject, CompletionHandler)} instead

*/

@Deprecated

public void getRecommendationWithScenarioId(String scenarioId,

JSONObject queryParameters,

Completion completion)

The following example uses the recommended method of retrieving Recommendation 2.0 results—getRecommendationWithScenarioId() with the productId parameter.

scenarioId: The scenario ID of the recommendation scenario retrieved from the AIQUA Dashboard.

productId: Required by some recommendation models. See Recommendation model reference for a list of all models and the data they require.

queryParameters: A JSON object containing optional query parameters.

completion: The completion handler that will handle the response.

queryParameters is a JSON object containing optional query parameters that you can use to specify what type of recommendation results you want to receive. 

user_id: Required if you want to exclude products the user already purchased.



Android SDK: Recommendation 2.0 [2]

https://docs.aiqua.appier.com/docs/android-sdk-recommendation-20



user_id: Required if you want to exclude products the user already purchased.

num: Specifies the maximum number of recommended products to be returned. If the number of available products is less than num, all available products will be returned. The default value is 20 and the maximum value is 50.

filter: An object containing filtering rules to be applied to recommendation results. In the following example, only products with a product category equal to "3C > Mobile" will be returned. To learn more about creating recommendation filters, see Defining API filter rules.

{

"version": 2,

"filterRule": {

"operator": "OR",

"ruleList": [

{

"operator": "AND",

"conditionList": [

{

"key": "category",

"value": [

"3C > Mobile"

],

"operator": "in",

}

]

}

]

}

}

completion is the CompletionHandler you've implemented to handle responses from the Recommendation 2.0 service.

String scenarioId = "";

String productId = "";

JSONObject queryParameters = new JSONObject();

try {

// Example filter string

String filterString = "{\"version\":2,\"filterRule\":{\"operator\":\"OR\",\"ruleList\":[{\"operator\":\"AND\",\"conditionList\":[{\"key\":\"category\",\"value\":[\"3C > Mobile\"],\"operator\":\"in\"}]}]}}";

JSONObject filter = new JSONObject(filterString);

queryParameters.put("num", 3);

queryParameters.put("user_id", "");

queryParameters.put("filter", filter);

} catch (JSONException e) {

Log.e(LOG_TAG, "Generate JSON query exception", e);

}

QG.getInstance(mContext).getRecommendationWithScenarioId(

scenarioId,

productId,

queryParameters,

new CompletionHandler() {

@Override

public void onComplete(JSONObject response) {

if (response != null) {

Log.d(LOG_TAG, "Recommendation response: " + response.toString());

} else {

Log.d(LOG_TAG, "Recommendation response: null response");

}

}

});

val scenarioId = ""

val productId = ""

val queryParameters = JSONObject()

try {

// Example filter string

val filterString = """

{

"version": 2,

"filterRule": {



Android SDK: Recommendation 2.0 [3]

https://docs.aiqua.appier.com/docs/android-sdk-recommendation-20



val queryParameters = JSONObject()

try {

// Example filter string

val filterString = """

{

"version": 2,

"filterRule": {

"operator": "OR",

"ruleList": [

{

"operator": "AND",

"conditionList": [

{

"key": "category",

"value": [

"3C > Mobile"

],

"operator": "in"

}

]

}

]

}

}

""".trimIndent()

val filter = JSONObject(filterString)

queryParameters.put("num", 3)

queryParameters.put("user_id", "")

queryParameters.put("filter", filter)

} catch (e: JSONException) {

Log.e(LOG_TAG, "Generate JSON query exception", e)

}

QG.getInstance(context).getRecommendationWithScenarioId(

scenarioId,

productId,

queryParameters,

(CompletionHandler { response: JSONObject? ->

if (response != null) {

Log.d(LOG_TAG, response.toString())

} else {

Log.d(LOG_TAG, "null response")

}

})

)

{

"items": [

{

"productId": "TEST_SKU_16",

"position": 2,

"image": "",

"title": "Mobile_16",

"description": "hTC",

"customLabel00": "Foo’s bar",

"customLabel01": "false",

"customLabel02": "-10",

"customLabel03": "200.65",

"customLabel04": "",

"url": "",

"category": "3C > Mobile",

"currency": "TWD",

"price": "5999",

"originalPrice": "5999",

"order": "PRIMARY"

... // optional fields are not listed

}

...

],

"recId": "8c4d2657-5a0e-4b77-aa25-e22fa5ba5633",

"scenarioId": "Aj2MMx5KHzPau2pv4aQ26i",

"modelId": "5",

"expType": "normal",

"respCode": "1000",

...

}

recId, scenarioId, modelId, and productId: These IDs are used to track clicks on recommended products.

items: An array containing the recommendation results.

To log click events on recommended products, call logRecommendationClicked() with the parameters obtained from the recommendation response (scenarioId, modelId, productId, and recId).

public void logRecommendationClicked(String scenarioId, String modelId, String productId, String recommendationId)

fun logRecommendationClicked(scenarioId: String, modelId: String, productId: String, recommendationId: String)



Android SDK: Recommendation 2.0 [4]

https://docs.aiqua.appier.com/docs/android-sdk-recommendation-20



fun logRecommendationClicked(scenarioId: String, modelId: String, productId: String, recommendationId: String)

The following example demonstrates how to log a click event for a recommended product.

try {

String scenarioId = response.getString("scenarioId");

String modelId = response.getString("modelId");

String recId = response.getString("recId");

JSONArray items = response.getJSONArray("items");

JSONObject product = items.getJSONObject(index);

String productId = product.getString("productId");

QG.getInstance(context).logRecommendationClicked(scenarioId, modelId, productId, recId);

} catch (JSONException e) {

Log.e(LOG_TAG, "JSON query exception", e);

}

try {

val scenarioId = response.getString("scenarioId")

val modelId = response.getString("modelId")

val recId = response.getString("recId")

val items = response.getJSONArray("items")

val product = items.getJSONObject(index)

val productId = product.getString("productId")

getInstance(context).logRecommendationClicked(scenarioId, modelId, productId, recId)

} catch (e: JSONException) {

Log.e(LOG_TAG, "JSON query exception", e)

}

The Android SDK automatically logs a recommendation_impression event whenever a non-empty recommendation response is successfully received, regardless of the number of recommended products contained in the response.Updated 4 months ago Table of Contents

Overview

Prerequisites

Fetching recommendations

(Recommended) With productId

Without productId

(Deprecated) Returning recommended products only

Usage (with productId)

Parameters

Sample request

Sample response

Tracking clicks and impressions

Tracking clicks

Tracking impressions



iOS SDK: Recommendation 2.0 [0]

https://docs.aiqua.appier.com/docs/ios-sdk-recommendation-20



Recommendation can be fetched using the below function. To successfully fetch the recommended products, be sure to first create a recommendation scenario on AIQUA dashboard and obtain a scenarioId.

There are two methods provided by the SDK.

Here, productId can be directly passed as a parameter to get more precise recommendation. However, this productId is an optional parameter and can be passed as nil if required. Refer to the Sample Response below for detailed spec.

📘Note

The product ID you pass into the request must match the product ID specified in your product data feed

getRecommendationWithScenarioId() with the productId parameter is only supported in iOS SDK 7.5.0 and later

/*!

@abstract

Returns recommendation data with 2.0 url for the user with scenario Id, product Id and query parameters

*/

- (void)getRecommendationWithScenarioId:(NSString *)scenarioId

withProductId:(NSString *)productId

withQueryParameters:(NSDictionary * _Nullable)queryStringDict

withCompletionHandler:(void (^)(id _Nullable response))completion;

This method can be used similar to the first method but it does not have productId parameter. It is recommended to use method 1 above in all the use cases. 

📘Note:This method is supported in iOS SDK versions 7.4.0 and above.

/*!

@abstract

Returns recommendation data with 2.0 url for the user with scenario Id and query parameters

*/

- (void)getRecommendationWithScenarioId:(NSString *)scenarioId 

withQueryParameters:(NSDictionary * _Nullable)queryStringDict 

withCompletionHandler:(void (^)(id _Nullable response))completion;

Below is a sample request using method 1 above with productId and category filter.

Use the scenario ID generated on AIQUA dashboard.

The user_id is required if you are filtering out purchased products based on user_id. See here for details.

The productId is required for some recommendation models. See Recommendation model reference for a list of all models and the data they require.



iOS SDK: Recommendation 2.0 [1]

https://docs.aiqua.appier.com/docs/ios-sdk-recommendation-20



filter: An object containing filtering rules to be applied to recommendation results. In the following example, only products with a product category equal to "3C > Mobile" will be returned. To learn more about creating recommendation filters, see Defining API filter rules.

You can use num to specify the maximum number of the recommended products that can be returned.

If the number of available products is less than num, all available products will be returned.

The maximum of num is 50. If num is larger than 50, 50 products will be returned at most.

If num is not specified, the default is 20 products.

let parameters: [String:Any] = [

"num": 10,

"user_id": "9afdf84f-1d55", // Required if filtering purchased product based on user_id

"filter": [

"version": 2, // Required

"filterRule": [

"operator": "OR",

"ruleList": [

[

"operator": "OR",

"conditionList": [

[

"key": "category",

"value": [

"3C > Mobile"

],

"operator": "in"

]

]

]

]

]

]

]

let scenarioId = "2t7koCuCDGqBtLMxXXXXXX"

let productId = "SKU_12435"

QGSdk.getSharedInstance().getRecommendationWithScenarioId(scenarioId, withProductId:productId, withQueryParameters: parameters, withCompletionHandler: { response in

if response != nil {

// Process response here

}

})

NSDictionary *parameters = @{

@"num": @10,

@"user_id": @"9afdf84f-1d55", // Required if filtering purchased product based on user_id

@"filter": @{

@"version": @2, // Required

@"filterRule": @{

@"operator": @"OR",

@"ruleList": @[

@{

@"operator": @"OR",

@"conditionList": @[

@{

@"key": @"category",

@"value": @[

@"3C > Mobile"

],

@"operator": @"in"

}

]

}

]

}

}

};

NSString *scenarioId = @"2t7koCuCDGqBtLMxXXXXXX";

NSString *productId = @"SKU_12435";

[[QGSdk getSharedInstance] getRecommendationWithScenarioId:scenarioId withProductId:productId withQueryParameters:parameters withCompletionHandler:^(id _Nullable response) {

if (response) {

// Process response here

}

}];



iOS SDK: Recommendation 2.0 [2]

https://docs.aiqua.appier.com/docs/ios-sdk-recommendation-20



if (response) {

// Process response here

}

}];

The response returns the recId, scenarioId, modelId, and productId. You will need these IDs to track clicks on the recommended products. 

All recommended products will be included in the items key.

{

"items": [

{

"productId": "TEST_SKU_16",

"position": 2,

"image": "",

"title": "Mobile_16",

"description": "hTC",

"customLabel00": "Foo’s bar",

"customLabel01": "false",

"customLabel02": "-10",

"customLabel03": "200.65",

"customLabel04": "",

"url": "",

"category": "3C > Mobile",

"currency": "TWD",

"price": "5999",

"originalPrice": "5999",

"order": "PRIMARY"

... // optional fields are not listed

}

...

],

"recId": "8c4d2657-5a0e-4b77-aa25-e22fa5ba5633",

"scenarioId": "Aj2MMx5KHzPau2pv4aQ26i",

"modelId": "5",

"expType": "normal",

"respCode": "1000",

...

}

To log click events on recommended products, call the following method and pass in parameters obtained from the recommendation response (scenarioId, modelId, productId, and recId).

func logRecommendationClicked(scenarioId: String, 

modelId: String,

productId: String,

recommendationId: String)

- (void)logRecommendationClickedWithScenarioId:(NSString *)scenarioId

withModelId:(NSString *)modelId

withProductId:(NSString *)productId

withRecommendationId:(NSString *)recommendationId;

The following example demonstrates how to log a click event for a recommended product.

let sId = response["scenarioId"]

let modelId = response["modelId"]

let rId = response["recId"]

let items = response["items"]

let firstProduct = items?.firstObject()

let productId = firstProduct?["productId"] as? String

QGSdk.getSharedInstance().logRecommendationClicked(

withScenarioId: sId,

withModelId: modelId,

withProductId: productId,

withRecommendationId: rId)

NSString *sId = response[@"scenarioId"];

NSString *modelId = response[@"modelId"];

NSString *rId = response[@"recId"];

NArray *items = response[@"items"];

NSDictionary *firstProduct = [items firstObject];



iOS SDK: Recommendation 2.0 [3]

https://docs.aiqua.appier.com/docs/ios-sdk-recommendation-20



NSString *rId = response[@"recId"];

NArray *items = response[@"items"];

NSDictionary *firstProduct = [items firstObject];

NSString *productId = firstProduct[@"productId"];

[[QGSdk getSharedInstance] logRecommendationClickedWithScenarioId:sId 

withModelId:modelId

withProductId:productId

withRecommendationId:rId];

The iOS SDK automatically logs a recommendation_impression event whenever a non-empty recommendation response is successfully received, regardless of the number of recommended products contained in the response.Updated 4 months ago Table of Contents

Methods available

Method 1: With product ID parameter (Recommended)

Method 2: Without product ID parameter

Sample request

Sample response

Tracking clicks and impressions

Tracking impressions



React Native SDK: Recommendation 2.0 [0]

https://docs.aiqua.appier.com/docs/react-native-sdk-recommendation-20



The React Native SDK provides several API methods to retrieve product recommendations generated by Recommendation 2.0. 

Before using the API methods to fetch product recommendations, complete the following:

Complete the required setup for the Appier React Native SDK

Create a recommendation scenario

Retrieve the scenarioId for the recommendation scenario

In addition:

Your app must be using React Native SDK 1.5.0 or later

The status of the scenario must be Ready, indicating that the recommendation model has completed training, before recommendation results can be retrieved

Use getRecommendation() to fetch recommendation results. This method returns a Promise, and the recommendation results will be returned to the resolve() function as a JSON object. Refer to the following sections for the sample request and response.

async function getRecommendation(scenarioId, productId, parameters)

Parameter nameData typeNullableDescriptionscenarioIdstringNoThe scenario ID of the recommendation scenario retrieved from the AIQUA Dashboard.productIdstringYesRequired by some recommendation models. See Recommendation model reference for a list of all models and the data they require.

The product ID you pass into the request must match the product ID specified in your product data feed.parametersJSON objectYesA JSON object containing optional query parameters. See parameters for a detailed description of this object.

parameters is a JSON object containing optional query parameters that you can use to specify what type of recommendation results you want to receive.

user_id: Required if you want to exclude products the user already purchased.

num: Specifies the maximum number of recommended products to be returned. If the number of available products is less than num, all available products will be returned. The default value is 20 and the maximum value is 50.



React Native SDK: Recommendation 2.0 [1]

https://docs.aiqua.appier.com/docs/react-native-sdk-recommendation-20



filter: An object containing filtering rules to be applied to recommendation results. In the following example, only products with a product category equal to "3C > Mobile" will be returned. To learn more about creating recommendation filters, see Defining API filter rules.

{

"version": 2,

"filterRule": {

"operator": "OR",

"ruleList": [

{

"operator": "AND",

"conditionList": [

{

"key": "category",

"value": [

"3C > Mobile"

],

"operator": "in",

}

]

}

]

}

}

var scenarioId = '';

var productId = '';

var parameters = {

filter: {

"version": 2,

"filterRule": {

"operator": "OR",

"ruleList": [

{

"operator": "AND",

"conditionList": [

{

"key": "category",

"value": [

"3C > Mobile"

],

"operator": "in",

"isCaseSensitive": false

}

]

}

]

}

},

user_id: '',

num: 10

}

RNAiqua.getRecommendation(scenarioId, productId, parameters)

.then(result => Alert.alert('Success', JSON.stringify(result)), 

error => Alert.alert('Failure', JSON.stringify(error)));

{

"items": [

{

"productId": "TEST_SKU_16",

"position": 2,

"image": "",

"title": "Mobile_16",

"description": "hTC",

"customLabel00": "Foo’s bar",

"customLabel01": "false",

"customLabel02": "-10",

"customLabel03": "200.65",

"customLabel04": "",

"url": "",

"category": "3C > Mobile",

"currency": "TWD",

"price": "5999",

"originalPrice": "5999",

"order": "PRIMARY"

... // optional fields are not listed

}

...

],

"recId": "8c4d2657-5a0e-4b77-aa25-e22fa5ba5633",

"scenarioId": "Aj2MMx5KHzPau2pv4aQ26i",

"modelId": "5",

"expType": "normal",

"respCode": "1000",

...

}

recId, scenarioId, modelId, and productId: These IDs are used to track clicks on recommended products.

items: An array containing the recommendation results.

To log click events on recommended products, call logRecommendationClicked() with the parameters obtained from the recommendation response (scenarioId, modelId, productId, and recId).



React Native SDK: Recommendation 2.0 [2]

https://docs.aiqua.appier.com/docs/react-native-sdk-recommendation-20



function logRecommendationClicked(scenarioId, modelId, productId, recommendationId)

🚧modelId data typePlease note that modelId is returned as string in the recommendation response, but it must be converted to Number before being passed into logRecommendationClicked().

The following example demonstrates how to log a click event for a recommendation product.

RNAiqua.logRecommendationClicked('Aj2MMx5KHzPau2pv4aQ26i', 12, 'TEST_SKU_1', 'recId');

The React Native SDK automatically logs a recommendation_impression event whenever a non-empty recommendation response is successfully received.Updated 12 months ago Table of Contents

Overview

Prerequisites

Fetching recommendations

parameters

Sample request

Sample response

Tracking clicks and impressions

Tracking clicks

Tracking impressions



Flutter SDK: Recommendation 2.0 [0]

https://docs.aiqua.appier.com/docs/flutter-recommendation-20



The Flutter SDK provides several API methods to retrieve product recommendations generated by Recommendation 2.0.

Before using the API methods to fetch product recommendations, complete the following:

Integrate your app with the Appier Flutter SDK

Create a recommendation scenario

Retrieve the scenarioId for the recommendation scenario

In addition, the status of the scenario must be Ready, indicating that the recommendation model has completed training.

Fetch product recommendations using getRecommendation(). This method returns a Future instance of type Map containing the recommended products. If an error occurs, a String error will be thrown indicating the reason.

Future?> getRecommendation(String scenarioId, {String? productId, Map? parameters})

getRecommendation() takes in the following parameters:

scenarioId: Required. The recommendation scenario's ID. See Creating a Scenario.

productId: Required for some recommendation models. See Recommendation model reference for a list of all models and the data they require. The product ID you pass into the request must match the product ID specified in your product data feed.

parameters: Optional parameters.

user_id: Required if you want to exclude products the user already purchased.

num: Specifies the maximum number of recommended products to be returned. If the number of available products is less than num, all available products will be returned. The default value is 20 and the maximum value is 50.

filter: An object containing filtering rules to be applied to recommendation results. In the following example, only products with a product category equal to "3C > Mobile" will be returned. To learn more about creating recommendation filters, see Defining API filter rules.

{

"version": 2,

"filterRule": {

"operator": "OR",

"ruleList": [

{

"operator": "AND",

"conditionList": [

{

"key": "category",

"value": [

"3C > Mobile"

],

"operator": "in",

}

]

}

]

}

}

// Example filter string



Flutter SDK: Recommendation 2.0 [1]

https://docs.aiqua.appier.com/docs/flutter-recommendation-20



{

"key": "category",

"value": [

"3C > Mobile"

],

"operator": "in",

}

]

}

]

}

}

// Example filter string

var filterString = '{"version":2,"filterRule":{"operator":"OR","ruleList":[{"operator":"AND","conditionList":[{"key":"category","value":["3C > Mobile"],"operator":"in"}]}]}}';

var filter = jsonDecode(filterString);

var scenarioId = '';

var productId = '';

AppierFlutter.getRecommendation(

scenarioId,

productId: productId,

parameters: {

'num': 1,

'user_id': '',

'filter': filter,

},

).then((data) {

print('Recommendation items: $data');

}).catchError((dynamic error) {

print('Recommendation error: ${error as String}');

});

{

"items": [

{

"productId": "TEST_SKU_16",

"position": 2,

"image": "",

"title": "Mobile_16",

"description": "hTC",

"customLabel00": "Foo’s bar",

"customLabel01": "false",

"customLabel02": "-10",

"customLabel03": "200.65",

"customLabel04": "",

"url": "",

"category": "3C > Mobile",

"currency": "TWD",

"price": "5999",

"originalPrice": "5999",

"order": "PRIMARY"

... // optional fields are not listed

}

...

],

"recId": "8c4d2657-5a0e-4b77-aa25-e22fa5ba5633",

"scenarioId": "Aj2MMx5KHzPau2pv4aQ26i",

"modelId": "5",

"expType": "normal",

"respCode": "1000",

...

}

recId, scenarioId, modelId, and productId: IDs used to track clicks on recommended products.

items: An array containing the recommendation results.

To log click events on recommended products, call logRecommendationClicked() with the parameters obtained from the recommendation response (scenarioId, modelId, productId, and recId).

Future logRecommendationClicked(String scenarioId, int modelId, String productId, String recId)

🚧modelId data typeNote that the modelId is returned as a string by the Recommendation API, and must be converted to int before being passed it into logRecommendationClicked().

The following example demonstrates how to log a click event for a recommended product.



Flutter SDK: Recommendation 2.0 [2]

https://docs.aiqua.appier.com/docs/flutter-recommendation-20



The following example demonstrates how to log a click event for a recommended product.

AppierFlutter.logRecommendationClicked('Aj2MMx5KHzPau2pv4aQ26i', 12, 'TEST_SKU_1', 'recId');

The Flutter SDK automatically logs a recommendation_impression event whenever a non-empty recommendation response is successfully received.Updated about 1 year ago Table of Contents

Overview

Prerequisites

Fetching recommendations

Sample request

Sample response

Tracking clicks and impressions

Tracking clicks

Tracking impressions



Getting Started with the Recommendation 2.0 API [0]

https://docs.aiqua.appier.com/reference/recommendation-getting-started



Recommendation 2.0 uses AI models trained with user event data to generate tailored product recommendations. The Recommendation 2.0 REST API is an alternate way of uploading user event data and retrieving product recommendations without needing to use the Appier SDK.

Use the REST API if you want more flexibility when using product recommendations. For example, you might want to use the REST API over the SDK methods if:

You're developing for a platform without a supported Appier SDK (e.g. apps for smart TVs). The Recommendation 2.0 REST API is the only way to retrieve recommendations for these types of apps.

You want to retrieve recommendation results in an offline setting; for example, if you're integrating your physical store's point of sale system with Recommendation 2.0. 

Recommendation 2.0Using SDK MethodsUsing the REST APISupported platformsOnly available for platforms supported by one of the following Appier SDKs:

Appier Web SDK

Appier iOS SDK

Appier Android SDK

Appier React Native SDK

Supported on any device that can make an HTTP request.

For devices on platforms without an Appier SDK (e.g. smart TV), the REST API is the only available way to retrieve recommendations.Event dataEvent data logged using the SDK is automatically used to train recommendation models.To begin uploading event data for REST API-enabled scenarios, please contact Appier Support (ess_support@appier.com).Retrieving product recommendations Call the recommendation method from the appropriate Appier SDK:

Appier Web SDK

Appier iOS SDK

Appier Android SDK

Appier React Native SDK

Appier Flutter SDK

Make an HTTP request to Get Recommendations.

📘PrerequisitesBefore using the Recommendation 2.0 REST API, complete the following steps:

Complete the product data feed onboarding process.

Create a Recommendation scenario on the AIQUA dashboard.

Contact your customer success manager to enable the Recommendation 2.0 REST API for the scenario(s) you created.



Getting Started with the Recommendation 2.0 API [1]

https://docs.aiqua.appier.com/reference/recommendation-getting-started



Contact your customer success manager to enable the Recommendation 2.0 REST API for the scenario(s) you created.

Work with your customer success manager to define an event schema for each event type you want to upload.

After you've completed the product data feed onboarding process, created a Recommendation scenario, and enabled the Recommendation 2.0 REST API, you can upload event data and get product recommendation results.

To begin uploading event data for REST API-enabled scenarios, please contact Appier Support (ess_support@appier.com).

Recommendation results are available after you upload valid event data and the recommendation model has completed its training, which can take up to two days. If you're uploading event data for the first time, recommendation results won't be available until the model has finished training.

Make a request to the Get Recommendations endpoint to get product recommendations. The JSON response contains:

A single list of recommended products and their metadata.

Metadata associated with the recommendation request; for example, the scenario ID and the filter rule(s) used.

📘NoteRecommendation scenario analytics are not supported for platforms without an Appier SDK.

Tracking clicks and impressions for recommendation scenarios requires the use of Appier SDK event logging methods. Performance data will be visible on the AIQUA dashboard under Recommendation > Scenario List. To learn more, see Recommendation Analytics.

Use the Appier SDK methods to log the recommendation_impression and recommendation_clicked events:

Appier Web SDK

Appier iOS SDK

Appier Android SDK

Appier React Native SDK

Appier Flutter SDK

Event name

Description

Event parameters

recommendation_impression

Log this event to track an impression on a recommendation scenario.



model_id: Required. The value of modelId included in the response from

Get Recommendations.

recommendation_id: Required. The value of recId included in the response from

Get Recommendations.



Getting Started with the Recommendation 2.0 API [2]

https://docs.aiqua.appier.com/reference/recommendation-getting-started



Get Recommendations.

recommendation_id: Required. The value of recId included in the response from

Get Recommendations.



scenario_id: Required. The value of scenarioId included in the response from

Get Recommendations.



user_id: Optional. The identifier of the user who initited the event.



recommendation_clicked

Log this event to track a click on a recommendation scenario.



model_id: Required. The value of modelId included in the response from

Get Recommendations.

recommendation_id: Required. The value of recId included in the response from

Get Recommendations.



scenario_id: Required. The value of scenarioId included in the response from

Get Recommendations.



product_id: Required. The value of productId included in the response from

Get Recommendations.



user_id: Optional. The identifier of the user who initited the event.



Table of Contents

Overview

Recommendation 2.0: SDK vs REST API

API usage

1. Upload event data

2. Get product recommendation results

Performance and analytics

SDK event logging methods



Creating a Scenario [0]

https://docs.aiqua.appier.com/docs/creating-scenario-recommendation-20



You can create a recommendation scenario for your website, app, and campaign creatives (dynamic content). Use recommendation scenario settings to specify:

Where you want to display recommendations

Which AI model you'd like to use to generate product recommendations

Advanced settings, such as filtering, fallback settings, and result shuffling

👍TipCreate separate recommendation scenarios for each placement and use case. For example, the settings for a scenario used in an e-commerce landing page may be different from the settings used for an email campaign creative.

Follow the steps below to create a recommendation scenario:

Create a new scenario 

Choose a placement 

Choose a recommendation model 

(Optional) Create filters 

(Optional) Configure advanced settings 

Implement the scenario in your website, app, or creative 

After creating the scenario, you can view the manage the scenario and view scenario analytics on the AIQUA dashboard.

On the AIQUA dashboard, navigate to Recommendation > Scenario list, then click Create scenario. Input a name for the scenario.

Choose where you'll be displaying the recommendation results. Note that the placement can't be changed after creating the scenario.

Website or app: Show recommendation results on your website or app. If you select this option, a dropdown will appear and you can select the type of page you want to display recommendation results in.

Dynamic content in creative: Show recommendation results as dynamic content in a campaign creative.

Recommendation models are AI models that train on data such as user events and your product data feed to generate product recommendation results that are most likely to be relevant to your target audience. 

There are two options:

Autopilot

Select a model

👍To learn more about AIQUA's recommendation models, the different model categories, and how results are generated, see Recommendation models.

📘The Autopilot option is only supported when the placement is set to Website or app.



Creating a Scenario [1]

https://docs.aiqua.appier.com/docs/creating-scenario-recommendation-20



📘The Autopilot option is only supported when the placement is set to Website or app.

Under the Autopilot mode, AIQUA automatically chooses several AI models that are suitable for the page type you have selected and distributes a portion of the website or app traffic to each model. AIQUA will continuously adjust the traffic distribution for each model to optimize recommendation performance. In other words, AIQUA will distribute more users to models that are performing well, and fewer users to models that are not doing well.

To use autopilot, it is required to have at least one of these events: product_viewed, product_added_to_cart, product_purchased

For optimal results, it is highly recommended to have the other data listed below as well.

TypeDataEvent• product_viewed

• product_added_to_cart

• product_purchasedProduct data feed• image

• title

• category

• descriptionAPI request parameter• productId

(include the product ID of the designated product in the recommendation API request)

To learn more about required data for recommendation models, see Recommendation Models. 

To select a model on your own, click Select a model and click Add AI Model to open the model selection panel. From the model selection panel, you can pick a recommendation model from one of AIQUA's top suggested models, or you can pick one from the full selection of recommendation models.

AIQUA automatically suggests recommendation models that generally have the best performance based on the placement you selected and places them at the top of the model selection panel.

If you don't want to use one of the AIQUA-suggested models, you can select your preferred model from the full selection of models. To make it easier to find a specific model, you can search for a model by its name and filter by its category.

Click on the links below to learn more about each recommendation model category:

User-Based

Product-Based

Popularity

Advanced

Build Your Own



Creating a Scenario [2]

https://docs.aiqua.appier.com/docs/creating-scenario-recommendation-20



User-Based

Product-Based

Popularity

Advanced

Build Your Own

Each model has different requirements for the data it requires to train properly, for example, certain types of event data, fields in the product data feed, or API request parameters. To see what type of data is required by the recommendation model, hover over the model's name in the selection panel.

To learn more about the required data for recommendation models, see Recommendation Models. 

You can apply filters to only show recommendation results that satisfy your filtering rules. For example, you can create a filter to only show products that belong to the category "jacket" or only show products where the discounted price is under $100.

To filter results, select Apply filter rules. You can set the filter rules directly on the AIQUA dashboard by selecting Define filter rules and adding the filter conditions. See Filtering Recommendation Results for more details on filtering recommendation results.

Further customize the scenario's results based on your specific needs, for example, you can:

Pin specific products to guarantee that the scenario always serves those products.

Set fallback rules or fallback products that should be served if the scenario is unable to generate enough AI-recommended results.

Enable shuffling to introduce more variety in recommendation results.

For details on configuring these settings, see Advanced scenario settings. 

After clicking Save to finish creating your scenario, its status will change to Preparing. Once the model finishes training and the status changes to Ready, the scenario will begin serving results.

📘NoteRecommendation models may require several days to complete training, depending on the size of your product data feed and the specific model your scenario is using.

Next, copy the scenario ID. The scenario ID will be required to use the scenario in your website, app, or campaign creative.

With the scenario ID, your developers can retrieve recommendation results on your website or mobile app.



Creating a Scenario [3]

https://docs.aiqua.appier.com/docs/creating-scenario-recommendation-20



With the scenario ID, your developers can retrieve recommendation results on your website or mobile app.

👍You can edit the scenario's settings on the AIQUA dashboard without requiring code modifications.

Use the scenario ID to generate the syntax for campaign creative dynamic content. Refer to Dynamic Content - Based on Recommendation for instructions on displaying recommendations in campaign creatives.

The following advanced settings are available to further customize the scenario's results:

Exclude duplicate products 

Add pinned products

Fallback product rule

Shuffle recommended products

This feature allows you to prevent duplicate or similar products from showing up in users' recommendation results. Here are some typical ways to use this feature. 

You can use this feature to diversify the recommendation results. Let's say on your homepage, you want to show products from different categories. You can deduplicate based on product category so that the recommendation results only include up to one product from each category.

You may have products that are essentially the same item, just different colors or sizes. You can exclude duplicate products based on a product attribute.

For example, there are three entries of "Everyday Classic Knit Top" in the product data feed to indicate the different colors available. If you want to prevent multiple entries of "Everyday Classic Knit Top" from being displayed in the user's recommendation results, you can deduplicate based on the product name field.

Product IDProduct NameDescriptionP111222-WHTEveryday Classic Knit TopEveryday classic knit top in white.P111222-BLUEveryday Classic Knit TopEveryday classic knit top in blue.P111222-PNKEveryday Classic Knit TopEveryday classic knit top in pink.



Creating a Scenario [4]

https://docs.aiqua.appier.com/docs/creating-scenario-recommendation-20



To set this up, select Exclude duplicate products and add at least one product attribute, such as the product name, product category, or product description. If you add more than one product attribute, the products will only be deduplicated if they have identical values for both fields. 

You can pin up to 20 products in the recommendation results. This feature can be used when you have products you want to highlight and always display in the results.

Select Add pinned products and enter the product ID of the product you want to pin. The product ID must be an exact match (case-sensitive) with the productId value in the product data feed. Invalid or duplicate product IDs will be dropped from the recommendation results.

Pinned products are displayed first when the recommendation results are not being shuffled. When results are being shuffled, pinned products will be shuffled with the rest of the products generated by the model. Refer to Shuffle recommended products to see how shuffling works.

📘Note

Pinned products will be displayed regardless of the filter rules set. Filter rules are not applied to pinned products.

Pinned products will not be displayed if they are out of stock (based on the availability field in product feed).

Fallback products are the products that will be displayed when the recommendation model does not generate enough recommended products for your placement. Common reasons for not generating enough results include not having the required training data, or not having a designated product for product-based models.

Choose a fallback product rule for this scenario.

Apply default fallback rules: When not enough products are generated by the model, the default fallback rules will be applied. For more details, see default fallback rules.

Select fallback products: When not enough products are generated by the model, the designated fallback products will be displayed first, followed by the products from the default fallback rules.



Creating a Scenario [5]

https://docs.aiqua.appier.com/docs/creating-scenario-recommendation-20



You can specify up to 20 fallback products by entering the product ID of the fallback products.

The product ID must be an exact match (case-sensitive) with the productId value in the product data feed. Invalid or duplicated product IDs will be dropped from the recommendation results.

Filter rules are not applied to designated fallback products. 

Fallback products will not be displayed if they are out of stock (based on the availibility field in product feed).

Don't add fallback products: When not enough products are generated by the model, no fallback products will be displayed and the default fallback rules will be ignored. An example of when you might want to use this option is if you're using a "Similar Products" model and don't want to display products that are not similar to the designated product.

To provide variety when displaying recommendation results, you can choose to randomize the order of the results. If the scenarios generate a larger set of recommended products than what is requested, a subset from that larger set is randomly selected and returned. Shuffling results exposes users to different product recommendations each time they view a page or campaign, potentially improving scenario performance. 

Choose a shuffling rule to control whether you want to shuffle the results.

Default: The default shuffle setting of the model being used will be applied. 

To see the default shuffle setting for each model, refer to the Shuffle results by default column under Recommendation model reference.

If you are using Autopilot or Professional Service - Custom Model, only Default can be selected.

Shuffle: Ignore the default setting of the model and always shuffle results. 

Don't shuffle: Ignore the default setting of the model and don't shuffle results. The original order of the results will be shown. For example, if the model is "Bestsellers in Last 30 Days", the most-purchased products in the past 30 days will be shown first.



Creating a Scenario [6]

https://docs.aiqua.appier.com/docs/creating-scenario-recommendation-20



Here are some examples to show how the products will be ordered and shuffled when you have pinned products and fallback products in the results. In the examples below, 10 recommended products are set to be displayed.

Example 1: Shuffling is not applied

Pinned products (PP1, PP2) ➜ products generated by the model (A, B, C) ➜ designated fallback products (DF1, DF2) ➜ products from default fallback rules (F1, F2, F3).

Example 2: Shuffling is applied

[Pinned products (PP1, PP2) & products generated by the model (A, B, C)] ➜ [Designated fallback products (DF1, DF2) + products from default fallback rules (F1, F2, F3)].

Click the edit button next to a scenario's name to open its settings.

After editing the scenario settings, the model re-trains based on the new settings. The previously configured settings will be used until the training is complete.

The placement can't be edited.

For scenarios using Autopilot or Professional Service - Custom Model recommendation model, the model setting can't be edited.

Click the three vertical dots next to the scenario's name to access additional scenario actions.

Copy scenario ID: Copy the scenario ID for usage in recommendation requests via API or SDK.

Activity log: View records of all operations on this scenario (e.g. edited, archived).

Archive: Once archived, the recommendation model will stop serving recommendation results. 

Preparing: The recommendation model is still training and isn't ready for use. It can take several days for the model to finish training depending on how large your product data feed is and which model the scenario is using.

Ready: The recommendation model has finished training and is ready for use. The model will continue to collect data and optimize results.

Updating: The scenario settings have been updated, and the recommendation model is in the process of retraining. During this time, results continue to be served based on the previous settings.

Archived: Archived scenarios can't be used and no longer serve recommendation results.



Creating a Scenario [7]

https://docs.aiqua.appier.com/docs/creating-scenario-recommendation-20



Archived: Archived scenarios can't be used and no longer serve recommendation results.

Use recommendation analytics to understand how your scenarios are performing. Note that analytics data isn't available for scenarios placed in campaign creatives.Updated 5 months ago Table of Contents

Overview

1. Create a new scenario

2. Choose a placement

3. Choose a recommendation model

Autopilot

Select a model

4. (Optional) Create filters

5. (Optional) Configure advanced settings

6. Implement the scenario in your website, app, or creative

Website or app

Campaign creative

Advanced scenario settings

Exclude duplicate products

Add pinned products

Fallback product rule

Shuffle recommended products

Managing scenarios

Editing scenario settings

Scenario actions

Scenario statuses

Recommendation scenario analytics



Filtering Recommendation Results [0]

https://docs.aiqua.appier.com/docs/filtering-recommendation-results



AIQUA provides different ways for you to control what products to include or exclude from recommendation results.

Set filter rules

Exclude purchased products

📘Note:If you have included the availability field in the product data feed, AIQUA automatically excludes out-of-stock products from recommendation results. However, if a product becomes out-of-stock recently, it is possible for the recommendation results to still include the out-of-stock product until the next time AIQUA fetches the updated data feed. See more about the update frequency of product data feed.

You can apply filter rules to only show recommendation results that meet your filtering criteria. AIQUA compares the value defined in the filter rules with the product data feed to determine whether a filter condition is met. For example, you can set a filter to only show products that belong to the "jacket" category or only show products with a price range between $100 - $500.

You can define filter rules in three different places:

AIQUA dashboard (scenario settings): Define filters on the AIQUA dashboard when creating a scenario.

API calls: Define filters in Appier SDK API or Recommendation 2.0 REST API.

Dynamic content in creatives: Define filters in dynamic content syntax.

Depending on where the filter rules are defined, the filter fields supported and the case sensitivity of filter values are different.

Defining filter rulesSupported filter fieldsFilter value case sensitivityAIQUA dashboard (scenario settings)Category

Original Price

Discounted Price

Product ID

Product Name

Not case-sensitiveAPI calls

(Appier SDK API or Recommendation REST API)Category

Original Price

Discounted Price

Product ID

Product Name

Not case-sensitiveDynamic content in creativesCategoryCase-sensitive

When creating a scenario on the AIQUA dashboard, in step 4, you can choose which filters you want to apply.



Filtering Recommendation Results [1]

https://docs.aiqua.appier.com/docs/filtering-recommendation-results



When creating a scenario on the AIQUA dashboard, in step 4, you can choose which filters you want to apply.

If you do not want to apply any filters, leave the Apply filter rules option unchecked. When this option is unchecked, all filter rules defined on the AIQUA dashboard, in API calls, and in dynamic content are ignored.

If you select Apply filter rules, the options available differ based on the placement you have selected.

If Website or app is selected:

Define filter rules: Only apply the filter rules specified in the scenario settings. Ignore the filter rules sent in the API calls from either the Appier SDK API or Recommendation 2.0 REST API.

Apply API filter rules first: Apply filter rules sent in the API calls first, if any exist. If filter rules are not sent in the API calls, the rules specified in the scenario settings are applied as a fallback. See Defining API filter rules for details. 

Append filter rules: In addition to applying the filter rules specified in the API calls, apply the rules specified in the scenario settings.

If Dynamic content in creative is selected:

Define filter rules: Only apply the filter rules specified on the AIQUA dashboard. Ignore filter rules set in the dynamic content of campaign creatives. See Defining filter rules on the AIQUA dashboard for details. 

Apply dynamic content filter rules first: Apply dynamic content filter rules first, if any exist. If none exist in the dynamic content, the rules specified on the AIQUA dashboard are applied as a fallback. See Recommendation 2.0 in dynamic content for details.

If you selected Define filter rules or Append filter rules when creating a scenario, define the filter rules directly on the AIQUA dashboard. 

You can have one or multiple filter rules. Each filter rule can include one or multiple rule conditions.



Filtering Recommendation Results [2]

https://docs.aiqua.appier.com/docs/filtering-recommendation-results



You can have one or multiple filter rules. Each filter rule can include one or multiple rule conditions.

You can select ​if a product only needs to satisfy Any one of the filter rules (at least one) or if it needs to satisfy All filter rules to be considered a match. Similarly, under each rule, you can select if a product needs to satisfy Any or All of the rule conditions.

You can create filter rules based on the following fields:

Category

Original Price

Discounted Price

Product ID

Product Name



The second drop-down list lets you select the operator. Different operators are supported for different fields based on the data type. See the Operators section.

Let's say you want to show recommendation products that belong to either the product category woman's > boots or woman's > hats, or recommendation products where the category contains the word jeans. 

In addition, you only want to include products that are on a clearance sale. In the product data feed, you have a custom label to indicate the products' clearance status by true or false.

Below is an example of how you can set this up on the AIQUA dashboard. 

For category-related requirements, set a condition for Category is any of woman's > boots or woman's > hats and set another condition for Category contains jeans.

Select Recommended products must satisfy Any of the following conditions to indicate that the product only needs to meet one of the conditions under Rule 1. 

For the clearance custom label, click Add Rule to create a Rule 2 and set Clearance to true. 

Above Rule 1, select Recommended products must satisfy All of the following rules to apply an AND operator between Rule 1 and Rule 2.

If you have selected Apply API filter rules first, have your developers pass the filter rules in the API calls for Appier SDK API or Recommendation 2.0 REST API. 

🚧Avoid special charactersAvoid using the following special characters in recommendation filters: ?, *,+,(, ) ,{,},[,],. , ^, $, \ , |

{

"version":2,

"filterRule":{

"operator":"OR",

"ruleList":[



Filtering Recommendation Results [3]

https://docs.aiqua.appier.com/docs/filtering-recommendation-results



{

"version":2,

"filterRule":{

"operator":"OR",

"ruleList":[

{

"operator":"OR",

"conditionList":[

{

"key":"category",

"operator":"in",

"value":["shoes"]

}

]

}

]

}

}

You can pass one or more filter rules into the API call, and you can have one or multiple rule conditions nested under each filter rule.

Under filterRule, you can set the operator parameter to AND or OR to control ​if a product needs to satisfy one or all of the filter rules to be considered a match. Under ruleList, the same operator parameter is available for rule conditions as well.

You can create filter rules based on the following fields:

Supported fieldsKey nameCategorycategoryOriginal PriceoriginalPriceDiscounted PricepriceProduct IDproductIdProduct NametitlecustomLabel00customLabel01customLabel02customLabel03customLabel04

Different operators are supported for different fields based on the data type. See the Operators section.

In the example below, a product is considered a match if it meets the rule condition below:

Rule condition: The product has a price between 100 and 300

{"version":2,"filterRule":{"operator":"OR","ruleList":[{"operator":"OR","conditionList":[{"key":"price","operator":"between","value":["100","300"]}]}]}}

In the example below, a product is considered a match if it meets both of the rule conditions below:

Rule condition: The product has a discounted price less than 500, AND

Rule condition: The product's category value in the data feed contains the word jeans

{"version":2,"filterRule":{"operator":"OR","ruleList":[{"operator":"AND","conditionList":[{"key":"price","operator":"lt","value":["500"]},{"key":"category","operator":"contains","value":["jeans"]}]}]}}

In the example below, a product is considered a match if it meets at least one rule condition under Rule 1, and meets both conditions under Rule 2.

Rule 1: 

Rule condition: The product belongs to the category woman's > boots, OR

Rule condition: The product category contains the word jeans

Rule 2:



Filtering Recommendation Results [4]

https://docs.aiqua.appier.com/docs/filtering-recommendation-results



Rule condition: The product category contains the word jeans

Rule 2:

Rule condition: The product's custom label 01 value is true, AND

Rule condition: The product title does not contain the word unisex

{"version":2,"filterRule":{"operator":"AND","ruleList":[{"operator":"OR","conditionList":[{"key":"category","operator":"in","value":["woman's > boots"]},{"key":"category","operator":"contains","value":["jeans"]}]},{"operator":"AND","conditionList":[{"key":"customLabel01","operator":"eq","value":["true"]},{"key":"title","operator":"not_contains","value":["unisex"]}]}]}}

Web SDK sample request 

Android SDK sample request 

iOS SDK sample request 

React Native SDK sample request

Flutter SDK sample request

REST API sample request

This section lists the operators that are supported based on the data type of the filter condition when setting the filter rules using:

AIQUA dashboard (scenario settings)

API calls

📘Note:This section does not apply to filter rules set in dynamic content syntax.

Below are the supported operators for productId, title (Product Name), and custom labels with the data type set to string.

Operators (AIQUA dashboard)Operators (API calls)Descriptionis any ofinThe data feed value includes at least one of the filtering values.Example

The data feed value is Blue Jeans.

If the filter value is:

• Blue Jeans or shoes → Match

• Classic Blue Jeans→ Not a match

• Jeans → Not a matchis notninThe data feed value does not include any of the filtering values.containscontainsThe data feed value contains and partially matches at least one of the filtering values.Example

The data feed value is Blue Jeans.

If the filter value is:

• Jeans or shoes → Match

• Classic Blue Jeans → Not a matchdoes not containnot_containsThe data feed value doesn't contain any exact matches with the filtering values.starts withstarts_withThe data feed value starts with the filtering value.Example

The data feed value is Blue Jeans.

If the filter value is:

• Blue → Match



Filtering Recommendation Results [5]

https://docs.aiqua.appier.com/docs/filtering-recommendation-results



The data feed value is Blue Jeans.

If the filter value is:

• Blue → Match

• Blu → Matchends withends_withThe data feed value ends with the filtering value.

Some fields in the product data feed, such as product category, contain values with a hierarchy structure or have multiple values in a field. 

For example, you might have a category called "Woman's > Blue Jeans", where "Blue Jeans" is a sub-category under the Woman's category. There might be a product Classic denim blue jeans that belongs to the category Woman's > Blue Jeans and the category Classic Collection at the same time. 

These fields are categorized into a special type of string called "tag".

📘Note:

Currently, AIQUA does not support setting custom labels to the "tag" data type. 

The hierarchy must match the category structure and spacing specified in the product data feed. Be sure to include a space before and after the >.

Below are the supported operators for category (Category). 

Operators (AIQUA dashboard)Operators (API Calls)Descriptionis any ofinThe data feed value includes at least one of the filtering values.Example

The data feed value is Woman's > Blue Jeans and Classic Collection.

If the filter value is:

• Woman's > blue jeans → Match

• classic collection → Match

• Blue Jeans → Not a matchis notninThe data feed value does not include any of the filtering values.containscontainsThe data feed value contains and partially matches at least one of the filtering values.Example

The data feed value is Woman's > Pants > Blue Jeans.

If the filter value is:

• Blue Jeans → Match

• pants → Match

• Woman's > Pants → Match

• Woman's > Blue Jeans → Not a matchdoes not containnot containsThe data feed value doesn't contain any exact matches with the filtering values.

Below are the supported operators for originalPrice, price (Discounted Price), and custom labels with the data type set to float.



Filtering Recommendation Results [6]

https://docs.aiqua.appier.com/docs/filtering-recommendation-results



Operators (AIQUA dashboard)Operators (API Calls)Description>gtGreater than>=gteGreater than or equal to=eqEqual to<=lteLess than or equal toFor custom labels with the data type set to boolean, you can set the condition to true or false on the AIQUA dashboard.

In API calls, use the operator eq.

Operators (API Calls)DescriptioneqEqual to

You can prevent products already purchased by the users from showing up in the recommendation results on your platforms or inside campaign creatives. This is useful for some product types where users are unlikely to purchase the same products again, such as ebooks.

AIQUA will try to match purchase data with users across platforms based on user_id (customer user ID used by your company). If a web user and an Android user have the same user_id, they are considered as the same person, and the purchased products of both the web user and Android user will be filtered out. If user_id isn't available (e.g. user is not logged in), the purchased product filter will be based on userId, the unique identifier AIQUA assigns to each user. In this case, each web, Android, and iOS user is treated as a different user. 

You can set a look-back period to remove purchased products based on the purchase data within a specified time period. For example, if the look-back period is 14 days, products purchased by the user in the past 14 days (14 days x 24 hours) will be eliminated from the recommendation results. 

The maximum look-back period is 180 days.

To enable this feature, contact Appier Support (ess_support@appier.com). Note that the change takes about an hour to take effect. 

The product_id in product_purchased events must be identical to the product ID onboarded in the data feed. 

To filter based on user_id, you need to pass the user_id parameter in the product_purchased event, and in SDK, you need to pass the user_id as the parameter in the recommendation request.

See Web SDK: Recommendation 2.0 

See Android SDK: Recommendation 2.0



Filtering Recommendation Results [7]

https://docs.aiqua.appier.com/docs/filtering-recommendation-results



See Web SDK: Recommendation 2.0 

See Android SDK: Recommendation 2.0 

See iOS SDK: Recommendation 2.0 

See React Native SDK: Recommendation 2.0 

See Flutter SDK: Recommendation 2.0

If you're using a custom iOS web view implementation and want to filter based on user_id, you need to re-integrate the web view. See Custom Web View Implementation for instructions.

This feature has the following mobile SDK version requirements:

AppRequired SDK VersionsiOS (Native)Filter by user_id and userId: iOS SDK 7.5.0 or lateriOS (Web view)Filter by user_id: iOS SDK 7.12.0 or later

Filter by userId: iOS SDK 7.5.0 or laterAndroid (Native)Filter by user_id and userId: Android SDK 6.5.1 or laterAndroid (Web View)Filter by user_id: Android SDK 7.2.0 or later

Filter by userId: Android SDK 6.5.1 or laterFlutter (Native)Filter by user_id and userId: Flutter SDK 2.0.0.-dev.1Flutter (Web view)Filter by user_id and userId: Flutter SDK 2.0.0.-dev.1React Native (Native)Filter by user_id and userId: React Native SDK 1.5.0 or laterReact Native (Web view)Filter by user_id: React Native SDK 1.6.0 or later

Filter by userId: React Native SDK 1.5.0 or later

You can exclude duplicate or similar products when setting up the scenario. For details, see Exclude duplicate products.Updated 7 months ago Table of Contents

Set filter rules

Choosing which filters to apply

Defining filter rules on the AIQUA dashboard

Defining API filter rules

Operators

Exclude purchased products

Requirements

Exclude duplicated products



Recommendation Models [0]

https://docs.aiqua.appier.com/docs/recommendation-models



When creating a Recommendation 2.0 scenario, you must select which type of recommendation model you want to use to generate product recommendations. 

For explanations of important concepts used in Recommendation 2.0, see Recommendation 2.0 concepts.

For a list of all available recommendation models, what type of results they produce, and what data they require, see Recommendation model reference.

The following concepts form the basis of the Recommendation 2.0 feature, and are important to understand in order to get optimal results from AIQUA's recommendation service.

Recommendation models are AI models that train on data (i.e. the product ID parameter in user events and the information in your product data feed) to generate product recommendation results that are most likely to be relevant to your target audience. There are five categories of recommendation models, each containing models that generate specific types of results:

User-Based

Product-Based

Popularity

Advanced

Build Your Own

📘Note

Recommendation models may require several days to complete training, depending on the size of your product data feed and the specific model your scenario is using.

When logging events, only the product ID parameter is used to train recommendation models. Other event parameters are not used for model training.

Some models require specific events to be logged (or uploaded via API), specific fields to be present in your product data feed, or certain parameters to be included in the recommendation API request. For the specific requirements of each model, see Recommendation model reference.

When the required event data is unavailable:

If the scenario has never completed training before: The first model training will fail and no recommendation results will be available.

If the scenario has completed training at least once before: The subsequent model training will fail and fallback rules will be used to generate recommendation results instead of the selected model.



Recommendation Models [1]

https://docs.aiqua.appier.com/docs/recommendation-models



The designated product is the product used to generate other product recommendations. A designated product is required for models that generate results based on a specific product's attributes or user interactions with a specific product. This means that the recommendation results you receive will be influenced by the designated product you choose, for example:

If a scenario uses the Similar Product Title model and the designated product is "Sneaker A", the recommendation results will be products with titles similar to "Sneaker A".

If a scenario uses the Similar Product Attributes model and the designated product is "Shirt B", the recommendation results will be products with attributes that are similar to "Shirt B".

If a scenario uses the Complementary Products model and the designated product is "Jacket C", the recommendation results will be products that are typically purchased together with "Jacket C".

Refer to the Required data columns in Recommendation model reference to see which models require you to pass a product ID in the recommendation API request.

To specify a designated product in a recommendation request, pass that product's product ID (as specified in your product data feed) in the recommendation API request.

👍Setting a default designated product for websitesWhen you begin integrating Recommendation 2.0 with you website, we recommend setting a default designated product on each page that contains product data. Setting a default designated product ensures that all recommendation requests will contain the product ID parameter by default.

The set of products from your product data feed that are used to train recommendation models is called the model training set. For some models, there are limitations on the size of the model training set:

Similar Product Attributes: Only the first 700,000 products in the data feed are included in the training set.

Similar Titles: Only the first two million products in the data feed are included in the training set.



Recommendation Models [2]

https://docs.aiqua.appier.com/docs/recommendation-models



Similar Titles: Only the first two million products in the data feed are included in the training set.

If the designated product isn't part of the model training set (e.g. one of the first 700,000 items in the product data feed for a scenario using the Similar Product Attributes model), recommendation results will be generated based on fallback rules instead of the selected recommendation model.

Fallback products are the products that will be displayed when not enough recommended products are generated from the recommendation model.

When creating a scenario on AIQUA dashboard, you can select a fallback product rule for the scenario. See fallback product rule for more details.

Here's how the default fallback rules work.

If a product category filter is specified in the recommendation scenarios or API requests, the most-viewed product from the last 49 days that satisfies the filter conditions will be returned. If no product category filter is specified, the next fallback rule will be used instead.

The most-viewed product from the last 49 days that is in the same category as the designated product will be returned. If the productId for the designated product isn't provided, the next fallback rule will be used instead.

The most-viewed product from the last seven days will be returned. If no products were viewed in the last seven days, the next fallback rule will be used instead.

A random product from the product data feed will be returned.

When creating a scenario on AIQUA dashboard, you can go to the Shuffle recommended products section and choose whether or not to shuffle the order of the recommendation results generated. You can also choose to apply the default shuffle setting of each recommendation model. 

To see the default shuffle setting of each model, refer to the Shuffle results by default column under Recommendation model reference.



Recommendation Models [3]

https://docs.aiqua.appier.com/docs/recommendation-models



The following recommendation models can be used with Recommendation 2.0 scenarios to generate product recommendations. Refer to the sections below to learn more about each model and the data it requires to generate optimal results.

User-based recommendation models generate product recommendations based on individual user preferences and behaviors. These models work best in non-product-specific placements, such as homepages.

Model nameDescriptionRequired dataShuffle results by defaultRecommended for YouRecommends products that were frequently viewed by people with similar browsing and purchasing behavior.Event: At least one of product_viewed, product_added_to_cart, product_purchasedYesSimilar to Your Recently Browsed ProductsRecommends products that are similar to other products the user recently browsed. Event: At least one of product_viewed, product_added_to_cart, product_purchased Product data feed: Must include title. For the best results, include category and description as well. YesRecently ViewedRecommends up to 20 products the user has viewed in the past 30 days, prioritizing the most recent activities.Event: product_viewedNoRecently Added to CartRecommends up to 20 products the user has added to their cart in the past 30 days, prioritizing the most recent activities.Event: product_added_to_cartNoRecently PurchasedRecommends up to 20 products the user has purchased in the past 30 days, prioritizing the most recent activities.Event: product_purchasedNo

Product-based recommendation models generate results based on a specific product, called the designated product; for example, you can use these models to recommend products that are purchased together with or share similar attributes with the designated product.

These models require you to include the product ID of the designated product in the recommendation API request.

🚧ImportantThe product ID you pass into the API request must match the product ID specified in your product data feed.



Recommendation Models [4]

https://docs.aiqua.appier.com/docs/recommendation-models



🚧ImportantThe product ID you pass into the API request must match the product ID specified in your product data feed.

Model nameDescriptionRequired dataShuffle results by defaultSimilar Product Images (Premium)Recommends products that are visually similar to the designated product. This model also considers other product attributes to determine similarity.

Suitable for large product catalogs or catalogs with many new products with limited page view data.

Contact your customer success manager to enable this model.

Product data feed:image, title, category

API request parameter: productId

NoSimilar Product Attributes Recommends products with attributes similar to the attributes of the designated product. The model training set is limited to the first 700,000 items in the product data feed.

Suitable for:

Large product catalogs or catalogs with many new products with limited page view data.

Scenario placements where users have shown strong intent for the content (e.g. a product category page).

Product data feed: Must include title and category. For the best results, include description as well.

API request parameter: productId

YesSimilar Product Title Recommends products with titles similar to the title of the designated product. The model training set is limited to the first two million items in the product data feed.

Suitable for large product catalogs or catalogs with many new products with limited page view data.

Product data feed: Must include title. For the best results, include category and description as well.

API request parameter: productId

YesPeople Also Viewed Recommends products that are often viewed by people who also viewed the designated product.

Event: product_viewed

API request parameter: productId

YesPeople Also Bought Recommends products that are often purchased by people who also purchased the designated product.

Event: product_purchased

API request parameter: productId



Recommendation Models [5]

https://docs.aiqua.appier.com/docs/recommendation-models



Event: product_purchased

API request parameter: productId

YesRelated Products that You Can't Miss Recommends products that are typically purchased after the designated product is added to cart.

Events: product_added_to_cart, product_purchased

API request parameter: productId

YesRelated High-Converting Products Recommends products that are typically purchased after the designated product is viewed.

Events: product_viewed, product_purchased

API request parameter: productId

YesShopping Cart Inspiration Recommends products that are typically added to cart together with the designated product.

Event: product_added_to_cart

API request parameter: productId

YesPost-Purchase Upsell Recommends products that are typically purchased after the designated product is purchased.

Events: product_purchased

API request parameter: productId

YesComplementary Products Recommends products that are typically purchased together with the designated product.

Events: product_viewed, product_purchased

API request parameter: productId

Yes

Popularity recommendation models generate results from products that are considered popular among your site and app users; for example, you can use these models to recommend the most-viewed or most-purchased products on your website. Popularity models are re-trained once a day using the event data available at the time. Recent data may not be considered until the next time the model re-trains the following day.

Some models use recency weighting, such as Trending Popular Products in Last 7 days. Recency weighting means that more recent events have a greater influence on the recommendation results than older events. 

👍For more flexibility with popularity models, such as having the ability to choose the event and time period used to determine popularity, see the Popular Products model from the Build Your Own category.



Recommendation Models [6]

https://docs.aiqua.appier.com/docs/recommendation-models



Model nameDescriptionRequired dataShuffle results by defaultPopular Products in Last 7 DaysRecommends the most-viewed products from the last seven days.Event: product_viewedNoTrending Popular Products in Last 7 DaysRecommends the most-viewed products from the last seven days, with recency weighted.Event: product_viewedNoBestsellers in Last 30 DaysRecommends the most-purchased products from the last 30 days.Event: product_purchasedNoTrending Bestsellers in Last 30 DaysRecommends the most-purchased products from the last 30 days, with recency weighted.Event: product_purchasedNo

Advanced recommendation models aren't just based on a single dimension, such as product attributes or user preference; instead, these models use multiple dimensions, are fully customized by Appier Professional Service, or are AI-selected.

🚧ImportantThe product ID you pass into the API request must match the product ID specified in your product data feed.

Model nameDescriptionRequired dataShuffle results by defaultRecommended for You (Advanced) Recommends personalized products based on each user's browsing behavior and individual preferences.

Event: Must include product_viewed. For the best results, include product_added_to_cart and product_purchased as well.

Product data feed: category

YesRelated Products You May Like Recommends products that are often browsed by people who also browsed the designated product. This recommendation model also considers individual user preferences.

Event: At least one of product_viewed, product_added_to_cart, product_purchased

API request parameter: productId

YesSimilar Products You May Like Recommends products that are similar to the designated product. This recommendation model also considers individual user preferences.

Event: At least one of product_viewed, product_added_to_cart, product_purchased

Product data feed: Must include title. For the best results, include category and description as well.

API request parameter: productId



Recommendation Models [7]

https://docs.aiqua.appier.com/docs/recommendation-models



API request parameter: productId

YesProfessional Service - Custom Model (Premium) Fully customized recommendation models provided by Appier Professional Services.

Contact your customer success manager for details.Required data depends on the customizations you request.Dependent on requested customizationsAI-Selected Automatically selects the most optimal model for your recommendation scenario placement.

Event: At least one of product_viewed, product_added_to_cart, product_purchased

Product data feed: For the best results, include image, title, category, and description.

API request parameter: For the best results, include productId

Yes

These models allow you to select the parameters and events used to generate recommendation results.

🚧ImportantThe product ID you pass into the API request must match the product ID specified in your product data feed.

Model nameDescriptionRequired dataShuffle results by defaultPopular ProductsRecommends the most popular products based on a selected event during a specified time period.

Specify which event should be used to determine popularity as well as a time period. You can choose whether to apply a time-decay, which means that more recent events have a greater influence on the recommendation results than older events.

Example: "This model displays products that have the most product_added_to_cart in the last 30 days."

Event: Selected event

NoEvent to Event Model Analyzes people who Event 1 the designated product and recommends products that are then Event 2 by those same people.

Example: "Analyzes people who product_purchased the designated product and recommends products that are then product_viewed by those same people."

Events: Selected events

API request parameter: productId

YesEvent also Event Model Analyzes people who Event 1 the designated product and recommends products that are also Event 2 by those same people.

Example: "Analyzes people who product_clicked the designated product and recommends products that are also product_viewed by those same people."



Recommendation Models [8]

https://docs.aiqua.appier.com/docs/recommendation-models



Events: Selected events

API request parameter: productId

Yes

The events listed below will be selectable from the event dropdown when configuring a Build Your Own recommendation model on the AIQUA Dashboard, if the event was logged with the product_id event parameter:

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

Use the following table as a starting point to help you in deciding which recommendation model to use in your scenario for the specific type of page you'll be placing it in:

Suggested models for a scenario in your website or app

Suggested models for a scenario in a creative's dynamic content

PlacementSuggested modelsHome page• Recommended for You

• Recommended for You (Advanced)

• Trending Popular Products in Last 7 DaysProduct page• People Also Viewed

• Related Products You May Like

• Similar Product TitleProduct category page• Recommended for You

• Similar to Your Recently Browsed Products

• Trending Bestsellers in Last 30 Days

We recommend including filtering rules in order to provide more relevant results.Search results page• Popular Products in Last 7 Days

• Recommended for You

• Similar to Your Recently Browsed ProductsShopping cart page• Complementary Products

• Related Products that You Can't Miss

• Shopping Cart InspirationCheckout page• Complementary Products

• People Also Bought

• Trending Bestsellers in Last 30 DaysOrder confirmation page• Complementary Products

• Post-Purchase Upsell

• Recommended for You404 error page• Recommended for You

• Recommended for You (Advanced)

• Trending Popular Products in Last 7 DaysOther• Recommended for You

• Recommended for You (Advanced)

• Trending Popular Products in Last 7 Days



Recommendation Models [9]

https://docs.aiqua.appier.com/docs/recommendation-models



• Recommended for You (Advanced)

• Trending Popular Products in Last 7 Days

For scenarios placed in dynamic content (e.g. in a push or email campaign), the suggested recommendation models are as follows:

Recommended for You

Recommended for You (Advanced)

Trending Bestsellers in Last 30 Days

Updated about 1 month ago Table of Contents

Overview

Recommendation 2.0 concepts

Recommendation models and model training

Required data for recommendation models

Designated product

Model training set

Fallback rules

Shuffled results

Recommendation model reference

User-Based

Product-Based

Popularity

Advanced

Build Your Own

Suggested recommendation models

Website or app

Dynamic content in creatives



Product Data Feed Onboarding [0]

https://docs.aiqua.appier.com/docs/product-data-feed



A product data feed is a spreadsheet file that lists all your products along with various product information such as product title, description, link, price, inventory availability, and more. You will need to prepare a data feed file and then host the file on your server.

Integrating product data feed allows you to utilize the following functions of AIQUA:

Recommendation 2.0 

Use product data feed information in dynamic content

Trigger campaign based on changes in product data feed

File format: AIQUA supports CSV, JSON, and XML formats. 

File encoding: The supported encoding is UTF-8 without BOM. Do not use UTF-8 BOM or other encodings.

Multiple files: In case you have multiple product feed files, for example, one for production environment and the other for testing environment, you will need to provide separate data feed files.

Refer to the table below for the fields to include in the data feed file and follow the guidelines below.

Field names

It is highly recommended to use the field names listed below in your data feed file. However, if the field names of your data feed file do not match the field names in the table, you can have Appier Support map your fields to the field names used in Appier's system.

Make sure you do not change the field names in the data feed after you provide the data feed to Appier.

The field names in the data feed are case-sensitive. 

Do not use non-alphabetical characters in field names.

Escaping commas and double-quotes

Fields with embedded commas or double-quote characters must be enclosed in double-quotes.

Example: Extra Virgin Olive Oil,ID002173,"Organic and natural, cold-pressed, 500ml"

If double-quotes are used to enclose fields, then a double-quote appearing inside a field must be escaped by preceding it with another double quote.

Example: Extra Virgin Olive Oil,ID002173,"Organic and natural, ""cold-pressed"", 500ml"

👍Sample fileHere's a sample data feed file: Sample Data Feed.



Product Data Feed Onboarding [1]

https://docs.aiqua.appier.com/docs/product-data-feed



👍Sample fileHere's a sample data feed file: Sample Data Feed.

Field nameDescriptionSyntax and specificationsRequired?productIdThe unique ID that represents the product.

Example:

b14s001-8100• String

• Max 32 bytes (equivalent to 32 characters in ASCII encoding)

• Only characters within the ASCII range 0x21 ~ 0x7e are allowedRequiredtitleThe name of the product.

Example:

Lemon Herbal Tea

抗UV太陽眼鏡

お香２０種セット• String

• Max 100 bytes (equivalent to 100 characters in ASCII encoding)RequiredurlThe URL that directs to the product details page.• StringRequiredimageThe URL that links to the product image.• String

• Must start with http:// or https://

• Image format should be PNG, GIF, JPG/JPEG or WebP.

• Use the same image size across all products.

• Use images that let users easily identify the product.

• Remove noise from the images (e.g. watermarks, discount tags)Required if using Similar Images recommendation modeldescriptionThe product’s description.• String

• Use informative description to build high-quality product recommendation models.

• Avoid using repetitive descriptions. Keep it unique to help users easily identify and remember your products.

• Max 5000 bytes (equivalent to 5000 characters in ASCII encoding)Required if using Similar Product Attributes recommendation modelcategoryThe category IDs or names based on your product taxonomy.

Example:

L0 > L1 > L2 > L3 > L4

Category_A > Category_B, Category_C• String

• Use > to separate multiple levels in a category and include a space before and after the >.

• If there are multiple product hierarchy, use , (comma) to separate the categories.

• To have better Recommendation results, avoid categories that are too generic (e.g. a toy store using "toy" as the category).

• To have better Recommendation results, avoid categories that are irrelevant to the product attributes (e.g. "on-sale").Required if using Similar Product Attributes or Similar Images recommendation modelcurrencyThe price currency.

Example:

JPY

KRW

TWD• String



Product Data Feed Onboarding [2]

https://docs.aiqua.appier.com/docs/product-data-feed



Example:

JPY

KRW

TWD• String

• Currency should follow the standard 3-letter code from ISO-4217. Do not use currency symbols.Required

If your data feed does not include a field for currency, you can ask CSM to apply a constant value such as "USD".originalPriceThe retail price (excluding discount).

Example:

1000

199.9• FloatRequiredpriceThe current price (including discount).

Example:

800

149.9• FloatRequiredavailabilityThe product’s availability.

Example:

available / unavailable

1 / 0

in stock / out of stock• String

• Binary scheme to indicate whether the product is available or not.RequiredconditionThe product's condition.

Example:

New

Like New

Used• StringRequired if using trigger campaign based on changes in product conditionandroid_urlIf you have an Android app where you'd like to use deep links, provide the deep link that redirects to the in-app page for Android.• StringRequired if you have an Android appios_urlIf you have an iOS app where you'd like to use deep links, provide the deep link that redirects to the in-app page for iOS.• StringRequired if you have an iOS appcustomLabel00customLabel01customLabel02customLabel03customLabel04If your data feed includes other fields that are not listed in this table, they will be mapped as custom labels.• String or float or boolean

• Max 5000 bytes (equivalent to 5000 characters in ASCII encoding)Optional

You need to host the data feed file on your server, and AIQUA will regularly synchronize the feed file from the specified URL.

You should provide a direct HTTP/HTTPS URL of the data feed file hosted on your own server.

You can provide an authentication such as Username-Password to control the access. Examples:

https://username:password@your-web-server/dir/products.json

If you're using an access control list to manage permissions for your data feed file, please allow the following IP addresses so Appier's services can access it:

61.216.8.104

210.64.18.56

210.64.18.57

61.216.8.103

13.229.23.41

3.0.119.155

35.185.163.29

35.189.177.52



Product Data Feed Onboarding [3]

https://docs.aiqua.appier.com/docs/product-data-feed



61.216.8.104

210.64.18.56

210.64.18.57

61.216.8.103

13.229.23.41

3.0.119.155

35.185.163.29

35.189.177.52

If you have experience with creating feeds for Google Shopping or Facebook Catalog, then it would be a similar procedure to create the product data feed for AIQUA. In general, we recommend working with your Customer Success Manager to walk through the following steps.

Work with your Customer Success Manager to design the scenarios and decide which data fields to include in the product data feed, and the semantics of the fields.

Prepare a hosting server for the data feed file.

Provide the URL of the data feed to your Customer Success Manager. Your Customer Success Manager will proceed with the following steps:

Validate the data feed requirements (File format, encoding, CSV delimiter, XML product tag names)

Inspect products of the data feed file

Map your fields to AIQUA product schema (for Recommendation only)

Test parsing data feed

Enable the data feed to your AIQUA AppId

Once enabled, you will be notified by your Customer Success Manager and get a data feed id, such as your-app.com. 

Test your scenario to see if the campaign contents or the product recommendation are functioning properly.

To decide what product data to include in the data feed, think about whether and how you will be utilizing the following features. Below are some scenarios of how the features can be used and the product data required.

FeaturesScenarioProduct recommendationsTo generate product recommendations, it is best to integrate all fields labeled as "Required" in the table above. For the description column, having informative info about the product is important for AIQUA to build high-quality AI models for recommendations.Using product feed in dynamic contentLet's say you want to include the brand of the products viewed by users in dynamic content, but this information is not collected by the SDK. If you provide a brand field in the product feed, you can now include brand information in a message like this:



Product Data Feed Onboarding [4]

https://docs.aiqua.appier.com/docs/product-data-feed



"Check out the latest collection from {{product_viewed.0.feed.brand}}!"Trigger campaign based on feed changesYou can set up a trigger campaign based on changes in the product price. Whenever the product price drops by 10%, a "Don’t miss it. Your favorite item is now on sale!" notification can be sent to users who have added the product to their carts before. To achieve this, you need to have price in your data feed.

The update frequency depends on the nature of your business. In general, it is usually sufficient to have an automatic update from your system to your hosting server on a daily basis. Some people choose to update hourly or twice a day as the products in their CMS/PLM systems update more frequently and they need to have more timely data for their marketing campaigns.

By default, AIQUA fetches the data feed from your hosting server every 3 hours. This update frequency can impact the related features in the following ways.

FeatureImpactProduct recommendationsAIQUA excludes out-of-stock products from recommendation results. However, if a product becomes out-of-stock recently, it is possible for the recommendation results to still include the out-of-stock product until the next time AIQUA fetches the updated data feed.Using product feed in dynamic contentChanges in product attributes that happened after AIQUA last fetches the data feed may not be reflected yet.Trigger campaign based on feed changesTrigger campaigns based on feed changes will be sent when AIQUA fetches the updated data feed.

For product recommendations, this frequency can be adjusted based on your needs. 

Usually, AIQUA does a full update by replacing the entire data feed file. If you want AIQUA to fetch data feed at a higher frequency and your data feed has a large file size that takes a long time to synchronize, it is recommended to do partial updates instead. With partial updates, you need to also provide a smaller feed file with the updated products only in addition to the entire data feed file.



Product Data Feed Onboarding [5]

https://docs.aiqua.appier.com/docs/product-data-feed



You need to provide a feed file to AIQUA that includes the entire product data feed.

AIQUA replaces the existing product data feed with the new source file. 

If an existing product is not in the new source file, AIQUA excludes this product from the latest product data feed.

For partial updates, you also need to provide a feed file that only includes the updates you want to make to the product data feed. In this partial feed file: 

Product data with a new product id would be added as a new product. 

To delete a product, change the availability to out of stock.

To update an existing product, the product id needs to match with the product id in an existing row. AIQUA overwrites the entire row, so make sure you include the value for the unchanged columns as well.

Below is an example of a data feed file that includes three products.

Let's say you want to make the following changes.

Update the price of product "P001"

Delete product "P002"

Add a new product "P004"

Using partial update, you will need to prepare a feed file that looks like this.

Updated over 1 year ago Table of Contents

1. Preparing the data feed file

File format and encoding

Data specifications

2. Hosting the data feed file

Requirements: File hosting

3. Onboarding process

Work with your customer success manager to complete the integration procedures

4. FAQs

What product data should I include in the data feed?

How often should I update my product data?

How often does AIQUA fetch data feed from my hosting server?

Can I change how often AIQUA fetches the data feed?



FAQs

https://docs.aiqua.appier.com/docs/faqs



How do I add devices to Test Segment?

How do I segment by notification ID?

LINE Segment FAQs

How do I see Conversion Value in campaign performance?

How do I track clicks with shortened URLs?

Why do I see discrepancies between AIRIS and AIQUA reports? (Links to AIRIS Resource Center)

Why are users receiving delayed notifications? 

Why can't I find some of my past campaigns?

Why do my app push campaigns have low delivery rates? 

Can I also trigger a fake prompt for users who aren’t opted-in?

How do I disable Web push and system prompts?

How can users opt out of web push?

What's Quieter Permission UI? 

How can I manage the traffic coming from my web push campaign?

Why do some users have different userId and wUserId?

If I switch to AIQUA from another service, will my users be prompted to allow web push notifications again? 

Creative Studio FAQs

Journey Map FAQs

Where is AIQUA's data center located?

Updated about 1 year ago Recommendation AnalyticsSegment FAQsTable of Contents

Segment FAQs

Performance FAQs

Campaign FAQs

App push FAQs

Web push FAQs

Creative Studio FAQs

Journey Map FAQs

Other FAQs



How do I segment by notification ID? [0]

https://docs.aiqua.appier.com/docs/how-do-i-segment-by-notification-id



If you want to segment based on users’ past interaction with the notifications of a particular campaign (e.g. include users who have clicked on notifications from campaign A), you'll need to segment by condition using the notification ID (notificationId) as the event parameter. 

This section explains how to retrieve notification IDs for different campaign types and how to use these IDs for segmentation.

Regular merged push campaigns

Experiment campaigns

Non-experiment campaigns

You can retrieve the notification ID for regular merged push campaigns from the following locations:

Campaign edit page

Campaign performance page 

For campaigns sent to multiple channels (e.g. Android, iOS, and web), clicking the Copy notification IDs button will copy a comma-separated list of notification IDs, where each ID corresponds to a single channel and the order of channels is Android, iOS, then web. For example:

ChannelsDescriptionAndroid, iOS, and WebIf you select all available channels (Android, iOS, and web), the notification IDs for the variant will be listed in the following order: 1571600000, 1571610000, 1571620000.

• 1571600000 is the Android notification ID.

• 1571610000 is the iOS notification ID.

• 1571620000 is the web notification ID.Android, WebIf you only selected Android and Web, the IDs will be listed in the following order: 7600210000, 7600220000.

• 7600210000 is the Android notification ID.

• 7600220000 is the web notification ID.

Go to the campaign list and click the pencil icon to edit the campaign.

📘NotesYou must save the campaign to generate the notification IDs.

Navigate to the Creative section. Click on a variant, then click Copy notification ID. 

Alternatively, go to the final step, Review & launch. Click the copy icon corresponding to a variant to copy its notification IDs.

Go to the campaign list and click the campaign name to view the performance page.

In the performance page, open the Campaign details tab. Click the copy icon corresponding to a variant to copy its notification IDs.



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
