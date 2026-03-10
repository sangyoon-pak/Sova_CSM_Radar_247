---
source: notebooklm_export
file_id: "070"
filename: "070_bb_rc_part_2.txt.txt"
doc_type: "reference_card"
product: "BotBonnie"
content_type: "txt"
language: "en"
guide_summary: "This comprehensive documentation details various **message types and advanced kits** available within the BotBonnie platform for creating sophisticated and interactive chatbot experiences across multiple messaging channels.  The message types cover media such as **Video and Audio**, specifying file requirements and necessary URL modifications for hosting via FTP, Dropbox, or Google Drive, as well as unique formats like **Imagemap and Video Imagemap** which are exclusive to LINE for interactive v"
guide_keywords: "Messaging platform features, Advanced kit functionalities, User engagement tools, Campaign and broadcast management, Data and user properties"
---

# 070 bb rc part 2

Video

https://docs.botbonnie.appier.com/docs/message-type-video



👍Supported platforms

Facebook

Instagram

LINE (see requirements and limitations)

WebChat

WhatsApp

Provide the URL to a video file hosted on an FTP server, Dropbox, or Google Drive to play video in your message.

Video files must be less than 5 MB

Only MP4 files are accepted

LINE only supports video files with an HTTPS URL

The URL for the video file must be hosted via FTP, Dropbox, or Google Drive. Dropbox and Google Drive URLs must be modified before being added to the module.

Video files can be hosted via FTP, Dropbox, or Google Drive, and downloads must be allowed.

Dropbox and Google Drive file URLs must be modified before being added to the module.

🚧Unsupported video URLsVideo files on hosting and streaming services not listed above, e.g. YouTube, are not supported.

Before inputting the Dropbox file URL in your bot settings, complete the following steps:

Retrieve the file ID. The file ID is the string located between https://drive.google.com/file/d/ and /view?usp=sharing.

Append the file ID to the following URL: https://drive.google.com/uc?export=download&id=.

For example:

Original: https://drive.google.com/file/d/FILE_ID/view?usp=sharing

Modified: https://drive.google.com/uc?export=download&id=FILE_ID

Before inputting the Dropbox file URL in your bot settings, replace the "www" in the Dropbox file URL with "dl". For example:

Original: http://www.dropbox.com/s/qwertyuiop/MY_VIDEO_FILE.mp4

Modified: http://dl.dropbox.com/s/qwertyuiop/MY_VIDEO_FILE.mp4

Updated 9 days ago



Audio

https://docs.botbonnie.appier.com/docs/message-type-audio



👍Supported platforms

Facebook

LINE (see requirements and limitations)

WebChat

WhatsApp

Provide the URL to an audio file hosted on an FTP server, Dropbox, or Google Drive to play audio in your message.

Audio files must be less than 5 MB and be one of the following formats:

MP3

OGG

M4A

LINE only supports M4A audio files with an HTTPS URL

The URL for the audio file must be hosted via FTP, Dropbox, or Google Drive. Dropbox and Google Drive URLs must be modified before being added to the module.

Audio files can be hosted via FTP, Dropbox, or Google Drive, and downloads must be allowed.

Dropbox and Google Drive file URLs must be modified before being added to the module.

Before inputting the Dropbox file URL in your bot settings, complete the following steps:

Retrieve the file ID. The file ID is the string located between https://drive.google.com/file/d/ and /view?usp=sharing.

Append the file ID to the following URL: https://drive.google.com/uc?export=download&id=.

For example:

Original: https://drive.google.com/file/d/FILE_ID/view?usp=sharing

Modified: https://drive.google.com/uc?export=download&id=FILE_ID

Before inputting the Dropbox file URL in your bot settings, replace the "www" in the Dropbox file URL with "dl". For example:

Original: http://www.dropbox.com/s/qwertyuiop/MY_AUDIO_FILE.mp4

Modified: http://dl.dropbox.com/s/qwertyuiop/MY_AUDIO_FILE.mp4

Updated 9 days ago



Imagemap

https://docs.botbonnie.appier.com/docs/message-type-imagemap



👍Supported channels

LINE

Imagemap messages let users interact with tappable areas on full size images. With this message type, you can set tappable areas to open links, trigger actions, or track engagement with tags.

This message type is only supported for LINE.

Image file size must be 1 MB or smaller.

The following table summarizes the differences between the imagemap and image messages. Use the table below to compare message types and choose the best fit for your campaign.

FeatureImagemap messagesImage messagesSupported channelsLINE is the only supported channel.Available for all channels.ImageCreate customizable tappable areas in an image to open URLs, navigate to bot modules, or trigger actions.Single static image without interactive elements.UsageFor campaigns that need interaction with specific areas of a single image.Share simple visual content when no interaction is needed.

Follow these steps to create an imagemap message:

Go to Flow > Add module and select Imagemap from the list.

Select an aspect ratio. Click ... > Change image in the upper-right corner to upload an image file no larger than 1 MB.

Select Edit layout and set up the imagemap layout based on your aspect ratio.

Aspect ratioDescription1:1, 1:2Choose an imagemap layout that divides your image into predefined tappable areas.

CustomManually drag to define tappable areas and assign actions.

Hover over a tappable area and select an action:

None: Leave this area without an action.

Go-to Module: Direct users to a specific chatbot module.

Open a URL: Enter a link to take users to a webpage.

Add a descriptive Alt text to explain the imagemap's purpose in LINE notifications.

Use Triggered actions to tag users for retargeting in future remarketing campaigns.

Test your imagemap to ensure tappable areas align seamlessly for easy interaction.

Updated 9 days ago



Video Imagemap

https://docs.botbonnie.appier.com/docs/message-type-video-imagemap



👍Supported platforms

LINE

Video imagemap messages allow you to upload a video file that can be played in full screen when the message is sent. This message type can have a single button with a link, which is revealed when the user taps the video to enable full screen viewing mode. After clicking the button, the URL you configured in the message settings will be opened.

This message type is only supported for LINE

Video files must be less than 200 MB

Only MP4 files are accepted

The following table summarizes the differences between the video imagemap message type and the video message type.

Video imagemap messageVideo messageSupported channelsLINE is the only supported channel• Facebook

• Instagram

• LINE

• WebChat

• WhatsAppButtons (with links)Video imagemap messages can include a button which is visible in fullscreen viewing modeVideo messages can't contain buttonsFilesizeVideo files can be up to 200 MBVideo files can be up to 5 MBAppearanceFull message widthStandard message widthUpdated 9 days ago



Delay

https://docs.botbonnie.appier.com/docs/message-type-delay



👍Supported channels

Facebook

Instagram

Delay messages help control the timing of messages, making conversations feel more natural and engaging. You can use delays to simulate real typing speed, give users time to process previous messages, or pace interactions effectively.

Follow these steps to create a delay message:

Go to Flow > Add module, then select Delay.

Use the slider to set a delay between 1 and 20 seconds, in increments of 0.5 seconds.

Use delay messages to make conversations feel more natural, like simulating typing or giving users a moment to enjoy images or carousels before moving on to the next message.

Place delay message between different message in a module to improve flow.

Adjust the delay time based on the context. For text-based responses, a short delay is enough. For more complex messages, such as carousels or videos, a slightly longer delay can help users engage with the content.

Updated 9 days ago



One-Time Notification Request [0]

https://docs.botbonnie.appier.com/docs/message-type-one-time-notification-request



👍Supported platforms

Facebook

LINE

A one-time notification request allows you to ask users for permission to send them another message within one year of their acceptance. Users can accept the request by clicking Notify Me, and you'll have the opportunity to send one notification to those users via broadcast. One-time notifications allow you to send the notification without being restricted to the 24 hour messaging window.

The one-time notification workflow consists of three steps:

Send the one-time notification request

Users click Notify me to accept the request

Send a broadcast within one year to reach the users who opted in

Follow the steps below to send a one-time notification to your audience:

(Facebook Pages only) Request access to one-time notification for your Facebook Page

Select a method for sending the request: Choose whether the request via chatbot flows, broadcasts, or Growth Tools.

Create the request message: Configure the settings for your one-time notification request, such as the image and title.

Broadcast the one-time notification: Use broadcasts to send the one-time notification the interval you specified in the initial request.

📘NoteIf your chatbot isn't connected to a Facebook page, skip this step and go to step 2 directly.

In the settings page for your Facebook Page, go to New Pages Experience > Advanced Messaging

Find the section titled Requested features

Submit a request to use One-time notification

Select one of the following methods to send the one-time notifications request to your audience:

Chatbot flows

Broadcasts

Growth Tools

In your chatbot flows, click Add module > One-time notification request, then create the request message.

Go to Broadcasting > Broadcasts, then click +Broadcast to create a broadcast with a module containing the one-time notification request message, then create the request message

Go to Growth Tools, click +Growth Tool, select one of the following supported options, then create the request message.

PlatformSupported optionsFacebook• Start chats with URL



One-Time Notification Request [1]

https://docs.botbonnie.appier.com/docs/message-type-one-time-notification-request



PlatformSupported optionsFacebook• Start chats with URL

• Start conversations with QR code

• Facebook Post Comment Reply (Private message reply)

• Facebook Post Multiple Auto Reply (Private message reply)LINE• Start chats with URL

• Start conversations with QR code

In the input box under Get notified, input a message describing what type of notification the user will receive in the future. This message is limited to 65 characters.

Configure button settings for the Notify Me button. Under On click, select the module that should be sent to the user after clicking Notify Me to indicate that they've opted in to the one-time notification.

All users who accept the request will be added to the one-time notification user list called Default notification list. In the next step, you'll be able to send a broadcast to all users in Default notification list.

Once you're ready to send the message, use a broadcast to notify the users who opted in to the one-time notification request.

In the left menu, go to Broadcasting > Broadcasts, then click +Broadcast.

Under Filter user segments, click +Add condition, then select One-time notification list from the dropdown menu. Select when to broadcast the message, then click Next.

Select an existing module or create a new module that will be sent in the broadcast, then click Next.

📘NoteYou can only send a module containing a single message. Modules containing multiple messages can't be used in one-time notification broadcasts.

Click Broadcast message to send the broadcast. Users in the default one-time notification list, i.e. users who accepted the one-time notification request, will receive the module you selected for this broadcast.

👍Broadcast reportsA broadcast report containing performance data will be available several minutes after the broadcast is sent.Updated 9 days ago



Recurring Notifications Request [0]

https://docs.botbonnie.appier.com/docs/message-type-recurring-notifications-request



👍Supported channels

Facebook

Facebook Messenger's recurring notifications feature enables you to proactively message your users at a predefined cadence, driving re-engagement and creating a customer-centric experience. With recurring notifications, you can send notifications without being restricted to the 24-hour messaging window, enabling you to stay connected with users throughout the customer journey.

Recurring notifications are great for marketing scenarios such as:

New product launches and restocks

Countdowns and early-bird discounts for upcoming sales

Event promotions

The workflow for using recurring notifications consists of three steps:

Send a request for sending recurring notifications at a certain frequency.

User opts in to your recurring notifications.

Send broadcasts at the previously selected frequency to users who opted in.

📘NoteNote

To enable this feature, please reach out to your customer success manager.

See Facebook's official documentation for best practices and limitations.

Follow the steps below to start send recurring notifications to your audience:

Select a method for sending the request: Choose whether the request via chatbot flows, broadcasts, or Growth Tools.

Create the request message: Configure the settings for your recurring notification request, such as the image and title.

Broadcast the recurring notifications: Use broadcasts to send the recurring notification the interval you specified in the initial request.

Select one of the following methods to send the recurring notifications request to your audience:

Chatbot flows

[Broadcasts](#sending-request-via-broadcast)

Growth tools

After you've selected a method for sending the request, create the request message.

In your chatbot flows, click Add module > Recurring notification request, then create the request message.

Go to Broadcasting, click +Create broadcast, add a module that contains the recurring notifications request, then create the request message.



Recurring Notifications Request [1]

https://docs.botbonnie.appier.com/docs/message-type-recurring-notifications-request



Go to Growth tools, click + Add growth tool, select one of the supported options, add a private reply module that contains the recurring notifications request, then create the request message.

PlatformSupported optionsFacebook• Facebook Auto reply for post comment (Private message reply)

• Facebook Multiple Auto Reply (Private message reply)

Configure the following settings for your recurring notifications request:

SettingDescriptionRequested broadcast frequencySelect the frequency of your recurring notifications:

• Daily message for 6 months.ImageThis image is displayed at the top of your recurring notifications request. The image file must meet the following requirements:

• File format must be GIF, JPG, or PNG

• File size must be less than 1 MBNotification titleThis title should describe what the future notifications will be about.Opt-in buttonSelect the module that will be sent to users when they click the opt-in button to indicate that they've opted in to recurring notifications.Users who click this button will be added to the default recurring notifications user list. You'll be able to use this list to send broadcasts to all users who opted in.

Once you're ready to send a follow-up notification, use a broadcast to notify the users who opted in to the recurring notifications request. You'll be able to send broadcasts at the cadence you selected for the Requested broadcast frequency in your module settings.

In the left-hand menu, go to Broadcasting, then click + Create broadcast.

Under Filter user segments, click +Add condition, then select Recurring notification from the dropdown menu. Select when to broadcast the message, then click Next.

Select an existing module or create a new module that will be sent in the broadcast, then click Next.

📘NoteNoteYou can only send a module containing a single message. Modules containing multiple messages can't be used in broadcasts for recurring notifications.



Recurring Notifications Request [2]

https://docs.botbonnie.appier.com/docs/message-type-recurring-notifications-request



Click Broadcast message to send the broadcast. Users in the default recurring notification list, i.e. users who accepted the recurring notifications request, will receive the module you selected for this broadcast.

👍Broadcast reportsA broadcast report containing performance data will be available several minutes after the broadcast is sent.Updated 9 days ago



Random Reply Kit

https://docs.botbonnie.appier.com/docs/random-reply-kit



The random reply kit can be used in campaigns or games where you want to randomly show a different module to users each time. Using this kit, you can:

Add multiple modules and BotBonnie will randomly display one module to the user

You can set the probability for each reply.

Here are some examples of how the random reply kit can be used.

Run a fortune-telling game by having each module be a different fortune result

Conduct a random prize draw by setting each module to be a different prize

From the left menu, go to Flow, then click Advanced kits and select Random reply.

Click Start editing or double-click the kit to open the kit.

Next, click Add module to create some modules. From these modules, BotBonnie will randomly display one to users.

Click Settings and set the probability for each module. You can also click Divide evenly to divide the probability equally among the modules.

Go back to the Flows page, and connect the random reply kit to the rest of the flow.

Updated 9 days ago



Survey Kit [0]

https://docs.botbonnie.appier.com/docs/survey-kit



👍Supported channelsThe survey kit is available for the following channels:

Facebook

Instagram

LINE

WebChat

WhatsApp

Kakao Talk

The survey kit allows you to conduct surveys or have users fill out forms in a more interactive way. Using the survey kit, you can easily:

Collect and save survey responses in a Google spreadsheet

Store users' answers as profile information, user attributes, or user tags

Reward users who successfully completed the survey

Here are some examples of how the survey kit can be used.

Generate leads by having users fill out contact information for an event you're hosting

Conduct a customer satisfaction survey to collect feedback and segment users based on their satisfaction level

Collect product surveys and save users' preferences as tags for precise targeting

From the left menu, go to Flow, then click Advanced kits and select Survey > Add kit.

Click Start editing or double-click the kit to enter the sub-flow of the kit.

Click the Start circle.

Under the Basic section, complete the following settings.

Name: Enter a kit name that helps you identify the kit on the console.

Campaign period: To set a campaign period, switch on the toggle and set the start time and the end time. Select an Out-of-period module to display if the user enters the kit outside of the campaign period.

Survey responses: Enter your Google account. The survey responses will be stored as a Google spreadsheet in this Google account.

Change owner: To change the owner of the sheet, type a different Google account and click Change Owner. The existing survey responses will be transferred to the new account.

Open spreadsheet: Click to see the survey results collected.

Start module: Select the module to display to the users when they start the campaign.

End module: Select the ending module to display to the users when they finish the survey.

📘NoteIf the user leaves the survey halfway through and doesn't reach the final end module, the survey responses already provided by the user will not be recorded in the Google Sheet.



Survey Kit [1]

https://docs.botbonnie.appier.com/docs/survey-kit



Under Column settings, you will see two types of user data you can collect in the survey response:

Auto-recorded info (Blue label): User information that is automatically collected by the messaging platforms such as LINE and Facebook Messenger.

User-submitted info (Gray label): User information gathered through interacting with the module. Each question module in the flow corresponds to a response column labeled in gray.

Use the following settings to adjust how you want the Google spreadsheet to look like.

Switch on the Save toggle for any user information you want to store in the spreadsheet.

You can edit the Column name of the user-submitted info in the spreadsheet.

You can adjust the order of the columns displayed in the spreadsheet.

In the default template of the Survey kit flow, your survey questions are the modules between the start module and the end module.

Click Add module to add a new question or edit from an existing module in the default template.

You can encourage users to participate in the survey by providing a reward. For example, you can let users know about the reward in the Start module and connect the Done module to a lucky wheel or scratch-off kit.

To set up a multiple-choice question, click Add quick reply to add your answer options. Users who click on different answers can be directed to a different module.

To add an input validation, click the User input tab in the module, click Add behavior, select Input format, and select one of the input formats.

Phone number: The user input has to be a number between four to ten digits, without any symbols.

Email: The user input has to be in email format with an @ symbol followed by a domain name.

Date: The user input has to be one of the following formats: yyyy-mm-dd, yyyy/mm/dd, yyyy.mm.dd, yyyymmdd, mm-dd-yyyy, mm/dd/yyyy, mm.dd.yyyy, mmddyyyy

Day-month-year format is not accepted (e.g. 30/9/2023).

The date must include the year, month, and day. A date with just the month and year is not accepted (e.g. 9/2023).



Survey Kit [2]

https://docs.botbonnie.appier.com/docs/survey-kit



The date must include the year, month, and day. A date with just the month and year is not accepted (e.g. 9/2023).

If the format includes slashes, hyphens, or periods, the month and day can be single-digit without a 0 in front (e.g. 9/1/2023).

For mmddyyyy and yyyymmdd, you must add a 0 before a single-digit day or month and make sure there are 8 digits total. For example, "May 8, 2023" must be written as 05082023 or 20230508.

Number: The user input has to be a number.

When the user enters the correct input format, the Bot reply should go to the next question module or the end module. When the user enters incorrect input formats, the Bot reply should go to a module that reminds users to use the correct format.

Answers submitted by users will be automatically stored in a Google spreadsheet, but you can also store them as user profile information, user tags, or user parameters for future marketing purposes. For example, if your user answered that their favorite ice cream flavor is "vanilla", you can store this as a user tag.

To do this, click the User input tab in the question module and under Triggered actions, click Set up triggered actions under the correct input behavior. Click Add action and select one of the options below:

Add tag

Save as user demographic (Phone, email, birthday, location, gender)

Save user parameter

For configurations details, see Triggered Actions.

To see the survey responses, simply open the Google spreadsheet. Go to Survey kit settings and click Open spreadsheet. You need to be logged into the Google account.

Updated 9 days ago



Persona Kit

https://docs.botbonnie.appier.com/docs/persona-kit



👍Supported channels

Facebook

LINE

The persona kit allows you to create engaging roles with unique names and avatars, enabling users to interact with characters that represent your brand or campaign for a more immersive experience. This feature enhances interactions by making conversations feel more dynamic and personalized.

Here are some ways you can use the persona kit:

Create interactive personas for customer engagement: Design a virtual assistant with multiple expert roles or a customer support chatbot with different personas to handle inquiries. You can also use brand characters to enhance interactive campaigns and deepen user engagement.

Enhance brand storytelling in campaigns: Use different personas to represent various aspects of your campaign, switching them dynamically based on campaign needs or user interactions.

From the left menu, go to Flow, click on Advanced kits, then select Persona to add kit to your flow.

Click Start editing or double-click the module to open the Persona kit sub-flow.

Click Settings and select + Add persona to enter a name and upload an avatar image for the new persona. You can add up to 10 roles.

In the persona kit sub-flow, click + Add module to create a new interaction. Then, in the module settings:

Add a message to create the module's content.

Switch to the Persona tab. Select and assign a role from the dropdown to this module. This ensures that the selected persona is displayed as the character for this interaction.

Updated 9 days ago



Receipt Registration Kit [0]

https://docs.botbonnie.appier.com/docs/receipt-registration-kit



👍Supported channelsThe receipt registration kit is available for the following channels:

Facebook

Instagram

LINE

WebChat

The receipt registration kit helps you collect and understand users' purchase behaviors. Users can upload receipt photos or enter receipt details, and you can:

Store and organize receipt and user data.

Filter receipt submissions to identify user's eligibility for rewards.

From the left menu, go to Flow, then click Advanced kits and select Receipt registration.

Click Start editing or double-click the module to open the kit's sub-flow.

Click the Receipt registration kit module to set up your kit. Each module has three tabs containing configuration options:

Settings

Others

Reset

Specify the period for when users can submit receipts to manage your campaign effectively.

Enter your Google account email and click Create Sheet. A spreadsheet link will be generated automatically to collect receipt data.

Check the integration settings and make sure all the IDs and domains are set up correctly across supported channels.

Use the Reset button to clear the receipt data.

🚧CautionResetting the kit will permanently delete all users' receipt data. This action cannot be undone.

Navigate to the Upload receipt module to customize the Messages and User input.

By default, the bot message includes an image, text, and two buttons, which are Upload receipt photo and Enter receipt info. You can modify these messages to match your brand's style and tone.

Behavior #1 is the default for the "Upload receipt" module. Configure the bot's response and triggered actions for this scenario.

Alternatively, use the + Add Behavior button to create custom input scenarios. This lets you specify the input method, bot replies, and triggered actions.

Customize the predefined scenarios for receipt recognition to meet your requirements. Each scenario comes with default text and settings you can customize to match your brand.

There are seven predefined scenarios available for customization:



Receipt Registration Kit [1]

https://docs.botbonnie.appier.com/docs/receipt-registration-kit



There are seven predefined scenarios available for customization:

Predefined scenariosDescriptionQualifiedSent when a receipt meets all validation criteria to confirm successful submission and encourage user participation.Not qualifiedSent when a receipt fails validation criteria to provide rejection reasons and instructions for correction and resubmission.DuplicateSent when the same receipt is submitted multiple times to inform users that it cannot be processed again.Campaign has endedSent when a submission is made after the campaign ends to notify users and direct them to future opportunities.Taiwan Ministry of Finance (MOF) system is busySent when the Taiwan MOF system is busy to reassure users about retry attempts and encourage patience.Taiwan Ministry of Finance (MOF) database not updatedSent when the Taiwan MOF database has not been updated to provide status updates and explain potential processing delays.Recognition failureSent when the system can't recognize a receipt, such as when users upload a low-quality image or unsupported file type, to guide users in resubmitting a clearer image.

Navigate to the Receipt conditions module to customize entry rules, bot replies, and triggered actions for each predefined scenarios.

👍TipRules are evaluated in the order listed in the Receipt conditions module. For example, placing disqualifying conditions before eligibility checks ensures that the bot processes them correctly.In this case, when you put "successfully qualified" as Scenario #1 and "receipt data duplicate" as Scenario #2, the bot will first check whether the uploaded receipt meets Scenario #1 before verifying if it is a duplicate.

After starting the campaign, you can follow the steps below to view receipt data submitted by your users:

Go to the Receipt registration module.

Open the Settings tab and click Open spreadsheet. You need to log in to your Google account to see the data collected.

Updated 9 days ago



Lucky Wheel Kit [0]

https://docs.botbonnie.appier.com/docs/lucky-wheel-kit



Using the lucky wheel kit, you can create a campaign that invites the users to spin a wheel to get a chance to win a prize. With the lucky wheel kit, you can easily:

Customize the appearance of the lucky wheel pages

Set the prizes and the probability of winning each prize

Export the list of participants to a CSV file

View performance report

From the left menu, go to Flow, then click Advanced kits and select Lucky wheel.

Click Start editing or double-click the kit to begin editing.

Enter a Kit name to help you identify the kit in the Flows, and set a Campaign period.

This is the maximum number of times a user can play the lucky wheel.

Maximum entries per user: Specify the total number of time users can play the lucky wheel.

Maximum entries per day: Specify the number of time users can play the lucky wheel each day. The count resets at midnight each day.

Use a parameter value as the number of entries per person: Dynamically apply different numbers of entries to users based on the parameter value associated with each user.

Here's an example of how to use a parameter value as the number of entries. Let's say you want to use this kit to encourage users to get a free trial of a new product in your physical stores by rewarding participants with a chance to play the lucky wheel.

To set this up, go to Growth tools > Start chat with QR code and set Triggered actions > Calculate parameter value to add 1 to a parameter (e.g. luckywheel_spin_num) when the user scans the QR code. After participating in the in-store free trial, users can scan a QR code to get one chance to play the lucky wheel.

Under the Appearance section, you can select a Theme and type up to 2 lines of text for the Headline text. Next to Preview, you can use the drop-down menu on the right to preview what each page looks like.

📘NoteEnterpriseThe Customize appearance option is available for Enterprise Plan only.



Lucky Wheel Kit [1]

https://docs.botbonnie.appier.com/docs/lucky-wheel-kit



📘NoteEnterpriseThe Customize appearance option is available for Enterprise Plan only.

Customize appearance allows you to change the colors of the visual components and upload your own images to replace the background images, wheel outer frame, and the spin button. Refer to the image specifications shown on the BotBonnie console to prepare the images.

You can add up to 7 different prizes and set the options for not winning a prize.

Enable this option if:

You want the probability of winning a remaining prize to remain unchanged after any prize has all been given out.

You don't want the probability of winning a prize to be 100%. Users who didn't win a prize will land on the "Try Next Time" section in the wheel.

You want the probably of winning a prize to be 100%, but you still want to display the "Try next time" message after a user spins.

If one of the prizes runs out first, the probability of getting each remaining prize stays the same, and the probability of not winning a prize increases.

If you want all participants to win a prize, disable the Display "Try next time" in the lucky wheel option and make sure the probability of all prizes adds up to 100%. In this scenario, it's recommended to have a high or unlimited quantity of prizes to prevent prizes from running out.

When a prize runs out, the probability of winning the remaining prizes will increase to allow all participants to win a prize. See the When a prize runs out section for details.

To add a prize, click Add prize.

For each prize, configure the following settings.

Name: Give a name to the prize. This name will be displayed to users when they win the prize.

Image: Upload a 1:1 image less than 1 MB to be the prize image.

Format: Select a prize format. The following prize formats are supported in the Lucky Wheel kit.

Prize formatDescriptionInform users of prizes wonUsers are immediately notified of their winning status. This prize type is ideal for digital prizes that don't require a physical exchange to occur.



Lucky Wheel Kit [2]

https://docs.botbonnie.appier.com/docs/lucky-wheel-kit



For example, this prize type can be used for digital assets such as images.

|

| Physical exchange | This prize type is suitable for brick-and-mortar locations and physical events, where winning users can physically redeem a prize by presenting the winning screen to an employee.

|

| Unique serial number | Upload a CSV file containing a list of unique serial numbers (text, barcode, or URL) that users can exchange for a prize. If this prize type is selected, winners will see the serial number when they win. For example:

• Text: Users who win this prize will be assigned a unique serial number from the CSV file in sequential order. Serial number are suitable for coupons in e-commerce shops or rewards in mobile games.

• Barcode: The serial number will be converted and displayed as a barcode. Barcodes are suitable for physical stores with POS machines.

• URL: The CSV file should contain a list of URLs. When users click the button, they will be directed to the URL to receive the reward. URLs are suitable for distributing LINE points, as it allows users to redeem points with a single click.

Please note the following serial number file requirements:

• Only CSV files are supported

• The file must be less than 10 MB

• The file must contain a single column with the list of serial numbers |

| Fixed serial number | Specify a serial number (text, barcode, or URL) that users can exchange for a prize. If this prize type is selected, winners will see the serial number when they win. For example:

• Text: Users who win this prize will be shown the serial number. Serial number are suitable for coupons in e-commerce shops or rewards in mobile games.

• Barcode: The serial number will be converted and displayed as a barcode. Barcodes are suitable for physical stores with POS machines.

• URL: When users click the button, they will be directed to the URL to receive the reward. URLs are suitable for distributing LINE points, as it allows users to redeem points with a single click. |



Lucky Wheel Kit [3]

https://docs.botbonnie.appier.com/docs/lucky-wheel-kit



| Point card | Select an existing point card kit to send to users who win. |

Quantity: Set the number of prizes to distribute. This setting is unavailable for Unique serial number since the number of prizes available will be based on the number of serial numbers in the CSV file.

Probability: Set the probability of winning this prize. The probability of all prizes can be less than or equal to 100%. The remaining probability will be the chance of not winning a prize.

Let's say you have two prizes each with a 10% chance of winning. This means that for each spin, the user has a 20% chance of winning a prize, and an 80% chance of not winning a prize.

Daily maximum: Set a daily maximum for the number of prizes distributed per day. You can also enable Divide evenly by days if you want to distribute approximately the same number of prizes each day for the duration of the campaign. For example, if the quantity of "Prize A" is 40 and the campaign is 10 days, checking this option will distribute "Prize A" up to 4 times per day.

👍TipFor more details on how BotBonnie calculates the prize distribution and probability, see Understanding prize distribution and probability.

Send a message through chat: Select this option if you want to send a message to the user who won this prize. You can edit the content of the message in the flows.

📘NoteEnterpriseThe Use customized background image option is available for Enterprise Plan only.

Select if you want to display the prize quantity to users.

Show total quantity: Let users see the total number of prizes in the prize list.

Show remaining quantity: Let users see the number of prizes left in the prize list.

Do not show: Do not show the prize quantity in the prize list.

Under this section, you can select Use customized background image if you want to upload your own background image when a prize is won. This image will replace the default animation for the prize redemption page and the result page when a prize is won.



Lucky Wheel Kit [4]

https://docs.botbonnie.appier.com/docs/lucky-wheel-kit



Select Show prize image to display the prize image on these two pages on top of the customized background image.

This section is available when you have set a probability of not winning a prize.

Under this section, you can select Use customized background image if you want to upload your own background image when no prize is won. This image will replace the default animation for the result page when no prize is won.

Select Send a message through chat if you want to send a message to the user who didn't win a prize. You can edit the content of the message in the flows.

Modify the terms and conditions of this campaign or type any information about the game to suit your campaign. These terms and conditions are displayed at the bottom of the lucky wheel homepage.

Under normal circumstances, no action is needed in this section. BotBonnie will automatically detect if your channels are successfully connected with BotBonnie. If you run into issues here, contact Appier Support or your customer success manager for assistance.

Go back to the Flows page, and adjust the content of each module to suit your campaign.

Resetting a kit is useful if you ran the campaign to do internal testing, and now want to clear all test data before officially launching the campaign.

Resetting a kit will clear all data associated with the kit.

All records of participant data (e.g. user details, spins, and wins) will be deleted

All prizes will be returned to the prize pool

The kit report will be cleared

🚧WarningCautionThis action can't be reversed.

In the lucky wheel kit settings, go to the Reset section, then click Reset. You'll be prompted to type in Reset into the input box, then click Reset again to confirm.

To view the performance report of the lucky wheel kit, in the sub flow of the lucky wheel kit, click Kit Report.

The report includes prize inventory status, number of participants, and number of spins.

To export the list of participants and their related data, click Export participant list in the top-right corner.



Lucky Wheel Kit [5]

https://docs.botbonnie.appier.com/docs/lucky-wheel-kit



To export the list of participants and their related data, click Export participant list in the top-right corner.

Type the email address where you'd like the CSV file to be sent to, then click Confirm. A CSV file will be sent to you within an hour.

The exported file contains a list of users who participated in the game with details such as user name, prize won, drawn time...etc.

Total participants: This is the number of users who played the game, including users who didn't win a prize.

Number of entries: This is the number of times users played the game, including the draws where no prize is won.

Prize status: You can monitor the number of prizes left in the prize pool in the Remaining column.

Select a time period to see the performance data during that period. There are three line graphs available:

Participants

Number of prizes won in each category

Number of entries

This section explains how BotBonnie distributes prizes and adjusts the probability of winning a prize under different scenarios.

If you select Evenly distribute this prize in prize settings, BotBonnie tries to distribute the same number of prizes each day during the campaign period.

If the divided number is not a whole number, BotBonnie will round up to the next whole number.

For example, let's say you have 10 prize A and the campaign period is 20 days, which equals to 0.5 prizes per day. When distributing prizes, BotBonnie will round up this number and distribute up to 1 prize on the first day.

PrizeQuantityCampaign durationFirst dayFirst 2 daysFirst 3 daysPrize A1020 days0.5 (Round up to 1)11.5 (Round up to 2)

📘NoteNoteIn actual distribution, it's also possible that no prize is drawn on the first day or first two days (e.g. due to too few participants), and 2 prizes are distributed on the third day.

When a prize runs out, the distribution of the remaining prizes differs based on whether the Display "Try next time" in the lucky wheel option is enabled under the Didn't win a prize section.

If the total probability of winning a prize adds up to 100%:



Lucky Wheel Kit [6]

https://docs.botbonnie.appier.com/docs/lucky-wheel-kit



If the total probability of winning a prize adds up to 100%:

If Display "Try next time" in the lucky wheel is enabled, the probability of winning each remaining prize stays the same when a prize runs out.

If Display "Try next time" in the lucky wheel isn't enabled, after a prize is finished being distributed, the probability of winning of remaining prizes increases to ensure the total probability of winning a prize adds up to 100%.

For example, let's say you have 2 different prizes, Prize A with a 10% probability and Prize B with a 30% probability. When Prize A runs out, the probability of Prize B stays the same, and the probability of not getting a prize increases.

PrizesOriginal probabilityProbability after Prize A runs outPrize A10%Runs outPrize B30%30% (Unchanged)No prize60%70%

If Display "Try next time" in the lucky wheel is disabled, BotBonnie will automatically adjust the probability of winning the remaining prizes to allow all participants to win a prize.

One remaining prize: Let's say you have 2 different prizes, Prize A with a 10% probability and Prize B with a 90% probability. When Prize A runs out, the probability of Prize B now becomes 100% to allow all participants to win a prize.

PrizesOriginal probabilityProbability after Prize A runs outPrize A10%Runs outPrize B90%100%No prize0%0%

Multiple remaining prizes: If there are multiple remaining prizes, BotBonnie will adjust the probability proportionally. Let's say you have 3 different prizes. Prize A has a 10% probability, Prize B has a 30% probability, and Prize C has a 60% probability.

When Prize A runs out, BotBonnie will distribute the 10% chance of winning Prize A proportionally to Prize B and Prize C based on the ratio of Prize B to Prize C (3:6). As a result, the probability of Prize B and Prize C becomes 33.3% and 67.7% respectively.

PrizesOriginal probabilityProbability after Prize A runs outPrize A10%Runs outPrize B30%33.3%Prize C60%66.7%No prize0%0%Updated 9 days ago



Scratch-Off Kit [0]

https://docs.botbonnie.appier.com/docs/scratch-off-kit



Use the scratch-off kit to create a campaign that allows users to play a scratchcard game from their mobile device or web browser. With the scratch-off kit, you can easily:

Update prize inventory

Export the list of participant to a CSV file

View detailed performance data in the kit report page

From the left menu, go to Flow. Click Advanced kits, select Scratch-off, then click Add kit to add the kit to your flow. To start editing the kit's settings, click Start editing or double-click the kit module.

Enter a Kit name to help you identify the kit in your flow, and set a Campaign period by selecting a start and end time.

This is the maximum number of times a user can play the scratch-off game.

Maximum entries per user: Specify the total number of time users can play the scratch-off game.

Maximum entries per day: Specify the number of time users can play the scratch-off game each day. The count resets at midnight each day.

Use a parameter value as the number of entries per person: Dynamically apply different numbers of entries to users based on the parameter value associated with each user.

In the following example, we want to encourage users to participate in a free trial of a new product in your physical stores by rewarding participants with a chance to play the scratch-off game. To accomplish this, we'll use a scratch-off kit using a parameter value as the number of entries per person.

Set up the in-store scannable QR code. Go to Growth tools > Start chat with QR code and select the module containing the promotional message.

Give users an additional chance to play the scratch-off game after scanning the QR code. Set Triggered actions > Calculate parameter value to add 1 to a parameter (e.g. scratch_off_attempts) when the user scans the QR code.

After completing these steps, we can let users scan the QR code to get another chance to play the scratch-off game after participating in the in-store free trial.

Upload the image for the scratch card. Images must meet the following requirements:



Scratch-Off Kit [1]

https://docs.botbonnie.appier.com/docs/scratch-off-kit



Upload the image for the scratch card. Images must meet the following requirements:

The file format must be JPG or PNG

The aspect ratio should be 1:1 (square)

The kit provides a default terms and conditions statement enumerating the rules for participation in this promotion. These terms and conditions are displayed at the bottom of the scratch card screen. Modify this field if you'd like to customize the terms and conditions statement to suit your campaign.

To add a prize, click Add prize

To remove a prize, click X in the top right-hand corner of the prize

Prize name: The name of the prize that's displayed to the user when they win.

Prize format: Prizes can have one of the following formats:

Prize formatDescriptionInform users of prizes wonUsers are immediately notified of their winning status. This prize type is ideal for digital prizes that don't require a physical exchange.

For example, this prize type can be used for digital assets, such as exlusive images.

|

| Physical exchange | This prize type is suitable for brick-and-mortar locations and physical events, where winning users can physically redeem a prize by presenting the winning screen to an employee.

|

| Unique serial number | Upload a CSV file containing a list of unique serial numbers (text, barcode, or URL) that users can exchange for a prize. If this prize type is selected, winners will see the serial number when they win the scratchcard game. For example:

• Text: Users who win this prize will be assigned a unique serial number from the CSV file in sequential order. Serial number are suitable for coupons in e-commerce shops or rewards in mobile games.

• Barcode: The serial number will be converted and displayed as a barcode. Barcodes are suitable for physical stores with POS machines.

• URL: The CSV file should contain a list of URLs. When users click the button, they will be directed to the URL to receive the reward. URLs are suitable for distributing LINE points, as it allows users to redeem points with a single click.



Scratch-Off Kit [2]

https://docs.botbonnie.appier.com/docs/scratch-off-kit



Please note the following serial number file requirements:

• Only CSV files are supported

• The file must be less than 10 MB

• The file must contain a single column with the list of serial numbers |

| Fixed serial number | Specify a serial number (text, barcode, or URL) that users can exchange for a prize. If this prize type is selected, winners will see the serial number when they win the scratchcard game. For example:

• Text: Users who win this prize will be shown the serial number. Serial number are suitable for coupons in e-commerce shops or rewards in mobile games.

• Barcode: The serial number will be converted and displayed as a barcode. Barcodes are suitable for physical stores with POS machines.

• URL: When users click the button, they will be directed to the URL to receive the reward. URLs are suitable for distributing LINE points, as it allows users to redeem points with a single click. |

| Point card | Select an existing point card kit to send to users who win the scratchcard game. |

Quantity: Set the number of prizes to distribute. This setting is unavailable for prizes with the prize type set to Unique serial number.

Probability: Set the probability of winning this prize.

Set an upper limit for the number of prizes that can be distributed per day.

To distribute approximately the same number of prizes each day for the duration of the campaign, check Divide evenly by days. For example, if the quantity of "Prize A" is 10 and the campaign is five days, checking this option will distribute "Prize A" approximately twice per day.

When this option is checked, the estimated maximum number of prizes to be distributed per day will be shown:

Under When no prize is won, select the module or message that users should see if they don't win a prize.

To view the scratch-off kit report, in the left-hand navigation bar, go to Analytics > Kit Report, then open the report you'd like to view. Scratch-off kit reports contain a summary of the number of participants and prizes distributed.



Scratch-Off Kit [3]

https://docs.botbonnie.appier.com/docs/scratch-off-kit



In addition, under Detailed data, graphs are provided to visualize the kit's performance data for a specific time period. You can view:

The total number of participants

The total number of prizes won, broken down by prize (counts for total prizes and counts for individual prizes)

The total number of draws (scratch-off attempts)

From the kit report page, you can export a CSV containing a list of participants and their associated data.

Click Export participant list.

In the modal that pops up, input the email address where you'd like the CSV file to be sent to.

Click Confirm. An email containing the file will be sent to the email address you specified within one hour.

The participant list file contains the following details:

User ID

User Name

Conversation Platform

User Gender

Prize Title

Prize

Serial number

Kit ID

Drawn time

Redeemed time

User profile

Reset a kit to refresh all data associated with the kit:

All records of participant data (e.g. user details, draws, and wins) will be deleted

All prizes will be returned to the prize pool

All data in the kit report will be cleared

🚧WarningCautionResetting the kit can't be reversed. Once the kit is refreshed, all records of participant data and prize distribution (including the kit report) will be cleared and all prizes will be returned to the prize pool.

In the scratch-off kit settings, go to the Reset section, then click Reset. You'll be prompted to type in "Reset" into the input box, then click Reset again to confirm your choice.

When setting distribution probabilities for prizes, please note the following behaviors:

The probability of losing

The probability when a prize runs out

Calculating the maximum daily prize distribution

If the probabilities don't add up to 100%, the remainder will be the probability of losing (not winning any prize).

For example, given two prizes, "Prize A" and "Prize B", each with a probability of 30%, totaling 60% (30% + 30% = 60%), the probability of losing would be 40% (100% - 60% = 40%).



Scratch-Off Kit [4]

https://docs.botbonnie.appier.com/docs/scratch-off-kit



If there are multiple prizes and one prize runs out, the probability of winning the remaining prize(s) stays the same, and the probability of not winning a prize increases.

PrizeOriginal probabilityProbability after Prize A runs outPrize A10%0% (Runs out)Prize B20%20% (Unchanged)Prize C30%30% (Unchanged)No prize40%50%

The daily prize distribution maximum is calculated in real-time for each prize based on how many days have passed since the beginning of the campaign. The calculation for the maximum number of prizes to be distributed by the end of a given day is calculated as follows:

Campaign elapsed time (days) / Total campaign duration (days) * Prize pool quantity

The difference between the total expected number of distributed prizes (the total number of prizes that should be distributed by this point in the campaign) and the actual number of distributed prizes (the total number of prizes that have already been distributed so far during the campaign) determines the distribution limit for that day.

📘NoteNoteIf the daily distribution maximum isn't a whole number, it will be rounded up to the nearest whole number. This can result in variations in the daily prize distribution limit for each day of the campaign.

For example, given a campaign period of seven days, and a single prize, "Prize A", with a quantity of 30 and a 100% probably of winning (no other prizes, no chance of losing), the estimated counts for the daily distribution are listed in the table below:

DayDaily calculationPrizes distributed so farPrizes to distribute today1(1/7 * 30) = 4.28 → 5

A maximum of 5 prizes should be distributed by the end of day one. | 0 prizes | (5 - 0) = 5

Up to 5 prizes can be distributed today. |

| 2 | (2/7 * 30) = 8.57 → 9

A maximum of 9 prizes should be distributed by the end of day two. | 5 prizes | (9 - 5) = 4

Up to 4 prizes can be distributed today. |

| 3 | (3/7 * 30) = 12.85 → 13

A maximum of 13 prizes should be distributed by the end of day three. | 9 prizes | (13 - 9) = 4

Up to 4 prizes can be distributed today |



Scratch-Off Kit [5]

https://docs.botbonnie.appier.com/docs/scratch-off-kit



Up to 4 prizes can be distributed today |

| 4 | (4/7 * 30) = 17.14 → 18

A maximum of 18 prizes should be distributed by the end of day four. | 13 prizes | (18 - 5) = 5

Up to 5 prizes can be distributed today. |

| 5 | (5/7 * 30) = 21.42 → 22

A maximum of 22 prizes should be distributed by the end of day five. | 18 prizes | (22 - 18) = 4

Up to 4 prizes can be distributed today. |

| 6 | (6/7 * 30) = 25.71 → 26

A maximum of 26 prizes should be distributed by the end of day six. | 22 prizes | (26 - 22) = 4

Up to 4 prizes can be distributed today. |

| 7 | (7/7 * 30) = 30

A maximum of 30 prizes should be distributed by the end of day seven. | 26 prizes | (30 - 26) = 4

Up to 4 prizes can be distributed today. |Updated 9 days ago



Account Linking Kit [0]

https://docs.botbonnie.appier.com/docs/account-linking-kit



👍Supported channels

LINE

Facebook

Use the account linking kit to establish a mapping between a user's account on the connected platform, such as LINE or Facebook, with their BotBonnie profile.

With account linking, you can:

Create user segments based on a user's account linking status

Enrich a user's profile by adding their ID from your customer relationship management platform, e.g. for enhanced customer service and support and filtering

After you've established a link between the user in your CRM and the user in BotBonnie, you'll be able to see the user's CRM ID in their profile in the Personalization Cloud console under Audience > User list:

To reflect a user's new linking status when linking or unlinking an account via API, you can also choose to optionally update the following details associated with the BotBonnie user:

Tags

Parameters

Assigned menu groups (LINE menus, Messenger menus)

Work with your developers to implement a login page for account linking—this is the page that will be opened by the account linking kit. The login page is required to:

Collect the details required to link the account, i.e. the user's ID

Receive URL parameters that will be to sent to BotBonnie to authorize the account linking process

Create a login page for users who want to link their account.

When the user navigates to the account linking page, you'll need to:

Extract BotBonnie account linking parameters from the query string of the login page. The parameters differ depending on the messaging platform you're using:

LINE account linking parameters

Messenger account linking parameters

Retrieve the user's ID in your CRM. This is a required account linking parameter.

Add the user's messaging platform ID (i.e. LINE user ID or Messenger ID) to your database.



Account Linking Kit [1]

https://docs.botbonnie.appier.com/docs/account-linking-kit



Add the user's messaging platform ID (i.e. LINE user ID or Messenger ID) to your database.

NameDescriptioncarryAn account linking parameter contained in the login page URL's query string.Note: carry must be extracted from the login page URL and appended to the account linking success page's URL.linkTokenAn account linking parameter contained in the login page URL's query string.Note: linkToken must be extracted from the login page URL and appended to the account linking success page's URL. This parameter is only valid for 10 minutes.nonceThe user's unique ID in your CRM. Must be 10-255 characters.

NameDescriptioncarryAn account linking parameter contained in the login page URL's query string.Note: carry must be extracted from the login page URL and appended to the account linking success page's URL.redirect_uriAn account linking parameter contained in the login page URL's query string.Note: redirect_uri must be extracted from the login page URL and appended to the account linking success page's URL.account_linking_tokenAn account linking parameter contained in the login page URL's query string.Note: account_linking_token must be extracted from the login page URL and appended to the account linking success page's URL.authorization_codeThe user's unique ID in your CRM. Must be 10-255 characters.

Once the user has entered their details in your login page, redirect the user to the account linking success page and pass the account linking parameters in the URL.

The redirect URL must include all account linking parameters in its query string for BotBonnie to update the user's profile. Once the page is loaded, BotBonnie will extract the parameters from the query string to complete the process.

Messaging platformAccount linking success page URLLINEhttps://rd.botbonnie.com/account/link?carry=&linkToken=&nonce=Messengerhttps://rd.botbonnie.com/account/link?carry=&redirect_uri=&account_linking_token=&authorization_code=



Account Linking Kit [2]

https://docs.botbonnie.appier.com/docs/account-linking-kit



From the left menu, go to Flow, then click Advanced kits and select Account linking.

Open the kit and click Start editing to open the account linking kit sub-flow.

In the module titled Start account linking, click the button used to initiate the account linking process (the default name is Link now), then set the following settings:

Button name: Input a button label. This is visible to the user.

On click: Paste the URL of your login page.

(Optional) In the module titled Result conditions #2 and Linked successfully, you can set a custom reply and triggered actions upon a successful account linking.

Deploy your changes.

Updated 9 days ago



Daily Check-In Kit [0]

https://docs.botbonnie.appier.com/docs/daily-checkin-kit



## Overview

> 👍 Supported channels

>

> The daily check-in kit is available for the following channels:

>

> * Facebook

> * Instagram

> * LINE

> * WebChat

The daily check-in kit allows you to provide incentives for users to check in. You can set up consecutive or nonconsecutive check-ins, with different rewards for each check-in day or after completing a series of check-ins.

Using the daily check-in kit, you can easily:

* Create campaigns with consecutive or nonconsecutive check-in types.

* Set different rewards for each check-in milestone.

* Track check-in progress and monitor remaining rewards.

***

### Example use case: Encouraging daily visits

A breakfast chain wants to increase customer visits to their physical stores. To accomplish this, the business can use BotBonnie's daily check-in kit with their LINE official channel's rich menu to offer rewards for daily visits. When customers complete seven consecutive daily check-ins, they can redeem a free cookie in-store.

![](https://files.readme.io/f3b776e-Screen_Shot_2023-05-29_at_4.59.11_PM.png)

***

## Daily check-in kit setup

### 1. Add the kit to your flow

From the left menu, go to **Flow**, then click **Advanced kits** and select **Daily check-in**.



Click **Start editing** or double-click the kit to enter the kit's subflow.



Click on the **Check in** module to set up the kit.



### 2. Configure basic kit settings

Under the **Basic** section, complete the following settings:

* **Kit name**: Enter a name to help you identify the kit in your flow.

* **Campaign period**: Set a campaign start and end time. 

* **Headline text**: Enter the headline displayed on the check-in page.



Daily Check-In Kit [1]

https://docs.botbonnie.appier.com/docs/daily-checkin-kit



* **Headline text**: Enter the headline displayed on the check-in page.

* **Terms and conditions**: Modify the terms and conditions of this campaign or type any information about the campaign to suit your needs. These terms and conditions are displayed at the bottom of the campaign page.



### 3. Set the check-in rules and rewards

In the **Rules** section, configure the [check-in rules](#check-in-rules) and [day-specific reward rules](#each-check-in-day-settings) to customize the check-in kit.

#### Check-in rules

Define the following rules:









Rule





Description





Example













Check-in type





Identify user eligibility for rewards based on consecutive or nonconsecutive check-in patterns. 

Options:\

• Consecutive\

• Nonconsecutive





• For three consecutive check-ins:\

If a user misses a day after two check-ins, the check-in count is reset, and the user has to start over with the consecutive check-ins. 

• For three nonconsecutive check-ins:\

Users can check in on any three days during the campaign.









Maximum consecutive check-ins





Set a limit for consecutive check-ins (up to seven days).





If set to three days, users must check in three days in a row without missing any.









Nonconsecutive check-ins





Set the number of nonconsecutive check-ins required (up to seven days).





If set to three days, users can check in on any three days within the campaign period, no matter the order.









Maximum check-in rounds





Set how many times a user can complete the check-in process. 

Options:\

• Unlimited\

• Enter a number between 1 and 10.







Daily Check-In Kit [2]

https://docs.botbonnie.appier.com/docs/daily-checkin-kit



Options:\

• Unlimited\

• Enter a number between 1 and 10.





If the maximum check-in round is set to 1, each user can complete the process only once during the campaign.











> 📘 Note

>

> When switching from nonconsecutive to consecutive check-ins, only check-ins from the previous day will carry forward. 

>

> For example, if the check-in campaign was configured as follows:

>

> * Start date: December 20

> * Required check-ins: 5 days

> * Change date: December 23

>

> After the switch:

>

> * System keeps: Only December 22 check-ins

> * System resets: All other check-ins

> * New check-ins: Start fresh consecutive count from December 23

#### Day-specific reward configuration

For each check-in day, use the **Grant a reward** toggle to specify whether users receive a reward. For example, you can set no reward for the first two days and only provide a reward after the third check-in, whether consecutive or nonconsecutive.



If you've enabled **Grant a reward**, configure the following reward settings.

* **Name:** Enter the name of the reward, for example, "20% off coupon". This name will be displayed to the user when they open the check-in page.

* **Format:** Select a reward format. The following table describes the format in this kit.









Prize format





Description













**Inform users of prizes won**





Users are immediately notified of their winning status. This prize type is ideal for digital prizes that don't require a physical exchange to occur. 

For example, this prize type can be used for digital assets such as images.



Daily Check-In Kit [3]

https://docs.botbonnie.appier.com/docs/daily-checkin-kit



For example, this prize type can be used for digital assets such as images. 











**Physical exchange** 





This prize type is suitable for brick-and-mortar locations and physical events, where winning users can physically redeem a prize by presenting the winning screen to an employee. 











**Unique serial number**





Upload a CSV file containing a list of unique serial numbers (text, barcode, or URL) that users can exchange for a prize. If this prize type is selected, winners will see the serial number when they win. For example: 

• **Text**: Users who win this prize will be assigned a unique serial number from the CSV file in sequential order. Serial number are suitable for coupons in e-commerce shops or rewards in mobile games.\

• **Barcode**: The serial number will be converted and displayed as a barcode. Barcodes are suitable for physical stores with POS machines.\

• **URL**: The CSV file should contain a list of URLs. When users click the button, they will be directed to the URL to receive the reward. URLs are suitable for distributing LINE points, as it allows users to redeem points with a single click. 



Please note the following serial number file requirements:

• Only CSV files are supported

• The file must be less than 10 MB

• The file must contain a single column with the list of serial numbers









**Point card**





Select an existing point card kit to send to users who win.











Daily Check-In Kit [4]

https://docs.botbonnie.appier.com/docs/daily-checkin-kit



**Point card**





Select an existing point card kit to send to users who win.









* **Quantity:** Set the number of rewards available. This setting is unavailable for **Unique serial number** since the number of rewards available will be based on the number of serial numbers in the CSV file.

* **Image:** Upload the main reward image if needed. This image will be shown on the reward result page. 

### 4. Check the messaging platform status

In the **Others** section, verify that all messaging platforms are properly configured and active.



***

## Check-in status

After you start running the kit, you can go to the **Check-in Status** section to see the number of users who have checked in for each day and monitor the number of rewards left in the **Remaining** column.



***

## Reset kit data

You can reset a kit if you've used it for internal testing and want to clear all test data before officially launching your campaign.

When you reset a kit, the following data will be permanently deleted:

* Participant data: Includes user details, entries, and rewards.

* Rewards: All distributed rewards will be returned to the reward pool.

* Check-in status: All check-in progress will be reset.

> 🚧 Caution

>

> Resetting the kit will permanently delete all participant data and check-in progress. This action cannot be undone.

### How to reset a kit

1. Go to the **Reset** section.

2. Click **Reset**. 

3. Enter "Reset" into the input box.

4. Click **Reset** again to confirm your choice.

Updated 9 days ago



Serial Number Verification Kit [0]

https://docs.botbonnie.appier.com/docs/serial-number-verification-kit



👍Supported channelsThe serial number verification kit is available for the following platform:

Facebook

Instagram

LINE

WebChat

WhatsApp

The serial number verification kit allows you to control which users enter a specific flow by requesting them to provide a serial number. Using this kit, you can:

Upload a list of serial numbers

Export a report with serial number usage details

Reset the serial number list so that serial numbers can be reused

Our brand is running a promotion where unique prize codes are printed on bottle caps. Customers who purchase these bottles can submit prize codes via messaging channels (e.g. Messenger, LINE, WhatsApp) to redeem a free gift.

The serial number verification kit allows us to create a flow that prompts users to input their contact information to receive the prize, while also ensuring that only users with valid, winning prize codes enter that flow. For example, using this kit, we can:

Prompt the user to enter the prize code in a chat message

If the prize code is valid, the user enters the flow to enter their contact information to receive the prize

If the prize code is invalid, reply to the user notifying the user of the reason for invalidity

In addition to verifying serial numbers and distributing standard prizes, we also want to hold a raffle for all users who participated in this promotion and pick a grand winner who will win an additional special prize.

We can accomplish this by:

Adding an action to the flow scenario that tags all participating users who submitted a valid serial number. For example, we can tag all participating users with the following tag: CampaignA_20220101.

After the campaign is completed, filter the user list by the tag we applied (i.e. CampaignA_20220101) to retrieve the list of users who participated in this campaign.

From the list of tagged users, randomly select one grand winner who will receive the special prize.

From the left menu, go to Flow, then click Advanced kits and select Serial number verification.



Serial Number Verification Kit [1]

https://docs.botbonnie.appier.com/docs/serial-number-verification-kit



From the left menu, go to Flow, then click Advanced kits and select Serial number verification.

To start editing the kit's settings, click Start editing or double-click the kit module.

Under the Basic section, upload a CSV file with a single column containing the serial numbers you'd like to use for this kit. The serial number CSV file must be under 10 MB.

After you successfully upload the serial number file, the number of serial numbers contained in the file will be displayed next to Amount.

Under the Valid serial number and Invalid serial number sections, you can set bot replies and actions for the kit's four flow scenarios.

Valid serial number

Flow scenario #1: The user entered a valid and unused serial number

Flow scenario #2: The user entered a valid serial number that has already been used by that user

Flow scenario #3: The user entered a valid serial number that has already been used by another user

Invalid serial number

Flow scenario #4: The user entered an invalid serial number

To change the bot reply configured for a flow scenario, go to the flow scenario you want to edit the bot reply for, and from the dropdown, select the kit module you want to use as the bot reply.

Add any required actions for the flow scenarios. For an example use case of how actions can be used in your kit's flows, see Adding actions to flow scenarios.

The serial number usage report contains the usage details for each serial number. Columns corresponding to unused serial numbers will be empty. Refer to the following table for descriptions of each column in the report:

Column nameDescriptioncustomerIdThe ID of the user.pageIdThe ID of the page as provided by the third-party channel (e.g. LINE, Facebook).platformA number representing the platform the user used to submit the serial number. For example, if this column has a value of 1, it means the user submitted the serial number using LINE.The mappings for each platform are as follows:• 0: Facebook

• 1: LINE

• 2: WebChat

• 4: Google Business Messages

• 5: Instagram

• 6: WhatsApp



Serial Number Verification Kit [2]

https://docs.botbonnie.appier.com/docs/serial-number-verification-kit



• 1: LINE

• 2: WebChat

• 4: Google Business Messages

• 5: Instagram

• 6: WhatsApp

• 7: AIQUAUsed timestampA timestamp indicating the time that the user submitted the serial number.Serial NumberThe serial number as specified in the uploaded CSV file.

To export the serial number usage report:

Go to Basic > Upload serial number, then click Export report.

Input the email address where you'd like the report download link to be sent to, then click Confirm.

When the report is ready, a download link will be sent to the email address you provided.

Resetting serial numbers allows you to:

Make all serial numbers valid again

Clear all activity logs for this kit

Clear the serial number usage report for this kit

🚧CautionThis action can't be reversed. Once the serial number list is refreshed, the kit's activity log (including all data in the serial number usage report) will be cleared and all serial numbers will become valid again.

In the serial number verification kit settings, go to the Reset section, then click Reset. You'll be prompted to type in "Reset" into the input box, then click Reset again to confirm your choice.

Updated 9 days ago



Prize Distribution Kit [0]

https://docs.botbonnie.appier.com/docs/prize-distribution-kit



👍Supported channelsThe prize distribution kit is available for the following channels:

Facebook

Instagram

LINE

WebChat

The prize distribution kit allows you to give away prizes to all users who are directed to the prize distribution kit. Differing from other advanced kits where you set a winning probability to only let some users win a prize, prize distribution kit is suitable for campaigns where you want all eligible users to get a prize.

With the prize distribution kit, you can easily:

Hand out prizes to users

See the number of prizes that are distributed and redeemed

Export the list of winners to a CSV file

View performance report

A brand is giving the followers of its LINE official channel a free gift for Thanksgiving. The marketers can connect the rich menu of their LINE official channel to BotBonnie's prize distribution kit. Users who click the gift button in the LINE rich menu can get the free gift.

In the Flows page, click Advanced kits, select Prize distribution, and click Add kit to add the kit to your flows.

Click Start editing or double-click the kit to enter the sub-flow of the kit.

Click the Prize distribution module.

Under Basic section, enter a Kit name to help you identify the kit in the Flows and set a Campaign period.

You can set the maximum number of times a user can enter the campaign.

Alternatively, you can select Use a parameter value as the number of entries to dynamically apply different numbers to users based on the parameter value associated with each user.

If users are still eligible for more entries after a prize is distributed, there will be a Get another one button in the prize distributed page.

👍TipTo create a parameter, go to Audience > User properties > Parameters and click New parameter.

Configure the following prize settings.

Prize name: Type the name of the prize (e.g. "20% off coupon"). This name will be displayed to users when they win the prize.

Thumbnail: Upload a thumbnail image of the prize if needed. This image will be shown in the prize list.



Prize Distribution Kit [1]

https://docs.botbonnie.appier.com/docs/prize-distribution-kit



Thumbnail: Upload a thumbnail image of the prize if needed. This image will be shown in the prize list.

Detailed image: Upload the main prize image if needed. This image will be shown in the prize result page.

Prize format: Select a prize format. The following prize formats are supported in the prize distribution kit.

Prize typeDescriptionInform users of prizes wonUsers are immediately notified of their winning status. This prize type is ideal for digital prizes that don't require a physical exchange to occur.For example, this prize type can be used for multi-use coupon codes and digital assets such as images.Physical exchangeThis prize type is suitable for brick-and-mortar locations and physical events, where winning users can physically redeem a prize by presenting the winning screen to an employee.Unique serial number: TextThis option allows you to upload a CSV file containing a list of unique serial numbers. Users who win this prize will be assigned a unique serial number based on the order of the serial number in the file until the serial number runs out. For example, the first winning user will receive serial number A001, the second user will receive A002, etc.Serial number file requirements:

• Only CSV files are supported

• The file must be less than 10 MB

• The file must contain a single column with the list of unique serial numbers\ This prize type is suitable for coupons in e-commerce shops or rewards in mobile games.Unique serial number: BarcodeThis prize type is similar to the text-format unique serial number, except that the serial number will be converted and displayed as a barcode. Select the appropriate barcode type such as Code-39.This prize type is suitable for physical stores with POS machines.Unique serial number: URLThe CSV file should include the URL of each serial number. When users click the button, they will be directed to the URL to receive the reward.This prize type is suitable for giving out LINE points. Users can redeem this type of prize with one simple click.



Prize Distribution Kit [2]

https://docs.botbonnie.appier.com/docs/prize-distribution-kit



Quantity: Set the total number of prizes that can be distributed. This setting is unavailable for Unique serial number since the number of prizes available will be based on the number of serial numbers in the CSV file.

Redemption period:

Never expire: Users can redeem the prize at anytime.

Apply redemption period: Set a time period for users to redeem the prize and the prize will be expired after the end time. The expiration date will be displayed to users when they win the prize.

Apply daily maximum: If you want to set a maximum number of prizes that can be distributed per day, select the option and type the maximum number of prizes that can be distributed each day.

Click Divide evenly by days to evenly divide the prize quantity by the number of days in the campaign period. If you edit the quantity or campaign period, the changes will not be reflected automatically. You will need to click this button again.

If the actual number of prizes distributed on a day is less than the daily maximum, the remaining prizes will be accumulated to the next day.

Send a message through chat: Select this option if you want to send a message to the user who won this prize. You can edit the content of the message in the flows.

You can customize the message that will be shown to users in the result page when the user didn't get a prize. There are two scenarios:

When prizes run out

When daily maximum is reached

Modify the terms and conditions of this campaign or type any information about the campaign to suit your needs. These terms and conditions are displayed at the bottom of the result pages.

Under normal circumstances, no action is needed in this section. BotBonnie will automatically detect if your channels are successfully connected with BotBonnie. If you run into issues here, contact Appier Support or your customer success manager for assistance.

Go back to the Flows page, and adjust the content of other modules in the sub-flow to suit your campaign.



Prize Distribution Kit [3]

https://docs.botbonnie.appier.com/docs/prize-distribution-kit



Go back to the Flows page, and adjust the content of other modules in the sub-flow to suit your campaign.

Resetting a kit is useful if you ran the campaign to do internal testing, and now want to clear all test data before officially launching the campaign.

Resetting a kit will clear all data associated with the kit.

All records of participant data (e.g. user details, entries, and prizes) will be deleted

All prizes will be returned to the prize pool

The kit report will be cleared

🚧WarningWarningCautionThis action can't be reversed.

In the kit settings, go to the Reset records section, then click Reset. You'll be prompted to type in Reset into the input box, then click Reset again to confirm.

To view the performance report of the prize distribution kit, go to Analytics > Kit report and click the view icon.

In the report, the following metrics are available.

Total participants: This is the number of users who entered the campaign, including user who didn't get a prize.

Number of prizes distributed: This is the number of prizes distributed to users.

Prizes redeemed: This is the number of prizes that are redeemed by the users.

Under Prize status, you can monitor the number of prizes left in the prize pool in the Remaining column.

To export the list of winners and their related data, click Export list in the top-right corner.

Type the email address where you'd like the CSV file to be sent to, then click Confirm. A CSV file will be sent to you within an hour.

The exported file contains a list of users who won a prize with details such as user name, prize won, drawn time...etc.

Updated 9 days ago



Point Card Kit [0]

https://docs.botbonnie.appier.com/docs/point-card-kit



Use BotBonnie's point card kit to build customer loyalty by letting users earn points when they shop or interact with your brand. You can set up different rewards that can be redeemed with points to motivate users.

Using the point card kit, you can easily:

Customize the appearance of the point card

Let users earn points through QR code/URL or as an incentive in other advanced kits

Set up different rewards that can be redeemed with points

In the Flows page, click Advanced kits, and select Point card to begin editing kit settings.

Click Start editing or double-click the kit to open the kit.

Click the Point card module.

Under the Basic section, complete the following settings.

Kit name: Enter a kit name that helps you identify the kit on the console.

Total points per card: This is the maximum number of points that can be accumulated on each point card.

Welcome points: This is the number of points granted to users when they join the campaign. When points are given at the beginning, users are more motivated to continue earning points. For example, you can let users start off with 3 points already on the point card.

Under the Schedule section, set up the following time periods.

Campaign period: Set the campaign period of this point card. Point collection, point redemption, and point expiration period all need to be within the campaign period.

Point collection period: Users can only earn points during this period.

The point collection period needs to be within the campaign period.

The start date of the point collection period must be earlier than the end date of the point redemption period

Point redemption period: Users can only exchange points for rewards during this period.

The point redemption period needs to be within the campaign period.



Point Card Kit [1]

https://docs.botbonnie.appier.com/docs/point-card-kit



The point redemption period needs to be within the campaign period.

The point redemption period is different from the reward redemption period under the Rewards section. Users need to redeem points for rewards during the point redemption period. However, if the reward needs to be further exchanged for or used (e.g. users need to visit a physical store to retrieve it), the period will be based on the reward redemption period.

Point expiration period: All points that are not redeemed yet will expire after this time period.

We recommend not changing this setting once you have started issuing points to avoid disputes.

If the point expiration setting is later than the end date of the campaign period, points will expire on the campaign end date.

Here's an example. Let's say the Amount of time after last earned point is set to one month. If the user earned points on Oct 10, the points will expire after one month on Nov 10. If the user earned some more points on Oct 25, the expiration date of all points will extend to Nov 25, including the points earned on Oct 10. However, all points will expire by the end of the campaign period.

Under the Appearance section, you can select an existing Theme. Next to Preview, you can use the drop-down menu on the right to preview what each page looks like.

You can also enable Customize appearance to make further customization on the visual appearance.

You can select a Theme color and upload your own images for the Background, Earned stamp, and Redeemed stamp of the point card. Refer to the image specifications shown on the console to prepare the images.

There are three ways users can earn points for point cards.

Use a QR code or URL

Advanced kit: Earn points from a triggered action

Advanced kit: Earn points as a prize

📘NoteNoteNote

Currently, only QR codes or URLs are shown in the Ways to earn points list.

Earning points using QR codes or URLs is only supported for Facebook Messenger and LINE Official Account.



Point Card Kit [2]

https://docs.botbonnie.appier.com/docs/point-card-kit



Earning points using QR codes or URLs is only supported for Facebook Messenger and LINE Official Account.

You can let users earn points by scanning a QR code or by visiting a URL. Up to 20 can be created.

To create one, click Add QR code or URL.

Issue points: This is the number of points users can receive each time they use this QR code or URL.

Bot reply: Under When points earned successfully and When failed to earn points, select a module to inform users whether they have successfully earned points from this QR code or URL. Note that sending notifications on LINE will incur extra charges.

Select channel: Select the Facebook Messenger or LINE Official Account to open when this QR code or URL is scanned.

Frequency cap: There are two options.

Each user can only earn points once with this URL: Limit each user to only earn points once with this URL or QR code.

Set frequency cap: Let users earn points up to once during the time duration you set. For example, if the frequency cap is set to 1 day and a user earned points at 18:00 today, this user will be able to use this URL to earn points again after 18:00 tomorrow.

Triggered actions: Set up any actions you want to trigger when the QR code or URL is used.

After the QR code / URL is created, click the share icon to find the QR code or URL.

In the following advanced kits, you can let users win points as a triggered action when they meet the requirements.

Member-get-member (MGM)

Serial number verification

Receipt registration

To set point card as a triggered action, follow the steps below for each kit:

MGM: Open the kit, find the Meet target or not conditions, find the "Met target" scenario, and set the Triggered actions to Point Card. Next, select a point card kit and set the number of points to issue to users.



Point Card Kit [3]

https://docs.botbonnie.appier.com/docs/point-card-kit



Serial number verification: Go to the kit settings page, find the "The user entered a valid and unused serial number" scenario, and set the Triggered actions of the scenario to Point Card. Next, select a point card kit and set the number of points to issue to users.

Receipt registration: Go to the kit flow, find the Receipt conditions conditions, find the scenario for qualified receipts, and set the Triggered actions to Point Card. Next, select a point card kit and set the number of points to issue to users.

In the following advanced kits, you can let users win points as a prize.

Lucky wheel

Daily check-in

Prize distribution

Scratch-off

To set this up, go to the settings of the kit (e.g. lucky wheel), set the prize format to Point card, and select a point card kit. Under Issue points, set the number of points to issue to users if they win this prize.

Under Rewards, set up the rewards that can be redeemed with points.

For each reward, configure the following settings. To add more rewards, click Add reward.

Name: Give a name to the reward. This name will be displayed to users when they get the reward.

Points required: This is the number of points required to get this reward.

Format: Select a reward format. The following formats are supported.



Point Card Kit [4]

https://docs.botbonnie.appier.com/docs/point-card-kit



Format: Select a reward format. The following formats are supported.

Prize typeDescriptionInform users of rewards earnedUsers are immediately presented with the reward. This reward type is ideal for digital rewards that don't require a physical exchange to occur. For example, this prize type can be used for multi-use coupon codes and digital assets such as images.Physical ExchangeThis reward type is suitable for brick-and-mortar locations and physical events, where winning users can physically redeem a reward by presenting the winning screen to an employee.This option is also suitable if you want to ship the physical reward to the users. To let users enter shipping information, select Show the form on the page and the following fields will be added to the reward page: Name, Phone, Email, Address.Unique serial number: TextThis option allows you to upload a CSV file containing a list of unique serial numbers. Users who win this reward will be assigned a unique serial number based on the order of the serial number in the file until the serial number runs out. For example, the first winning user will receive serial number A001, the second user will receive A002, etc.Serial number file requirements:

• Only CSV files are supported

• The file must be less than 10 MB

• The file must contain a single column with the list of unique serial numbers\ This reward type is suitable for coupons in e-commerce shops or rewards in mobile games.Unique serial number: BarcodeThis reward type is similar to the text-format unique serial number, except that the serial number will be converted and displayed as a barcode. Select the appropriate barcode type such as Code-39.This reward type is suitable for physical stores with POS machines.Unique serial number: URLThe CSV file should include the URL of each serial number. When users click the button, they will be directed to the URL to receive the reward.This reward type is suitable for giving out LINE points.



Point Card Kit [5]

https://docs.botbonnie.appier.com/docs/point-card-kit



Thumbnail: Upload a thumbnail image if needed. This is the thumbnail of the reward in the reward list.

Image: Upload the main reward image if needed. This is the reward image shown on the reward details page.

Details: Enter descriptions about the reward.

Shipping information form: This setting is only available for Physical exchange. If you want users to enter their shipping address, select Show the form on the page.

Quantity: Set the number of rewards available. This setting is unavailable for Unique serial number since the number of rewards available will be based on the number of serial numbers in the CSV file.

Triggered action: Set up any actions you want to trigger when the reward is redeemed. For example, you can add a tag to users who redeemed this reward.

Reward redemption period: Users can redeem the reward during this time period. If you set a reward redemption period beyond the campaign period, the reward can still be redeemed based on the reward redemption period even after the campaign period has ended.

Send a message through chat: Select this option if you want to send a message to the user through chat when they redeem this reward. You can edit the content of the message in the flows.

Under normal circumstances, no action is needed in this section. BotBonnie will automatically detect if your channels are successfully connected. If you run into issues here, contact Appier Support or your customer success manager for assistance.

Go back to the Flows page, and adjust the content of the modules in the sub-flow to suit your campaign.

Resetting a kit is useful if you ran the campaign to do internal testing, and now want to clear all test data before officially launching the campaign.

Resetting a kit will clear all data associated with the kit.

All points will be deleted

All rewards will be returned to the reward pool

🚧WarningWarningCautionThis action can't be reversed.



Point Card Kit [6]

https://docs.botbonnie.appier.com/docs/point-card-kit



All points will be deleted

All rewards will be returned to the reward pool

🚧WarningWarningCautionThis action can't be reversed.

In the kit settings, go to the Reset section, then click Reset. You'll be prompted to type "Reset" into the input box, then click Reset again to confirm your choice.

To view the performance reports, in the sub-flow of the point card kit, click Kit reports.

Type the email address where you'd like the reports to be sent to, then click Confirm. The reports will be sent to you shortly.

You will find three CSV files in the email.

Loyalty Point Card Distribution Report: This report shows the welcome points issued to users initially and the points issued for each point source.

Distributed points: The number of points issued each time a user earns points from this point source.

Total distributions: The number of times points are distributed from this point source.

Total distributed points: The total number of points distributed from this point source

Prize Inventory Status: The report shows the points required to redeem the reward, the number of rewards redeemed by users, and the number of remaining rewards.

Loyalty Point Card Prize Redemption Report: Each row represents each time a reward is redeemed by users. The report shows the user who redeemed the reward, the platform they used, the redeemed time, the time of physical exchange, and the profile picture of the user.

Updated 9 days ago



Condition Kit [0]

https://docs.botbonnie.appier.com/docs/condition-kit



The condition kit is designed to enhance user engagement and interaction through personalized experiences. Using the condition kit, you can specify different responses based on a user's tags or parameters, making interactions more dynamic and tailored. Condition kits can be used for:

Channel-specific welcome messages: Send different welcome messages depending on which channel the user is on.

Action-based rewards: For example, you can create a kit that gives a reward to users who have successfully linked their social account or completed a chatbot survey for the first time.

Personalized marketing campaigns and recommendations: Tailor messages or deliver specific product recommendations based on user behavior and interests. Offer exclusive discounts to frequent buyers or notify browsers about ongoing sales, ensuring targeted and relevant communication.

In the following guide, we'll create a condition kit that rewards new customers who have completed a survey with a prize code.

To add a condition kit to your flow, click Rule kits, then select Conditions.

Click the conditions module you just added, then click +Scenario.

📘Note: Multiple scenariosThe order in which the scenarios are created is also the priority they're evaluated in. If the conditions of multiple scenarios are met at the same time, the scenario that was created first will be used.

Under the new scenario, go to Rules, then click on the condition to configure its settings. For example, you can add a condition that specifies users with the "Survey completed" tag should be sent the module containing the prize code.

To add additional conditions, click Add condition. You can specify up to 5 conditions per scenario. Note that the scenario will only be used if all the conditions are met.

The default scenario specifies which module should be sent if the user doesn't satisfy the conditions for any other scenario.



Condition Kit [1]

https://docs.botbonnie.appier.com/docs/condition-kit



The default scenario specifies which module should be sent if the user doesn't satisfy the conditions for any other scenario.

In this example, the default scenario consists of all users who haven't completed the survey, i.e. users missing the "Survey completed" tag will receive a message prompting them to take the survey.

Updated 9 days ago



Sequence Kit

https://docs.botbonnie.appier.com/docs/sequence-kit



Sequence kits use customizable delays to send sequences of messages to users, allowing you to create a more personalized and interactive chatbot. For example, while a broadcast must be scheduled at a specific time, messages in a sequence kit can be sent at different times for each user depending on the time of that user's last interaction.

In your flow, click Rule kits and choose Sequence to add a sequence kit.

Open the sequence kit. You have the option to set up blackout window settings to prevent messages from being sent between certain times. Click Set blackout window to go to your bot settings page to configure blackout window settings.

If you want to send a message as soon as the user reaches this point in the flow, go to the Broadcast now setting and select a module from the dropdown.

Next, click + Sequence to add a sequence message.

👍You can add up to four sequence messages in a single kit module.

Configure the following sequence message settings:

Send at: Set the delay for the sequence message. The delay starts from when the user interacts with the message immediately prior to the sequence kit. For example, if the previous module is a text message with a button linking to the sequence kit, the delay will be calculated starting from the time the user clicks the button.

Sequence message type: Choose a topic for the message.

Broadcast: Select the module you'd like to send from the dropdown.

Updated 9 days ago



Knowledge Bot Setup [0]

https://docs.botbonnie.appier.com/docs/knowledge-bot-setup



📘Beta featureThis is a beta feature. While this feature is currently available for use, you may encounter occasional bugs or stability issues. Contact your customer success manager for more details.

BotBonnie's Knowledge Bot uses generative AI to automatically respond to users' questions. You can upload materials to train the chatbot with information about your business, such as business hours, return policies, troubleshooting instructions, and product specifications. In the case that the chatbot is unable to answer the question, the Knowledge Bot can transfer the user to human agents for assistance.

Using the Knowledge Bot kit, you can:

Leverage generative AI to answer user's questions

Add documents and URLs to train the chatbot

Transfer users to human agents when needed

In the Chat > Flows page, select Knowledge Bot, then click Start editing to begin editing the kit.

It is highly recommended to add content and train the chatbot with information specific to your business. The content should include information that will help the chatbot answer questions frequently asked by your users. Here are some examples:

Business hours, return policy, shipping options, pricing

Troubleshooting instructions, user manuals, product specifications

Membership benefits, course curriculum, tour itinerary

Knowledge Bot supports the following types of content. Make sure the documents meet the requirements below.

URLs

Documents

Supported formats are PDF, TEXT, XLSX, and CSV. Text files must be UTF-8 encoded.

Encrypted or password-protected documents are not supported.

Each file must be less than 5 MB.

📘Note

Knowledge Bot will only train based on the text content. Images won’t be processed.

Knowledge Bot doesn't automatically re-train. If you make changes to the webpage content after the URLs are trained, you will need to click Start training again to re-train the bot with the updated content.

The maximum number of documents and URLs that can be uploaded per kit may be different based on the Knowledge Bot plan you are subscribed to.



Knowledge Bot Setup [1]

https://docs.botbonnie.appier.com/docs/knowledge-bot-setup



To add content, click Add content and select URL or Document.

Document: Select the files you want to upload.

URL: Under Source page URL, you can enter the URL of a source page and click Fetch to retrieve all URLs found on this source page. You can also add URLs one by one under Specific URLs. Click Add when you are done.

If you want to bulk delete or download the contents added, select the items in the list and click Bulk actions. Only documents can be downloaded.

After adding the content, click Start training. The bot is usually trained within a day. You'll receive an email notification when completed.

Please note the following training statuses for the chatbot.

When you first add the kit, the status of the chatbot will be Not trained.

After you've added content and clicked Start training, the status will change to Training.

Finally, when the bot has finished training the content you've added, the status will be changed to Trained.

If you stop the bot's training before it has completed, e.g. to upload more documents, you'll need to restart the bot training by clicking Start training again, then wait for the training to finish. This will restart the training process.

Go to Reply settings to set up automatic bot replies to handle different scenarios. BotBonnie provides default auto replies to handle common scenarios such as letting users contact live agents. You can also create your own custom replies.

You can create up to 20 custom replies that can be sent to the user when the user's input includes an exact match of at least one of the keywords you entered.

To create a custom reply, click Add auto reply. Enter the reply name and the keywords to trigger the reply. Next, set the reply module and switch on the toggle.

The keyword matching is not case-sensitive.

The user's input needs to contain at least one of the keywords. If there are multiple words in a keyword, the user input needs to include all words in that keyword in the same order.

Here are some examples:

Keywords: Order , PO number



Knowledge Bot Setup [2]

https://docs.botbonnie.appier.com/docs/knowledge-bot-setup



Here are some examples:

Keywords: Order , PO number

User input: I would like to check the status of my order. >> Matched

User input: PO is 12345. Please check status >> Not matched

The live agent reply is designed to transition users to live agents when needed. This reply is sent to the user when a system-related issue has occurred or when the user's input exactly matches one of the keywords.

Adjust or add keywords if needed. Next, click the reply module on the right to adjust the default reply message.

The keyword matching is not case-sensitive.

The user's input needs to equal one of the keywords and cannot include other content.

Here are some examples:

Keyword: live agent

User input: live Agent >> Matched

User input: Agent live >> Not matched

User input: I need live agent >> Not matched

This reply is triggered when the chatbot is unable to answer the user’s question. Click the reply module on the right to adjust the default reply message.

In addition to the chatbot, the Knowledge Bot includes the following reply modules to handle special scenarios. You can adjust the module messages based on your specific needs.

Start AI chatbot: You can let the users know that they are speaking with an chatbot. You can also let users know what keywords to type if they want to speak to a human agent.

Unable-to-answer reply: Inform the users when the bot is unable to answer the question.

Live agent reply: When a trigger is met, ask the users if they need assistance from a human agent.

Competitor reply: When the user enters a competitor keyword, let users know that the chatbot cannot answer questions about competitors.

Reach limit response: When the message limit has been reached, let users know that the chatbot is out of response capacity.

Leave message: Ask users to leave a message for the human agent.

Test your Knowledge Bot to see what types of responses it gives. If you aren't satisfied with the responses, you can upload more training materials or create custom answers.



Knowledge Bot Setup [3]

https://docs.botbonnie.appier.com/docs/knowledge-bot-setup



Custom answers are responses you can provide to the bot that are tailored to specific questions for enhanced accuracy and precision. The custom answer will be used to respond to variations of the original question, so even if users asks it in different ways, they'll get the same helpful response.

👍Test messages don't count towards your message quota.

There are four categories of responses and different operations (uploading training materials, creating custom answers) are available depending on the response type:

Response typeDescriptionAvailable operationsAI responseKnowledge Bot generated this response.Create a custom answer for this question.Custom answerKnowledge Bot responded with a custom answer.Edit the custom answer for this question.Fallback responseKnowledge Bot is unable to answer to this question and responded with the Unable-to-answer reply.• Add content for additional training.

• Create a custom answer for this question.Module auto replyKnowledge Bot sent a conversation module as a response.No operations available.

Start testing your Knowledge Bot by entering the AI chatbot module and clicking Test Knowledge Bot, then enter your question.

After asking a question, you'll see the Knowledge Bot's response. Depending on the response type, you'll be able to add content for additional training or create a custom answer for this question.

To see the custom answers you've created, go to the Custom answer tab.

Knowledge Bot supports English, Chinese, Japanese, and Korean.

No, the content added for a Knowledge Bot kit is independent and not used by other Knowledge Bot kits.

Each time the Knowledge Bot generates an answer with AI to reply to a user's question, it counts as one message toward the limit. Default replies, such as the live agent reply or competitor reply, do not count toward the limit.



Knowledge Bot Setup [4]

https://docs.botbonnie.appier.com/docs/knowledge-bot-setup



When the message quota runs out, the Knowledge Bot will be disabled until the next billing cycle. During this time, the users will be directed to a live agent. You will receive email notifications when you are approaching the message limit.

To see your current message usage and limit for Knowledge Bot, go to Chat > Settings > Billing details.

Under the Knowledge Bot plan, you can find the following information.

Messages used: The number of messages already generated by AI during this billing cycle.

Message limit: The total number of messages that can be generated by AI in a billing cycle, including carry-over and add-on limit.

Carry-over: The unused monthly messages remaining from the previous month.

Add-on limit: The number of messages that can be used at a charge when the monthly limit and carry-over messages are used up.

Kit added: The number of Knowledge Bot kits you have added to the flow.

Kit limit: The total number of Knowledge Bot kits you can add to the flow.

Updated 9 days ago



User List [0]

https://docs.botbonnie.appier.com/docs/user-list



BotBonnie's audience list feature consolidates users from all your connected social platforms, such as Instagram and LINE Official Accounts, into one console. It offers advanced filtering options, including user tags, interaction time, and account linking status. Marketers and customer service agents can easily:

View user profiles

Add and remove tags

Manage subscriptions

Assign users to a menu group

The feature also supports bulk actions like setting LINE menu groups, exporting data, and importing users, making it a powerful tool for efficient audience management and personalized customer interactions.

If the chatbot is connected to supported channels, such as an Instagram account or LINE Official Account, all users from every platform can be seen simultaneously on the same console. In the audience list, you can see the following details for all users:

Profile picture

Name

First interaction time

Last interaction time

Platform

Channel

Subscription status

Bot status

To view the user list, go to Audience > User list.

To open the detailed user view, click the eye icon on the right side of the user list. In this view, you can see a user's specific details and modify their tags.

You can also filter out lists of users with specific information you want to see through filtering. To use multiple filters simultaneously, click + Add condition.

The following filtering conditions can be used:

Tag

Tag confidence index

Tag count

Tagged date

First interaction

Last interaction

Account linking status

Menu Group

One-time notification list

Recurring notifications

Platform

Not been sent broadcast recently

Birthday

AiDeal

AIQUA conditions

Parameters

If a user does not need bot services (e.g., when a response from a real customer service representative is required), just turn the status of the user’s bot to “off.” There is no need to cancel the link between the fan page and bot.

You can unsubscribe users directly from the user list by clicking the Subscribed button corresponding to the user.



User List [1]

https://docs.botbonnie.appier.com/docs/user-list



You can unsubscribe users directly from the user list by clicking the Subscribed button corresponding to the user.

In addition to modifying an individual user profile from the detailed user view, you can bulk update users from the user list by:

Checking the box next to each user you'd like to update.

Clicking the Bulk actions dropdown and selecting the operation you'd like to complete.

The following bulk operations are available:

Add Tag

Remove tag

Unsubscribe

Assign to Messenger

Assign to LINE menu

Export user data

From the user list, you can seamlessly upload user data to BotBonnie. To import users, complete the following steps:

Select a channel to import: Select the channel (e.g., Facebook, LINE) for which you want to import user IDs.

Upload a User ID File: Upload a CSV file containing user IDs, ensuring it doesn't exceed the size limit of 10 MB. Only user IDs of friends following your LINE Official Account will be processed.

Tag these users: Assign relevant tags to these users during the import process to enhance user segmentation and targeting.

Consider the following scenario:

A user followed the brand account on May 1.

The brand account was connected to BotBonnie on June 1, but the user didn't interact with the brand account after June 1.

Since BotBonnie didn't detect any activity, this user isn't in BotBonnie's database.

Because BotBonnie's database isn't aware of this user, you'll need to import the user manually.

You can use the LINE Messaging API to retrieve the user IDs required for the import file.

If your LINE Official Account is certified, you have the option to import users to BotBonnie automatically by selecting System automatically obtains user ID.

Updated 9 days ago



User Properties

https://docs.botbonnie.appier.com/docs/user-properties



User properties help you organize and track information about your users through tags and parameters. Use tags to group users based on shared characteristics, and parameters to store specific user attributes.

👍You can also view each user's tags and parameters in the User list .

From the user properties page, you can view your existing tags and manually create tags and tag folders.

To manage your tags, go to Audience > User properties and navigate to the Tags tab.

Use tag folders to organize your tags. Click + Create folder to add a new folder.

Tags help you segment users based on their characteristics, behaviors, or preferences. Each tag includes a name, type, and the number of users associated with it.

Add: Click + Create tag to add a new tag.

Move: Click the folder icon or use drag-and-drop to move tags into folders.

Edit or delete: Click the pencil icon to rename it, or click the trash bin icon to remove it.

📘NoteNew tags appear under Uncategorized tags until you move them into a folder.

Use parameters to store and reference custom user data, including demographic information.

To manage parameters, go to Audience > User properties and navigate to the Parameters tab.

Create and manage custom parameters to store user information:

Add: Click + New parameter, then enter a name and select the parameter's data type (text or number).

Edit: Click the pencil icon to modify the name or type of the parameter.

Delete: Click the trash bin icon on the right of parameter to delete.

User demographics are default attributes that can be used to store basic user information such as birthday, gender, phone number, location, and email address.

Updated 9 days ago



Segments

https://docs.botbonnie.appier.com/docs/segments



BotBonnie segments allow you to segment users by specifying conditions, such as users who have a certain tag or interacted with your bot in a certain time frame. After creating a segment, you can:

Download a CSV file containing details about users in the segment, e.g. username or first interaction time.

Send a LINE narrowcast to users in the segment.

👍LINE narrowcastUse LINE narrowcasts to reach your audience with pinpoint accuracy, ensuring messages reach the right people at the right time to achieve higher engagement.In addition, broadcasts support detailed reporting, including metrics like the percentage of a video watched by users, providing valuable insights for refining future campaigns.

Go to Audience > Segments, then click + Create segment.

Enter a name and add conditions specifying which users should be included in the segment. After adding conditions, the segment size will be displayed on the right side of the page.

Wait for the segment to finish processing. When processing is complete, the status will change from In progress to Ready. Once a segment's status is Ready, you'll be able to download the CSV segment file or send LINE narrowcasts to users in this segment.

After creating the segment, you can:

Re-sync the segment: Recalculate the segment to ensure it's up-to-date.

Download the CSV segment file: Send a CSV file via email containing details about users in the segment.

Delete the segment.

Updated 9 days ago



Export User Data for LINE Ads [0]

https://docs.botbonnie.appier.com/docs/export-user-data-for-line-ads



BotBonnie allows you to export a list of users in a CSV file and import the users to your LINE Ads account for retargeting. You can either export all LINE users, or export only the LINE users who meet certain filter conditions (e.g. users who have the tag dessert). This feature helps you target the right users with relevant content on LINE Ads.

From the left menu, go to Audience > User list.

Click Filter, click Add condition, set Platform to LINE, and select your LINE Official Account.

📘NoteThe LINE Ads account needs to be registered using a LINE account that has administrator access to the LINE Official Account selected here.

If needed, you can click Add condition to add more segmentation conditions. For example, you can choose to include only LINE users with the tag dessert.

On the right, click Bulk action and select Export user data.

Type your email address and click Confirm.

Go to your inbox and download the file.

Open the CSV file, delete the header row, and save it as a new CSV file.

If you open the CSV file in Excel and the numbers (e.g. User ID, Account ID) are displayed in scientific notation, you can change the data format to Number.

📘Note

LINE only accepts up to 1,500,000 LINE user IDs in a CSV file.

To use the uploaded user list in LINE Ads, the list needs to include more than 100 valid, reachable LINE user IDs.

Log in to LINE Official Account Manager and click the account name of your LINE channel.

In the left menu, go to Data controls > Audiences, and click Create New.

Set Audience type to User ID upload, enter an audience name, and click Next. You can name the audience based on the purpose of your LINE Ads campaign (e.g. User ID upload: Christmas sale).

Click Browse +, select the CSV file, and click Update.

The newly created audience will appear in the audience list.

It may take a while for LINE to finish processing it.

Make sure the Share status is set to Public.



Export User Data for LINE Ads [1]

https://docs.botbonnie.appier.com/docs/export-user-data-for-line-ads



It may take a while for LINE to finish processing it.

Make sure the Share status is set to Public.

You can now go to your LINE Ads account, click the menu icon at the top-left corner of the page, and click Audience under Shared library. You will see the audience you uploaded in the audience list.

Updated 9 days ago



Getting Started with Journey Maps [0]

https://docs.botbonnie.appier.com/docs/getting-started-with-journey-maps



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

https://docs.botbonnie.appier.com/docs/getting-started-with-journey-maps



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
