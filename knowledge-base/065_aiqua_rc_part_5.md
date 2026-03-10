---
source: notebooklm_export
file_id: "065"
filename: "065_aiqua_rc_part_5.txt.txt"
doc_type: "reference_card"
product: "AIQUA"
content_type: "txt"
language: "en"
guide_summary: "This comprehensive documentation outlines the necessary steps for **integrating the Appier SDK** into iOS applications, focusing specifically on enabling and handling **push notifications**, a crucial component of mobile engagement. The instructions detail the process of **requesting user authorization** for notifications and providing the subsequent **push token** to the Appier server, accommodating both Apple Push Notification service (APNs) and Firebase Cloud Messaging (FCM). Furthermore, the"
guide_keywords: "Push Notifications, SDK Integration, Rich Push, User Data, Appier/AIQUA"
---

# 065 aiqua rc part 5

Registering for Push Notifications [1]

https://docs.aiqua.appier.com/docs/registering-push-notifications-for-ios



let settings = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories: nil)

UIApplication.shared.registerUserNotificationSettings(settings)

}

// Registering Push Notification

if (@available(iOS 10.0, *)) {

UNAuthorizationOptions options = (UNAuthorizationOptions) (UNAuthorizationOptionAlert | UNAuthorizationOptionBadge | UNAuthorizationOptionSound | UNAuthorizationOptionCarPlay);

UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];

center.delegate = self;

[center requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError *error){

NSLog(@"GRANTED: %i, Error: %@", granted, error);

}];

} else {

// Fallback on earlier versions - iOS 8 & 9

UIUserNotificationType types = UIUserNotificationTypeAlert | UIUserNotificationTypeSound |

UIUserNotificationTypeBadge;

UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:types categories:nil];

[[UIApplication sharedApplication] registerUserNotificationSettings:settings];

}

👍TipThe iOS SDK offers an optional feature, "Provisional Push Notification," that allows you to silently deliver a trial push notification to iOS 12 users before asking for push permission. More details

If the user grants permission for push notifications, a push token is generated from the APNs or FCM servers. Follow the steps for APNs or FCM below to pass the token to the Appier server.

If your app is using APNs, copy the following methods and paste inside your AppDelegate class so that the application will pass the push token to the Appier server.

// add these delegate methods to your AppDelegate class

func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {

let QG = QGSdk.getSharedInstance()

print("My token is: \(deviceToken.description)")

QG.setToken(deviceToken as Data)

}

func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {



Registering for Push Notifications [2]

https://docs.aiqua.appier.com/docs/registering-push-notifications-for-ios



}

func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {

print("Failed to get token, error: \(error.localizedDescription)")

}

// add these delegate methods to your AppDelegate class

- (void)application:(UIApplication*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData*)deviceToken

{

NSLog(@"My token is: %@", deviceToken);

[[QGSdk getSharedInstance] setToken:deviceToken];

}

- (void)application:(UIApplication*)application didFailToRegisterForRemoteNotificationsWithError:(NSError*)error

{

NSLog(@"Failed to get token, error: %@", error.localizedDescription);

}

📘Note:If you requested for a push token using registerForRemoteNotification before the Appier SDK is initialized, save the token and send it when you initialize the SDK.

If your app is using FCM, follow the steps below.

Add the Firebase/Messaging pod to your Podfile and install the pod. For more details on adding Firebase SDKs to your app, refer to the Firebase documentation.

target 'PROJECT_TARGET' do

...



// Add the pod for Firebase Cloud Messaging

pod 'Firebase/Messaging'

end

Initialize Firebase in your app by importing the Firebase module in your UIApplicationDelegate.

import Firebase

@import Firebase;

Configure a FirebaseApp shared instance, typically in your app's application:didFinishLaunchingWithOptions: method.

// Use Firebase library to configure APIs

FirebaseApp.configure()

// Use Firebase library to configure APIs

[FIRApp configure];

Set the messaging delegate. Add in your AppDelegate interface.

Messaging.messaging().delegate = self

[FIRMessaging messaging].delegate = self;

Pass the token to the Appier server using setFCMToken().

// Use FIRMessagingDelegate

// Firebase FCM subscribe to any topic

func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String) {

// TODO: If necessary send token to application server.

// Note: This callback is fired at each app startup and whenever a new token is generated.



Registering for Push Notifications [3]

https://docs.aiqua.appier.com/docs/registering-push-notifications-for-ios



// Note: This callback is fired at each app startup and whenever a new token is generated.

print("Firebase registration token: \(fcmToken)")

// Important for Appier

QGSdk.getSharedInstance().setFCMToken(fcmToken)

}

// Use FIRMessagingDelegate

// Firebase FCM subscribe to any topic

- (void)messaging:(FIRMessaging *)messaging didReceiveRegistrationToken:(NSString *)fcmToken {

// TODO: If necessary send token to application server.

// Note: This callback is fired at each app startup and whenever a new token is generated.

NSLog(@"My FCM token is: %@", fcmToken);

// Important for Appier

[[QGSdk getSharedInstance] setFCMToken:fcmToken];

}

At this checkpoint, make sure your app builds correctly and run the app on a physical iOS device.

When the app is launched, you should be prompted to subscribe to notifications.

Updated over 1 year ago Table of Contents

1. Add the UserNotifications framework

2. Include headers

3. Request permission

4. Pass the push token to Appier

Option 1: For iOS apps using APNs

Option 2: For iOS apps using FCM

Checkpoint



Handling Push Notifications [0]

https://docs.aiqua.appier.com/docs/handling-push-notifications-for-ios



To handle the push notifications (both silent and foreground) and push notification events in your app, add the methods described below into your app delegate (AppDelegate.swift).

In addition, you can use isAppierPush: to handle push notifications sent by Appier in any of the app delegate methods if your app will also receive notifications from other services.

Add the methods provided below in your app delegate to handle:

Events for push notifications

Silent push notifications

Foreground push notifications

Add userNotificationCenter:didReceive:withCompletionHandler: into your app delegate to handle events for push notifications:

userNotificationCenter:didReceive:withCompletionHandler: is called whenever the user responds to the notification by opening the application, dismissing the notification, or choosing the UNNotificationAction.

The delegate must be set before the application returns from applicationDidFinishLaunching

This method is required for carousels and sliders to work

// Handle click and deep link events for push notification

@available(iOS 10.0, *)

func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler:@escaping() -> Void) {

QGSdk.getSharedInstance().userNotificationCenter(center, didReceive: response)

completionHandler()

}

// handling the click and deeplink events from push notification

- (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void(^)(void))completionHandler API_AVAILABLE(ios(10.0)){

[[QGSdk getSharedInstance] userNotificationCenter:center didReceiveNotificationResponse:response];

completionHandler();

}

Add application:didReceiveRemoteNotification:fetchCompletionHandler: into your app delegate to handle silent push notifications.

// Handle silent push notifications

// pass completion handler UIBackgroundFetchResult accordingly



Handling Push Notifications [1]

https://docs.aiqua.appier.com/docs/handling-push-notifications-for-ios



// Handle silent push notifications

// pass completion handler UIBackgroundFetchResult accordingly

func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {

let QG = QGSdk.getSharedInstance()

QG.application(application, didReceiveRemoteNotification: userInfo)

completionHandler(UIBackgroundFetchResult.noData)

}

// used for silent push handling

// pass completion handler UIBackgroundFetchResult accordingly

- (void)application:(UIApplication *)application didReceiveRemoteNotification:(nonnull NSDictionary *)userInfo fetchCompletionHandler:(nonnull void(^)(UIBackgroundFetchResult))completionHandler

{

[[QGSdk getSharedInstance] application:application didReceiveRemoteNotification:userInfo];

completionHandler(UIBackgroundFetchResultNoData);

}

Add userNotificationCenter:willPresentLwithCompletionHandler: into your app delegate to handle foreground push notifications.

userNotificationCenter:willPresentLwithCompletionHandler: is only called if the application is in the foreground. The notification won't be shown if this method is not implemented or the handler is not called in a timely manner. The application can choose to have the notification as a sound, badge, alert, and in the notification list. This must be based on whether the notification's information is otherwise visible to the user.

@available(iOS 10.0, *)

func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {

QGSdk.getSharedInstance().userNotificationCenter(center, willPresent: notification)

completionHandler([.alert, .badge, .sound]);

}

- (void)userNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void(^)(UNNotificationPresentationOptions options))completionHandler API_AVAILABLE(ios(10.0)){



Handling Push Notifications [2]

https://docs.aiqua.appier.com/docs/handling-push-notifications-for-ios



[[QGSdk getSharedInstance] userNotificationCenter:center willPresentNotification:notification];

UNNotificationPresentationOptions option = UNNotificationPresentationOptionBadge | UNNotificationPresentationOptionSound | UNNotificationPresentationOptionAlert;

completionHandler(option);

}

If your app will also receive push notifications from services other than Appier, use isAppierPush: to determine whether a push notification was sent by Appier.

The following code sample demonstrates one way to implement a notification handler that treats notifications differently depending on whether they were sent by Appier or not by using isAppierPush::

@available(iOS 10.0, *)

func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler:@escaping() -> Void) {

let isAppierPush = QGSdk.getSharedInstance().isAppierPush(response.notification.request.content.userInfo)

if (isAppierPush) {

// Handle push notifications from Appier

QGSdk.getSharedInstance().userNotificationCenter(center, didReceive: response)

completionHandler()

} else {

// Handle other push notifications

}

}

- (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void(^)(void))completionHandler API_AVAILABLE(ios(10.0)){

BOOL isAppierPush = [[QGSdk getSharedInstance] isAppierPush:response.notification.request.content.userInfo];

if (isAppierPush) {

// Handle push notifications from Appier

[[QGSdk getSharedInstance] userNotificationCenter:center didReceiveNotificationResponse:response];

completionHandler();

} else {

// Handle other push notifications

}

}

If you're using AppierExtensionFramework, override the following methods as well:

Swift: didReceive(_:withContentHandler:) and serviceExtensionTimeWillExpire()

Objective-C: didReceiveNotificationRequest:withContentHandler: and serviceExtensionTimeWillExpire



Handling Push Notifications [3]

https://docs.aiqua.appier.com/docs/handling-push-notifications-for-ios



Objective-C: didReceiveNotificationRequest:withContentHandler: and serviceExtensionTimeWillExpire

The following code sample demonstrates one way to override the appropriate methods in your notification extension:

import AppierExtension

class NotificationService: UNNotificationService {



var contentHandler: (UNNotificationContent) -> Void

var bestAttemptContent: UNMutableNotificationContent



override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {

self.bestAttemptContent = request.content.mutableCopy() as! UNMutableNotificationContent

self.contentHandler = contentHandler



let isAppierPush = QGNotificationSdk.sharedInstance(withAppGroup:APPIER_APP_GROUP_ID).isAppierPush(request.content.userInfo)

if isAppierPush {

QGNotificationSdk.sharedInstance(withAppGroup:APPIER_APP_GROUP_ID).didReceive(request) { content in

contentHandler(content);

}

}

}



override func serviceExtensionTimeWillExpire() {

let isAppierPush = QGNotificationSdk.sharedInstance(withAppGroup:APPIER_APP_GROUP_ID).isAppierPush(self.bestAttemptContent.userInfo)

if isAppierPush {

self.contentHandler(self.bestAttemptContent)

}

}

}

@interface NotificationService ()

@property (nonatomic, strong) void (^contentHandler)(UNNotificationContent *contentToDeliver);

@property (nonatomic, strong) UNMutableNotificationContent *bestAttemptContent;

@end

- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler

{

self.contentHandler = contentHandler;

self.bestAttemptContent = [request.content mutableCopy];

BOOL isAppierPush = [[QGNotificationSdk sharedInstanceWithAppGroup:APPIER_APP_GROUP_ID] isAppierPush:request.content.userInfo];

if (isAppierPush) {

[[QGNotificationSdk sharedInstanceWithAppGroup:APPIER_APP_GROUP_ID] didReceiveNotificationRequest:request withContentHandler:^(UNNotificationContent *content){

contentHandler(content);

}];

}

}



Handling Push Notifications [4]

https://docs.aiqua.appier.com/docs/handling-push-notifications-for-ios



contentHandler(content);

}];

}

}

- (void)serviceExtensionTimeWillExpire

{

BOOL isAppierPush = [[QGNotificationSdk sharedInstanceWithAppGroup:APPIER_APP_GROUP_ID] isAppierPush:self.bestAttemptContent.userInfo];

if (isAppierPush) {

self.contentHandler(self.bestAttemptContent);

}

}

Updated about 10 hours ago Table of Contents

Overview

App delegate methods for handling push notifications

1. Handling events for push notifications

2. Handling silent push notifications

3. Handling foreground push notifications

Handling push notifications from Appier



Adding Required Extensions [0]

https://docs.aiqua.appier.com/docs/rich-push-notifications



This guide will explain how to add the Notification Service Extension and Notification Content Extension to your app. These extensions are required for:

Tracking impressions for push notifications: Tracking impression events for push notifications is only possible after the extensions are added.

Sending rich push notifications: A rich push notification is a push notification that includes an image, video, GIF, audio, carousel, or slider. With the release of iOS 10, AppierFramework and AppierExtensionFramework were introduced to support rich push notifications and notification UI customization.

Use Appier iOS SDK 7.10.0 or later. Follow the migration steps to upgrade from version 7.0.0-7.9.0.

If you're using a new App Group ID, ensure that you are using Appier iOS SDK 7.7.0 or later, otherwise iOS users will be duplicated. 

Starting from Appier iOS SDK 8.0.0, AppierFramework is not supported in the Notification Service Extension and Notification Content Extension.

Starting from Appier iOS SDK 7.10.0, AppierExtensionFramework is used in the Notification Service Extension and Notification Content Extension. AppierFramework is only used in the main app target.

The App Group ID will be used in your main app target as well as the two extension targets you'll create. The App Group ID must be the same ID used when you enabled the App Group.

🚧Caution: Using a New App Group IDEnsure that you're using the proper SDK version if you need to use a new App Group ID to avoid unwanted side effects.

Add a notification service extension target. Under to File > New > Target, select Notification Service Extension, then click Next.

For Product Name, enter "AppierNotificationServiceExtension" and click Finish.

After clicking Finish, you'll be prompted to activate the "AppierNotificationServiceExtension" scheme. Select Cancel. 

Add a notification content extension target. In Xcode, navigate to File > New > Target, select Notification Content Extension, and click Next.



Adding Required Extensions [1]

https://docs.aiqua.appier.com/docs/rich-push-notifications



For Product Name, enter "AppierNotificationContentExtension" and click Finish.

After clicking Finish, you'll be prompted to activate the "AppierNotificationContentExtension" scheme. Select Cancel. 

Choose an installation method depending on your project settings:

Option 1: Swift Package Manager

Option 2: Installing with CocoaPods 

Option 3: Manual Installation (Not Recommended)

No additional steps required; continue to the next step.

🚧use_frameworks!Your Podfile will look different depending on whether it contains use_frameworks! or not. Make sure you are referencing the correct Podfile sample.

If your Podfile has use_frameworks!, add the following lines to your Podfile:

platform :ios, '10.0'

use_frameworks!

target 'PROJECT_TARGET' do

pod 'AppierFramework', '8.2.2'

# other pods

end

# Add the following lines for service and content extensions

target 'AppierNotificationServiceExtension' do

pod 'AppierExtensionFramework', '8.2.2'

end

target 'AppierNotificationContentExtension' do

pod 'AppierExtensionFramework', '8.2.2'

end

Otherwise, add the following lines to your Podfile instead:

platform :ios, '10.0'

target 'PROJECT_TARGET' do

pod 'AppierFramework', '8.2.2'

pod 'AppierExtensionFramework', '8.2.2'

# other pods

end

# Add the following lines for service and content extensions

target 'AppierNotificationServiceExtension' do

pod 'AppierExtensionFramework', '8.2.2'

end

target 'AppierNotificationContentExtension' do

pod 'AppierExtensionFramework', '8.2.2'

end

Ensure that the target names in the Podfile match the product names you used when creating the extensions (AppierNotificationServiceExtension and AppierNotificationContentExtension).

📘Upgrading the iOS SDKWhen upgrading the iOS SDK, make sure to also update the versions of AppierExtensionFramework and AppierFramework in your Podfile to match the iOS SDK version.

After adding the extensions to the Podfile, run the following commands in the project directory to install the extensions:

$ pod repo update

$ pod install



Adding Required Extensions [2]

https://docs.aiqua.appier.com/docs/rich-push-notifications



$ pod repo update

$ pod install

❗️WarningDon't follow the manual installation steps if your project uses CocoaPods or Swift Package Manager (SPM) for package management.

Download the Appier iOS SDK.

Add the AppierExtension.xcframework folder you downloaded to the main app target. Under the Build Phases tab, expand Link Binary With Libraries, and click +. Go to Add Other > Add Files and select the AppierExtension.xcframework folder.

Add the AppierExtension.xcframework folder to the main app target.

Add the AppierExtension.xcframework folder to the AppierNotificationServiceExtension and AppierNotificationContentExtension targets. 

Add the AppierExtension.xcframework folder to the AppierNotificationServiceExtension and AppierNotificationContentExtension targets.

In the main app target, go to General > Frameworks and Libraries, select AppierExtension.xcframework, and set the Embed column to Embed & Sign.

In the AppierNotificationServiceExtension and AppierNotificationContentExtension targets, go to General > Frameworks and Libraries, then set the Embed columns of AppierNotificationServiceExtension.xcframework and AppierNotificationContentExtension.xcframework to Do Not Embed.

In the AppierNotificationServiceExtension folder, open the NotificationService.* files and replace the contents of the entire file with the following:

For Swift: NotificationService.swift

import AppierExtension

class NotificationService: QGNotificationService {

override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {

super.didReceive(request, withContentHandler: contentHandler)

}



override func serviceExtensionTimeWillExpire() {

super.serviceExtensionTimeWillExpire()

}

}

For Objective-C: NotificationService.h and NotificationService.m

#import 

#import 



@interface NotificationService : QGNotificationService

@end

#import "NotificationService.h"



@implementation NotificationService



Adding Required Extensions [3]

https://docs.aiqua.appier.com/docs/rich-push-notifications



@end

#import "NotificationService.h"



@implementation NotificationService



- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {

[super didReceiveNotificationRequest:request withContentHandler:contentHandler];

}

- (void)serviceExtensionTimeWillExpire {

[super serviceExtensionTimeWillExpire];

}

@end

Go to the project navigator and select the AppierNotificationServiceExtension target.

Navigate to Signing & Capabilities > App Groups, and then add the app group using your App Group ID.

In the project navigator, select the AppierNotificationServiceExtension target. Under the General tab, change the deployment target of your service extension to iOS 10.0.

Find the Info.plist file in the AppierNotificationServiceExtension folder. Add the following row under Information Property List:

KeyTypeValueAppierAppGroupStringYour App Group ID

In the AppierNotificationContentExtension folder, open the following files and replace the contents of the entire file with the following:

For Swift: NotificationViewController.swift

import UIKit

import AppierExtension

class NotificationViewController: QGNotificationContentViewController {

override func viewDidLoad() {

super.viewDidLoad()

// Do any required interface initialization here.

}

}

For Objective-C: NotificationViewController.h and NotificationViewController.m 

#import 

#import 



@interface NotificationViewController : QGNotificationContentViewController

@end

#import "NotificationViewController.h"



@implementation NotificationViewController



- (void)viewDidLoad {

[super viewDidLoad];

}

@end

Go to the project navigator and select the AppierNotificationContentExtension target.

Navigate to Signing & Capabilities > App Groups, and then add the app group using your App Group ID.



Adding Required Extensions [4]

https://docs.aiqua.appier.com/docs/rich-push-notifications



Navigate to Signing & Capabilities > App Groups, and then add the app group using your App Group ID.

In the project navigator, select the AppierNotificationContentExtension target. Under the General tab, change the deployment target of your content extension to iOS 10.0. 

Find the Info.plist file in the AppierNotificationContentExtension folder. Under NSExtension > NSExtensionAttributes, update UNNotificationExtensionCategory and add UNNotificationExtensionDefaultContentHidden and UNNotificationExtensionUserInteractionEnabled with the following values:

KeyTypeValueUNNotificationExtensionDefaultContentHiddenBooleanYES or 1UNNotificationExtensionUserInteractionEnabledBooleanYES or 1UNNotificationExtensionCategoryStringQGCAROUSEL

Add the following row under Information Property List:

KeyTypeValueAppierAppGroupStringYour App Group ID

Info.plist for AppierNotificationContentExtension should look like this:

In MainInterface.storyboard, remove the default Label.

In MainInterface.storyboard, select View and change the Background to System Grouped Background Color.

Build the target and follow the instructions in Sending Test Notification for iOS to verify that the rich push notification works as expected.

See the troubleshooting steps below if you encounter issues sending notifications.

Ensure that the deployment target of AppierNotificationServiceExtension and AppierNotificationContentExtension is set to iOS 10.0.

Remove -ObjC/$(inherited) if it exists in the build settings of the AppierNotificationServiceExtension and AppierNotificationContentExtension.

Ensure that the same App Group ID is used in all three targets.

Under the AppierNotificationServiceExtension and AppierNotificationContentExtension targets, go to Build Phases > Compile Sources to make sure the following files are correctly configured. If not, click + to add the files.

AppierNotificationServiceExtension Compile Sources

AppierNotificationContentExtension Compile SourcesUpdated over 1 year ago Table of Contents

Overview

SDK version requirement



Adding Required Extensions [5]

https://docs.aiqua.appier.com/docs/rich-push-notifications



AppierNotificationContentExtension Compile SourcesUpdated over 1 year ago Table of Contents

Overview

SDK version requirement

1. Save your App Group ID

2. Add the extensions

3. Install the extensions

Swift Package Manager

Installing with CocoaPods

Manual installation (not recommended)

4. Set up the Notification Service Extension

5. Set up the Notification Content Extension

Send a test push notification

Troubleshooting



Sending Test Notifications [0]

https://docs.aiqua.appier.com/docs/test-notification-for-ios



Prepare a physical iOS device to test push notifications.

Connect your iOS device to your Mac.

In Xcode, choose the device in the run destination menu, then build and run the app.

Open the app on your device and allow notifications.

On the AIQUA Dashboard, click your account name in the lower-left corner and click Recent Users, select either the iOS Development or iOS Production tab depending on your iOS build configuration, then save your device's User ID.

Create a new segment. Go to Audience > Create Segment and select Segment by Condition.

Under Include Users, select All, click Add New Condition, and set userId equal to the User ID of your test device.

Click Save to return to the Segment List page. You should see a new subscriber listed under iOS (Dev) Subscribers for a development build, or under iOS Subscribers for a production build.

Go to Campaigns > Regular Campaigns and click + Create New Campaign.

Set following fields:

Setting TypeValueCampaignCampaign Type: PushScheduleSend ManuallyAudience

Platform: iOS

Include Users of the Segment: SEGMENT_NAME

Creative

Type: Standard

Title: Hello Push

Subtitle: 1st Push test

Message: Hello Push🤩👍

Media Attachment URL: https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg

Click Save.

In the campaign list, click the send button. Select the option that corresponds to your build configuration.

Your iOS device should now receive a push notification. Tap the notification.

If you haven't completed the Rich Push Notification integration, you won't see the image:

In the Campaign List, you should see the Imp (Impression) and Clicks counts increment, indicating that both metrics are being tracked properly.

Ensure you've completed all the required steps in the following pages:

Installing the iOS SDK 

Enabling Capabilities and App Group

Initializing the iOS SDK

Push Notifications

Next, check that the following conditions are met:

The test device is in a stable network environment.

The segment contains the test device you are using.



Sending Test Notifications [1]

https://docs.aiqua.appier.com/docs/test-notification-for-ios



The test device is in a stable network environment.

The segment contains the test device you are using.

The correct profile (Production Profile or Development Profile) was selected depending on your build configuration.

The Recent Users page on the AIQUA Dashboard does not have an uninstallTime. If it does, re-install the app and subscribe to push notifications again.

Make sure Rich Push Notifications steps have been completed.

Make sure you are using HTTPS URLs for the attached media.

Make sure Implementing Deep Links steps have been completed.

Make sure Rich Push Notifications steps have been completed.

Make sure Rich Push Notifications steps have been completed.

Updated over 1 year ago Table of Contents

1. Build and Run the App on Your Device

2. Create an Audience Segment

3. Create an iOS Push Campaign

4. Send the Campaign

Troubleshooting

I didn't receive a notification

The image in the notification isn't displaying

The link in the notification isn't working

A notification with a Carousel creative doesn't display properly

I received the notification, but the impression isn't tracked



(Optional) Sending Provisional Push Notifications [0]

https://docs.aiqua.appier.com/docs/provisional-push-notifications-in-ios-12



iOS 12 introduced a new feature called Provisional Authorization to give you the ability to send notifications silently, without user permission. The notification is only delivered in the notification center, and the user gets the option to keep receiving notifications from the app silently, prominently, or to turn them off.

Here's how you can use the UNAuthorizationOptionProvisional API:

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {

// Override point for customization after application launch

let QG = QGSdk.getSharedInstance()

#if DEBUG

QG.onStart("AIQUA_APPID", withAppGroup:"APPIER_APP_GROUP_ID", setDevProfile: true)

#else

QG.onStart("AIQUA_APPID", withAppGroup:"APPIER_APP_GROUP_ID", setDevProfile: false)

#endif

if #available(iOS 10.0, *) {

let center = UNUserNotificationCenter.current()

center.delegate = self

var options = UNAuthorizationOptions([.alert, .sound, .badge, .carPlay])



// sample code to enable Provisional Authorization

if #available(iOS 12.0, *) {

options.update(with: .provisional)

}





center.requestAuthorization(options: options) { (granted, error)in

print("Granted: \(granted), Error: \(String(describing: error))")

}

} else {

let settings = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories:nil)

UIApplication.shared.registerUserNotificationSettings(settings)

}

return true

}

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions

{

//Initializing the SDK 

QGSdk *qgsdk = [QGSdk getSharedInstance];

#ifdef DEBUG

[qgsdk onStart:@"your aiqua appid" withAppGroup:@"group.com.company.product.notification" setDevProfile:YES];

#else

[qgsdk onStart:@"your aiqua appid" withAppGroup:@"group.com.company.product.notification" setDevProfile:NO];

#endif

//Registering Push Notification

if (@available(iOS 10.0, *)) {



(Optional) Sending Provisional Push Notifications [1]

https://docs.aiqua.appier.com/docs/provisional-push-notifications-in-ios-12



#endif

//Registering Push Notification

if (@available(iOS 10.0, *)) {

UNAuthorizationOptions options = (UNAuthorizationOptions) (UNAuthorizationOptionAlert | UNAuthorizationOptionBadge | UNAuthorizationOptionSound | UNAuthorizationOptionCarPlay);



//add provisional for silent push in notification center

if (@available(iOS 12.0, *)) {

options = options | UNAuthorizationOptionProvisional;

}

UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];

center.delegate = self;

[center requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError *error){

NSLog(@"GRANTED: %i, Error: %@", granted, error);

}];

} else {

// Fallback on earlier versions - iOS 8 & 9

UIUserNotificationType types = UIUserNotificationTypeAlert | UIUserNotificationTypeSound |

UIUserNotificationTypeBadge;

UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:types categories:nil];

[[UIApplication sharedApplication] registerUserNotificationSettings:settings];

}



return YES;

}

Updated over 1 year ago Table of Contents

What is Provisional Authorization

Sending a Provisional Push Notification



(Optional) Storing Push Notifications [0]

https://docs.aiqua.appier.com/docs/storing-push-notification-for-ios



With Appier iOS SDK, you can store the push notifications you have sent to users, and retrieve these data later. You can use the following methods to enable notification storage, retrieve stored notifications, set the maximum limit for storage, and delete stored notifications. 

📘Note

This feature is supported for iOS SDK 5.2.1 or later.

The SDK will only save the notifications sent from AIQUA servers.

It is required to integrate QGNotification SDK and initialize SDK with AppGroup assigned.

By default, the SDK disables push notification storage at every launch. 

To enable it: After Initializing the iOS SDK using [[QGSdk getSharedInstance] onStart...], call the method below.

To disable it: Simply remove this method. 

QGSdk.getSharedInstance().enablePushNotificationStorage()

[[QGSdk getSharedInstance] enablePushNotificationStorage];

The following code shows you how to retrieve stored notifications. You will get an array of dictionary if existed; Nil will be returned if there are no stored push notifications.

let list = QGSdk.getSharedInstance().fetchSavedPushNotifications()

NSArray* list = [[QGSdk getSharedInstance] fetchSavedPushNotifications];

By default, the maximum number of notifications that can be stored is 20. After Initializing the iOS SDK using onStart, you can call the following method to set a different limit.

QGSdk.getSharedInstance().setPushNotificationStorageLimit(100)

[[QGSdk getSharedInstance] setPushNotificationStorageLimit:100];

If the limit you set is smaller than the existing limit, for example changing from 100 to 80, the oldest 20 notifications will be deleted.

You can delete all stored push notifications:

QGSdk.getSharedInstance().deleteSavedPushNotifications()

[[QGSdk getSharedInstance] deleteSavedPushNotifications];

You can delete a specific notification by index from the list returned by the SDK. For example, to delete the 4th notifications, set the index to 3:

QGSdk.getSharedInstance().deleteNotification(at: 3)

[[QGSdk getSharedInstance] deleteNotificationAtIndex:3];



(Optional) Storing Push Notifications [1]

https://docs.aiqua.appier.com/docs/storing-push-notification-for-ios



QGSdk.getSharedInstance().deleteNotification(at: 3)

[[QGSdk getSharedInstance] deleteNotificationAtIndex:3];

SDK will ignore the call if the input index is out of bound or invalid. For example, if there are only two notifications in the example above, SDK will ignore the call.Updated over 1 year ago Table of Contents

Enabling/Disabling Push Notification Storage

Retrieving Stored Notifications

Setting the Maximum Number of Stored Notifications

Deleting All Stored Notifications

Deleting a Stored Notification



(Optional) Receiving Key-Value Pairs

https://docs.aiqua.appier.com/docs/customizing-push-notifications-ios



If you've set key-value pairs in the campaign, you can get them from the notification delegate callback.

Let’s say you passed a key called myKey in the campaign, you can get its value as:

func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {

let userinfo = request.content.userInfo

if userinfo != nil {

let customKeyPairs = userinfo["qgPayload"] as? [AnyHashable : Any]

if let customKeyPair = customKeyPairs?["myKey"] {

print("NotificationService EX: \(customKeyPair)")

}

}

// Existing QGNotificationSdk code ...

let qgsdk = QGNotificationSdk.sharedInstance(withAppGroup: APP_GROUP)

qgsdk?.didReceive(request, withContentHandler: { content in

contentHandler(content)

})

}

- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler

{

NSDictionary *userinfo = request.content.userInfo;

if (userinfo) {

NSDictionary *customKeyPairs = userinfo[@"qgPayload"];

NSLog(@"NotificationService EX: %@", customKeyPairs[@"myKey"]);

}



//Existing QGNotificationSdk code ...

QGNotificationSdk *qgsdk = [QGNotificationSdk sharedInstanceWithAppGroup:APP_GROUP];

[qgsdk didReceiveNotificationRequest:request withContentHandler:^(UNNotificationContent *content){

contentHandler(content);

}];

}

Updated 6 months ago Table of Contents

Receiving Key-Value Pairs



(Optional) Customizing Notification Sounds

https://docs.aiqua.appier.com/docs/custom-push-notification-sound-for-ios



iOS supports using custom sounds when sending push notifications. AlQUA lets you enable this for iOS users via a compatible sound file added on AIQUA dashboard.

Before adding the sound file, make sure that it meets the following requirements:

Maximum sound length - 30 seconds

Format - AIFF (.aif)

To know the exact details about configuring the sound file, refer to Preparing Custom Alert Sounds and other related information from Apple's developer guide.

On AIQUA Dashboard, add the sound file name with its file extension under the ADVANCED section of the Campaign creation page.

📘NoteIf the Sound File field is empty, the default sound is played when your notification reaches the user's device.

Updated over 1 year ago Table of Contents

Configuring the Sound File

Adding the Sound File in a Campaign



(Optional) Customizing Action Buttons for Carousel and Slider [0]

https://docs.aiqua.appier.com/docs/custom-action-buttons-for-ios



The iOS version of a carousel or slider push have action buttons. By default, some action buttons are displayed with ▶▶ to go to the next image in the carousel or slider, while Open App enables opening the app with an image deep link. By default, these actions are registered by the main SDK with default buttons. The title to these buttons can be customized inside the main target when registering for the remote push notification prompt.

Starting with the SDK version 4.4.2, AIQUA will default register action buttons for the carousel and slider push notifications with a default title. You will learn how to registering action button titles for the push notification prompt.

📘NoteThis feature is only supported on iOS 10 or later.

▶▶ This is the play button that animates the carousel (for iOS 10 and iOS 11 only).

Open App - Opens the app with the deep link corresponding to the image shown. If there is no deep link for the image, the default deep link for the notification is called.

iOS 12 allows user interactions such as scrolling the images inside the notification view. For iOS 12 and above, the play button is hidden. 

In iOS 10 and iOS 11, user interactions can only be done using the play button. If the images are clicked, the default deep link is called because there are no user interactions, which is an Apple restriction. The Open App button can be clicked to call the deep link that corresponds to the image. 

There are two ways to customize the carousel notification's action button title using the Appier SDK.

To customize only the action button, use:

+ (void)setCarouselNotificationCategoryWithNextButtonTitle:(nullable NSString *)next withOpenAppButtonTitle:(nullable NSString *)openApp API_AVAILABLE(ios(10.0));

To register other action categories, the AIQUA carousel category must also be registered. Doing this returns the action category and can be added using the following method:



(Optional) Customizing Action Buttons for Carousel and Slider [1]

https://docs.aiqua.appier.com/docs/custom-action-buttons-for-ios



+ (UNNotificationCategory *)getQGSliderPushActionCategoryWithNextButtonTitle:(nullable NSString *)next withOpenAppButtonTitle:(nullable NSString *)openApp API_AVAILABLE(ios(10.0));

if #available(iOS 10.0, *) {

let center = UNUserNotificationCenter.current()

center.delegate = self



var categories: Set = Set.init()

categories.insert(QGSdk.getQGSliderPushActionCategory(withNextButtonTitle: ">> Next >>", withOpenAppButtonTitle: "Interested"))

center.setNotificationCategories(categories)



center.requestAuthorization(options: [.badge, .carPlay, .alert, .sound]) { (granted, error) in

print("Granted: \(granted), Error: \(error)")

}

}

if (@available(iOS 10.0, *)) {

UNAuthorizationOptions options = (UNAuthorizationOptions) (UNAuthorizationOptionAlert | UNAuthorizationOptionBadge | UNAuthorizationOptionSound | UNAuthorizationOptionCarPlay);

UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];

center.delegate = self;

// also add any other custom action category in the set

NSSet *categories = [NSSet setWithObjects:[QGSdk getQGSliderPushActionCategoryWithNextButtonTitle:@">> Next >>" withOpenAppButtonTitle:@"Interested"], nil];

[center setNotificationCategories:categories];



[center requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError *error){

NSLog(@"GRANTED: %i, Error: %@", granted, error);

}];

}

Updated over 1 year ago Table of Contents

Default Action Buttons

User Interaction

Changing the Button Title



iOS SDK Web View Support [0]

https://docs.aiqua.appier.com/docs/ios-webview-support



Track custom user events and attributes logged from a web page within a web view by establishing a JavaScript bridge between the Appier Web SDK and the Appier iOS SDK. If the web-to-mobile SDK bridge is not established, your mobile app users will be tracked in AIQUA as web users rather than iOS users.

When a web page is integrated with the Appier Web SDK and web view logging has been configured:

Web SDK custom user events and attributes are passed to the iOS SDK. 

Web SDK default user events and attributes are not tracked at all.

📘NoteThe Appier Web SDK's default user events and attributes (such as page_viewed and visited) aren't tracked from within a web view.

FeatureRequired iOS SDK versionWeb view loggingRequires Appier iOS SDK 4.1.0 or later.Recommendation 2.0Requires Appier iOS SDK 7.8.0 or later.Filtering out purchased products by user_id from Recommendation 2.0 results is supported in iOS SDK 7.12.0 or later.Multiple app IDs

(iOS SDK 8.1.0 or later)If your app and website use different app IDs, contact Appier Support (ess_support@appier.com ) to modify the SDK's app ID allowlist to ensure web data is logged to the correct app ID.

Using the QGWKWebView class is the recommended approach for implementing web view logging, as this class is continually updated to support new features.

Alternatively, if you have an existing web view implementation and prefer not to migrate your implementation to the QGWKWebView class, you can use custom JavaScript injections.

Instantiate a QGWKWebView instance with one of the following methods:

Swift: init()

Objective-C: init() or initWithFrame()

The following example shows how to create a QGWKWebView instance:

var webview = QGWKWebView(frame: view.frame)

// or specify a configuration with:

// var webview = QGWKWebView(frame: view.frame, configuration: config)

// Inside the view controller

#import "QGWKWebView.h"



// Using initWithFrame:

QGWKWebView *webview = [[QGWKWebView alloc] initWithFrame:self.view.frame];

// or specify a configuration with:



iOS SDK Web View Support [1]

https://docs.aiqua.appier.com/docs/ios-webview-support



QGWKWebView *webview = [[QGWKWebView alloc] initWithFrame:self.view.frame];

// or specify a configuration with:

// QGWKWebView *webview = [[QGWKWebView alloc] initWithFrame:self.view.frame configuration:config];

Add a WKWebView object in the Storyboard or Nib view, then change the class to QGWKWebView from the identity inspector.

Updated 4 months ago Table of Contents

Overview

Version requirements

Implementing web view logging

Option 1: Initialize QGWKWebView

Option 2: Use Storyboard or Nib



Custom Web View Implementation [0]

https://docs.aiqua.appier.com/docs/ios-custom-webview-implementation



You can inject custom JavaScript into your own web view implementation to track custom events and attributes logged from a web view. If you don't need a custom web view implementation, we recommend using the QGWKWebView class to configure WebView logging, as QGWKWebView is continually updated to support new features.

Ensure your app uses SDK v7.28.0 or later before implementing a custom web view.

The Web SDK's default user events and attributes (such as page_viewed and visited) aren't logged from within a web view.

Use WKUserScript to inject AIQUA's script as soon as the WKWebView instance is loaded.

let userScript = WKUserScript(source: QGWKWebViewUserScript, injectionTime: .atDocumentStart, forMainFrameOnly: false)

// add the user script to the webview user controller

webview.configuration.userContentController.addUserScript(userScript)

WKUserScript *aiqUserScript = [[WKUserScript alloc] initWithSource:QGWKWebViewUserScript

injectionTime:WKUserScriptInjectionTimeAtDocumentStart

forMainFrameOnly:NO];

// add the user script to the webview user controller

[self.webView.configuration.userContentController addUserScript:aiqUserScript];

To invoke the native iOS code from JavaScript code, create a message handler class conforming to the WKScriptMessageHandler protocol. The message body contains the data to be sent.

Use the following code sample containing handleScriptMessage()/handleScriptMessageOfWebView()—these methods contain the message handling implementation and greatly simplifies the required code:

func userContentController(_ userContentController: WKUserContentController,

didReceive message: WKScriptMessage) {

if message.name == "aiqua" {

QGSdk.getSharedInstance().handleScriptMessage(of: self,

userContentController: userContentController,

didReceive: message)

} else {

// handle other messages

}

}

- (void)userContentController:(nonnull WKUserContentController *)userContentController

didReceiveScriptMessage:(nonnull WKScriptMessage *)message {

if ([message.name isEqualToString: @"aiqua"]) {



Custom Web View Implementation [1]

https://docs.aiqua.appier.com/docs/ios-custom-webview-implementation



didReceiveScriptMessage:(nonnull WKScriptMessage *)message {

if ([message.name isEqualToString: @"aiqua"]) {

[[QGSdk getSharedInstance] handleScriptMessageOfWebView:self

userContentController:userContentController

didReceiveScriptMessage:message];

} else {

// handle other messages

NSLog(@"received message %@", message.name);

}

}

Finally, add the message handler to the web view's user content controller:

self.webview.configuration.userContentController.add(self, name: "aiqua")

[self.webView.configuration.userContentController addScriptMessageHandler:self name:@"aiqua"];

Launch your web view and verify that events and attributes are logged in the Recent Activity or Recent Users section of the AIQUA dashboard.Updated 4 months ago Table of Contents

Overview

Requirements and limitations

Integration guide

1. Inject the AIQUA script

2. Implement a native interface

3. Verify your web view integration



Advanced Features and Customization

https://docs.aiqua.appier.com/docs/advanced-features-and-customization-for-ios



The iOS SDK offers the following advanced features and customization:

Configuring Batching for Network Requests

Regenerating iOS Users

Method Swizzling in the iOS SDK

Updated over 1 year ago Custom Web View ImplementationConfiguring Batching for the iOS SDKDid this page help you?



Configuring Batching for the iOS SDK

https://docs.aiqua.appier.com/docs/configure-batching-for-the-ios-sdk



To optimize network usage, the Appier iOS SDK batches the network requests it makes to the AIQUA server. By default, it flushes data to the server every 15 seconds in release builds, and every second in debug builds. 

You can configure your preferred BATCH_INTERVAL (in seconds) using this method:

QGSdk.getSharedInstance().flushInterval = BATCH_INTERVAL

[[QGSdk getSharedInstance] setFlushInterval:BATCH_INTERVAL];

To force the Appier SDK to flush the data to the server at any time, call:

QGSdk.getSharedInstance().flush()

[[QGSdk getSharedInstance] flush];

To invoke a completion handler after flush, use:

QGSdk.getSharedInstance().flush(completion: {

//some method

})

[[QGSdk getSharedInstance] flushWithCompletion:^{

//some method

}];

Updated over 1 year ago



Managing iOS Users

https://docs.aiqua.appier.com/docs/regenerate-user-id-ios



AIQUA iOS users are identified using the Appier SDK-generated userId. 

Retrieving userId

Deleting and regenerating iOS users

📘Retrieving the userId is only available in iOS SDK v7.25.0 and later.

To retrieve the value of userId, call getAppierId():

let qgsdk = QGSdk.getSharedInstance()

let appierUserId = qgsdk?.getAppierId()

QGSdk *qgsdk = [QGSdk getSharedInstance];

NSString *appierUserId = [qgsdk getAppierId];

To delete an iOS user's data and regenerate userId, for example, when a user modifies their data tracking consent settings, you'll need to complete two steps:

Delete the user's data with the Delete Users API using their unique identifier from your CRM (user_id).

Regenerate userId using the iOS SDK. In addition to generating a new userId, calling this method will delete all locally cached data, including events, attributes, and campaigns.

iOS SDK 7.25.0 and later: Use renewAppierId()

iOS SDK 7.5.0 to 7.24.0: Use renewUserId()

iOS SDK 7.4.0 and earlier: Regenerating userId is not supported

📘NoteWhen regenerating userId:

The iOS SDK won't renew the app's push token. This prevents users from receiving campaigns before cached data (deleted using the Delete Users API) is purged from AIQUA's servers.

User data collection permissions will remain unchanged. Reconfigure the relevant user data permissions after regenerating the user if needed.

let qgsdk = QGSdk.getSharedInstance()

// iOS SDK 7.25.0 and later

qgsdk?.renewAppierId({

// Do anything you want after the Appier ID is renewed

})

// iOS SDK 7.5.0 to 7.24.0

qgsdk?.renewUserId({

// Do anything you want after the Appier ID is renewed

})

QGSdk *qgsdk = [QGSdk getSharedInstance];

// iOS SDK 7.25.0 and later

[qgsdk renewAppierId:^() {

// Do anything you want after the Appier ID is renewed.

}];

// iOS SDK 7.5.0 to 7.24.0

[qgsdk renewUserId:^() {

// Do anything you want after the Appier ID is renewed.

}];

Updated over 1 year ago Table of Contents

Overview

Retrieving userId

Deleting and regenerating iOS users



Method Swizzling in the iOS SDK

https://docs.aiqua.appier.com/docs/ios-sdk-method-swizzling



Method swizzling is disabled by default starting from iOS SDK 7.26.0. You can enable method swizzling to automatically enable the following LINE-related features:

LINE user sync

Logging click events (notification_clicked and qg_line_click) for LINE campaigns that open your app

Enabling method swizzling automatically enables LINE-related functions (LINE user sync and logging click events for LINE campaigns that open your app).

To enable method swizzling, add the flag AppierAppDelegateProxyEnabled in your app’s Info.plist file and set it to YES (boolean value). The iOS SDK implements the following swizzled methods:

application:openURL:options:

application:continueUserActivity:restorationHandler:

If you enable method swizzling and any other SDKs used by your app swizzle the same methods the Appier iOS SDK swizzles, you will encounter app crashes. Method swizzling conflicts can be identified by error message such as:

Appier [DEBUG] [AIQUA] Appier setAppierDelegate CALLED:

EXEC_BAD_ACCESS

Appier `-[AppierAppDelegate appierApplication:openURL:options]:) 

To resolve method swizzling conflicts that result in app crashes, disable method swizzling in the Appier iOS SDK or in the third-party SDK your app uses.

To disable method swizzling, set the flag AppierAppDelegateProxyEnabled in your app’s Info.plist file and set it to NO (boolean value). 

Note that if method swizzling is disabled, you'll need to set up iOS deep link handling in your app to support LINE user sync.Updated over 1 year ago Table of Contents

Overview

Enabling method swizzling

SDK conflicts

Disabling method swizzling



React Native SDK Overview [0]

https://docs.aiqua.appier.com/docs/versions-for-react-native-integration



The Appier Enterprise Service SDK ("Appier SDK") is the main SDK for Appier's Enterprise Products: AIXON, AIQUA, and AiDeal.

Refer to the following versions when setting up React Native integrations in AIQUA. 

🚧IMPORTANT NOTICES

If you're upgrading from version 1.8.0 or earlier, you'll need to change the React Native SDK package name from react-native-aiqua-sdk to @appier/react-native-sdk in all the import lines in your app and your app's dependencies in package.json

If you're setting your Android app's targetSdkVersion to 31 (Android 12), you'll need to upgrade to React Native SDK 1.8.0.

Starting in November 2021, Android app updates will be required to target API level 30 or above and adjust for behavioral changes in Android 11. See the official Android Developer guides here.

[SDK Upgrade Required] To avoid a crash issue in Android apps targeting API level 30 or above, upgrade your app to Appier React Native SDK 1.6.1. See Release Notes.

Starting from version 1.4.0, Appier SDK uses CocoaPods dependency. We recommend you to upgrade to React Native version > 0.60. 

If you are upgrading to Appier SDK 1.4.0 or above for the first time, some migration steps are needed for iOS Rich Push integration. Refer to this Migration Doc.

Appier SDK does NOT support Expo Managed Workflow. If you want to use Appier SDK in Expo, eject to Bare Workflow.

Supported VersionsDependency• React - 16.0.0 and above

• React Native - 0.46.0 and aboveReact Native WebView - 5.0.1 and above

📘NoteFor React Native versions 0.60.0 and above,

Use Appier SDK versions 1.3.1 and above only.

Appier SDK versions 1.3.1 and above support CocoaPods installation and automatic linking.

For React Native versions 0.59.x and below, Appier SDK version 1.3.1 is also supported.

Release notes of Appier React Native SDK can be found here.



React Native SDK Overview [1]

https://docs.aiqua.appier.com/docs/versions-for-react-native-integration



Release notes of Appier React Native SDK can be found here.

Any Appier SDK version with rc in the version number is a release candidate. When installing SDK, use release versions such as 1.3.0 or 1.3.1 instead of release candidates such as 1.3.1-rc-1 or 1.3.1-rc-2. Release candidates may be unstable and are intended for testing purposes.Updated 8 months ago Installing the SDK via React NativeTable of Contents

Dependencies Version Support

Release Notes

Release Candidates (Testing Only)



Development React Native SDK Versions [0]

https://docs.aiqua.appier.com/docs/react-native-sdk-release-notes



Updated the bridged Appier Android SDK version from 8.2.1 to 8.2.4. See the Android SDK release notes for a detailed summary of changes.

Added logic to map incorrectly regenerated Appier IDs to their original correct IDs, enabling data recovery efforts initiated due to the known issue present in versions 2.1.0 and 2.1.1.

The Appier ID (userId) is no longer incorrectly regenerated on the first app launch (either in the foreground or background). This issue is present in versions 2.1.0 and 2.1.1

Updated the bridged Appier Android SDK version from 8.2.0 to 8.2.1. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 8.2.0 to 8.2.1. See the iOS SDK release notes for a detailed summary of changes.

The Appier ID (userId) is mistakenly regenerated on the first app launch (either in the foreground or background) after upgrading to this SDK version. These regenerated Appier IDs were mistakenly counted as new users, impacting related metrics and segments.

Updated the bridged Appier Android SDK version from 8.0.1 to 8.2.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 8.0.1 to 8.2.0. See the iOS SDK release notes for a detailed summary of changes.

Calling setCustomKey with a large non-integer number on Android produced incorrect output.

The Appier ID (userId) is mistakenly regenerated on the first app launch (either in the foreground or background) after upgrading to this SDK version. These regenerated Appier IDs were mistakenly counted as new users, impacting related metrics and segments.

react-native-webview is now an optional dependency.

Support for Retail Media Network features (beta). To learn more, contact your customer success manager.

Updated the bridged Appier Android SDK version from 7.25.0 to 8.0.1. See the Android SDK release notes for a detailed summary of changes.



Development React Native SDK Versions [1]

https://docs.aiqua.appier.com/docs/react-native-sdk-release-notes



Updated the bridged Appier iOS SDK version from 7.33.0 to 8.0.1. See the iOS SDK release notes for a detailed summary of changes.

configure() now returns a promise that resolves to a boolean, enabling you to verify that the SDK has initialized successfully before calling other methods. To learn more, see Initializing the SDK via React Native.

Starting from this version, the Appier React Native SDK requires additional initialization code for Android. For details, see Initializing the React Native SDK.

For Android notifications to work, you need to apply the Google Services Gradle plugin in android/app/build.gradle file. For details, see [Android] Push Notifications.

Updated 15 days ago Table of Contents

v2.1.2 - March 14, 2025

v2.1.1 - February 7, 2025 (Deprecated)

v2.1.0 - January 23, 2025 (Deprecated)

v2.0.1 - December 9, 2024

v2.0.0 - November 22, 2024

New

Changed



[iOS] Migrating to React Native SDK 1.5 or Later

https://docs.aiqua.appier.com/docs/ios-sdk-migration-for-react-native



If you are using the Appier React Native SDK 1.4.0 and you are upgrading to the latest SDK version, you need to follow the Rich Push Migration instructions below to migrate.

Starting from React Native SDK 1.4.0, Appier uses dynamic framework AppierFramework to make integration easier. 

Starting from React Native SDK 1.5.0, Appier uses AppierExtensionFramework in Notification Service Extension and Notification Content Extension for Rich Push integration. 

From SDK VersionTo SDK Versions1.4.01.5.0 or above

To migrate your app to Appier React Native SDK 1.5.0, update the following parts of your project:

The Notification Service Extension

The Notification Content Extension

Your project's Podfile (if you use CocoaPods for package management)

Update the contents of the NotificationService.* files.

Remove Appier.framework or Appier.xcframework from AppierNotificationServiceExtension target > General tab > Frameworks and Libraries. 

Update the contents of the NotificationViewController.* files.

Remove Appier.framework or Appier.xcframework from AppierNotificationContentExtension target > General tab > Frameworks and Libraries. 

If your project uses CocoaPods for package management, update your Podfile to include AppierExtensionFramework, AppierNotificationServiceExtension, and AppierNotificationContentExtension.Updated over 1 year ago Table of Contents

Rich Push Migration

Notification Service Extension

Notification Content Extension

Podfile (CocoaPods only)



Installing the SDK via React Native [0]

https://docs.aiqua.appier.com/docs/installing-the-sdk-via-react-native



Refer to the following methods when integrating the Appier Enterprise Service SDK ("Appier SDK") using React Native. 

$ npm install @appier/react-native-sdk --save

$ yarn add @appier/react-native-sdk

After installing the SDK, it needs to be linked to native Android and iOS libraries. Follow the below section based on the React Native version you are using.

📘Web viewsIf you need to log custom data from app web views, you'll also need to install react-native-webview. Refer to React Native SDK Web View Support for details.

Automatic linking is supported for Appier React Native SDK versions 1.3.1 or later.

All the dependencies should be automatically added. In case of issues, refer to Gradle files in Android Studio.

Install the Appier iOS SDK via CocoaPods.

📘Note:In a later step, you'll need to use the same Podfile created to add Notification Service Extension and Notification Content Extension targets and their dependency for AppierFramework. This dependency will be managed by node_modules for the main app target in iOS.

$ react-native link @appier/react-native-sdk

📘Manual linkingManual linking is not recommended, but if needed, follow the instructions described in Manual linking.

Open up android/app/src/main/java/[...]/MainActivity.java then add import com.reactlibrary.RNAiquaSdkPackage; to the imports at the top of the file.

Add the new RNAiquaSdkPackage() to the list returned by the getPackages() method.

Append the following lines to android/settings.gradle: 

include ':appier_react-native-sdk' project(':appier_react-native-sdk').projectDir = new File(rootProject.projectDir, '../node_modules/@appier/react-native-sdk/android')

Insert the following lines inside the dependencies block in android/app/build.gradle: 

implementation project(':appier_react-native-sdk')

In Xcode, go to the project navigator then right-click Libraries > Add Files to [your project's name].

Go to node_modules > @appier/react-native-sdk and add RNAiquaSdk.xcodeproj.



Installing the SDK via React Native [1]

https://docs.aiqua.appier.com/docs/installing-the-sdk-via-react-native



Go to node_modules > @appier/react-native-sdk and add RNAiquaSdk.xcodeproj.

In Xcode, go to the project navigator then select your project. Add libRNAiquaSdk.a to your project's Build Phases > Link Binary With Libraries.

Run your project using (Cmd+R)<.

Updated 4 months ago Initial Setup for Native Android and iOSTable of Contents

1. Installation

2. Link native modules in React Native

React Native 0.60.0 or later

React Native 0.46.0 to 0.59.10

Manual linking

Android

iOS



Required Setup for Native Android and iOS

https://docs.aiqua.appier.com/docs/initial-setup-for-native-android-and-ios



Open your Android project and use Android Studio to set up a Firebase messaging service inside your sub-project. For more details, see https://firebase.google.com/docs/android/setup.

📘Gradle Dependency and Conflict ResolutionGradle build may fail if there is version mismatch between Appier SDK dependency and your app dependency. To resolve such dependency conflicts, refer to this section.

On AIQUA Dashboard, go to the Android Integration page and complete the setup. For more details, see Entering App Info on AIQUA Dashboard.

Some initial setup is required inside the native part of iOS before you can proceed to the SDK usage.

If your app is using APNs, follow the steps below:

Configure iOS Push Credentials 

Enable Capabilities - Open iOS project in Xcode to enable Capabilities.

If your app is using Firebase Cloud Messaging (FCM), follow the steps below:

Enable Capabilities - Open iOS project in Xcode to enable Capabilities.

Provide the Firebase Server Key and Sender ID to Appier Support (ess_support@appier.com).

To find your Server Key and Sender ID, go to FCM Console > Setting icon > Project Settings > Cloud Messaging.

Upload p12 or p8 certificates to FCM Console. Go to FCM Console > Setting icon > Project Settings > Cloud Messaging.

If you are using p8 certificates, click Upload under APNs Authentication Key.

If you are using p12 certificates, click Upload under APNs Certificates.

Do NOT upload the certificates to AIQUA dashboard.Updated over 1 year ago Initializing the SDK via React NativeTable of Contents

For Android

For iOS

For iOS App Using APNs

For iOS App Using FCM



Initializing the React Native SDK

https://docs.aiqua.appier.com/docs/initializing-the-sdk-via-react-native



Follow the steps below to initialize the Appier React Native SDK.

Import the Appier React Native SDK in App.js or App.tsx.

import RNAiqua from '@appier/react-native-sdk';

Initialize the SDK in App.js or App.tsx file using the following parameters:

NameDescriptionappIdYour app ID. It is inside the account settings in the dashboard.senderIdOptional. Your own FCM sender ID for Android. If empty, AIQUA's default sender ID will be used instead.

We recommend using your own FCM sender ID, as AIQUA will be deprecating the default sender ID in the future. appGroupYour iOS app group.isDevOptional. Your iOS app environment. Set to true for a development build or false for a production build. By default, it is set to false for production builds.

const isConfigured = await RNAiqua.configure({

appId: '',

senderId: '', // (Optional) Android sender ID

appGroup: '', 

isDev: // (Optional) iOS environment type, default `false`

});

// If you need to call other APIs immediately after initializing the SDK,

// check that SDK was initialized successfully.

if (isConfigured) {

RNAiqua.setName('name');

RNAiqua.setEmail('email');

RNAiqua.setUserId('userId');

}

(SDK 2.0.0 or later) For Android, import and create an instance of the Appier SDK inMainApplication.kt.

import com.appier.sdk.Appier // 1. Import the Appier SDK

...

override fun onCreate() {

super.onCreate()

SoLoader.init(this, false)

Appier.create(this) // 2. Create an instance of the Appier SDK

...

}

isDev - For iOS, this defaults to false for the production build.

RNAiqua.configure({

appId: '', 

appGroup: ''

});

Updated 5 months ago [Android] Push Notifications[iOS] Push Notifications



[iOS] App Tracking Transparency for React Native [0]

https://docs.aiqua.appier.com/docs/app-tracking-transparency-react-native



📘Note:Support for App Tracking Transparency requires React Native SDK 1.5.0 or above.

Starting with iOS 14.5, Apple now requires app to ask for permission to track users using the device's advertising identifier (IDFA). See https://developer.apple.com/app-store/user-privacy-and-data-use/.

To do this, you will need to use the App Tracking Transparency framework provided by Apple. Once the App Tracking Transparency framework is integrated, users will see a dialog box that asks for permission to track them.

Below is a brief summary on how to integrate App Tracking Transparency framework, but be sure to go through Apple's official documents on AppTrackingTransparency framework for more details.

In your project’s Info.plist file, add a NSUserTrackingUsageDescription key. Write a message describing the purpose for tracking user data that is specific to your use case. ​The message shown below is just an example. 

NSUserTrackingUsageDescription

This allows us to serve personalized contents and ads based on your browsing pattern across apps and websites.

This message will be displayed on the dialog box to request user permission.

To request user's permission for tracking, add the AppTrackingTransparency framework to your app. Below is an example of requesting for user's permission at app launch.

import AppTrackingTransparency

import Appier

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

if #available(iOS 14, *) {

ATTrackingManager.requestTrackingAuthorization { _ in

...

}

}

}

#import 

#import 

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

if (@available(iOS 14.0, *)) {

[ATTrackingManager requestTrackingAuthorizationWithCompletionHandler:^(ATTrackingManagerAuthorizationStatus status) {

...

}];

}

}



[iOS] App Tracking Transparency for React Native [1]

https://docs.aiqua.appier.com/docs/app-tracking-transparency-react-native



...

}];

}

}

If the user chooses to allow tracking, an ATTrackingManagerAuthorizationStatusAuthorized value will be returned. See Apple's documentation for details on the authorization values available.

If you want Appier SDK to collect IDFA only when an "Authorized" status is returned, call the setIDFAConsent method and set it to true in your react-native application.

If setIDFAConsent is set to false, Appier SDK will collect IDFA regardless of user's authorization status. However, depending on the user's authorization status, the IDFA collected may be valid or invalid (e.g. 00000000-0000-0000-0000-000000000000). The same applies if setIDFAConsent is not set.

Put the code snippet below into your initilization method.

RNAiqua.configure({

appId: '',

appGroup: '',

isDev: true // ios dev or prod - default is true

});

//If true, IDFA is sent ONLY if user authorizes tracking

//If false or not set, IDFA is sent regardless of user's authorization status

RNAiqua.setIDFAConsent(true);

Updated over 1 year ago Table of Contents

Integrate App Tracking Transparency Framework

Add Usage Description to Info.plist

Request Authorization to Track

Sending IDFA Based on Authorization Status



Push Notifications

https://docs.aiqua.appier.com/docs/push-notifications-for-react-native



AIQUA React Native Library supports sending push notifications in Android as well as iOS builds. To be able to send push notifications, complete the following integrations.

📘Note:Make sure you have already configured the initial setups required for Android and iOS. See here.

For Android

Required IntegrationInstructionsPush NotificationsFollow the steps in [Android] Push Notifications.Implementing Deep LinksFollow the steps in [Android] Implementing Deep Links.

For iOS

Required IntegrationInstructionsRegistering Push NotificationsFollow the steps in [iOS] Registering Push Notifications.Handling Push NotificationsFollow the steps in [iOS] Handling Push Notifications.Rich Push NotificationsFollow the steps in [iOS] Rich Push Notifications.Implementing Deep LinksFollow the steps for implementing iOS deep links.Updated over 1 year ago [iOS] App Tracking Transparency for React Native[Android] Push NotificationsDid this page help you?Table of Contents

For Android

For iOS



[Android] Push Notifications [0]

https://docs.aiqua.appier.com/docs/registering-push-notifications-react-native-android



There are three different ways to set up push notifications using the Appier SDK; select the method that suits your app's requirements (choose only one method):

Option A: Using the Appier SDK's built-in FirebaseMessagingService

Option B: Using a customized FirebaseMessagingService

Option C: Using React Native Firebase

📘NoteFor apps targeting API level 33 or higher: Your app's AndroidManifest.xml must include the POST_NOTIFICATIONS permission for devices running Android 13 or later to receive push notifications.

The Appier SDK directly handles all push notifications for Android devices. To enable push notification functionality:

Initialize the Appier SDK.

If you're using version 2.x.x of the Appier React Native SDK, apply the Google Services Gradle plugin in android/app/build.gradle by adding the following line:

apply plugin: "com.google.gms.google-services"

If you don't want to use the default FirebaseMessagingService in Appier SDK, we also support customizations on the native Android side. In short, you have to implement FirebaseMessagingService on your own and send the message to Appier Android SDK whenever a remote message is received in your FirebaseMessagingService.

Add the dependencies of Firebase Cloud Messaging Service and Appier Android SDK in android/app/build.gradle depending on the Appier React Native SDK version you're using.

dependencies {

// Appier React Native SDK v2.x.x

implementation 'com.appier:appier-android:8.0.1'

implementation 'com.google.firebase:firebase-messaging:23.0.0'

// Appier React Native SDK v1.x.x

implementation 'com.google.firebase:firebase-messaging:20.0.1'

implementation 'com.appier:appier-android:7.26.0'

}

If you're using version 2.x.x of the Appier React Native SDK, apply the Google Services Gradle plugin in android/app/build.gradle.

apply plugin: "com.google.gms.google-services"

Create your customized FirebaseMessagingService. Skip this step if you have already implemented FirebaseMessagingService in your project.



[Android] Push Notifications [1]

https://docs.aiqua.appier.com/docs/registering-push-notifications-react-native-android



To send the remote message to Appier Android SDK, add codes in your FirebaseMessagingService following this guide.

🚧Important

React Native Firebase is supported on Android in Appier SDK 1.6.0 and above.

The sample codes in this section only work for Android devices. The SDK will ignore the operations below if the device is iOS. To set up React Native Firebase on iOS, follow this guide.

Refer to React Native Firebase's official documentation to set up Firebase on React Native.

Set up Cloud Messaging according to the official guide. Make sure you have installed @react-native-firebase/app and @react-native-firebase/messaging in your project.

To listen to messages in the foreground, you have to implement the onMessage method inside your application code. When receiving a remote message in the onMessage method, send it to Appier SDK by calling RNAiqua.handleRemoteMessage(). Here's an example of how to add the codes in your App.js.

import React from 'react';

import messaging from '@react-native-firebase/messaging';

import RNAiqua from '@appier/react-native-sdk';

export default class App extends React.Component {

...

componentDidMount() {

messaging().onMessage(async remoteMessage => {

// When receiving a remote message, check if it's from AIQUA first.

if (remoteMessage.from && remoteMessage.data && remoteMessage.data.message) {

var json = JSON.parse(remoteMessage.data.message);

if (json.source === "QG") {

// If the message is from AIQUA, send it to Appier SDK by calling this API.

RNAiqua.handleRemoteMessage(remoteMessage.data.message);

}

}

});

...

}

...

}

To receive push when the application is in the background or quit state, you need to set up a background callback handler via the setBackgroundMessageHandler method in index.js. In this callback handler, send the message to Appier SDK by calling RNAiqua.handleRemoteMessage(). Here's an example of how to add the codes in your index.js.

...

import messaging from '@react-native-firebase/messaging';

import RNAiqua from '@appier/react-native-sdk';



[Android] Push Notifications [2]

https://docs.aiqua.appier.com/docs/registering-push-notifications-react-native-android



...

import messaging from '@react-native-firebase/messaging';

import RNAiqua from '@appier/react-native-sdk';

messaging().setBackgroundMessageHandler(async remoteMessage => {

// When receiving a remote message, check if it's from AIQUA first.

if (remoteMessage.from && remoteMessage.data && remoteMessage.data.message) {

var json = JSON.parse(remoteMessage.data.message);

if (json.source === "QG") {

// If the message is from AIQUA, send it to Appier SDK by calling this API.

RNAiqua.handleRemoteMessage(remoteMessage.data.message);

}

}

});

...

To handle notification clicks with onNotificationOpenedApp method, you need to set up logic in your Android MainActivity and connect the Intent from notification clicks to onNotificationOpenedApp via ReactNativeFirebaseEventEmitter. In order to determine if the Intent is coming from AIQUA campaigns, you need to set the key-value pair when creating the push campaign on AIQUA dashboard.

In the following example code, we will use the key-value pair source = aiqua.

import android.content.Intent;

import android.os.Bundle;

import android.util.Log;

import com.facebook.react.ReactActivity;

import com.facebook.react.ReactActivityDelegate;

import com.facebook.react.ReactRootView;

import com.facebook.react.bridge.Arguments;

import com.facebook.react.bridge.WritableMap;

import io.invertase.firebase.common.ReactNativeFirebaseEventEmitter;

import io.invertase.firebase.messaging.ReactNativeFirebaseMessagingSerializer;

public class MainActivity extends ReactActivity {

@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

processIntent(getIntent());

}

@Override

public void onNewIntent(Intent intent) {

super.onNewIntent(intent);

processIntent(intent);

}

private void processIntent(Intent intent) {

// Check if the Intent is coming from AIQUA via customized key-value pair.

if (intent != null && "aiqua".equals(intent.getStringExtra("source"))) {



[Android] Push Notifications [3]

https://docs.aiqua.appier.com/docs/registering-push-notifications-react-native-android



if (intent != null && "aiqua".equals(intent.getStringExtra("source"))) {

ReactNativeFirebaseEventEmitter emitter = ReactNativeFirebaseEventEmitter.getSharedInstance();

WritableMap extras = Arguments.fromBundle(intent.getExtras());

emitter.sendEvent(ReactNativeFirebaseMessagingSerializer.remoteMessageMapToEvent(extras, true));

}

}

...

}

With the above logic, ReactNativeFirebaseEventEmitter will pass { source: 'aiqua' } as remoteMessage to the onNotificationOpenedApp listener in the JavaScript layer.

...

import messaging from '@react-native-firebase/messaging';

import RNAiqua from '@appier/react-native-sdk';

messaging().onNotificationOpenedApp(remoteMessage => {

console.log(

'Notification caused app to open:',

remoteMessage,

);

if (remoteMessage && remoteMessage.source === 'aiqua') {

// Handle Android notification click here

}

...

});

...

For more details and usages, refer to the official page of React Native Firebase Cloud Messaging.

Updated about 1 month ago Table of Contents

Overview

Option A: Using the Appier SDK's built-in FirebaseMessagingService

Option B: Using a Customized FirebaseMessagingService

Option C: Using React Native Firebase



[iOS] Registering Push Notifications [0]

https://docs.aiqua.appier.com/docs/registering-push-notifications-react-native



To be able to send push notifications in iOS, you need to request permission from the user. If the user grants permission to receive push, a push notification token will be generated from the APNs or FCM servers and the token must be passed to the Appier server.

There are 4 steps required for registering push notifications. Step 4 is different depending on the push notification service provider you are using.

[Option A] Using APNs 

[Option B] Using Firebase Cloud Messaging: Firebase Native iOS SDK 

[Option C] Using Firebase Cloud Messaging: React Native Firebase 

If you are using Firebase Cloud Messaging, it is recommended to use Firebase Native iOS SDK.

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

#import 



// Add UNUserNotificationCenterDelegate to the class interface

@interface AppDelegate ()

@end



@implementation AppDelegate

...

@end

You need to prompt the users to grant permission for sending push notifications.

Include the code sample below within your app’s application:didFinishLaunchingWithOptions delegate method. They register for userNotificationSettings (for iOS 8 and iOS 9) or requestAuthorization (for iOS 10 and above). 

// Registering Push Notification 

if #available(iOS 10.0, *) {

let center = UNUserNotificationCenter.current()

center.delegate = self

center.requestAuthorization(options: [.badge, .carPlay, .alert, .sound]) { (granted, error) in



[iOS] Registering Push Notifications [1]

https://docs.aiqua.appier.com/docs/registering-push-notifications-react-native



center.delegate = self

center.requestAuthorization(options: [.badge, .carPlay, .alert, .sound]) { (granted, error) in

print("Granted: \(granted), Error: \(String(describing: error))")

}

} else {

// Fallback on earlier versions - iOS 8 & 9

let settings = UIUserNotificationSettings(types: [.alert, .badge, .sound], categories: nil)

UIApplication.shared.registerUserNotificationSettings(settings)

}

// Registering Push Notification

if (@available(iOS 10.0, *)) {

UNAuthorizationOptions options = (UNAuthorizationOptions) (UNAuthorizationOptionAlert | UNAuthorizationOptionBadge | UNAuthorizationOptionSound | UNAuthorizationOptionCarPlay);

UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];

center.delegate = self;

[center requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError *error){

NSLog(@"GRANTED: %i, Error: %@", granted, error);

}];

} else {

// Fallback on earlier versions - iOS 8 & 9

UIUserNotificationType types = UIUserNotificationTypeAlert | UIUserNotificationTypeSound |

UIUserNotificationTypeBadge;

UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:types categories:nil];

[[UIApplication sharedApplication] registerUserNotificationSettings:settings];

}

If the user grants your app permission to send push notifications, a push token will be generated by APNs or FCM . Follow the steps for one of the three options below to use APNs or FCM to pass the token to the Appier:

Option A: Using APNs

Option B: Using FCM with Firebase Native iOS SDK

Option C: Using FCM with React Native Firebase

If your app is using APNs, copy the following methods and paste then inside your AppDelegate class the push token to the Appier's server.

// add these delegate methods to your AppDelegate class

func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {

let QG = QGSdk.getSharedInstance()

print("My token is: \(deviceToken.description)")



[iOS] Registering Push Notifications [2]

https://docs.aiqua.appier.com/docs/registering-push-notifications-react-native



let QG = QGSdk.getSharedInstance()

print("My token is: \(deviceToken.description)")

QG.setToken(deviceToken as Data)

}

func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: Error) {

print("Failed to get token, error: \(error.localizedDescription)")

}

// add these delegate methods to your AppDelegate class

- (void)application:(UIApplication*)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData*)deviceToken

{

NSLog(@"My token is: %@", deviceToken);

[[QGSdk getSharedInstance] setToken:deviceToken];

}

- (void)application:(UIApplication*)application didFailToRegisterForRemoteNotificationsWithError:(NSError*)error

{

NSLog(@"Failed to get token, error: %@", error.localizedDescription);

}

📘Note:If you requested for a push token using registerForRemoteNotification before the Appier SDK is initialized, save the token and send it when you initialize the SDK.

If your app is integrated with Firebase, follow the steps for registering notifications for iOS apps using FCM.

🚧Important

Users can only receive push notifications in the background if you are using React Native Firebase. See https://rnfirebase.io/messaging/usage#message-handlers.

To integrate React Native Firebase, we recommended using React Native SDK 0.60.0 or later.

Complete the following setup steps as described in the React Native Firebase documentation:

Complete the steps described in Getting Started.

Under the Cloud Messaging section, complete the instructions provided in the following pages (Note: Skip for "iOS Notification Images" to prevent conflicts with AppierExtensionFramework):

Usage. Install the following module versions:

"@react-native-firebase/app": "^15.6.0"

"@react-native-firebase/messaging": "^15.6.0"

iOS Project Setup

iOS Permissions

(Optional) Notifications

(Optional) Server Integration

Pass the token to Appier. In your app's App.js file, call setFCMToken() in two locations:

import messaging from '@react-native-firebase/messaging';

// Call setFCMToken()



[iOS] Registering Push Notifications [3]

https://docs.aiqua.appier.com/docs/registering-push-notifications-react-native



import messaging from '@react-native-firebase/messaging';

// Call setFCMToken()

await messaging().registerDeviceForRemoteMessages();

const fcmToken = await messaging().getToken();

RNAiqua.setFCMToken(token);

...

// Call setFCMToken()

messaging().onTokenRefresh((token) => {

RNAiqua.setFCMToken(token);

});

At this checkpoint, make sure your app builds correctly and run the app on a physical iOS device.

When the app is launched, you should be prompted to subscribe to notifications.

Updated 8 months ago Table of Contents

1. Add relative frameworks

2. Including headers

3. Request permissions

4. Passing the push token to Appier's servers

Option A: Using APNs

Option B: Using FCM with Firebase Native iOS SDK

Option C: Using FCM with React Native Firebase

Checkpoint



[iOS] Adding Required Extensions [0]

https://docs.aiqua.appier.com/docs/rich-push-notifications-react-native



A rich push notification is a push notification that includes an image, video, GIF, audio, carousel, or slider. With the release of iOS 10, AppierFramework and AppierExtensionFramework were introduced to support rich push notifications and notification UI customization.

This guide will explain how to set up the Notification Service Extension and Notification Content Extension. These extensions are required for:

Sending rich push notifications (notifications using creative types such as banners, carousels, and sliders)

Tracking impression events for all push notifications, regardless of the creative type used

Use Appier React Native SDK 1.5 or later. Follow the migration steps to upgrade from version 1.4.

If you are using a new App Group ID, ensure that you are using Appier React Native SDK 1.5 or later, otherwise iOS users will be duplicated. 

Starting from Appier React Native SDK 1.5, AppierExtensionFramework is used in the main app target, the Notification Service Extension target, and the Notification Content Extension target.

❗️Caution: Using a New App Group IDEnsure that you're using the proper SDK version if you need to use a new App Group ID to avoid unwanted side effects.

The App Group ID will be used in your main app target as well as the two extension targets you'll create. The App Group ID must be the same ID used when you enabled the App Group.

Add a notification service extension target. Under to File > New > Target, select Notification Service Extension, then click Next.

For Product Name, enter "AppierNotificationServiceExtension" and click Finish.

After clicking Finish, you'll be prompted to activate the "AppierNotificationServiceExtension" scheme. Select Cancel. 

Add a notification content extension target. In Xcode, navigate to File > New > Target, select Notification Content Extension, and click Next.

For Product Name, enter "AppierNotificationContentExtension" and click Finish.

After clicking Finish, you'll be prompted to activate the "AppierNotificationContentExtension" scheme. Select Cancel.



[iOS] Adding Required Extensions [1]

https://docs.aiqua.appier.com/docs/rich-push-notifications-react-native



After clicking Finish, you'll be prompted to activate the "AppierNotificationContentExtension" scheme. Select Cancel. 

Choose an installation method depending on your project settings:

Option 1: Swift Package Manager

Option 2: Installing with CocoaPods

Option 3: Installing with React Native Firebase 

Option 4: Manual Installation (Not Recommended)

No additional steps required; continue to the next step.

Add the following lines to your project's Podfile: 

target 'PROJECT_TARGET' do

...

pod 'AppierExtensionFramework', ''

# other pods

en

# Add the following lines for service and content extensions

target 'AppierNotificationServiceExtension' do

pod 'AppierExtensionFramework', ''

end

target 'AppierNotificationContentExtension' do

pod 'AppierExtensionFramework', ''

end

Ensure that the target names in the Podfile match the product names you used when creating the extensions (AppierNotificationServiceExtension and AppierNotificationContentExtension).

After adding the extensions to the Podfile, run the following commands in the project directory to install the extensions:

$ pod repo update

$ pod install

📘Upgrading the React Native SDKWhen upgrading the React Native SDK, check the relevant release notes to see whether the bridged iOS SDK version was updated. If the bridged iOS SDK version was updated, you'll also need to update the version of AppierExtensionFramework in your Podfile to match the iOS SDK version.

Add the following lines to your project's Podfile:

target 'PROJECT_TARGET' do

...

pod 'AppierExtensionFramework', ''

# other pods

end

target 'ServiceExtension' do

use_frameworks! :linkage => :static

pod 'AppierExtensionFramework', ''

end

target 'ContentExtension' do

use_frameworks! :linkage => :static

pod 'AppierExtensionFramework', ''

end



[iOS] Adding Required Extensions [2]

https://docs.aiqua.appier.com/docs/rich-push-notifications-react-native



use_frameworks! :linkage => :static

pod 'AppierExtensionFramework', ''

end

After adding the extensions to the Podfile, run the following commands in the project directory to install the extensions:

$ pod repo update

$ pod install

❗️WarningDon't follow the manual installation steps if your project uses CocoaPods or Swift Package Manager (SPM) for package management.

Download the Appier iOS SDK.

Add the AppierExtension.xcframework folder you downloaded to the main app target. Under the Build Phases tab, expand Link Binary With Libraries, and click +. Go to Add Other > Add Files and select the AppierExtension.xcframework folder.

Add the AppierExtension.xcframework folder to the main app target.

Add the AppierExtension.xcframework folder to the AppierNotificationServiceExtension and AppierNotificationContentExtension targets. 

Add the AppierExtension.xcframework folder to the AppierNotificationServiceExtension and AppierNotificationContentExtension targets.

In the main app target, go to General > Frameworks and Libraries, select AppierExtension.xcframework, and set the Embed column to Embed & Sign.

In the AppierNotificationServiceExtension and AppierNotificationContentExtension targets, go to General > Frameworks and Libraries, then set the Embed columns of AppierNotificationServiceExtension.xcframework and AppierNotificationContentExtension.xcframework to Do Not Embed.

In the AppierNotificationServiceExtension folder, open the NotificationService.* files and replace the contents of the entire file with the following:

For Swift: NotificationService.swift

import AppierExtension

class NotificationService: QGNotificationService {

override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {

super.didReceive(request, withContentHandler: contentHandler)

}



override func serviceExtensionTimeWillExpire() {

super.serviceExtensionTimeWillExpire()

}

}



[iOS] Adding Required Extensions [3]

https://docs.aiqua.appier.com/docs/rich-push-notifications-react-native



}



override func serviceExtensionTimeWillExpire() {

super.serviceExtensionTimeWillExpire()

}

}

For Objective-C: NotificationService.h and NotificationService.m

#import 

#import 



@interface NotificationService : QGNotificationService

@end

#import "NotificationService.h"



@implementation NotificationService



- (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {

[super didReceiveNotificationRequest:request withContentHandler:contentHandler];

}

- (void)serviceExtensionTimeWillExpire {

[super serviceExtensionTimeWillExpire];

}

@end

Go to the project navigator and select the AppierNotificationServiceExtension target.

Navigate to Signing & Capabilities > App Groups, and then add the app group using your App Group ID.

In the project navigator, select the AppierNotificationServiceExtension target. Under the General tab, change the deployment target of your content extension to iOS 10.0.

Find the Info.plist file in the AppierNotificationServiceExtension folder. Add the following row under Information Property List:

KeyTypeValueAppierAppGroupStringYour App Group ID

In the AppierNotificationContentExtension folder, open the following files and replace the contents of the entire file with the following:

For Swift: NotificationViewController.swift

import UIKit

import AppierExtension

class NotificationViewController: QGNotificationContentViewController {

override func viewDidLoad() {

super.viewDidLoad()

// Do any required interface initialization here.

}

}

For Objective-C: NotificationViewController.h and NotificationViewController.m 

#import 

#import 



@interface NotificationViewController : QGNotificationContentViewController

@end

#import "NotificationViewController.h"



@implementation NotificationViewController



- (void)viewDidLoad {

[super viewDidLoad];

}

@end



[iOS] Adding Required Extensions [4]

https://docs.aiqua.appier.com/docs/rich-push-notifications-react-native



@implementation NotificationViewController



- (void)viewDidLoad {

[super viewDidLoad];

}

@end

Go to the project navigator and select the AppierNotificationContentExtension target.

Navigate to Signing & Capabilities > App Groups, and then add the app group using your App Group ID.

In the project navigator, select the AppierNotificationContentExtension target. Under the General tab, change the deployment target of your content extension to iOS 10.0. 

Find the Info.plist file in the AppierNotificationContentExtension folder. Under NSExtension > NSExtensionAttributes, update UNNotificationExtensionCategory and add UNNotificationExtensionDefaultContentHidden and UNNotificationExtensionUserInteractionEnabled with the following values:

KeyTypeValueUNNotificationExtensionDefaultContentHiddenBooleanYES or 1UNNotificationExtensionUserInteractionEnabledBooleanYES or 1UNNotificationExtensionCategoryStringQGCAROUSEL

Add the following row under Information Property List:

KeyTypeValueAppierAppGroupStringYour App Group ID

Info.plist for AppierNotificationContentExtension should look like this:

In MainInterface.storyboard, remove the default Label.

In MainInterface.storyboard, select View and change the Background to System Grouped Background Color.

Build the target and follow the instructions in Sending Test Notification for iOS to verify that the rich push notification works as expected.

See the troubleshooting steps below if you encounter issues sending notifications.

Ensure that the deployment target of AppierNotificationServiceExtension and AppierNotificationContentExtension is set to iOS 10.0.

Remove -ObjC/$(inherited) if it exists in the build settings of the AppierNotificationServiceExtension and AppierNotificationContentExtension.

Ensure that the same App Group ID is used in all three targets.

Under the AppierNotificationServiceExtension and AppierNotificationContentExtension targets, go to Build Phases > Compile Sources to make sure the following files are correctly configured. If not, click + to add the files.



[iOS] Adding Required Extensions [5]

https://docs.aiqua.appier.com/docs/rich-push-notifications-react-native



AppierNotificationServiceExtension Compile Sources

AppierNotificationContentExtension Compile SourcesUpdated about 1 year ago Table of Contents

SDK version requirement

Notes for Earlier Appier SDK Versions

1. Save your app group ID

2. Add the extensions

3. Install the extensions

Swift Package Manager

Installing with CocoaPods

Installing with React Native Firebase

Manual installation (Not recommended)

4. Set up the Notification Service Extension

5. Set up the Notification Content Extension

Send a test push notification

Troubleshooting



Implementing Deep Links

https://docs.aiqua.appier.com/docs/react-native-implementing-deep-links



The Appier React Native SDK supports passing deep links to your app. Note that the React Native SDK doesn't resolve or handle deep links—the links are passed directly to the app for handling.

Refer to the instructions below to start using deep links with your app:

Android deep links

iOS deep links

Follow the deep link implementation instructions for Android.

iOS deep links can be implemented using one of the following methods:

Option 1: Using a custom URL scheme

Option 2: Using universal links

Follow the deep link implementation instructions for iOS.

Call setUniversalLinkDomains() after RNAiqua.configure():

RNAiqua.setUniversalLinkDomains(["YOUR_DOMAIN_1", "YOUR_DOMAIN_2"])

🚧ImportantTo prevent unexpected issues, don't call setUniversalLinkDomains() in the native iOS code.Updated over 1 year ago Table of Contents

Overview

Android deep links

iOS deep links

Option 1: Using a custom URL scheme

Option 2: Using universal links



Logging Custom User Data for React Native

https://docs.aiqua.appier.com/docs/event-and-profile-logging-for-react-native



👍Tip:Before you start, refer to the guidelines for logging Custom Events and Attributes.

Event PropertyDescriptioneventNameEvent nameparametersA dictionary of all the parameters for the eventvalueToSumMonetary value associated to the eventcurrencyCurrency code of the value to sum

RNAiqua.logEvent(eventName)

RNAiqua.logEvent(eventName, parameters)

RNAiqua.logEvent(eventName, valueToSum)

RNAiqua.logEvent(eventName, valueToSum, currency)

RNAiqua.logEvent(eventName, parameters, valueToSum)

RNAiqua.logEvent(eventName, parameters, valueToSum, currency)

Refer to the following sample values when logging user attributes.

RNAiqua.setUserId('USER_ID')

RNAiqua.setName('NAME')

RNAiqua.setFirstName('FIRST_NAME')

RNAiqua.setLastName('LAST_NAME')

RNAiqua.setCity('CITY')

RNAiqua.setEmail('user@mail.xxx')

RNAiqua.setDayOfBirth(1)

RNAiqua.setMonthOfBirth(7)

RNAiqua.setYearOfBirth(1997)

RNAiqua.setPhoneNumber('0912345678') 

RNAiqua.setCustomKey('KEY_STR', 'strval')

RNAiqua.setCustomKey('KEY_BOOL', true)

Follow the steps below to check if user events and attributes are tracked properly.

Launch your app and complete the action that sends the event or attribute.

On AIQUA dashboard, click your account name in the lower-left corner:

Select Recent Activity to check if users events behaviors are being logged correctly.

Select Recent Users to check if user attributes are being logged correctly.

Select Android, iOS Production, or iOS Development based on your platform. You should see the user event or attribute after a few minutes.

Updated over 1 year ago Table of Contents

Logging User Events

Logging User Attributes

Checkpoint



React Native SDK Web View Support [0]

https://docs.aiqua.appier.com/docs/react-native-webview-support



📘Note

Using Recommendation 2.0 in web pages using web views requires Appier React Native SDK 1.5.0 or later.

Filtering out purchased products by user_id from recommendation 2.0 results when using web views requires Appier React Native SDK 1.6.0 or later.

Recommendation 1.0 is not supported in web views.

The Appier React Native SDK provides the RNAiquaWebView class, which uses react-native-webview as a dependency and inherits all the properties and methods provided by the react-native-webview library. 

RNAiquaWebView provides the following functions:

Display web content as part of your app.

Track custom events and attributes from the web pages via WebView.

Make sure you have integrated Appier Web SDK into your web pages.

All custom events and attribute parameters logged in the web page can be tracked natively using the Appier SDK. 

Default events and attributes collected by Appier Web SDK (e.g. page_viewed, visited) will NOT be tracked since web SDK is initialized in app SDK mode.

Follow the React Native WebView Getting Started Guide for instructions on installing the latest react-native-webview version.

The Appier SDK leverages the React Native WebView component. For details on the available web view methods, refer to the React Native WebView API Reference. 

The following code samples demonstrates how to reload a web view using the reload() method. Note that in SDK versions 1.9.1 and earlier, an additional webref call is required to reference React Native WebView API methods.

import React, { useRef } from 'react';

import { RNAiquaWebView } from '@appier/react-native-sdk';

const MyWeb = () => {

const webViewRef = useRef(null);



const callWebViewMethods = () => {

// React Native SDK 1.9.1 and earlier, one more call of `webref` is necessary.

webViewRef.current?.webref?.reload();

// React Native SDK 1.10.0 or later

webViewRef.current?.reload();

};

return (

ref={webViewRef}

source={{uri: 'https://www.example.com'}}

style={{marginTop: 20}}

/>

);

}



React Native SDK Web View Support [1]

https://docs.aiqua.appier.com/docs/react-native-webview-support



};

return (

ref={webViewRef}

source={{uri: 'https://www.example.com'}}

style={{marginTop: 20}}

/>

);

}

🚧ImportantiOS uses WebKit by default and it can't be changed.Updated 4 months ago Table of Contents

Overview

Installation

Usage



Other Important Methods [0]

https://docs.aiqua.appier.com/docs/react-native-sdk-methods



Some additional useful and important methods are listed here. Use these to call functions in the React Native SDK.

Method DescriptionRNAiqua.setInAppCampaignVisible(true)• Passing true Allows in-app campaigns to be displayed.

• Passing false Closes the in-app campaign that's currently being displayed and prevents future in-app campaigns from displaying.RNAiqua.removeInAppCampaign()Closes the in-app campaign that's currently being displayed.RNAiqua.disableInAppCampaigns(true)Disable in-app pop-up campaigns.RNAiqua.hideInAppCampaigns()Clear all the foreground in-app pop-ups.RNAiqua.flush()By default, queued data is flushed to the AIQUA servers every 15 seconds--the default for flushInterval. Call this method manually if you want to force a flush at a particular moment.RNAiqua.setAttributionWindow(7200)Sets the view-through attribution window. The default is one hour, i.e. 3600 seconds. Value should be passed in seconds.

Starting from React Native SDK 1.5, if set to 0, the attribution window will fall back to its default value.RNAiqua.setClickAttributionWindow(43200)Sets the click-through attribution window. The default is 24 hours, i.e. 86,400 seconds. Value should be passed in seconds.

Starting from React Native SDK 1.5, if set to 0, the attribution window will fall back to its default value.RNAiqua.renewUserId()Deprecated starting from React Native SDK 1.10.0.



Other Important Methods [1]

https://docs.aiqua.appier.com/docs/react-native-sdk-methods



Creates a new AIQUA userId and clean all local data related to the previous userId. When the process is completed, return a promise with no return values.RNAiqua.enableStoredNotification()Enables the local storage of push notifications.RNAiqua.setMaxNumStoredNotifications(60)Sets the maximum number of push notifications that can be stored locally.RNAiqua.getStoredNotifications( ret => { //ret is the stored notifications } )Retrieves locally-stored push notification data. Return a promise with an array of the stored notifications.RNAiqua.deleteStoredNotification(5)Removes a specific locally stored push notification with its index.RNAiqua.deleteStoredNotifications()Removes all locally stored push notification data.RNAiqua.getAppierId()Returns the Appier ID.RNAiqua.renewAppierId()Regenerate the ID.RNAiqua.isAppierPush("string")Checks if the entered message is an AIQUA message.

The following methods are only available for iOS.

Method DescriptionRNAiqua.setUniversalLinkDomains( ["first.domain.com", "second.domain.com”])Use this method to set the Associated Domains for Universal Links.RNAiqua.setIDFAConsent(true)To use this method, you need to integrate the App Tracking Transparency framework first.

Refer to the App Tracking Transparency document for details.RNAiqua.disableInAppCampaigns(false)Re-enable in-app pop-up campaigns.

The following methods are only available for Android.

Method DescriptionRNAiqua.setUtmSource('UTMSOURCE')RNAiqua.setUtmMedium('UTMMEDIUM')RNAiqua.setUtmTerm('UTMTERM')RNAiqua.setUtmContent('UTMCONTENT')RNAiqua.setUtmCampaign('UTMCAMPAIGN')Apart from default user profile parameters, you can also log the UTM source through which the user installed the app via these methods.RNAiqua.isQGMessage( 'SOME_MESSAGE', ret => { //ret is the result--true or false } )Deprecated starting from React Native SDK 1.10.0.

Checks if the entered message is an AIQUA message.RNAiqua.enablePushBooster()Enables push booster.RNAiqua.disableLocationTracking()Disables location tracking.



Other Important Methods [2]

https://docs.aiqua.appier.com/docs/react-native-sdk-methods



Updated 5 months ago Table of Contents

Common methods

iOS methods

Android methods



Flutter SDK Integration Overview

https://docs.aiqua.appier.com/docs/flutter-sdk-integration-overview



Integrate your app with Appier Flutter SDK to take advantage of features such as sending push notifications, logging custom user data, and delivering in-app campaigns. This page summarizes the setup steps required to begin using the Appier Flutter SDK and all the features it supports.

We recommend using the latest Appier Flutter SDK for continual updates and feature support. See the Flutter SDK Release Notes for details about the latest releases.

The Appier Flutter SDK is built with the following environment and dependencies:

environment:

sdk: ">=2.17.0 <4.0.0"

flutter: ">=3.0.0"

dependencies:

flutter:

sdk: flutter

flutter_inappwebview: ^6.0.0

environment:

sdk: ">=2.12.0 <3.0.0"

flutter: ">=1.20.0"

dependencies:

flutter:

sdk: flutter

flutter_inappwebview: ^5.0.5

Any Appier Flutter SDK version with alpha, beta, rc, in the version number are testing versions or release candidates. These pre-release versions may be unstable and are intended for testing purposes.

Integrating your app with Appier Flutter SDK allows you to utilize the following features:

Send push notifications

Send in-app campaigns

Track user events and attributes

You need to complete the following steps.

Installing the SDK via pub.dev 

Required Setup for Native Android and iOS 

Initializing the SDK via Flutter 

Push Notifications 

Logging Custom User Data for Flutter

Updated 7 months ago Table of Contents

Overview

Latest Appier SDK version

Dependencies

Pre-release versions (testing only)

Integration overview



Development Flutter SDK Versions

https://docs.aiqua.appier.com/docs/flutter-sdk-release-notes



Updated the bridged Appier Android SDK version from 8.2.1 to 8.2.4. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier Android SDK version from 7.26.0 to 8.2.1. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.34.0 to 8.2.2. See the iOS SDK release notes for a detailed summary of changes.

Upgraded the InAppWebView plugin to version 6.1.5.

The Appier ID (userId) is incorrectly regenerated on the first app launch (either in the foreground or background) after upgrading to this SDK version. These regenerated Appier IDs were treated as new users, impacting related metrics and segments.

Updated 15 days ago Table of Contents

v3.1.1 - March 19, 2025

v3.1.0 - February 21, 2025 (Deprecated)



Installing the SDK via pub.dev

https://docs.aiqua.appier.com/docs/installing-the-sdk-via-flutter



Installing the SDK via pub.devFirst, add dependency in Pubspec.yaml:

dependencies:

...

appier_flutter: 3.1.1

And then pull the package by running flutter pub get:

Updated over 1 year ago Flutter SDK Integration OverviewTroubleshooting Dependency Conflicts



Troubleshooting Dependency Conflicts [0]

https://docs.aiqua.appier.com/docs/flutter-troubleshooting-dependency-conflicts



If you're using one of the libraries listed below, follow the instructions provided on this page to resolve dependency conflicts with the Appier SDK:

Google Analytics API for Firebase (Android)

Firebase Messaging (Android)

Firebase BoM (Android)

👍Android SDK dependenciesRefer to the Android SDK's dependencies to ensure that they don't conflict with your app's other dependencies.

The Google Analytics API for Firebase conflicts with the Appier Android SDK's com.google.android.gms:play-services-analytics dependency.

If your project uses the Google Analytics API, append the following configuration to android/app/build.gradle to resolve this dependency conflict:

configurations.all { conf ->

conf.dependencies.all { dep ->

if (dep.name == 'appier_flutter') {

dep.exclude group: 'com.google.android.gms'

dependencies {

implementation 'com.google.android.gms:play-services-ads-identifier:16.0.0'

}

}

}

}

The configuration above includes the play-services-ads-identifier:16.0.0 dependency required by the Appier Android SDK and excludes com.google.android.gms.

The Appier Android SDK uses firebase-messaging version 17.3.4. If your app uses a different version, update android/app/build.gradle to exclude the version used by the Appier SDK, then include the version that your app uses. Additionally, if you are using version 22.0.0 or later, you'll need to include the com.google.firebase:firebase-iid:20.0.1 dependency as well.

To use a different version of firebase-messaging in your app, append the following to configuration to android/app/build.gradle:

configurations.all { conf ->

conf.dependencies.all { dep ->

if (dep.name == 'appier_flutter') {

dep.exclude group: 'com.google.firebase'

dependencies {

implementation 'com.google.firebase:firebase-messaging:'

// If you're using firebase-messaging version 22.0.0+, add this line as well. 

implementation 'com.google.firebase:firebase-iid:20.0.1'

}

}

}

}



Troubleshooting Dependency Conflicts [1]

https://docs.aiqua.appier.com/docs/flutter-troubleshooting-dependency-conflicts



implementation 'com.google.firebase:firebase-iid:20.0.1'

}

}

}

}

If you're using firebase-bom version 8.0.0 or later, you'll need to exclude the Appier Android SDK's com.google.firebase:firebase-messaging:17.3.4 dependency and include the com.google.firebase:firebase-iid:20.0.1 dependency.

To resolve this dependency conflict, append the following configuration to android/app/build.gradle:

configurations.all { conf ->

conf.dependencies.all { dep ->

if (dep.name == 'appier_flutter') {

dep.exclude group: 'com.google.firebase'

dependencies {

implementation platform('com.google.firebase:firebase-bom:')

implementation 'com.google.firebase:firebase-iid:20.0.1'

}

}

}

}

Updated 9 months ago Table of Contents

Google Analytics API for Firebase (Android)

Firebase Messaging (Android)

Firebase BoM (Android)



Required Setup for Native Android and iOS

https://docs.aiqua.appier.com/docs/initial-setup-for-native-android-and-ios-for-flutter



Complete the following required setup for each mobile platform:

Required setup for Android 

Required setup for iOS 

Set up the Firebase messaging service in your sub-project

Register your App with AIQUA

If your app is using Appier Flutter SDK 3.1.0 or later, update your Android Application class, Gradle file, and manifest file.

In your Android Application class, add the following:

class MyApplication: Application() {

override fun onCreate() {

Appier.create(this)

super.onCreate()

}

}

public class MyApplication extends Application {

@Override

public void onCreate() {

Appier.create(this);

super.onCreate();

}

}

In your Gradle file, add the following:

dependencies {

...

implementation 'com.appier:appier-android:8.2.1'

...

}

In your manifest file, add the following:

android:label="@string/app_name"

android:name=".MyApplication"

android:icon="@mipmap/ic_launcher">

The Gradle build may fail if there is version mismatch between the Appier SDK's dependencies and your app's dependency. To resolve such dependency conflicts, refer to Troubleshooting Dependency Conflicts.

🚧ImportantRemember to add google-services.json into the app module. To do this, you'll need to download google-services.json from your Firebase project.

Some initial setup is required inside the native part of iOS before you can proceed to the SDK usage:

Configure iOS push credentials 

Enable capabilities for your iOS project

Updated about 2 months ago Table of Contents

Overview

Required setup for Android

Gradle dependency conflict resolution

Required setup for iOS



Initializing the SDK via Flutter

https://docs.aiqua.appier.com/docs/initializing-the-sdk-via-flutter



To initialize the Android or iOS SDK via Flutter, refer to the following procedures.

You need to import the Appier SDK in main.dart:

import 'package:appier_flutter/appier_flutter.dart';

The SDK should be configured before using any methods. Initialize the SDK in the initState() of main app state using the following:

appId - This is your app ID. It is inside the account settings in the dashboard.

senderId - This is your own FCM sender ID for Android. (Optional)

appGroup - This is your iOS app group. 

isDev - This is your iOS app environment. Set this parameter to true for development build, false for production build. (Optional)

@override

void initState() {

super.initState();

AppierFlutter.configure(

'',

senderId: '', // android sender id - optional

appGroup: '',

isDev: true // ios dev or prod - default `false` - optional

);

}

If you leave out the optional parameters, the following default settings will be used:

senderId - By default, AIQUA's sender ID will be used for FCM.

isDev - For iOS, this defaults to false for the production build.

@override

void initState() {

super.initState();

AppierFlutter.configure(

'',

appGroup: '',

);

}

Updated over 1 year ago Table of Contents

Importing the Appier SDK



Flutter User Data Permission Controls [0]

https://docs.aiqua.appier.com/docs/flutter-user-data-permission-controls



📘Required SDK versionUser data permissions controls are only available on Flutter SDK 2.5.0 or later. See known issues in iOS here.

To allow your app to comply with data privacy policies and regulations, the Appier Flutter SDK allows you to manage user data permissions for the following types of data:

Google Advertising ID (AAID): Collection is enabled by default.

Identifier for Advertising (IDFA): Collection is disabled by default starting from Flutter SDK 2.6.0 (iOS SDK 7.32.0). In earlier SDK versions, IDFA collection is enabled by default.

Location data: Collection is disabled by default.

You can enable or disable collection for this data at any point in your app's lifecycle, even before the Appier SDK is initialized, and the changes will be effective immediately. For example, you may want to update user data collection settings in the following scenarios:

After the app is launched

After a user has responded to a data collection consent prompt

After regenerating the user's Appier ID

After a user logs in or logs out of their account

📘Note

Flutter SDK 2.6.0 or later: The Appier SDK automatically collects the device's AAID upon initialization by default.

Flutter SDK 2.5.1 and earlier: The Appier SDK automatically collects the device's AAID and IDFA upon initialization by default.

If you want to avoid this scenario, we strongly recommend disabling AAID/IDFA collection before initializing the Appier SDK.

The DataTrackingConfig object contains the SDK's current data permissions settings. The default settings are as follows:

class DataTrackingConfig {

bool collectLocation = false; // Location data collection disabled by default

bool collectAaid = true; // AAID collection enabled by default 

bool collectIdfa = false; // IDFA collection disabled by default

}

Use getDataTrackingConfig() to retrieve the current data permission settings.

final currentConfig = await AppierFlutter.getDataTrackingConfig();

// currentConfig contains all of the user data permission settings



Flutter User Data Permission Controls [1]

https://docs.aiqua.appier.com/docs/flutter-user-data-permission-controls



// currentConfig contains all of the user data permission settings

final currentIdfaConfig = currentConfig.collectIdfa;

final currentAaidConfig = currentConfig.collectAaid;

final currentLocationConfig = currentConfig.collectLocation;

To set all data permissions simultaneously, instantiate a DataTrackingConfig instance and pass it into setDataTrackingConfig().

// Instantiate a new DataTrackingConfig object with custom settings

final newConfig = DataTrackingConfig(collectLocation: true, collectAaid: true, collectIdfa: true);

// Modify individual settings if needed

newConfig.collectLocation = false;

// Apply the custom data permission settings

await AppierFlutter.setDataTrackingConfig(newConfig);

Updated 12 months ago Table of Contents

Overview

DataTrackingConfig object

Retrieving data permissions settings

Setting data permission settings

Setting data permission settings



Logging Custom User Data for Flutter [0]

https://docs.aiqua.appier.com/docs/event-and-profile-logging-for-flutter



👍See Custom Events and Attributes for detailed guidelines on defining and logging custom data.

Custom user data consists of free-form attributes and events that you can define depending on your business needs. Custom data isn't collected by the Appier SDK by default; instead, these custom events and attributes must be manually logged using the SDK logging methods as described below.

The Flutter SDK provides the following built-in methods for logging custom user attributes:

Future setUserId(String userId)

Future setName(String name)

Future setFirstName(String firstName)

Future setLastName(String lastName)

Future setCity(String city)

Future setEmail(String email)

Future setPhoneNumber(String phoneNo)

Future setDayOfBirth(int day)

Future setMonthOfBirth(int month)

Future setYearOfBirth(int year)

Use the method corresponding to the attribute you want to log. For example:

To log the user's name attribute, call setName()

To log the user's email attribute, call setEmail()

To log the user's year of birth attribute, call setYearOfBirth()

AppierFlutter.setName('NAME')

AppierFlutter.setEmail('user@example.com')

AppierFlutter.setYearOfBirth(1997)

In addition to using the built-in methods, you can also specify which type of custom data to log by using setCustomKey() and specifying a value for key, where key is the custom attribute you want to log:

Future setCustomKey(String key, dynamic value)

In the following example, setCustomKey() is used to set the user's current rating:

// Sets the value of the `rating` attribute to 5

AppierFlutter.setCustomKey('rating', 5);

📘NoteSetting an attribute to null may result in unexpected segmentation behavior.

To clear the value of a user attribute with setCustomKey(), log a null value.

// Clears the user's `rating` attribute by logging a null value

AppierFlutter.setCustomKey('rating', null);

Events can be tracked with logEvent(). eventName is the only required parameter; all other parameters are optional.



Logging Custom User Data for Flutter [1]

https://docs.aiqua.appier.com/docs/event-and-profile-logging-for-flutter



Events can be tracked with logEvent(). eventName is the only required parameter; all other parameters are optional.

Future logEvent(String eventName, {Map? parameters, double? vts, String? vtsCurr})

ParameterTypeDescriptioneventNameStringRequired. Event nameparametersMapOptional. Parameters for the eventvtsdoubleOptional. Monetary value associated to the eventvtsCurrStringOptional. Currency code of the value to sum

Include vts when logging an event to track the monetary value associated with the event (e.g. the total conversion value associated with a checkout_completed event), and log vtsCurr to specify an ISO 4217 currency code.

The following example logs a product_viewed event and includes metadata such as name, image_url, and category, as well as a vts of "100" and a vtsCurr of "USD", meaning that the monetary value associated with this event is $100 USD.

AppierFlutter.logEvent(

"product_viewed",

parameters: {

"product_id": "E0238", 

"product_name": "Brand A Shoes",

"produdt_image_url": "https://www.example.com",

"category_name": "Fashion"

},

vts: 100,

vtsCurr: "USD"

)

Verify that user events and attributes are being properly tracked by following the steps listed below.

Launch your app and complete the action that logs the event or attribute.

Go to the AIQUA dashboard and click your account name in the lower-left corner.

Select Recent Activity to check if user events are being logged correctly.

Select Recent Users to check if user attributes are being logged correctly.

Select Android, iOS Production, or iOS Development, depending on which platform you are using. You should see the user event or attribute after a few minutes.

Updated over 1 year ago Table of Contents

Overview

Logging custom attributes

Using built-in methods

Using custom keys

Logging custom events

vts and vtsCurr

Event logging example

Checkpoint



Push Notifications

https://docs.aiqua.appier.com/docs/push-notifications-for-flutter



There are two ways to implement push notifications in your Flutter app. 

Option 1: Native setup

Option 2: Using the Firebase Messaging plugin for Flutter

The Appier SDK supports the firebase_messaging plugin for push notifications; this push notification setup method works for both Android and iOS platforms.

Updated over 1 year ago Logging Custom User Data for FlutterNative Push SetupDid this page help you?



Native Push Setup

https://docs.aiqua.appier.com/docs/flutter-push-native-setup



Android

The Appier SDK will automatically handles push notifications for Android apps. No additional setup is required.

If you have special requirements such as requiring the use of multiple Firebase Cloud Messaging (FCM) services, using custom FCM services, or your want to disable push notifications from AIQUA, you can customize your own FCM service, customize the native FirebaseMessagingService class.

iOS

Prerequisites

Before configuring push notifications for iOS, complete the following: 

Configure iOS credentials

Enable capabilities

Required steps

Complete the following steps to send push notifications:

Complete steps 1-3 and step 4A in Registering for Push Notifications

Handle push notifications

Configure rich push notifications

Implement deep links

Apps using Firebase Cloud Messaging

For Flutter apps using FCM to send push notifications, developers should set the delegate of UNUserNotificationCenter for iOS 10 or later. For more details, see Registering for Push Notifications.Updated 9 months ago Push NotificationsUsing the Firebase Messaging PluginDid this page help you?Table of Contents

Android

iOS

Prerequisites

Required steps

Apps using Firebase Cloud Messaging



Using the Firebase Messaging Plugin [0]

https://docs.aiqua.appier.com/docs/flutter-using-the-firebase-messaging-plugin



The Appier SDK supports the firebase_messaging plugin to enable push notifications for both the Android and iOS platforms. For more information about the firebase_messaging plugin, see Flutter’s Cloud Messaging docs.

Complete the prerequisites.

Follow the push setup steps for Android and iOS.

Before proceeding with the push notification setup, complete the following steps in your Flutter project:

Add Firebase to your Flutter app. Complete the instructions for both Android and iOS.

Install the firebase_messaging plugin.

Complete the steps to register your Android app with AIQUA.

Follow the instructions in the Flutter guides listed below to allow your app to handle incoming messages:

Handling foreground messages

Handling background messages

Define a function for handling both background and foreground messages:

/// This handler can handle normal and silent pushes.

Future _handleFcmMessage(RemoteMessage message) async {

final from = message.from;

final data = message.data;

final dataString = jsonEncode(data);

final isAppierPush = await AppierFlutter.isAppierPush(dataString);

if (from != null && isAppierPush) {

await AppierFlutter.handleRemoteMessage(dataString);

}

}

📘NoteThis function was changed in Flutter SDK 2.5.0 to support geofencing and silent push notifications. If you have set up push notifications with Firebase Messaging Plugin before Flutter SDK 2.5.0 and would like to use these features, please reconfigure this step.

Connect foreground messages to the handler function:

FirebaseMessaging.onMessage.listen((message) {

...

_handleFcmMessage(message);

...

});

Connect background messages to the handler function:

Future _firebaseMessagingBackgroundHandler(RemoteMessage message) async {

...

await _handleFcmMessage(message);

...

}

...

FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

...

Send a test push campaign to verify that your push notification implementation is correct.



Using the Firebase Messaging Plugin [1]

https://docs.aiqua.appier.com/docs/flutter-using-the-firebase-messaging-plugin



...

Send a test push campaign to verify that your push notification implementation is correct.

Follow the instructions listed in Configuring Push Credentials to generate APNs credentials. 

Get the FCM token by calling FirebaseMessaging.instance.getToken(), then provide it to Appier SDK using setFcmToken():

final token = await FirebaseMessaging.instance.getToken();

if (token != null) {

await AppierFlutter.setFcmToken(token);

}

Follow the Flutter guides listed below request push permission and enable foreground notifications:

Requesting push permission for iOS

Enabling foreground notifications for iOS

Follow this Flutter guide to enable the "Push Notifications" and "Background Modes" capabilities in Xcode.

Open your native iOS Xcode project workspace by navigating to your project project directory and running the following command:

open ios/Runner.xcworkspace

Find your AppDelegate.swift file. The original AppDelegate.swift generated by flutter will look like this:

import UIKit

import Flutter

@UIApplicationMain

@objc class AppDelegate: FlutterAppDelegate {

override func application(

_ application: UIApplication,

didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?

) -> Bool {

GeneratedPluginRegistrant.register(with: self)

return super.application(application, didFinishLaunchingWithOptions: launchOptions)

}

}

First, add import Appier under import Flutter and UNUserNotificationCenter.current().delegate = self under GeneratedPluginRegistrant.register(with: self):

import UIKit

import Flutter

import Appier

@UIApplicationMain

@objc class AppDelegate: FlutterAppDelegate {

override func application(

_ application: UIApplication,

didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?

) -> Bool {

GeneratedPluginRegistrant.register(with: self)

UNUserNotificationCenter.current().delegate = self

return super.application(application, didFinishLaunchingWithOptions: launchOptions)

}

}

Next, override these three methods in the AppDelegate:



Using the Firebase Messaging Plugin [2]

https://docs.aiqua.appier.com/docs/flutter-using-the-firebase-messaging-plugin



}

}

Next, override these three methods in the AppDelegate:

application(_:didReceiveRemoteNotification:fetchCompletionHandler:)

userNotificationCenter(_:didReceive:withCompletionHandler)

userNotificationCenter(_:willPresent:withCompletionHandler:)

@objc class AppDelegate: FlutterAppDelegate {

...

override func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any], fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {

QGSdk.getSharedInstance().application(application, didReceiveRemoteNotification: userInfo)

super.application(application, didReceiveRemoteNotification: userInfo, fetchCompletionHandler: completionHandler)

}

@available(iOS 10.0, *)

override func userNotificationCenter(_ center: UNUserNotificationCenter, didReceive response: UNNotificationResponse, withCompletionHandler completionHandler:@escaping() -> Void) {

QGSdk.getSharedInstance().userNotificationCenter(center, didReceive: response)

super.userNotificationCenter(center, didReceive: response, withCompletionHandler: completionHandler)

}

@available(iOS 10.0, *)

override func userNotificationCenter(_ center: UNUserNotificationCenter, willPresent notification: UNNotification, withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {

QGSdk.getSharedInstance().userNotificationCenter(center, willPresent: notification)

super.userNotificationCenter(center, willPresent: notification, withCompletionHandler: completionHandler)

}

}

Follow the steps listed in Configuring Rich Push Notifications to enable the feature.

Send a test push campaign to verify that your push notification implementation is correct.Updated over 1 year ago Table of Contents

Overview

Prerequisites for using the firebase_messaging plugin

Push notification setup for Android devices

1. Register app info with AIQUA

2. Set up message handling

3. Route messages to the Appier SDK

4. Send a test push campaign

Push notification setup for iOS devices



Using the Firebase Messaging Plugin [3]

https://docs.aiqua.appier.com/docs/flutter-using-the-firebase-messaging-plugin



3. Route messages to the Appier SDK

4. Send a test push campaign

Push notification setup for iOS devices

1. Configure your APNS credentials on FCM

2. Provide FCM tokens to the Appier SDK

3. Request push permission and enable foreground notifications

4. Enable capabilities

5. Bridge notification handling in AppDelegate.swift

6. Enable rich push notifications

7. Send a test push campaign



[iOS] Rich Push Notifications [0]

https://docs.aiqua.appier.com/docs/rich-push-notifications-for-flutter



A rich push notification is a push notification that includes an image, video, GIF, audio, carousel, or slider. With the release of iOS 10, AppierFramework and AppierExtensionFramework were introduced to support rich push notifications and notification UI customization.

This guide will explain how to set up the Notification Service Extension and Notification Content Extension. These extensions are required for:

Sending rich push notifications (notifications using creative types such as banners, carousels, and sliders)

Tracking impression events for all push notifications, regardless of the creative type used

The App Group ID will be used in your main app target as well as the two extension targets you'll create. The App Group ID must be the same ID used when you enabled the App Group.

Add a notification service extension target. Under to File > New > Target, select Notification Service Extension, then click Next.

For Product Name, enter "AppierNotificationServiceExtension" and click Finish.

After clicking Finish, you'll be prompted to activate the "AppierNotificationServiceExtension" scheme. Select Cancel. 

Add a notification content extension target. In Xcode, navigate to File > New > Target, select Notification Content Extension, and click Next.

For Product Name, enter "AppierNotificationContentExtension" and click Finish.

After clicking Finish, you'll be prompted to activate the "AppierNotificationContentExtension" scheme. Select Cancel. 

Add the following lines to your Flutter project's Podfile:

target 'Runner' do

...

pod 'AppierExtensionFramework', '8.2.2'

end

target 'AppierNotificationServiceExtension' do

use_frameworks!

pod 'AppierExtensionFramework', '8.2.2'

end

target 'AppierNotificationContentExtension' do

use_frameworks!

pod 'AppierExtensionFramework', '8.2.2'

end

post_install do |installer|

...

end

Ensure that the target names in the Podfile match the product names you used when creating the extensions (AppierNotificationServiceExtension and AppierNotificationContentExtension).



[iOS] Rich Push Notifications [1]

https://docs.aiqua.appier.com/docs/rich-push-notifications-for-flutter



After adding the extensions to the Podfile, run the following commands in the ios/ directory to install the extensions:

$ pod repo update

$ pod install

In the AppierNotificationServiceExtension folder, open the NotificationService.* files and replace the contents of the entire file with the following:

For Swift: NotificationService.swift

import AppierExtension

class NotificationService: QGNotificationService {

override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {

super.didReceive(request, withContentHandler: contentHandler)

}



override func serviceExtensionTimeWillExpire() {

super.serviceExtensionTimeWillExpire()

}

}

Go to the project navigator and select the AppierNotificationServiceExtension target.

Navigate to Signing & Capabilities > App Groups, and then add the app group using your App Group ID.

In the project navigator, select the AppierNotificationServiceExtension target. Under the General tab, change the deployment target of your content extension to iOS 10.0.

Find the Info.plist file in the AppierNotificationServiceExtension folder. Add the following row under Information Property List:

KeyTypeValueAppierAppGroupStringYour App Group ID

In the AppierNotificationContentExtension folder, open the following files and replace the contents of the entire file with the following:

For Swift: NotificationViewController.swift

import UIKit

import AppierExtension

class NotificationViewController: QGNotificationContentViewController {

override func viewDidLoad() {

super.viewDidLoad()

// Do any required interface initialization here.

}

}

Go to the project navigator and select the AppierNotificationContentExtension target.

Navigate to Signing & Capabilities > App Groups, and then add the app group using your App Group ID.

In the project navigator, select the AppierNotificationContentExtension target. Under the General tab, change the deployment target of your content extension to iOS 10.0.



[iOS] Rich Push Notifications [2]

https://docs.aiqua.appier.com/docs/rich-push-notifications-for-flutter



Find the Info.plist file in the AppierNotificationContentExtension folder. Under NSExtension > NSExtensionAttributes, update UNNotificationExtensionCategory and add UNNotificationExtensionDefaultContentHidden and UNNotificationExtensionUserInteractionEnabled with the following values:

KeyTypeValueUNNotificationExtensionDefaultContentHiddenBooleanYES or 1UNNotificationExtensionUserInteractionEnabledBooleanYES or 1UNNotificationExtensionCategoryStringQGCAROUSEL

Add the following row under Information Property List:

KeyTypeValueAppierAppGroupStringYour App Group ID

Info.plist for AppierNotificationContentExtension should look like this:

In MainInterface.storyboard, remove the default Label.

In MainInterface.storyboard, select View and change the Background to System Grouped Background Color.

Build the target and follow the instructions in Sending Test Notification for iOS to verify that the rich push notification works as expected.

See the troubleshooting steps below if you encounter issues sending notifications.

Ensure that the deployment target of AppierNotificationServiceExtension and AppierNotificationContentExtension is set to iOS 10.0.

Remove -ObjC/$(inherited) if it exists in the build settings of the AppierNotificationServiceExtension and AppierNotificationContentExtension.

Ensure that the same App Group ID is used in all three targets.

Under the AppierNotificationServiceExtension and AppierNotificationContentExtension targets, go to Build Phases > Compile Sources to make sure the following files are correctly configured. If not, click + to add the files.

AppierNotificationServiceExtension Compile Sources

AppierNotificationContentExtension Compile SourcesUpdated 9 months ago Table of Contents

1. Save your app group ID

2. Add the extensions

3. Install the extensions with CocoaPods

4. Set up the Notification Service Extension

5. Set up the Notification Content Extension

6. Send a test push notification

Troubleshooting



Implementing Deep Links

https://docs.aiqua.appier.com/docs/flutter-deep-links



The Appier Flutter SDK supports passing deep links to your app. Note that the Flutter SDK doesn't resolve or handle deep links—the links are passed directly to the app for handling.

Refer to the instructions below to start using deep links with your app:

Android deep links

iOS deep links

Follow the deep link implementation instructions for Android.

iOS deep links can be implemented using one of the following methods:

Option 1: Using a custom URL scheme

Option 2: Using universal links

Follow the deep link implementation instructions for iOS.

Call setUniversalLinkDomains() after AppierFlutter.configure():

@override

void initState() {

super.initState();

AppierFlutter.configure(

'',

appGroup: '',

);

AppierFlutter.setUniversalLinkDomains(["YOUR_DOMAIN_1", "YOUR_DOMAIN_2"]);

}

🚧ImportantTo prevent unexpected issues, don't call setUniversalLinkDomains() in the native iOS code.Updated over 1 year ago Table of Contents

Overview

Android deep links

iOS deep links

Option 1: Using a custom URL scheme

Option 2: Using universal links



Storing Push Notifications [0]

https://docs.aiqua.appier.com/docs/flutter-storing-push-notifications



The Appier Flutter SDK allows you to enable push notification storage, and provides APIs for the following operations:

Setting the maximum notification storage limit

Retrieving stored notifications

Deleting stored notifications

Your app must be using Flutter SDK 2.4.0 or later

The Appier SDK can only store notifications sent by AIQUA

Push notification storage is disabled by default. To enable it, call enableStoredNotifications().

AppierFlutter.enableStoredNotifications();

By default, the notification storage limit is set to 20. Messages that exceed the storage limit are deleted, with the oldest messages being deleted first.

Use setStoredNotificationsLimit() to change the storage limit. In the following example, the storage limit is set to 3:

AppierFlutter.setStoredNotificationsLimit(3);

getStoredNotifications() returns a JSON array of the notifications and their fields.

AppierFlutter.getStoredNotifications().then((data) {

// handle the retrieved data

});

Different types of notifications may include different fields. However, all of them have a title and a message. They may also have imageUrl, bigImageUrl, deepLink and other fields depending on the notification type. For details on image specifications, see Image Specifications.

You can delete a single notification by retrieving it's position in the array returned by getStoredNotifications() and passing it into deleteStoredNotification(). The following example deleted the first stored notification (at position 0) in the array:

AppierFlutter.deleteStoredNotification(0);

For example, you can use deleteNotificationAtIndex() to delete a notification from the app's notification history after a user reads or clicks it.

Delete all locally stored AIQUA notifications using deleteAllStoreNotifications():

AppierFlutter.deleteAllStoredNotifications();

Updated over 1 year ago Table of Contents

Overview

Requirements and limitations

Enabling stored notifications

Setting the notification storage limit

Retrieving stored notifications

Deleting stored notifications



Storing Push Notifications [1]

https://docs.aiqua.appier.com/docs/flutter-storing-push-notifications



Setting the notification storage limit

Retrieving stored notifications

Deleting stored notifications

Deleting a single notification

Deleting all notifications



Flutter SDK Web View Support [0]

https://docs.aiqua.appier.com/docs/flutter-webview-support



The Appier plugin supports web views in Flutter apps via web-to-mobile SDK bridging with the InAppWebViewplugin.

Appier Flutter SDK versionCompatible InAppWebView plugins versions2.8.0 and earlier5.0.5 to 5.8.03.0.0 or later6.0.0

SDK bridging establishes a link between the embedded InAppWebView and your native app so that data logged by your website (Appier Web SDK) is automatically passed to the Appier plugin (Appier Flutter SDK). No modifications to your website's logging implementation are required.

The Appier Flutter SDK 3.0.0 uses version 6.0.0 of the InAppWebView plugin, which introduced a breaking change. If you're upgrading to the latest SDK version from Appier Flutter SDK 2.8.0 or earlier, please follow the steps in the InAppWebView migration guide to ensure your web views continue to function properly.

Initialize a web-to-mobile SDK bridge in an InAppWebView widget by hooking into the onWebViewCreated and onLoadStart events. Enable the bridge using AppierFlutter.enableWebSdkBridge().

InAppWebView(

...

onWebViewCreated: (controller) async {

...

await AppierFlutter.enableWebSdkBridge(

inAppWebViewController: controller);

...

},

onLoadStart: (controller, url) async {

...

await AppierFlutter.enableWebSdkBridge(

inAppWebViewController: controller);

...

});

...

},

🚧PrerequisitesIntegrate the Appier Web SDK with your website and verify the integration in a desktop browser before configuring a web SDK bridge.

Complete the following steps to verify that the SDK bridge is working.

Load your website with the InAppWebView (generally via initialUrlRequest).

Ensure AppierFlutter.enableWebSdkBridge() is hooked into onWebViewCreated and onLoadStart.

Run your app and open the InAppWebView screen—this step initializes the Appier Web SDK.

The Appier Web SDK will then initiate a handshake with the Appier plugin. If the SDK bridge has been configured properly, you'll see a message like this in your Flutter app's debug console:



Flutter SDK Web View Support [1]

https://docs.aiqua.appier.com/docs/flutter-webview-support



flutter: {message: [WebSdkBridge] Posting message: {"name":"request","body":{"id":"...","name":"getVersion","body":null}}, messageLevel: 0}

Interact with your website so that events and attributes are logged by the Web SDK.

Check the AIQUA Dashboard as described in these checkpoint steps to verify that data logged from your InAppWebView screen is captured by the Flutter SDK.

Updated 7 months ago Table of Contents

Overview

Migrating from Flutter SDK 2.8.0 and earlier

Initializing an SDK bridge in the InAppWebView widget

SDK bridge verification



AppierFlutter class - appier_flutter library - Dart API [0]

https://pub.dev/documentation/appier_flutter/latest/appier_flutter/AppierFlutter-class.html



menuAppierFlutter classdark_modelight_mode

Properties

hashCode

→ int

The hash code for this object.

no setterinherited

runtimeType

→ Type

A representation of the runtime type of the object.

no setterinherited

Methods

noSuchMethod(Invocation invocation)

→ dynamic

Invoked when a nonexistent method or property is accessed.

inherited

toString()

→ String

A string representation of this object.

inherited

Static Methods

configure(String appId, {String? senderId, String? appGroup, bool isDev = false})

→ Future

Configures the SDK



deleteAllStoredNotifications()

→ Future

Delete all stored notifications



deleteStoredNotification(int index)

→ Future

Delete stored notifications at index



disableIdfaConsent()

→ Future

Disables IDFA consent.



enableIdfaConsent()

→ Future

Enables IDFA consent.



enableStoredNotifications()

→ Future

Enable stored notifications



enableWebSdkBridge({InAppWebViewController? inAppWebViewController})

→ Future

Eanbles Web SDK bridge to web views.



flush()

→ Future

Immediately uploads queued data to the Appier server



getAppierId()

→ Future

Get appierId.



getDataTrackingConfig()

→ Future

getRecommendation(String scenarioId, {String? productId, Map? parameters})

→ Future?>

Gets recommendation by scenarioId with optional productId and

parameters.



getStoredNotifications()

→ Future>>

Get stored notifications



handleRemoteMessage(String messageString)

→ Future

Send the remote message string messageString to AIQUA

Rename this method to handlePushMessage in Native V8



hideInAppCampaigns()

→ Future

Hide the in-app campaigns



isAppierPush(String messageString)

→ Future

Check if the remote message is from AIQUA



logEvent(String eventName, {Map? parameters, double? vts, String? vtsCurr})

→ Future

Sends any event in your app to the Appier server



AppierFlutter class - appier_flutter library - Dart API [1]

https://pub.dev/documentation/appier_flutter/latest/appier_flutter/AppierFlutter-class.html



→ Future

Sends any event in your app to the Appier server



logRecommendationClicked(String scenarioId, int modelId, String productId, String recommendationId)

→ Future

Logs recommendation clicked by scenarioId, modelId, productId and

recommendationId.



renewAppierId()

→ Future

Regenerates appierId.



renewUserId()

→ Future

Regenerates userId.



setApnsToken(String token)

→ Future

Set the Apple Push Notification service (APNS) token.



setAttributionWindow(int seconds)

→ Future

Sets the View Through Attribution Window for event attribution



setCity(String city)

→ Future

Set the city of the user



setClickAttributionWindow(int seconds)

→ Future

Sets the Click Through Attribution Window for event attribution



setCustomKey(String key, dynamic value)

→ Future

Set any custom key for your user



setDataTrackingConfig(DataTrackingConfig config)

→ Future

setDayOfBirth(int day)

→ Future

Set the day of DOB of the user



setEmail(String email)

→ Future

Set the email of the user



setFcmToken(String token)

→ Future

Set Firebase Cloud Messaging token.



setFirstName(String firstName)

→ Future

Set the firstName of the user



setLastName(String lastName)

→ Future

Set the lastName of the user



setMonthOfBirth(int month)

→ Future

Set the month of DOB of the user



setName(String name)

→ Future

Set the name of the user



setPhoneNumber(String phoneNo)

→ Future

Set the phoneNumber of the user



setStoredNotificationsLimit(int limit)

→ Future

Set stored notifications limit



setUniversalLinkDomains(List linkDomains)

→ Future

Set the Associated Domains for Universal Links



setUserId(String userId)

→ Future

Set the unique user id for your users



setYearOfBirth(int year)

→ Future

Set the year of DOB of the user



Android SDK Release Notes

https://docs.aiqua.appier.com/docs/release-notes-android



Android SDK Release NotesAppier SDK versions follow a lifecycle with three statuses.

Development: Actively updated with new features and bug fixes. Ideal for clients adopting the latest capabilities.

Stable: Only critical bug fixes are provided—no new features. Recommended for clients prioritizing stability.

Archived: No longer supported. These versions receive no updates, including bug fixes, and may not function properly.

Updated 15 days ago Flutter SDK Web View SupportDevelopment Android SDK Versions



Stable Android SDK Versions [0]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



Support interactions with background while an in-app creative studio campaign is displayed. Creative studio is a beta feature. To learn more, contact your customer success manager.

Clicking the deep link in push campaigns where the deep link was set to an invalid URL caused the app to crash.

When push campaigns were stacked, clicking action buttons in any campaign redirected to the deep link configured in the most recently-received campaign.

Push notification small icons failed to display for apps using adaptive icons.

On devices running Android 12+, clicking push notification action buttons missing deep links didn't launch the app.

In Carousel creatives, if a single carousel card was missing the headline and description, the headline and description failed to display for all cards in the carousel.

Slider creatives occasionally failed to display large images.

In-app pop-up campaign weren't dismissed and will reappeared if the blank margin is double-clicked quickly.

In-app pop-up campaigns experienced the following abnormal behavior when the device’s orientation was changed:

The floating icon’s draggable area didn’t adjust according to the device’s orientation.

The campaign’s floating text wasn’t correctly resized according to the device’s orientation.

Support for GIF images (only standard gif87a & gif89a) for in-app pop-up campaign floating icons on devices running Android WebView 67 or later. GIFs may not display properly for devices running earlier WebView versions.

Upgraded the com.google.android.gms:play-services-location SDK dependency to version 21.3.0 to prevent unexpected crashes caused by a known issue with Google Play Services.

Upgraded the SDK to Kotlin 1.8. This update requires apps to use Android Gradle Plugin (AGP) 7.4.

In-app pop-up campaigns occasionally failed to display on devices running Android WebView 80 and earlier.

In-app pop-up campaigns weren't refreshed if the campaign creative was updated and the app was re-opened from the background.



Stable Android SDK Versions [1]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



In-app pop-up campaigns weren't refreshed if the campaign creative was updated and the app was re-opened from the background.

When switching between pages, the campaign would occasionally collapse into a floating icon, even if the notification persistence setting was set to Don’t persist.

Medium in-app creative messages became scrollable if the message content exceeded three lines. After this fix, creative messages can support 15 lines of content before becoming scrollable.

Small, Medium, and Full Screen in-app creatives failed to render or rendered incorrectly if the creative title or message contained ' or ".

Removed support for HTML tags (such as 

) and adding line breaks using \n in creative titles, messages, and button text.

In Slider and Carousel creatives, the arrows used to navigate between images disappeared after being clicked.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Support Recommendation for in-app creative studio campaigns.

Unexpected app crashes related to the following error messages:

java.lang.IllegalArgumentException: Size must be greater than zero

java.lang.NullPointerException: Attempt to invoke virtual method 'void com.appier.aiqua.sdk.k.b()' on a null object reference

android.database.sqlite.SQLiteDiskIOException: disk I/O error (code 3850)

java.lang.IllegalArgumentException: No such service ComponentInfo{APP_PACKAGE}/com.appier.aiqua.sdk.NotificationJobIntentService}

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Support for in-app creative studio. To learn more about this beta feature, contact your customer success manager.

Occasional memory leaks occurring in web views.



Stable Android SDK Versions [2]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



Occasional memory leaks occurring in web views.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

When an in-app campaign with persistence settings set to Don't persist or Persist until notification is clicked triggered a second in-app campaign by clicking on or closing the first campaign, the second in-app campaign would be automatically closed due to a race condition.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Added user data permissions controls for AAID and location data.

Added QG.getInstance(context).isAppierPush() to replace the deprecated QG.isQGMessage().

Deprecated QG.isQGMessage().

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Introduced geofencing. To learn more about this beta feature, contact your customer success manager.

An issue causing occasional app crashes.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

aiq-close-kill would close the in-app custom HTML campaign, but didn't kill it. As a result, relaunching the app would allow the campaign to be displayed again. Affected versions: 7.17.0 to 7.20.0.

Requesting recommendations in a web view caused a JSON syntax error.

Clicks on in-app pop-up campaigns action buttons without deep links were erroneously included in campaign attribution metrics.

Replaced getAppierId() with appierId.

In-app pop-up campaigns use fade-in and fade-out animations when being opened and closed.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).



Stable Android SDK Versions [3]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



Revamped the implementation of Small, Medium, and Full Screen in-app pop-up creatives for visual consistency across mobile platforms.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Compatibility issues with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Affected versions: 7.15.0 to 7.18.0.

Introduced getAppierId(), which returns the Appier SDK-generated identifier (userId).

Introduced renewAppierId(), which regenerates the Appier SDK-generated identifier (userId) and removes all locally cached data associated with the previous userId. This method replaces the deprecated renewUserId().

Increased the HTTP client timeout to reduce the probability of duplicated events. Affected versions: 7.11.0 to 7.17.3.

This SDK version is incompatible with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Using incompatible AGP versions breaks core SDK features, such as data logging and in-app campaigns, and occasionally causes app crashes. To prevent these issues, please add the required ProGuard rules and ensure you’re using a compatible version of AGP.

App crashes occurred when hideInAppCampaigns() was called before initializing the SDK.

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.

This SDK version is incompatible with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Using incompatible AGP versions breaks core SDK features, such as data logging and in-app campaigns, and occasionally causes app crashes. To prevent these issues, please add the required ProGuard rules and ensure you’re using a compatible version of AGP.

Using event parameters in trigger conditions for in-app pop-up campaigns caused app crashes. Affected versions: 7.15.0 to 7.17.1.



Stable Android SDK Versions [4]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.

This SDK version is incompatible with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Using incompatible AGP versions breaks core SDK features, such as data logging and in-app campaigns, and occasionally causes app crashes. To prevent these issues, please add the required ProGuard rules and ensure you’re using a compatible version of AGP.

The event set as the trigger rule of in-app campaigns will now count toward the event count set in audience filter based on events within 24 hours (if the same event is used as the trigger and the filter condition). Previously, trigger events were not considered in the 24-hour audience filter.

Using event parameters in trigger conditions for in-app pop-up campaigns caused app crashes.

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.

This SDK version is incompatible with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Using incompatible AGP versions breaks core SDK features, such as data logging and in-app campaigns, and occasionally causes app crashes. To prevent these issues, please add the required ProGuard rules and ensure you’re using a compatible version of AGP.

Support for tag recommendation. This feature is only available through Appier Professional Services. Contact your customer success manager to learn more.

In-app campaigns were displayed at incorrect positions after the app was relaunched from a killed state.

Using event parameters in trigger conditions for in-app pop-up campaigns caused app crashes. 

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.



Stable Android SDK Versions [5]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



This SDK version is incompatible with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Using incompatible AGP versions breaks core SDK features, such as data logging and in-app campaigns, and occasionally causes app crashes. To prevent these issues, please add the required ProGuard rules and ensure you’re using a compatible version of AGP.

Internal SDK updates to prepare for future multi-data center support

In-app floating icons changed positions when navigating to different screens.

Using event parameters in trigger conditions for in-app pop-up campaigns caused app crashes.

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.

This SDK version is incompatible with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Using incompatible AGP versions breaks core SDK features, such as data logging and in-app campaigns, and occasionally causes app crashes. To prevent these issues, please add the required ProGuard rules and ensure you’re using a compatible version of AGP.

Starting from SDK v7.15.0, the following Recommendation API base URL will be used by the SDK: https://aiqua-intel.prd.c.appier.net. If your app requires the Recommendation API and uses an allowlist to specify trusted domains, please add the new API endpoint URL to your allowlist.

Using event parameters in trigger conditions for in-app pop-up campaigns caused app crashes.

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.

This SDK version is incompatible with Android Gradle Plugin (AGP) versions 7.0.0 to 7.0.4. Using incompatible AGP versions breaks core SDK features, such as data logging and in-app campaigns, and occasionally causes app crashes. To prevent these issues, please add the required ProGuard rules and ensure you’re using a compatible version of AGP.



Stable Android SDK Versions [6]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



The updated collapsed push notification layout will only be applied to device running Android 12 or later. 

SDK v7.4.1 updated the layout of collapsed push notifications to fit in Android 12's smaller notification area. This update was mistakenly applied to devices running earlier Android versions (Android 11 and earlier).

Starting from this version, the image preview in collapsed push notifications using carousel creatives will only display the first image in the carousel. Previously, two images were shown in the preview.

The default text and background colors for push notification previews is automatically applied based on the system's light or dark mode settings.

Color defaults for collapsed push notifications titles and messages can be modified—see Customizing Push Notification Previews for details.

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.

Support for the Display background overlay option to display or disable background overlay in in-app notifications.

Removed the auto-collapse behavior in in-app notifications to align with iOS SDK. Previously, expanded notifications automatically collapsed when the app is switched to background.

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.

Support for syncing LINE users with app users via a link in AIQUA LINE campaigns that land on the SDK-integrated app or via a LIFF URL. For details, see LINE User Profile Sync.

Floating icon was displayed by mistake in the expanded mode of Small, Medium, Large, and HTML in-app campaign creatives if the campaign is set to Don't persist.

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.



Stable Android SDK Versions [7]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



The SDK now collects the app standby bucket assigned by Android OS. This data is only intended for internal troubleshooting purposes (i.e. Appier Support), and isn't available for general usage.

The qg_inapp_closed event for in-app pop-up campaign notifications is now logged when the pop-up is closed by the SDK due to notification persistence settings. 

Expanding in-app pop-up campaign floating icons occasionally caused the app to crash 

Events were more likely to be resent due to a short HTTP client timeout, resulting in duplicated events and potentially inflating event counts, e.g. inflated impression counts.

Support for configurable on-click behavior for in-app pop-up campaign floating icons.

The Android SDK has been migrated to AndroidX. AndroidX replaces the original Android Support Library, which is no longer maintained. Starting from SDK v7.10.0, apps using the Android Support Library won't be supported by the Android SDK.

On devices running Android 13, push notifications using carousels failed to display properly (only the notification title and message would display).

Carousel creatives didn’t display properly on high-DPI devices (550 DPI or higher).

Improved the SDK's event de-duplication mechanism.

Changed the ProGuard rule to prevent obfuscated class names conflict with other SDKs.

Some results returned by getRecommendationWithScenarioId() were incorrectly based on fallback rules rather than the scenario's recommendation model.

A certificate compatibility issue occurring on devices running Android 7.1.0 and earlier which resulted in getRecommendationWithScenarioId() returning an empty response.

UI enhancements for Floating text creatives used in in-app pop-up campaigns. Affected SDK versions: 7.8.0, 7.8.1, and 7.8.2.

Apps crashed when expanding floating icons for in-app pop-up campaigns containing messages exceeding the drawable area on the UI.

Calling getInboxes() before the Appier SDK finished initializing caused the app to crash.



Stable Android SDK Versions [8]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



Calling getInboxes() before the Appier SDK finished initializing caused the app to crash.

Introduced Talkback support for in-app pop-up campaigns. Talkback is Google’s screen reader which allows users to use their Android device when they are unable to or have difficulty seeing the screen. All visible text components of an in-app campaign support Talkback functionality.

Impression and click events for in-app inbox notifications weren't properly logged, leading to inaccurate campaign metrics being displayed on the AIQUA Dashboard.

The status of some in-app inbox messages stayed UNREAD after the message was opened, rather than changing to READ.

Clicking in-app campaign deep links would occasionally cause the app to crash.

The ability to clear all foreground in-app pop-up notifications using hideInAppCampaigns().

The ability to specify the floating icon's initial position in an in-app pop-up campaign.

Aligned the Android SDK's in-app campaign floating icon size with the iOS SDK's floating icon size. 

The notificationId attribute for in-app inbox notifications is now read-only. Previously, this variable was private. See In-App Inbox Notifications for details.

Action buttons with embedded deep links didn't work in notifications for apps targeting Android 12 (targetSdkVersion: 31).

The flush() method was unavailable in Android SDK 7.7.0.

For Medium and Full Screen in-app campaign creatives, tapping an image won't dismiss the campaign anymore. Previously, tapping the image would dismiss the campaign.

We recommend revisiting your Full-Screen creatives to verify that the in-app notification can be dismissed via an action button or close button. See Best Practices for Full Screen Creatives for details.

Changed the class name of com.quantumgraph.sdk.NotificationJobIntentService to com.appier.aiqua.sdk.NotificationJobIntentService. If you're using this class to customize Firebase Cloud Messaging (FCM) message handling, please update your import line to use the new class name.



Stable Android SDK Versions [9]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



We recommend using the handleRemoteMessage API to customize FCM message handling instead of using NotificationJobIntentService directly.

An Activity leak caused by the SDK.

Some push campaign notifications were unclickable after setting targetSdkVersion to 31.

OPPO, Xiaomi, and Realme devices occasionally crashed unexpectedly.

The flush() method is not available.

Several internal issues that occurred while bridging with the React Native SDK.

Support for filtering audience by events within 24 hours in in-app campaigns. 

In-app campaigns can be displayed multiple times after the trigger condition is met. Previously, in-app campaigns could only be displayed again after launching the app from a killed state.

In-app campaign data is pulled from AIQUA when the app is re-opened from the background. Previously, in-app campaign data was only refreshed when launching the app from a killed state.

The app_launched default event is logged when the app is re-opened from the background. Previously, app_launched was only logged when launching the app from a killed state.

The Appier Android SDK now enforces push campaign notification delivery restrictions (blackout windows and time to live) via SDK, in addition to the existing server-side enforcement.

The condition matching algorithm for In-App Campaign trigger rules didn't compare integer and decimal values properly.

In some cases, notifications in a collapsed state had overlapping titles and messages.

The Appier Android SDK now declares the com.google.android.gms.AD_ID permission to allow access to the advertising ID. Apps that don't require this permission can explicitly remove it.

Notifications are not clickable on apps targeting Android 12 (targetSdkVersion: 31). Use targetSdkVersion: 30 to ensure that notifications work properly for all Android versions.

Transparent backgrounds are now supported for in-app custom HTML campaigns.

All APIs related to Google Analytics have been deprecated and the following dependencies have changed:



Stable Android SDK Versions [10]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



All APIs related to Google Analytics have been deprecated and the following dependencies have changed:



Removed com.google.android.gms:play-services-analytics:16.0.7.

Added com.google.android.gms:play-services-ads-identifier:16.0.0. This package is required to obtain a Google Advertising ID (AAID).

[Fixed] Occasional crash in devices using Android 11 and above if the app is not granted READ_PHONE_STATE permission and the targetSdkVersion is set to 30 and above. (Affected SDK versions: v7.3.0 and below)

[New] Support for collecting the hybrid SDK version used in hybrid apps. This is supported in the following hybrid SDK versions:

React Native SDK 1.6 or later

[New] Support for collecting the SDK type used in the app. 

[New] Introduced new API for easier FCM customization. 

[Fixed] Incorrect version displayed for sdkVersion in some cases. 

[Fixed] Inability to display Big Image in collapsed mode in Android push campaigns that include a coupon code.

[New] Support for using = operator with event parameters in the trigger rule of in-app campaigns.

[New] Support for filtering out purchased products from recommendation results based on user_id in WebView.

[Improved] Explicitly declared com.google.firebase:firebase-iid:17.0.4 as a dependency

[New] Support for including new app users within 24 hours in "New Users" and "All Users" default segments in in-app campaigns.

[New] Support for first_app_launched event as trigger rule in in-app campaigns.

[Changed] Sequence of event tracking adjusted. first_app_launched is now tracked before app_launched when the user launches the app for the first time.

[Fixed] Campaign-level frequency cap is reset when the user clicks on a deeplink in the in-app campaign or when the user upgrades to app integrated with Android SDK 7.0.0 for the first time. (Affected SDK version: 7.0.0)

[Fixed] notification_displayed event not logged when the push creative falls back to basic mode with only title and message due to error (e.g. unable to load creative image).



Stable Android SDK Versions [11]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



[Fixed] notification_displayed event is logged even when notification is not displayed for users who have switched off the sub-toggles of the app's notification settings. This issue does not occur to users who have switched off the main notification toggle.

🚧Known Issue in Android SDK 7.0.1:In Android SDK 7.0.1, the sdkVersion is shown as 6.11.1.

[Changed] Migrated Maven package repository from jcenter() to mavenCentral().

[Changed] Migrated Maven package name from com.quantumgraph.sdk:QG to com.appier:appier-android. 

[Changed] Changed Java compatibility from Java 7 to 8. See here for more info.

[New] Support for priority management of in-app campaigns. If a user triggers multiple in-app campaigns at the same time, AIQUA displays the one with the highest priority. 

[Improved] Security improvements related to log messages.

[Fixed] Fixed the issue where recommendation_impression event is logged when no recommendation result is generated.

[Fixed] Frequency cap of in-app campaigns is reset when the user re-opens the app after more than 30 hours of inactivity. (Affected SDK versions: 6.10.0 and below.)

🚧Known Issue in Android SDK 7.0.0:

Campaign-level frequency cap does not work when the in-app campaign contains a deeplink. This issue has been fixed in Android SDK 7.0.1.

In Android SDK 7.0.0, the sdkVersion is shown as 6.11.0.

Updated 15 days ago Table of Contents

v7.26.0 - September 6, 2024

v7.25.1 - August 30, 2024

v7.25.0 - July 19, 2024

v7.24.4 - June 28, 2024

v7.24.3 - April 12, 2024

v7.24.2 - March 27, 2024

v7.24.1 - March 15, 2024

v7.24.0 - December 29, 2023

v7.23.1 - December 14, 2023

v7.23.0 - November 13, 2023

v7.22.0 - October 6, 2023

v7.21.0 - August 4, 2023

v7.20.0 - June 29, 2023

v7.19.0 - June 9, 2023

v7.18.0 - May 26, 2023

v7.17.3 - May 22, 2023

v7.17.2 - April 28, 2023

v7.17.1 - April 21, 2023

v7.17.0 - April 14, 2023

v7.16.0 - March 17, 2023

v7.15.0 - February 17, 2023

v7.14.0 - February 3, 2022

v7.13.0 - December 29, 2022

v7.12.0 - December 16, 2022

v7.11.0 - October 14, 2022



Stable Android SDK Versions [12]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-stable



v7.14.0 - February 3, 2022

v7.13.0 - December 29, 2022

v7.12.0 - December 16, 2022

v7.11.0 - October 14, 2022

v7.10.0 - September 2, 2022

v7.9.1 - July 15, 2022

v7.9.0 - July 1, 2022

v7.8.3 - May 27, 2022

v7.8.2 - May 6, 2022

v7.8.1 - April 15, 2022

v7.8.0 - March 21, 2022

v7.7.0 - March 4, 2022

v7.6.1 - February 22, 2022

v7.6.0 - January 28, 2022

v7.5.0 - January 7, 2022

v7.4.1 - December 2, 2021

v7.4.0 - November 5, 2021

v7.3.1 - August 30, 2021

v7.3.0 - August 12, 2021

v7.2.0 - July 7, 2021

v7.1.0 - June 23, 2021

v7.0.1 - May 12, 2021

v7.0.0 - April 15, 2021



Archived Android SDK Versions [0]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-archived



[New] Support for using recommendation 2.0 integrated in webpages via WebView

[Fixed] Fixed the issue where recommendation_impression event is logged even when failed to retrieve recommendation results

[New] Options to add a close button ("x" button) to the Small, Medium, and Full Screen creatives of in-app popup notifications.

[New] Support for including a control group in the Experiment feature of in-app campaigns.

[Improved] The titles of Android notifications are changed to bold to align with iOS notifications.

[Changed] Event attribution window can no longer be set to 0. The default attribution window will be applied if set to 0.

[Fixed] Fixed an edge case crash when regenerating user using renewUserId(). (Affected SDK version: v6.7.0)

[Improved] Deprecated static method renewUserId() and added a new version using instance method. 

[New] New method to regenerate user

[Improved] Reduced the occurrence of duplicated events

[New] Support for Push Booster (Beta feature)

[Fixed] Compatibility issue for Carousel Push images in Android 11

[Fixed] Added exception handling for runtime JobIntentService crash on Android Oreo and above (known Android issue link) 

[Fixed] Updated AiDeal SDK Dependency

[Fixed] Updated ProGuard file for Android Support Library

This version is deprecated. Please use the latest SDK version.

[New] Recommendation 2.0 method with productId as parameter

[Fixed] Fixed the missing response in recommendation method

[New] New recommendation 2.0 method that returns scenarioId, modelId, and recId in the json response.

[New] New method to log clicks on recommendation 2.0 items.

[New] Impression on recommendation 2.0 items will now be automatically logged.

[New] Options to add close button ("x" button) to floating message and circular icon (floating bubble) of in-app notifications.

[New] Delay Timer feature to support displaying in-app campaigns to users X seconds after the notification is triggered.



Archived Android SDK Versions [1]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-archived



[New] Delay Timer feature to support displaying in-app campaigns to users X seconds after the notification is triggered.

[New] New method to use Personalization without app versioning. Using this new method, personalization settings no longer need to be reconfigured when app version is changed.

[New] Security enhancement in API

[Changed] Upgraded Socket.IO Library

[Fixed] Security improvements

[Fixed] Memory issues

[New] Support for Recommendations 2.0 with recommendation scenario

[New] Added Volley as dependency

[Changed] Deprecation of Recommendations 1.0

This release only includes updates for AiDeal, and does not affect AIQUA and AIXON.

This release only includes updates for AiDeal, and does not affect AIQUA and AIXON.

[New] Support for Android integration with AiDeal. AiDeal is Appier's AI-powered platform that helps trigger purchase decisions for hesitant customers. Find out more about AiDeal.

[New] Support for Subtitle (Subtext) in push notifications (Reference)

[New] Kotlin dependency in Gradle

[Fixed] Fixed incorrect value for aiq_push_enabled status

[Fixed] Fixed display issue of in-app icon when the Margin from the Top specified exceeds the device height. In-App icons will now be reset to the bottom of the screen if the margin exceeds device height.

[Changed] Removed Glide library as dependency.

[Changed] Changed the FileProvider path used in SDK to avoid conflict with the FileProvider in application level AndroidManifest.xml file.

[Changed] Hide empty images in notification if the image failed to download.

[Fixed] Issues with handling uncaughtException which causes Firebase Crashlytics' crash report not to be sent (Affected SDK versions: v5.8.0 - v5.9.4).

[New] New methods for enabling/disabling storage of push notification and for deleting a stored notification at index.

[Fixed] Initial expanded state of In-App notifications not working when the trigger event is called inside onStart or onCreate.



Archived Android SDK Versions [2]

https://docs.aiqua.appier.com/docs/android-sdk-release-notes-archived



[Fixed] Initial expanded state of In-App notifications not working when the trigger event is called inside onStart or onCreate.

[Fixed] Incorrect creative height when using small content box creative. Creative height is now adjusted based on length of notification text. (Affected SDK version: v5.9.3 and below.)

[Fixed] Campaign performance recorded incorrectly due to integer overflow of notification id (Affected SDK versions: v5.9.2 and below).

Updated 15 days ago Table of Contents

v6.10.0 - March 12, 2021

v6.9.0 - February 24, 2021

v6.8.0 - January 26, 2021

v6.7.1 - January 4, 2021

v6.7.0 - December 28, 2020

v6.6.1 - December 14, 2020

v6.6.0 - December 10, 2020 (Deprecated)

v6.5.1 - November 27, 2020

v6.5.0 - November 25, 2020

v6.4.0 - November 10, 2020

v6.3.0 - November 4, 2020

v6.2.0 - September 30, 2020

v6.1.0 - September 14, 2020

v6.0.2 - August 27, 2020

v6.0.1 - August 14, 2020

v6.0.0 - August 12, 2020

v5.10.0 - June 30, 2020

v5.9.5 - February 19, 2020

v5.9.4 - February 18, 2020

v5.9.3 - January 30, 2020



iOS SDK Release Notes

https://docs.aiqua.appier.com/docs/release-notes-ios



iOS SDK Release NotesAppier SDK versions follow a lifecycle with three statuses.

Development: Actively updated with new features and bug fixes. Ideal for clients adopting the latest capabilities.

Stable: Only critical bug fixes are provided—no new features. Recommended for clients prioritizing stability.

Archived: No longer supported. These versions receive no updates, including bug fixes, and may not function properly.

Updated 15 days ago Archived Android SDK VersionsDevelopment iOS SDK Versions



Stable iOS SDK Versions [0]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



📘Apple app privacy changes (v7.32.0 or later)In December 2023, Apple introduced new privacy updates for App Store submissions. If you're upgrading to iOS SDK 7.32.0 or later and haven't reviewed the updates, please review Apple App Privacy to learn more about how to complete your app's Privacy Nutrition Label.

The following events were occasionally duplicated for custom HTML in-app campaigns: qg_inapp_toggled (when closing campaigns) and qg_inapp_clicked. Affected versions: 7.34.0 to 7.35.0, 8.0.0 to 8.2.1.

The model_id parameter's data type (included in recommendation_clicked events) is now sent as a string. If you're logging this event, you'll need to modify your implementation. Please refer to iOS SDK: Recommendation 2.0 for details.

A floating icon was incorrectly displayed when in-app pop-up campaigns using basic creatives with Notification Persistence set to Don't persist and were triggered immediately after app launch. Affected versions: 7.33.0 to 7.34.1.

The entire screen was incorrectly covered with a gray mask when in-app pop-up campaigns using basic creatives with background overlays enabled were triggered immediately after app launch by events other than app_launched. Affected versions: 7.32.1 to 7.34.1.

Improved debug logging for in-app Creative Studio campaigns.

Creative Studio campaigns now display every time the trigger event is detected. Previously, campaigns only displayed after the first instance of the trigger event and failed to display after subsequent events. Affected version: 7.34.0.

Deep links in Creative Studio campaigns are no longer incorrectly encoded. Affected versions: 7.32.2 to 7.34.0.

Support interactions with background while an in-app creative studio campaign is displayed. Creative studio is a beta feature. To learn more, contact your customer success manager.

When in-app creative studio campaigns were triggered, a loading indicator was displayed, blocking the user interface. Creative studio is a beta feature. To learn more, contact your customer success manager.



Stable iOS SDK Versions [1]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



HTML in-app campaigns not displaying in the center when triggered by the app_launched event.

After regenerating the Appier ID using renewAppierId():

Events stored by the SDK are not flushed.

In-app pop-up campaigns being displayed continue to display.

In-app pop-up campaigns set to display using time delays continue to display.

On apps running SDK 7.33.0, campaigns whose persistence setting is changed to Don't persist display a blank floating icon after the setting change.

Medium creatives with long descriptions pushed other creative elements out of the visible area. After this fix, descriptions have a maximum height, after which the description becomes scrollable.

Slider and Carousel creatives are not properly resized after rotating a device to landscape mode.

Support for GIF and APNG files for in-app pop-up campaign floating icon images on devices running iOS 13+. On devices running an operating system version earlier than iOS 13, the first frame of the GIF/APNG will be used as the floating icon image.

In-app pop-up campaigns weren't refreshed if the campaign creative was updated and the app was re-opened from the background.

Optimized the SDK's in-app pop-up campaign fetching mechanism to reduce occurrences of unexpected app crashes on app launch. 

Scrolling and zooming were inadvertently enabled for in-app pop-up campaigns. Affected versions: v7.27.0 to v7.32.3.

Occasional app crashes when the app storage I/O is limited. App crashes were associated with the following error message: __boundsFail: index 199 beyond bounds.

If the device was in portrait orientation, pages that should have been locked to landscape orientation would unexpectedly switch back to portrait mode after closing an in-app campaign.

Medium in-app creative messages became scrollable if the message content exceed three lines. After this fix, the creative message can support 15 lines of content before becoming scrollable.



Stable iOS SDK Versions [2]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



Small, Medium, and Full Screen in-app creatives failed to render or rendered incorrectly if the creative title or message contained ' or ".

Remove support for HTML tags (such as 

) and adding line breaks using \n in creative titles, messages, and button text.

Support Recommendation for in-app creative studio campaigns. Creative studio is a beta feature. To learn more, contact your customer success manager.

Image dimensions for in-app campaign Medium creatives were improperly rounded, causing image cropping when the campaign was displayed.

In-app creative studio campaigns didn't display unicode characters properly. Creative studio is a beta feature. To learn more, contact your customer success manager.

When users clicked on redirect links inside in-app creative studio campaigns, the in-app campaign would incorrectly redirect to the destination URL. After this fix, the redirect URL is opened in an external browser, and the in-app campaign remains unchanged.

App crashes due to lack of device storage. Associated error message: Reason:This NSPersistentStoreCoordinator has no persistent stores (disk full). It cannot perform a save operation.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Prevent app crashes caused by memory management issues that occurred during multithreading executions. Associated error messages: block_destroy_helper, __swift_memcpy, keypath_get_selector_isCollectLocation.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

In compliance with Apple's new privacy updates for App Store submissions, the Appier SDK now provides:

A privacy manifest: The privacy manifest includes a property list of all the types of data collected by the SDK, and the reasons for certain API usage. For details, see Apple App Privacy.



Stable iOS SDK Versions [3]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



Code signing: The XCFramework is now signed by Appier, ensuring that your app is using a secure SDK.

IDFA is no longer collected by default.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Support for in-app creative studio. To learn more about this beta feature, contact your customer success manager.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Introduced a new flag in Info.plist for handling universal links for apps using the scene delegate.

The app’s preferred font face settings weren't applied when rendering in-app campaigns in some languages, such as Japanese.

Occasional app crashes occurred when configuring user data permission settings in debug mode. Affected versions: v7.30.0 and v7.30.1. App crashes were associated with the following error message:

swift_isUniquelyReferenced_nonNull_native

-[QGSdk logUserDetailWithCompletionHandler:]

keypath_get_selector_isCollectLocation

User data permissions settings didn't take affect during the first app launch after app installation for apps:

Using iOS SDK 7.30.0

Where the data tracking settings are configured before the SDK initialization

Conversions for deleted users were attributed to the click or view completed by the user associated with the previous ID rather than the regenerated ID.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Apps upgraded from iOS SDK versions 7.11.0 and earlier to versions 7.12.0 or later crashed due to encoding/decoding incompatibilities. App crashes were associated with the following error message:

[NSKeyedUnarchiver decodeObjectForKey:]: cannot decode object of class (Condition) for key (NS.objects) because no class named "Condition" was found



Stable iOS SDK Versions [4]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



Apps using iOS SDK 7.27.0 or later occasionally crashed due to a race condition when displaying an in-app pop-up campaign. App crashes were associated with the following error message:

Reason:Application tried to present a nil modal view controller on target .

Apps occasionally crashed when the Appier SDK initialized the log collection mechanism. App crashes were associated with the following error messages:

Fatal Exception: NSInvalidArgumentException

+[QGUncaughtExceptionHandler backtrace]

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Added user data permission controls for IDFA and location data.

Support for handling universal links using UISceneDelegate.

Apps compiled using Xcode 15 and running on iOS 17.0 or later were unable to display rich media in rich push notifications properly. Instead, standard notifications containing only the notification title and message were displayed instead.

An additional app_launched event was logged once per day for apps using geofencing on iOS SDK 7.29.0.

Small, Medium, and Full Screen in-app creatives will fail to render or rendered incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Introduced geofencing. To learn more about this beta feature, contact your customer success manager.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Requesting recommendations in a web view caused a JSON syntax error.

Dark mode color scheme settings were incorrectly set for in-app pop-up campaigns.

Small, Medium, and Full Screen in-app creatives will fail to render or rendered incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).



Stable iOS SDK Versions [5]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



Revamped the implementation of Small, Medium, and Full Screen in-app pop-up creatives for visual consistency across mobile platforms.

Some duplicate in-app pop-up campaigns were displayed and couldn’t be dismissed.

Small, Medium, and Full Screen in-app creatives will fail to render or render incorrectly if the creative title or message contains ', ", \n, or any HTML tags (such as 

).

Disabled method swizzling by default to prevent conflicts with third-party SDKs. Method swizzling was automatically enabled in versions 7.20.0 to 7.25.0.

If you're upgrading from versions 7.20.0 to 7.25.0 and relied on method swizzling to enable LINE user sync and tracking click events for LINE campaigns via deep link, please configure iOS deep link handling in your app or explicitly enable method swizzling.

Introduced getAppierId(), which returns the Appier SDK-generated identifier (userId).

Introduced renewAppierId(), which regenerates the Appier SDK-generated identifier (userId) and removes all locally cached data associated with that userId. Replaces the deprecated renewUserId().

Clicking on an in-app pop-up campaign's Floating Text creative without a valid deep link and persistence settings set to Persist until the notification is click will now cause the floating icon to collapse without disappearing. Previously, the floating icon disappeared after collapsing.

Method swizzling is enabled by default, potentially causing conflicts with third-party SDKs.

Support for tag recommendation. This feature is only available through Appier Professional Services. Contact your customer success manager to learn more.

Method swizzling is enabled by default, potentially causing conflicts with third-party SDKs.

Apps displaying in-app campaigns using custom HTML occasionally crashed when users clicked on the campaign's close button multiple times.

App crashes occurred while displaying in-app campaigns with images whose URLs included a newline (\n).



Stable iOS SDK Versions [6]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



App crashes occurred while displaying in-app campaigns with images whose URLs included a newline (\n). 

Events which were logged by the SDK but had not yet been flushed to AIQUA were deleted after the app was killed. Starting from version 7.23.1, stored events will be flushed to AIQUA in the first batch interval in the subsequent app launch.

Method swizzling is enabled by default, potentially causing conflicts with third-party SDKs.

Internal SDK updates to prepare for future multi-data center support

A race condition which caused unexpected app crashes

Method swizzling is enabled by default, potentially causing conflicts with third-party SDKs.

Starting from SDK v7.22.0, the following Recommendation API base URL will be used by the SDK: https://aiqua-intel.prd.c.appier.net. If your app requires the Recommendation API and uses an allowlist to specify trusted domains, please add the new API endpoint URL to your allowlist.

Non-English characters weren't supported inside in-app campaign image URLs.

Method swizzling is enabled by default, potentially causing conflicts with third-party SDKs.

Support for the Display background overlay option to display or disable background overlay in in-app notifications.

In-app campaign data isn't refreshed promptly in some cases, causing a slight delay in applying campaign settings. Affected SDK versions: 7.19.0, 7.19.1, 7.19.2 and 7.20.0.

Method swizzling is enabled by default, potentially causing conflicts with third-party SDKs.

Use method swizzling to support syncing LINE users with app users via a LIFF URL or via links embedded in AIQUA LINE campaigns that direct to an iOS SDK-integrated app. For details, see LINE User Sync.

Method swizzling in the iOS SDK can be disabled. For details, see Disabling method swizzling.

Method swizzling in the iOS SDK may conflict with third-party SDK services. For details, see SDK conflicts.

In-app campaigns that target new app users weren't displayed. Affected SDK versions: 7.19.0, 7.19.1, and 7.19.2.



Stable iOS SDK Versions [7]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



In-app campaigns that target new app users weren't displayed. Affected SDK versions: 7.19.0, 7.19.1, and 7.19.2.

Apps occasionally crashed when calling flush().

Method swizzling is enabled by default, potentially causing conflicts with third-party SDKs.

isAppierPush: is now available in AppierExtensionFramework. This API allows you to determine whether a push notification was sent by Appier. For usage details, see Handling Push Notifications.

The # character in campaign notification deep links was incorrectly encoded, rendering some URLs invalid.

recommendation_impression events weren't logged in iOS SDK 7.19.1.

Calling getRecommendationWithScenarioId() without the optional productId parameter returned an empty array with no recommendation results in iOS SDK 7.19.1.

notification_displayed and notification_received weren't logged for apps that were:

Using iOS SDK 7.19.0

Newly installed by the user (i.e. this bug wasn't present if an app using iOS SDK 7.19.0 was updated by the user)

isAppierPush: has been introduced to the SDK to allow you to determine whether a push notification was sent by Appier. For usage details, see Handling Push Notifications.

Carousels and sliders wouldn't display properly if one or more images contained invalid URLs. After this fix, carousels and sliders will properly display images with valid URLs and won't display images with invalid URLs.

Support for configurable on-click behavior for in-app pop-up campaign floating icons.

The following API used to log events with multiple event parameter values has been deprecated: logEvent:withParameters:withValueToSum:withValueToSumCurrency:withConvertedEvent:withAttributionEnabled:

For details about the supported API methods, see Logging Custom User Events.

Improved the SDK's event de-duplication mechanism.

Certain special characters in Recommendation 2.0 request query parameters resulted in a 400 Bad Request response.

Apps occasionally crashed when calling the following methods on SDK versions 7.15.0, 7.16.0, 7.16.1, and 7.16.2:

logEvent()



Stable iOS SDK Versions [8]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



Apps occasionally crashed when calling the following methods on SDK versions 7.15.0, 7.16.0, 7.16.1, and 7.16.2:

logEvent()

getRecommendationWithScenarioId()

renewUserId()

On older iPhone models (iPhone XS and earlier), tap gestures performed on in-app pop-up floating icons were mistakenly recognized as drag gestures. As a result, floating icons in the expanded state wouldn't collapse after being tapped on.

In-app inbox notifications weren't being received during an app's first launch post-installation.

nil wasn't a supported value for the SDK's user attribute logging methods. This resulted in the attribute's value not being updated if nil was logged.

The ability to clear all foreground in-app pop-up notifications using hideInAppCampaigns().

The ability to specify the floating icon's initial position in an in-app pop-up campaign.

Support for filtering audience by events within 24 hours in in-app campaigns. 

Media URLs without filename extensions (.jpg or .png) weren't supported for push campaigns.

Transparent backgrounds are now supported for in-app custom HTML campaigns.

When publishing an app from the latest Xcode 13 release, the Manage Version and Build Number option is selected by default. This option sets a single version number for all the app's components (including the Appier Framework and Appier Extension Framework), which resulted in sdkVersion being incorrectly set to the app's version rather than the Appier SDK version.

[New] Support for collecting the hybrid SDK version used in hybrid apps. This is supported in the following hybrid SDK versions:

React Native SDK 1.6 or later

[New] Support for collecting the SDK type used in the app. 

[New] Support for using = operator with event parameters in the trigger rule of in-app campaigns.

[New] Support for filtering out purchased products from recommendation results based on user_id in WebView. If you are using custom implementation of WebView, you will need to redo the WebView integration.



Stable iOS SDK Versions [9]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



[Fixed] Floating bubble (icon image) of in-app custom HTML campaigns remains visible in the overlay background after the campaign is expanded. 

[New] Support for including new app users within 24 hours in "New Users" and "All Users" default segments in in-app campaigns.

[New] Support for first_app_launched event as trigger rule in in-app campaigns.

[Changed] Sequence of event tracking adjusted. When the user launches the app for the first time, first_app_launched is now tracked before app_launched.

[Improved] Updated the iOS device model list that maps Apple's machine ID (e.g. iPhone13,3) to product name (e.g. iPhone 12 Pro).

[Fixed] Debugging events (Migration - From NSDictionary and Migration - inApp) are tracked when users launch the app for the first time after upgrading to app integrated with iOS SDK 7.10.0 or 7.10.1. 

[Fixed] SDK sends invalid IDFA (0000) of iOS 14+ users when setIDFAConsent is set to true and the user's App Tracking Transparency status is NotDetermined. After the fix, SDK no longer sends IDFA of NotDetermined users when setIDFAConsent is set to true.

[Fixed] Issue where local cache related to the in-app campaign fails to be cleared after the campaign is turned off. 

🚧Known Issue in iOS SDK 7.10.1:Debugging events (Migration - From NSDictionary and Migration - inApp) are tracked when users launch app for the first time after upgrading. This issue has been fixed in iOS SDK 7.10.2.

[New] Introduced AppierExtensionFramework in Notification Service Extension and Notification Content Extension for Rich Push integration. 

Starting from iOS SDK 8.0.0, the original AppierFramework will no longer be supported in Rich Push integration. 

See here for instructions on migrating to iOS SDK 7.10.0 or later.

[New] Support for priority management of in-app campaigns. If a user triggers multiple in-app campaigns at the same time, AIQUA displays the one with the highest priority.



Stable iOS SDK Versions [10]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



📘Note:This in-app priority management feature is coming soon on AIQUA dashboard, and you will be able to configure the priority on AIQUA dashboard.

🚧Known Issues in iOS SDK 7.10.0:

Local cache related to the in-app campaign is not cleared after the campaign is turned off. This issue has been fixed in iOS SDK 7.10.1.

Debugging events (Migration - From NSDictionary and Migration - inApp) are tracked when users launch app for the first time after upgrading. This issue has been fixed in iOS SDK 7.10.2.

[New] Added support for App Tracking Transparency (ATT) framework. See here for details.

[Improved] Reduced the chance of push images being rendered in incorrect order (occurring at very low probability).

[New] Support for using recommendation 2.0 integrated in webpages via WebView

[New] Added pre-defined method for tracking user's phone number

[New] Options to add a close button ("x" button) to the Small, Medium, and Full Screen creatives of in-app popup notifications.

[Fixed] Issue where local cache and WebView cookies are cleared when in-app campaigns using custom HTML creatives are triggered.

[Fixed] userId changes when the App Group ID is changed, resulting in duplicated iOS users.

[New] Support for including a control group in the Experiment feature of in-app campaigns.

[Changed] Event attribution window can no longer be set to 0. The default attribution window will be applied when set to 0.

[New] New method to regenerate user.

[New] Recommendation 2.0 method with productId as parameter.

[New] New recommendation 2.0 method that returns scenarioId, modelId, and recId in the json response.

[New] New method to log clicks on recommendation 2.0 items.

[New] Impression on recommendation 2.0 items will now be automatically logged.

[New] Delay Timer feature to support displaying in-app campaigns to users X seconds after the notification is triggered.

[New] Options to add close button ("x" button) to floating message and circular icon (floating bubble) of in-app notifications.

[New] Security enhancement in API.



Stable iOS SDK Versions [11]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



[New] Security enhancement in API.

[Fixed] Excluded carousel items with invalid images from carousel push notifications.

[New] New method to use Personalization without app versioning. Using this new method, personalization settings no longer need to be reconfigured when app version is changed.

[Changed] SDK migrated from Framework to xcframework. See the notes about installing using CocoaPods here. 

[Fixed] Crash when the app runs in background.

🚧Important:SDK v7.2.0 fixed a critical issue. Please upgrade if you are using earlier SDK versions.

[New] Support for Recommendations 2.0 with recommendation scenario

[Improved] Logging and security related changes

[Changed] Deprecation of Recommendations 1.0

[Fixed] Added exception handling for personalized data

[New] First version of Appier Framework.

[New] Support for tracking bundle id of the app.

[New] Collect device info upon app version update to ensure device info is up-to-date

[Fixed] Notification Id overflow on 32-bit iOS devices.

[Changed] Device model now sent in native format.

[Changed] Replaced UIWebView with native Socket IO client.

Updated 15 days ago Table of Contents

v7.35.1 - February 21, 2025

v7.35.0 - December 27, 2024

v7.34.1 - November 22, 2024

v7.34.0 - September 6, 2024

v7.33.1 - September 2, 2024

v7.33.0 - July 19, 2024

v7.32.4 - June 21, 2024

v7.32.3 - April 12, 2024

v7.32.2 - March 15, 2024

v7.32.1 - February 23, 2024

v7.32.0 - February 2, 2024

v7.31.0 - December 29, 2023

v7.30.2 - December 22, 2023

v7.30.1 - December 1, 2023

v7.30.0 - November 13, 2023

v7.29.0 - October 6, 2023

v7.28.0 - August 4, 2023

v7.27.0 - June 29, 2023

v7.26.0 - June 9, 2023

v7.25.0- May 26, 2023

v7.24.0 - April 14, 2023

v7.23.1 - March 31, 2023

v7.23.0 - March 17, 2023

v7.22.0 - February 17, 2023

v7.21.0 - December 29, 2022

v7.20.0 - December 16, 2022

v7.19.2 - November 25, 2022

v7.19.1 - October 14, 2022

v7.19.0 - October 12, 2022 (Deprecated)

v7.18.0 - September 2, 2022

v7.17.0 - July 1, 2022

v7.16.3 - May 27, 2022

v7.16.2 - April 22, 2022

v7.16.1 - April 15, 2022



Stable iOS SDK Versions [12]

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-stable



v7.18.0 - September 2, 2022

v7.17.0 - July 1, 2022

v7.16.3 - May 27, 2022

v7.16.2 - April 22, 2022

v7.16.1 - April 15, 2022

v7.16.0 - March 21, 2022

v7.15.0 - January 28, 2022

v7.14.0 - November 5, 2021

v7.13.0 - August 12, 2021

v7.12.0 - July 15, 2021

v7.11.0 - June 23, 2021

v7.10.2 - May 19, 2021

v7.10.1 - May 13, 2021

v7.10.0 - April 14, 2021

v7.9.0 - March 31, 2021

v7.8.0 - March 12, 2021

v7.7.0 - February 24, 2021

v7.6.0 - January 26, 2021

v7.5.0 - December 29, 2020

v7.4.0 - November 25, 2020

v7.3.0 - November 9, 2020

v7.2.0 - October 15, 2020

v7.1.0 - September 14, 2020

v7.0.0 - August 27, 2020



Archived iOS SDK Versions

https://docs.aiqua.appier.com/docs/ios-sdk-release-notes-archived



[New] Support for iOS integration with AiDeal. AiDeal is Appier's AI-powered platform that helps trigger purchase decisions for hesitant customers. Find out more about AiDeal.

🚧ImportantAppier iOS SDK 6.0.0 includes UIWebView, which has been deprecated by Apple. When uploading your app to App Store, you may receive a warning email from Apple as shown below.

Apple will not accept new apps with UIWebView on App Store. 

For apps already on App Store, update is accepted until December 2020.

App using iOS SDK 6.0.0 must be upgraded to 7.x.x before November 2020.

[Fixed] Security improvements

[New] Support iOS integration with Firebase Cloud Messaging

[New] Support for new CocoaPods format

[New] Support for null value in event parameters and profiles. 

[Changed] The deeplink encoding method is updated to support notification URLs that contain decoded characters. Both encoded and decoded characters are now supported in URLs.

Updated 15 days ago Table of Contents

v6.0.0 - May 29, 2020 (Deprecated)

v5.4.0 - September 30, 2020

v5.3.0 - July 28, 2020

v5.2.3 - May 26, 2020

v5.2.2 - March 19, 2020



Flutter SDK Release Notes

https://docs.aiqua.appier.com/docs/release-notes-flutter



Flutter SDK Release NotesAppier SDK versions follow a lifecycle with three statuses.

Development: Actively updated with new features and bug fixes. Ideal for clients adopting the latest capabilities.

Stable: Only critical bug fixes are provided—no new features. Recommended for clients prioritizing stability.

Archived: No longer supported. These versions receive no updates, including bug fixes, and may not function properly.

Updated 15 days ago



Stable Flutter SDK Versions [0]

https://docs.aiqua.appier.com/docs/flutter-sdk-release-notes-stable



The Appier Flutter SDK now uses InAppWebView version 6.0.0. If your app uses web views and you're upgrading to this version of the Appier SDK, please follow the instructions in the InAppWebView migration guide.

Updated the bridged Appier Android SDK version from 7.25.0 to 7.26.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.33.0 to 7.34.0. See the iOS SDK release notes for a detailed summary of changes.

Updated the bridged Appier Android SDK version from 7.24.3 to 7.25.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.32.3 to 7.33.0. See the iOS SDK release notes for a detailed summary of changes.

Updated the bridged Appier Android SDK version from 7.24.0 to 7.24.3. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.32.1 to 7.32.3. See the iOS SDK release notes for a detailed summary of changes.

In compliance with Apple's new privacy updates for App Store submissions, the Appier SDK now provides:

A privacy manifest: The privacy manifest includes a property list of all the types of data collected by the SDK, and the reasons for certain API usage. For details, see Apple App Privacy.

Code signing: The XCFramework is now signed by Appier, ensuring that your app is using a secure SDK.

Support for in-app creative studio. To learn more about this beta feature, contact your customer success manager.

Updated the bridged Appier Android SDK version from 7.23.1 to 7.24.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.30.2 to 7.32.1. See the iOS SDK release notes for a detailed summary of changes.

Note that IDFA is no longer collected by default.

Updated the bridged Appier Android SDK version from 7.23.0 to 7.23.1. See the Android SDK release notes for a detailed summary of changes.



Stable Flutter SDK Versions [1]

https://docs.aiqua.appier.com/docs/flutter-sdk-release-notes-stable



Updated the bridged Appier iOS SDK version from 7.30.0 to 7.30.2. See the iOS SDK release notes for a detailed summary of changes.

Introduced geofencing. To learn more about this beta feature, contact your customer success manager.

Added user data permission controls for AAID, IDFA, and location data.

Updated the bridged Appier Android SDK version from 7.22.0 to 7.23.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.29.0 to 7.30.0. See the iOS SDK release notes for a detailed summary of changes.

Changed the handler function for routing push messages to Appier SDK with firebase_messaging plugin. To use geofencing or silent push notifications with firebase_messaging plugin, please reconfigure the function.

Requesting recommendations in a web view caused a JSON syntax error.

(iOS only) Potential app crashes when configuring user data permission controls in debug mode

(iOS only) User data permission controls configured before SDK initialization might not take effect for first-installed apps

(iOS only) Apps using UISceneDelegate are required to do additional implementations

📘Note: Known issuesPlease contact Appier Support for more details and ways to work around these issues.

Support for stored push notifications.

📘Note: GeofencingTo use geofencing, please refer to Flutter SDK 2.5.0. While geofencing is supported in the bridged iOS and Android SDK versions, this feature is untested in Flutter SDK 2.4.0.

Updated the bridged Appier Android SDK version from 7.20.0 to 7.22.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.27.0 to 7.29.0. See the iOS SDK release notes for a detailed summary of changes.

Revamped the implementation of Small, Medium, and Full Screen in-app pop-up creatives for visual consistency across mobile platforms.

Requesting recommendations in a web view caused a JSON syntax error.



Stable Flutter SDK Versions [2]

https://docs.aiqua.appier.com/docs/flutter-sdk-release-notes-stable



Requesting recommendations in a web view caused a JSON syntax error.

Note: While this issue has been fixed in the bridged Android and iOS SDK versions, it has not yet been fixed in Flutter SDK 2.4.0.

The Flutter SDK returned an error message when retrieving recommendations in a web view if the num parameter was an int value.

Updated the bridged Appier Android SDK version from 7.17.2 to 7.20.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.24.0 to 7.27.0. See the iOS SDK release notes for a detailed summary of changes.

Support for the Display background overlay option to display or disable the background overlay for in-app notifications.

Support for syncing LINE users with app users via a URL in AIQUA LINE campaigns that lands on the SDK-integrated app or via a LIFF URL. For details, see LINE User Profile Sync.

Note that the iOS SDK uses method swizzling to support LINE user profile sync by default. Method swizzling may cause conflicts with third-party SDKs resulting in app crashes. If your app uses third-party SDKs that conflict with iOS SDK, you can disable method swizzling and manually enable LINE user profile sync.

Updated the bridged Appier Android SDK version from 7.10.0 to 7.17.2. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.18.0 to 7.24.0. See the iOS SDK release notes for a detailed summary of changes.

Executing the flutter build apk command would fail with an error due to incompatibilities with certain third-party Android libraries.

Support for configurable on-click behavior for in-app pop-up campaign floating icons.

Updated the bridged Appier Android SDK version from 7.9.1 to 7.10.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.17.0 to 7.18.0. See the iOS SDK release notes for a detailed summary of changes.

The app_launched event wasn’t logged when launching the app:



Stable Flutter SDK Versions [3]

https://docs.aiqua.appier.com/docs/flutter-sdk-release-notes-stable



The app_launched event wasn’t logged when launching the app:

For the first time after being installed

After the app was killed by the user or OS

Support for regenerating users via renewUserId().

Support for the firebase_messaging plugin. For instructions on using this plugin to set up push notifications, see Using the Firebase Messaging Plugin.

Updated the bridged Appier Android SDK version from 7.3.1 to 7.9.1. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.13.0 to 7.17.0. See the iOS SDK release notes for a detailed summary of changes.

Updated 15 days ago Table of Contents

v3.0.0 - September 13, 2024

v2.8.0 - August 2, 2024

v2.7.0 - April 12, 2024

v2.6.0 - March 1, 2024

v2.5.1 - December 29, 2023

v2.5.0 - November 24, 2023

v2.4.0 - October 20, 2023

v2.3.0 - July 21, 2023

v2.2.0 - May 12, 2023

v2.1.1 - March 24, 2023

v2.1.0 - September 16, 2022

v2.0.0 - July 22, 2022



Archived Flutter SDK Versions

https://docs.aiqua.appier.com/docs/flutter-sdk-release-notes-archived



AllGuidesReferenceAnnouncementsPagesStart typing to search…Archived Flutter SDK Versions



React Native SDK Release Notes

https://docs.aiqua.appier.com/docs/release-notes-react-native



React Native SDK Release NotesAppier SDK versions follow a lifecycle with three statuses.

Development: Actively updated with new features and bug fixes. Ideal for clients adopting the latest capabilities.

Stable: Only critical bug fixes are provided—no new features. Recommended for clients prioritizing stability.

Archived: No longer supported. These versions receive no updates, including bug fixes, and may not function properly.

Updated 15 days ago Archived Flutter SDK VersionsDevelopment React Native SDK Versions



Stable React Native SDK Versions [0]

https://docs.aiqua.appier.com/docs/react-native-sdk-release-notes-stable



Updated the bridged Appier Android SDK version from 7.25.0 to 7.26.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.33.0 to 7.34.1. See the iOS SDK release notes for a detailed summary of changes.

No changes were introduced in this version.

Updated the bridged Appier Android SDK version from 7.24.3 to 7.25.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.32.3 to 7.33.0. See the iOS SDK release notes for a detailed summary of changes.

Updated the bridged Appier Android SDK version from 7.24.2 to 7.24.3. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.32.2 to 7.32.3. See the iOS SDK release notes for a detailed summary of changes.

Support for TypeScript.

Added the following SDK methods:

getAppierId()

renewAppierId()

isAppierPush()

Updated the bridged Appier Android SDK version from 7.11.0 to 7.24.2. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.19.1 to 7.32.2. See the iOS SDK release notes for a detailed summary of changes.

Added the following SDK methods:

renewUserId()

isQgMessage()

Requesting recommendations in a web view caused a JSON syntax error.

Updated the bridged Appier iOS SDK version from 7.19.1 to 7.19.2. See the iOS SDK release notes for a detailed summary of changes.

In mobile apps using React Native SDK 1.9.0, calling the Recommendation API resulted in an error message displaying in the app and no results being returned.

The React Native SDK's package name has been changed from react-native-aiqua-sdk to @appier/react-native-sdk

Updated the bridged Appier Android SDK version from 7.8.0 to 7.11.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.16.0 to 7.19.1. See the iOS SDK release notes for a detailed summary of changes.



Stable React Native SDK Versions [1]

https://docs.aiqua.appier.com/docs/react-native-sdk-release-notes-stable



The fractional portion of float values in event parameters was truncated when logging events using logEvent()

A method to clear all foreground in-app pop-up notifications. See hideInAppCampaigns() in the list of React Native SDK methods.

Updated the bridged Appier Android SDK version from 7.6.1 to 7.8.0. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.15.0 to 7.16.0. See the iOS SDK release notes for a detailed summary of changes.

An issue that caused Android push campaign notifications to be unclickable. This issue would occur after setting targetSdkVersion to 31.

An issue causing Activity leaks.

An issue that caused some OPPO, Xiaomi, and Realme devices to crash unexpectedly.

Aligned the Android SDK's in-app campaign floating icon size with the iOS SDK's floating icon size. 

Updated the bridged Appier Android SDK version from 7.3.1 to 7.6.1. See the Android SDK release notes for a detailed summary of changes.

Updated the bridged Appier iOS SDK version from 7.13.0 to 7.15.0. See the iOS SDK release notes for a detailed summary of changes.

If you've configured rich push notifications, please update your Podfile to use the latest version of ApperExtensionFramework.

Suppressed erroneous Android error messages when calling setFCMToken().

[Updated] Native Android SDK from 7.3.0 to 7.3.1. 

See Android SDK Release Notes.

[Updated] Native iOS SDK from 7.9.0 to 7.13.0. 

See iOS SDK Release Notes.

[Updated] Native Android SDK from 6.10.0 to 7.3.0. 

See Android SDK Release Notes.

[New] Support for collecting the React Native SDK version and SDK type used in the app. 

[New] Support for filtering out purchased products from recommendation results based on user_id in WebView. 

[New] Introduced new API for easier FCM customization in Android.

[Fixed] Improved compatibility with Expo Bare Workflow

Updated 15 days ago Table of Contents

v1.12.0 - December 6, 2024

v1.11.1 - August 12, 2024

v1.11.0 - August 9, 2024

Changed

v1.10.2 - May 2, 2024

Changed



Stable React Native SDK Versions [2]

https://docs.aiqua.appier.com/docs/react-native-sdk-release-notes-stable



v1.12.0 - December 6, 2024

v1.11.1 - August 12, 2024

v1.11.0 - August 9, 2024

Changed

v1.10.2 - May 2, 2024

Changed

v1.10.0 - March 27, 2024

New

Changed

Fixed

v1.9.1 - March 3, 2023

Changed

Fixed

v1.9.0 - October 28, 2022

Changed

Fixed

v1.8.0 - March 29, 2022

New

Changed

Fixed

v1.7.0 - February 22, 2022

v1.6.1 - September 7, 2021

v1.6.0 - August 24, 2021



Archived React Native SDK Versions

https://docs.aiqua.appier.com/docs/react-native-sdk-release-notes-archived



[Updated] Native iOS SDK from 7.3.0 to 7.9.0. 

See iOS SDK Release Notes.

See here for integrating App Tracking Transparency (ATT) framework. 

[Updated] Native Android SDK from 6.4.0 to 6.10.0. 

See Android SDK Release Notes.

[Fixed] Initialization of Appier Web SDK fails from time to time in RNAiquaWebView if web SDK is initialized before app SDK. (Android)

[New] iOS Rich Push Integration with CocoaPods AppierFramework.

[Updated] Native iOS SDK to version 7.3.0.

[Updated] Native Android SDK to version 6.4.0.

[Fixed] Crash issue on iOS 14 when the app runs in background. 

[New] Support for Firebase Integration in iOS.

[Fixed] Fixed issue with notification sound in Android Push.

[Fixed] Fixed issue with handling profile parameters in Android that occurs when using setCustomKey method and using numbers as value.

[New] Support for CocoaPods installation and automatic linking in React Native versions 0.60.0 and above.

Updated 15 days ago Table of Contents

v1.5.0 - May 07, 2021

v1.4.0 - November 11, 2020

v1.3.3 - July 28, 2020

v1.3.2 - June 19, 2020

v1.3.1 - April 6, 2020



Passing Dates and Times to AIQUA Servers

https://docs.aiqua.appier.com/docs/passing-dates-and-times-to-aiqua-servers



Sometimes you may wish to pass dates or time to AIQUA servers. For example, you may wish to pass the start date of a journey to AIQUA servers. Appier Android, iOS, and Web SDKs take only integers, real numbers, strings, and booleans as parameters. 

Thus, dates and times need to be formatted as strings before they can be passed to AIQUA. The following tables indicate the format which is understood by the AIQUA servers.

FormatSample ValueYYYY-MM-DD2017-07-12

The HH in the following parameters follows a 24-hour format.

FormatSample ValueHH:MM:SS15:10:06 for 3:10:06 PM02:04:42 for 2:04:42 AM

There are two datetime formats in AIQUA.

This datetime format is followed for logging the date and time, without the timezone.

FormatSample ValueYYYY-MM-DDTHH:MM:SS2017-07-12T15:10:06

This datetime format is followed for logging the date, time, and timezone. 

FormatSample valueYYYY-MM-DDTHH:MM:SS[+/-]HH:MM2017-07-12T15:10:06+05:30 for IST2017-07-12T15:10:06-08:00 for PSTUpdated over 1 year ago Table of Contents

Date Format

Time Format

Datetime Format

Timezone Unaware

Timezone Aware



Airbridge Integration Guide [0]

https://docs.aiqua.appier.com/docs/airbridge-integration-guide



Integrating Airbridge with AIQUA offers significant benefits for enhancing marketing strategies and outcomes. Airbridge provides robust measurement, analytics, and fraud protection, ensuring accurate attribution and performance metrics across multiple channels and devices. By combining these capabilities with AIQUA's omnichannel marketing automation features, you can create targeted campaigns, optimize customer journeys, and increase conversions.

Before proceeding with the Airbridge integration, ensure you've completed the integration prerequisites. Once the prerequisites have been completed, follow these steps to complete the Airbridge integration with your app.

Initialize the Airbridge SDK and track data 

Set up an ad channel integration in the Airbridge console 

Configure Appier postback settings

Verify that events are collected properly 

Complete the following steps before continuing with this guide:

Integrate your app with the Appier iOS or Android SDK. For detailed instructions, refer to the following guides:

iOS SDK Overview

Android SDK Overview

Integrate your app with the Airbridge SDK. For detailed instructions, refer to Airbridge's documentation.

Provide your app’s ID to your customer success manager. The app ID can be found in the app's URL. Refer to the instructions below for Android and iOS.

Retrieve the Android app ID from the id query parameter.

Example app URLExample app IDhttps://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox&hl=encom.google.android.googlequicksearchbox

Retrieve the iOS app ID from the final portion of the URL, only including the portion after id.

Example app URLExample app IDhttps://apps.apple.com/us/app/google/id284815942284815942

Follow the steps corresponding to the platform your app is for:

iOS

Android 

Initialize the Airbridge SDK with automatic event collection disabled (setAutoStartTrackingEnabled(false)).

AirBridge.setAutoStartTrackingEnabled(false)



Airbridge Integration Guide [1]

https://docs.aiqua.appier.com/docs/airbridge-integration-guide



AirBridge.setAutoStartTrackingEnabled(false)

AirBridge.getInstance("", appName: "", withLaunchOptions:launchOptions)

AirBridge.autoStartTrackingEnabled = NO;

[AirBridge getInstance:@"" appName:@"" withLaunchOptions:launchOptions];

Before tracking data:

Initialize the Appier SDK.

Use the Airbridge SDK to add the "appier_app_id" and "appier_user_id" user aliases.

QGSdk.getSharedInstance().onStart("", setDevProfile: false)

let appierAppId = ""

let appierUserId = QGSdk.getSharedInstance().getAppierId()

AirBridge.state()?.addUserAlias(withKey: "appier_app_id", value: appierAppId)

AirBridge.state()?.addUserAlias(withKey: "appier_user_id", value: appierUserId)

QGSdk *qgsdk = [QGSdk getSharedInstance];

[qgsdk onStart:@"" setDevProfile:NO];

NSString *appierAppId = @"";

NSString *appierUserId = [qgsdk getAppierId];

[AirBridge.state addUserAliasWithKey:@"appier_app_id" value: appierAppId];

[AirBridge.state addUserAliasWithKey:@"appier_user_id" value: appierUserId];

Start tracking data with the Airbridge SDK.

AirBridge.startTracking()

[AirBridge startTracking];

Initialize the Airbridge SDK with automatic event collection disabled (setAutoStartTrackingEnabled(false)).

AirbridgeConfig config = new AirbridgeConfig.Builder("", "")

.setAutoStartTrackingEnabled(false)

.build();

Airbridge.init(application, config);

val config = AirbridgeConfig.Builder("", "")

.setAutoStartTrackingEnabled(false)

.build()

Airbridge.init(application, config)

Before tracking data:

Initialize the Appier SDK.

Use the Airbridge SDK to add the "appier_app_id" and "appier_user_id" user aliases.

QG.initializeSdk(application, "");

String appierAppId = "";

String appierUserId = QG.getInstance(context).getAppierId();



Airbridge Integration Guide [2]

https://docs.aiqua.appier.com/docs/airbridge-integration-guide



String appierAppId = "";

String appierUserId = QG.getInstance(context).getAppierId();

Airbridge.getCurrentUser().setAlias("appier_app_id", appierAppId);

Airbridge.getCurrentUser().setAlias("appier_user_id", appierUserId);

QG.initializeSdk(application, "")

val appierAppId = ""

val appierUserId = QG.getInstance(context).appierId

Airbridge.getCurrentUser().setAlias("appier_app_id", appierAppId)

Airbridge.getCurrentUser().setAlias("appier_user_id", appierUserId)

Start tracking data with the Airbridge SDK.

Airbridge.startTracking();

Airbridge.startTracking()

Log in to the Airbridge console. Go to Integrations > Ad Channel Integration, then select the Appier integration.

Go to the Postback tab, and under the Event schema section, click Configuration.

Select all the events you want Airbridge to send to Appier, then click Next.

Next, customize event delivery rules based on your specific requirements, then click Save. For the best marketing automation results, we recommend sending all events (including unattributed) to Appier.

In the Ad Channel Integration page, confirm that the Attributed to column says All channels, meaning that your settings are configured properly, and Appier should successfully receive all postback events.

Next, go to the Postback URL section, and for each event, click the gear icon (under the Edit column) to begin configuring that event's postback settings.

Scroll to the bottom of the parameter list, click + Add. Add the following key-value pair, then click Save:

Key: user_alias

Value: {user.alias}

After you've added the key value pairs for each event, click Start postback sending.

On the Airbridge console, go to Raw Data > App real-time Log and verify that app events are displaying as expected.

On the AIQUA dashboard, click your email in the bottom left corner, then go to Recent activity, select the platform your app is on, and verify that app events are displaying as expected.

Updated 6 months ago Table of Contents

Overview

Prerequisites



Airbridge Integration Guide [3]

https://docs.aiqua.appier.com/docs/airbridge-integration-guide



Updated 6 months ago Table of Contents

Overview

Prerequisites

1. Initialize the Airbridge SDK and track data

iOS

Android

2. Set up an ad channel integration in the Airbridge console

3. Configure Appier postback settings

4. Verify that events are collected properly



AppsFlyer Integration Guide [0]

https://docs.aiqua.appier.com/docs/appsflyer-integration-guide



Integrating AppsFlyer with AIQUA offers significant benefits for enhancing marketing strategies and outcomes. AppsFlyer provides robust measurement, analytics, and fraud protection, ensuring accurate attribution and performance metrics across multiple channels and devices. By combining these capabilities with AIQUA's omnichannel marketing automation features, you can create targeted campaigns, optimize customer journeys, and increase conversions.

Before proceeding with the AppsFlyer integration, ensure you've completed the integration prerequisites. Once the prerequisites have been completed, follow these steps to complete the AppsFlyer integration with your app.

Initialize the AppsFlyer SDK and track data.

Add the Appier integration to your AppsFlyer app.

Verify that events are collected properly.

Ensure you've met the following prerequisites before continuing with this guide:

Retrieve your AppsFlyer dev key (Settings > App Settings > SDK authentication).

Integrate your app with the Appier iOS or Android SDK. For detailed instructions, see these guides:

iOS SDK Overview

Android SDK Overview

Provide your app’s ID to your customer success manager. The app ID can be found in the app's URL. Refer to the instructions below for Android and iOS.

Retrieve the Android app ID from the id query parameter.

Example app URLExample app IDhttps://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox&hl=encom.google.android.googlequicksearchbox

Retrieve the iOS app ID from the final portion of the URL, only including the portion after id.

Example app URLExample app IDhttps://apps.apple.com/us/app/google/id284815942284815942

Follow the steps corresponding to the platform your app is for:

iOS

Android

Initialize the AppsFlyer SDK.

AppsFlyerLib.shared().appsFlyerDevKey = ""

AppsFlyerLib.shared().appleAppID = ""

Before tracking data:

Initialize the Appier SDK.



AppsFlyer Integration Guide [1]

https://docs.aiqua.appier.com/docs/appsflyer-integration-guide



AppsFlyerLib.shared().appleAppID = ""

Before tracking data:

Initialize the Appier SDK.

Use the AppsFlyer SDK to assign values for the following custom data fields: appier_app_id and appier_user_id.

let sdk = QGSdk.getSharedInstance()

sdk.onStart("", setDevProfile: false)

let appierAppId = ""

let appierUserId = sdk.getAppierId()

AppsFlyerLib.shared().customData = ["appier_app_id": appierAppId, "appier_user_id": appierUserId]

Start tracking data with the AppsFlyer SDK.

AppsFlyerLib.shared().start()

Initialize the AppsFlyer SDK.

AppsFlyerLib.getInstance().init("", null, application);

Before tracking data:

Initialize the Appier SDK.

Use the AppsFlyer SDK to assign values for the following custom data fields: appier_app_id and appier_user_id.

QG.initializeSdk(application, "");

String appierAppId = "";

String appierUserId = QG.getInstance(application).getAppierId();

Map customData = new HashMap<>();

customData.put("appier_app_id", appierAppId);

customData.put("appier_user_id", appierUserId);

AppsFlyerLib.getInstance().setAdditionalData(customData);

Start tracking data with the AppsFlyer SDK.

AppsFlyerLib.getInstance().start(application);

Log in to the AppsFlyer console and go to Collaborate > Partner Marketplace

Search for "Appier", select the Appier integration, and click Set up integration to open the integration settings page.

Toggle Activate partner.

Enable In-app event postbacks, set the event postback window, and choose the events to send to Appier. 

Click Save Integration.

On the AppsFlyer console, then go to Analyze > Events to see if events are being collected.

On the AIQUA dashboard, click your email in the bottom left corner and go to Recent activity. Select the platform your app is on to verify that app events are displaying as expected.

Updated 6 months ago Table of Contents

Overview

Prerequisites

1. Initialize the AppsFlyer SDK and track data
