*********************************
Simple Notification Service (SNS)
*********************************

web service that coordinates and manages the delivery or sending of messages to subscribing endpoints or clients

publish - subscribe model, SNS notifies the message, and hence push based approach
Inexpensive pay as you go
CloudWatch or Autoscaling triggers SNS
SNS messages are stored redundantly to multiple AZs

Publishers
communicate asynchronously with subscribers by producing and sending a message to a topic, which is a logical access point and communication channel.

Subscribers
consume or receive the message or notification over one of the supported protocols

SNS can notify the following Protocols:
-HTTP/HTTPS
-EMAIL
-EMAIL-JSON
-SMS
-SQS
-Application

SNS Dataformat - JSON (Subject, Message, TopicArn, MessageId, unsubscribeURL etc..)
Message
MessageId
Signature
SignatureVersion
SigningCertURL
Subject
Timestamp
TopicArn
Type
UnsubscribeURL

HTTP/HTTPS Headers
x-amz-sns-message-type
x-amz-sns-message-id
x-amz-sns-topic-arn
x-amz-sns-subscription-arn

SNS API:
-Subscribe
-Unsubscribe
-Publish
-CreateTopic
-DeleteTopic
-ListTopics
-ListSubscriptions
-ListSubscriptionsByTopic
-SetTopicAttributes
-GetTopicAttributes
