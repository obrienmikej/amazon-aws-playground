1) While working with the S3 API you receive the error message: 404 Not Found. What is the most likely cause for this error?
= NoSuchBucket

2) You have created a mobile application that relies on reading data from DynamoDB. How could you give each mobile device permissions to read from DynamoDB?
= Create an IAM role that can be assumed by an app that allows federated users

Explanation
It is bad practice to store any API credentials in a mobile application. Each mobile device should have their own permissions and access credentials to DynamoDB. In order to facilitate this, you can integrate federated users (Facebook, Google, Twitter, Amazon, etc) credentials with IAM. After authenticated as a federated user, the user/app can then assume an IAM role with the proper read/write permissions to DynamoDB.

3) You attempt to store a new object in the US-STANDARD region in Amazon S3 and receive a confirmation that it has been successfully stored. You then immediately make another API call and attempt to read this object. Will you be able to read this object immediately after?
= Yes, US-Standard has read-after-write consistency which means you will have access to the object immediately after.

4) You have software on an EC2 instance that needs to access both the private and public IP address of that instance. What's the best way for the software to get that information?
= Look it up in instance metadata

5) For which of these languages does AWS provide an SDK? Select 3
= Go, PHP, Java

6) A DynamoDB table can contain ____ local secondary indexes on a table.
= 5

Explanation
You can define up to 5 local secondary indexes and 5 global secondary indexes per table.

7) You want to find out what AMIs are available for you to use in a given region. Which API call is most appropriate?
= DescribeImages

Explanation
DescribeImages is the only valid API call above. (http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) While there are a lot of EC2 API calls (see the URL), you do not need to learn all of them. Focus on the ones that are relevant to developers.

8) Which of the following cannot be used inside a CloudFormation template?
= Ruby statements

Explanation
CloudFormation uses JSON templates.

9) Your supervisor asks you to find a solution for scheduling a sequence of tasks. The sequence may take several months to complete and it’s very important that no tasks are processed more than once. What AWS service should you recommend?
= SWF

Explanation
SWF workflows can last up to a year and tasks are guaranteed to be processed in the correct order.

10) Which of the following is a default limit in S3?
Correct answer
Accounts can have a maximum of 100 buckets

Explanation
This "used" to be a hard limit. However, in 2015 AWS changed it so it was only a soft limit and an increase can be requested.

11) S3 Bucket ownership is transferable.
= False

Explanation
Bucket ownership is not transferable; however, if a bucket is empty, you can delete it. After a bucket is deleted, the name becomes available to reuse, but the name might not be available for you to reuse for various reasons.

12) “256” is not the correct answer to which of the following?
= What is the maximum size, in bytes, of a DynamoDB range primary key attribute value?

Explanation
The maximum size of a DynamoDB range primary key attribute value is 1024 bytes.

13) Which DynamoDB API call does not consume capacity units?
= UpdateTable

Explanation
The UpdateTable API call is used to change the required provisioned throughput capacity.

14) Which API call would you use to attach an EBS volume to an EC2 instance?
= AttachVolume

15) What is the function of a conditional write?
= A change to a DynamoDB attribute will only be written if it that attribute’s value has not changed since it was read

16) Default timeout for visibility queue is ____ seconds.
= 30

17) If you have an item that is 4KB in size and you want to provision read capacity units for 100 requests per second, how many read capacity units do you need to provision?
= 100

Explanation
100 x (4/4) =  100

18) Your EC2 component receives a message from a message queue. The message will then become invisible for 30 seconds. What API request must be called in order for the VisibilityTimeout not to make the message visible again?
= DeleteMessage

Explanation
The message will become invisible again if the worker instance that is processing the data in the message does not delete the message after it has been successfully completed. This allows another worker to then process the message again if the original worker fails to process the message.

19) Which of the following is true about S3 Server-Side Encryption?
= It uses AES-256

20) You define the following S3 bucket policy to grant users access to your bucket, but the S3 bucket policy editor will not allow you to submit it. Why is this policy not working? { "Id": "Policy1441839160967", "Version": "2012-10-17", "Statement": [ { "Sid": "Stmt1441839157568", "Action": [ "s3:ListBucket" ], "Effect": "Allow", "Resource": "arn:aws:s3::: linuxacademy.testbucket.2 " } ] }
= S3 bucket policies require a Principal be defined

21) You've enabled website hosting on a bucket named "linuxacademy.com" in the US-East-1 (US standard region). Select the URL you'll receive from AWS as the URL for the bucket.
= linuxacademy.com.s3-website-us-east-1.amazonaws.com

Explanation
The default URL for S3 hosted websites lists the bucket name first followed by s3-website-region.amazonaws.com

22) Your supervisor is upset about the fact that SNS topics that he subscribed to are now cluttering up his email inbox. How can he stop receiving email from SNS without disrupting other users’ ability to receive email from SNS?
= You can delete the subscription from the SNS topic responsible for the emails, He can use the unsubscribe information provided in the emails

Explanation
Deleting the topic would cause all message types to cease for this notification. You cannot delete the endpoint from the subscription, but you can delete the subscription from the topic.

23) When using the Ref function in CloudFormation, what do we get back if we pass in the logical ID of an AWS::EC2::Instance object?
= The object's InstanceId

Explanation
Example: i-437ba30

24) What is the only "required" CloudFormation section in a template? This section is also where you specify what AWS services are used by the template.
= resources

Explanation
CloudFormation service is designed to launch and deploy AWS resources. Thus, the only required section is the resource section which defines what AWS resources are to be launched during stack creation time.

25) You have an EC2 instance deployed with an IAM role with write access permissions to an SQS queue. The instance is attempting to write a 512 KB message to an SQS queue. What will the result of this attempt be?
= It will fail because it is greater than the 256 KB limit for SQS messages.

Explanation
While it is true that SQS requests are measured in 64 KB chunks, the maximum message size is 256 KB, so a 512 KB message will not be accepted.

26) 10.2.181.56 is a valid S3 bucket name.
= False

Explanation
Bucket names must not be formatted as an IP address.

27) S3 does not generally handle error codes with HTTP responses.
= False

Explanation
S3 handles error codes with HTTP response codes. e.g 404 - not founds 403 - permission issues etc.

28) One DynamoDB read capacity unit is equal to one strongly consistent read per second.
= True

Explanation
Strongly consistent reads require more effort and consume twice as many database resources as an eventually consistent read.

29) Which statement about DynamoDB is true?
= DynamoDB uses conditional writes for consistency.

Explanation
DynamoDB allows conditional writes to tables. Conditional writes are only performed if the current attributes of the item meet the specified conditions.

30) You have created an Elastic Load Balancer with Duration-Based sticky sessions enabled in front of your six EC2 web application instances in US-West-2. For High Availability, there are three web application instances in Availability Zone 1 and three web application instances in Availability Zone 2. To load test, you set up a software-based load tester in Availability Zone 2 to send traffic to the Elastic Load Balancer, as well as letting several hundred users browse to the ELB’s hostname. After a while, you notice that the users’ sessions are spread evenly across the EC2 instances in both AZ’s, but the software-based load tester’s traffic is hitting only the instances in Availability Zone 2. What steps can you take to resolve this problem?
= Use a third party load-testing service to send requests from globally distributed clients, Force the software-based load tester to re-resolve DNS before every request

Explanation
"If you do not ensure that DNS is re-resolved or use multiple test clients to simulate increased load, the test may continue to hit a single IP address when Elastic Load Balancing has actually allocated many more IP addresses. Because your end users will not all be resolving to that single IP address, your test will not be a realistic sampling of real-world behavior.” http://aws.amazon.com/articles/1636185810492479

31) Which of the following is not true about SWF?
= Humans can perform a decision task.

Explanation
Humans can perform an activity task, but not a decision task.

32) Which of the following are supported platforms in Elastic Beanstalk?
= Microsoft IIS, Apache

Explanation
Supported platforms are covered in this lecture: https://linuxacademy.com/cp/courses/lesson/course/613/lesson/1/module/11

33) If your table item's size is 3KB and you want to have 90 strongly consistent reads per second, how many read capacity units will you need to provision on the table?
= 90

Explanation
90 (reads per second) x 3KB/4 (round up to nearest number) = 90 Minimum capacity unit is 4KB in order to calculate required throughput we will need to take the number needed strongly consistent reads (90) and multiply it by the item request size. In order to easily solve that, we take the item size and divide by 4 (4 being the size of a read capacity unit) and round it up.

34) A local secondary index is an index that has the same hash key as the table, but a different range key.
= True

Explanation
A secondary index is a data structure that contains a subset of attributes from a table, along with an alternate key to support Query operations. With a secondary index, queries are no longer restricted to the table primary key; you can also retrieve the data using the alternate key defined by the secondary index. A table can have multiple secondary indexes, which gives your applications access to many different query patterns. A local secondary index is an index that has the same hash key as the table, but a different range key.

35) Which of the following bucket names is invalid?
= .linuxacademy.com, LinuxAcademy.com

Explanation
"." characters are allowed inside of bucket names. However, bucket names CANNOT start with "." or "-" characters.

36) Which statement about DynamoDB is true?
= DynamoDB uses optimistic concurrency control.

37) Which of the following AWS Services are offered at no cost?
= Auto Scaling, Amazon VPC

38) An item stored in a DynamoDB can contain any number of ___ associated to it.
= Attributes

Explanation
In DynamoDB, an item is a collection of attributes. Each attribute has a name and a value. An attribute value can be a number, a string, a binary, or a set of any of these types.

39) As you retrieve information from DynamoDB, you receive this error: "ProvisionedThroughputExceededException", but upon investigation you notice that you're not exceeding your table read capacity throughput. What is causing this error?
= We are exceeding a partition's throughput capacity, even if we're not exceeding the table throughput capacity

Explanation
How can we exceed a partition's capacity if we're not exceeding table capacity? Because DynamoDB distributes capacity among all of the different partitions. Since DynamoDB uses our partition keys (previously known as Hash keys) to group data in different partitions, if we query the similar data over and over again, we will exceed that partition's throughput capacity - we will have uneven distribution of load. This is why it's very important to choose partition keys that are well distributed.

40) You want 5 strongly consistent 1KB writes per second. How many units of throughput capacity do you need to provision?
= 5

Explanation
The only option for a write is strongly consistent. The throughput units needed to write 5 strongly consistent writes per second of 1KB in size is 5 x 1 =  5.

41) What is the maximum size of an S3 object?
= 5TB

Explanation
Minimum object size is 0Byte and Maximum object size is 5TB. AWS requires you to use the multi-part upload API in order to upload objects 5GB and larger. It is suggested to use the multi-part upload on objects 100MB or larger.

42) What is the minimum size of an S3 object?
= 0Bytes

Explanation
The minimum size of an object is 0 byte and the maximum size of an object is 5TB. Objects that are 5GB in size or larger must use the multi-part upload API in order to be uploaded to S3.

43) Multi-part upload API allows you to stop and resume uploads.
= True

44) Which S3 error code does not have a corresponding HTTP 404 Status code?
= MissingSecurityHeader

Explanation
An HTTP 404 status code means communication with the service was successful, but the request received a "not found" response. MissingSecurityHeader is an error message received if the S3 API call is missing security API information which prevents the request from being executed successfully. 400 bad request would be the HTTP response code for MissingSecurityHeader.

45) A global secondary index is an index with a has and range key that can be different from those on the table.
= True

Explanation
A secondary index is a data structure that contains a subset of attributes from a table, along with an alternate key to support Query operations. With a secondary index, queries are no longer restricted to the table primary key; you can also retrieve the data using the alternate key defined by the secondary index. A table can have multiple secondary indexes, which gives your applications access to many different query patterns. In a global secondary index, the Hash & Range key are different than that of the table therefore queries on the index can span all the data in the table across all partitions.

46) A SWF workflow task or task execution can live up to ______ long?
= 1 year

Explanation
SQS messages live up to 14 days, BUT an SWF workflow or task execution can last up to 1 year.

47) You are creating several DynamoDB tables for a new project. While doing so, you receive the error message, “LimitExceededException.” You are well below the maximum number of tables per account and there is no read or write activity on the tables yet. Why have you received this error?
= You attempted to create more than one table with a secondary index at a time

Explanation
You can create global and local secondary indexes at the same time you create a table, but you must wait for the first table with a secondary index to become active before creating the next one. Failure to do so produces the “LimitExceededException” error. http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html

48) Your application is trying to upload a 6 GB file to Simple Storage Service and you receive a "Your proposed upload exceeds the maximum allowed object size." error message. What is a possible solution for this?
= Use the multipart upload API for this object

Explanation
AWS S3 (Simple Storage Service) allows a maximum object size of 5TB. However, objects 5GB or larger are required to be uploaded using the multipart upload API.

49) Which of the following will not cause a CloudFormation stack deployment to rollback?
= The template contains invalid JSON syntax

Explanation
Invalid JSON syntax will cause an error message during template validation. Until the syntax is fixed, the template will not be able to deploy resources, so there will not be a need to or opportunity to rollback.

50) A recent increase in the amount of users of an application hosted on an EC2 instance that you manage has caused the instance’s OS to run out of CPU resources and crash. The crash caused several users’ unsaved data to be lost and your supervisor wants to know how this problem can be avoided in the future. Which of the following would you not recommend?
= Take frequent snapshots of the EBS volume during business hours to ensure users’ data is backed up.

Explanation
Snapshots can cause performance degradation. If your application is already under a heavy load, creating snapshots during business hours could worsen the problem. In addition, taking a snapshot of the EBS volume will not capture the users' unsaved data as it resides in the EC2 instance's memory, not on the EBS volume.

51) Each AWS account can own how many buckets?
= 100

Explanation
AWS accounts are limited to the total number of buckets allowed. Since S3 is a global namespace, the limitation is per account and not per region. The limit cannot be increased upon request to AWS.

52) DynamoDB supports two types of primary keys, "Hash Type" and "Hash and Range Type" primary keys.
= True

Explanation
These have been more recently renamed to Partition Key and Partition Key and Sort Key, though the exam may not reflect it yet.

53) A DynamoDB item is a collection of name and value attributes.
= True

54) You would like to set up a static website on S3 with the least possible effort. The URL of the website is unimportant to you. Which of the following steps are necessary?
= Upload an index document to your S3 bucket, Enable static website hosting in your S3 bucket properties, Select the “Make Public” permission for your bucket’s objects

55) Setting the VisibilityTimeout =  0 has what affect on your message?
= Makes the message immediately available

Explanation
VisbilityTimout defines how long a message is INVISIBLE to other workers after being accessed by a worker. It is invisible so the worker who retrieved the message has the opportunity to process the message and remove it from the queue. If the worker is not successfully in processing the message, the VisibilityTimout then expires and the message is again available to be accessed by another worker. This ensures that if part of your application fails the message is not lost.

56) Company B provides an online image recognition service and utilizes SQS to decouple system components for scalability. The SQS consumers poll the imaging queue as often as possible to keep end-to-end throughput as high as possible. However, Company B is realizing that polling in tight loops is burning CPU cycles and increasing costs with empty responses. How can Company B reduce the number of empty responses?
= Set the imaging queue ReceiveMessageWaitTimeSeconds attribute to 20 seconds.

Explanation
ReceiveMessageWaitTimeSeconds when set to greater than zero enables long polling. Long polling allows the Amazon SQS service to wait until a message is available in the queue before sending a response. Short polling continuously pools a queue and can have false positives. Enabling long polling reduces the number of poll requests, false positives, and empty responses.

57) Which of the following statements is true about DynamoDB?
= Requests are eventually consistent unless otherwise specified.

Explanation
Data is eventually consistent because DynamoDB maintains multiple copies of an item to ensure durability. The default read is an eventually consistent read. You can specify strongly consistent reads but it does require additional read capacity units each request. However, it will receive the most recent version of the item is you specify a strongly consistent read.

58) Which of the following types of servers would this CloudFormation template be most appropriate for? { "AWSTemplateFormatVersion" : "2010-09-09", "Description" : "My CloudFormation Template", "Resources" : { "MyInstance" : { "Type" : "AWS::EC2::Instance", "Properties" : { "InstanceType" : "t2.micro", "ImageId" : "ami-030f4133", "NetworkInterfaces" : [{ "AssociatePublicIpAddress" : "true", "DeviceIndex" : "0", "DeleteOnTermination" : "true", "SubnetId" : "subnet-0c2c0855", "GroupSet" : ["sg-53a4e434"] } ] }	} } }
= Bastion host

Explanation
The CloudFormation template specifies a public IP address for the server. A domain controller, database server, and log collection server typically would not require a public IP address. Bastion hosts do require public IP addresses.

59) Which of the following are subject to eventual consistency?
= Reads of a DynamoDB table, unless you specify otherwise

Explanation
Reads of a DynamoDB table are subject to eventual consistency by default, but you can choose strongly consistent reads instead.

60) What kind of message does SNS send to endpoints?
= A JSON document with parameters like Message, Signature, Subject, Type

Explanation
Amazon SNS messages do not publish the source/destination

61) Your application instance takes 60 seconds to process instructions received in an SQS message. Assuming the SQS queue is configured with the default Visibility Timeout, what is the best way to configure your application to ensure that no other instances retrieve a message that has already been processed or is currently being processed?
= Use the ReceiveMessage API call to retrieve the message, the ChangeMessageVisibility API call to increase the visibility timeout, and the DeleteMessage API call to delete the message when processing completes

Explanation
The message queue is using the default Visibility Timeout of 30 seconds, but the application takes 60 seconds to process the instructions from the message. It is therefore necessary to increase the Visibility Timeout of the message to prevent it from becoming visible in the queue for other instances to process while it is still being processed by the first instance. (Another solution could be to increase the visibility timeout of the entire queue.) It is also necessary for the instance to delete the message from the queue once it has finished processing it, otherwise the message will become visible in the queue after the Visibility Timeout expires.

62) By default, AWS allows you to have ____ tables per account, per region.
= 256

Explanation
Default table limit in EACH region is 256. If more tables are needed, than all is required is a request to AWS to increase the table limit.

63) Parts of a multi-part upload will not be completed until the "complete" request has been called which puts all the parts of the file together.
= True

Explanation
You first initiate the multi-part upload and then upload all parts using the Upload Parts operation (see Upload Part). After successfully uploading all relevant parts of an upload, you call this operation to complete the upload. Upon receiving this request, Amazon S3 concatenates all the parts in ascending order by part number to create a new object. In the Complete Multi-part Upload request, you must provide the parts list. You must ensure the parts list is complete, this operation concatenates the parts you provide in the list. For each part in the list, you must provide the part number and the ETag header value, returned after that part was uploaded.

64) You're creating a forum DynamoDB database for hosting web forums. Your "thread" table contains the forum name and each "forum name" can have one or more "subjects". What primary key type would you give the thread table in order to allow more than one subject to be tied to the forum primary key name?
= Hash and Range

65) At what size file should you use multi-part upload?
= 100 MB

Explanation
Objects 5GB or larger require multi-part upload API to be uploaded to AWS. However, it is best practice to use the multi-part upload api for objects 100MB or larger.

66) A corporate web application is deployed within an Amazon VPC, and is connected to the corporate data center via IPSec VPN. The application must authenticate against the on-premise LDAP server. Once authenticated, logged-in users can only access an S3 keyspace specific to the user.
= The application authenticates against LDAP, and retrieves the name of an IAM role associated with the user. The application then calls the IAM Security Token Service to assume that IAM Role. The application can use the temporary credentials to access th, Develop an identity broker which authenticates against LDAP, and then calls IAM Security Token Service to get IAM federated user credentials. The application calls the identity broker to get IAM federated user credentials with access to the appropriate

67) Your items are 6KB in size and you want to have 100 strongly consistent reads per second. How many read capacity units do you need to provision?
= 200

Explanation
100 (reads per second) x 2 (6KB/4KB = 1.5 round to 2) =  200 read throughput capacity units. A unit of read capacity is 4KB in size. In order to calculate the number of required capacity units, we take the item size (6KB) divided by the size of a single unit of read throughput capacity (4KB) and multiple that by the number of needed reads per second.

68) Which of the following statements about SQS is true?
= Messages will be delivered one or more times, and message delivery order is indeterminate.

Explanation
Due to the distributed nature of SQS, messages can be duplicated. SQS does not guarantee that messages will be delivered only once but SQS does guarantee at least one message will be delivered. It is up to the developer to build logic into the code to ensure duplicate messages do not influence your application.

69) You run an ad-supported photo sharing website using S3 to serve photos to visitors of your site. At some point you find out that other sites have been linking to the photos on your site, causing loss to your business. What is an effective method to mitigate this?
= Remove public read access and use signed URLs with expiry dates.

70) Which of the following can be increased by contacting AWS?
= S3 buckets per account, DynamoDB tables per account

71) You receive a call from a potential client who explains that one of the many services they offer is a website running on a t2.micro EC2 instance where users can submit requests for customized e-cards to be sent to their friends and family. The e-card website administrator was on a cruise and was shocked when he returned to the office in mid-January to find hundreds of angry emails complaining that customers’ loved ones had not received their Christmas cards. He also had several emails from CloudWatch alerting him that the SQS queue for the e-card application had grown to over 500 messages on December 25th. You investigate and find that the problem was caused by a crashed EC2 instance which serves as an application server. What do you advise your client to do first?
= Send an apology to the customers notifying them that their cards will not be delivered.

Explanation
If an autoscaling group had been in place, it could have prevented this situation by deploying a new application server when the first one crashed. Autoscaling can also help during peak load times, like the holiday season, by deploying additional instances to meet the increased load. Unfortunately, autoscaling cannot resolve the problem of the unsent Christmas cards at this point because the issue occurred in late December and the problem was not discovered until mid-January. The maximum time a message can remain in an SQS queue is 14 days, so these messages have already been deleted. Unless the webserver contains a log of the requests that can be used to re-create the cards, the data cannot be recovered.

72) Your supervisor calls you wanting to know why she has not been receiving email notifications for AWS billing alerts. What do you suspect the problem might be and how can you find out?
= Your supervisor has not responded to the confirmation email sent from SNS when you added a subscription for her email address. Verify by viewing Subscriptions for the appropriate Topic in SNS, The SNS Subscription is not configured for Email notifications. Verify by viewing Subscriptions for the appropriate Topic in SNS, Billing alerts are not configured. Verify by viewing Billing Alerts in Account Preferences

73) One unit of read capacity is ____ in size?
= 4KB

Explanation
One unit of read capacity is 4KB and one unit of write capacity is 1KB

74) You have reached your account limit for the number of CloudFormation stacks in a region. How do you increase your limit?
= Contact AWS.

Explanation
AWS CloudFormation by default allows 20 stacks per region to be running at any given time. In order to increase this limit all you can contact AWS through an limit increase form.

75) A unit of "read capacity" represents one strongly consistent read per second or two eventually consistent reads per second.
= True

76) You attempt to create a new S3 bucket “Linux-Academy-Bucket-12-US-East-1-Production-Envrionment-12.25.14” in the US-East-1 region and the bucket creation fails. Why?
= The bucket name uses capital letters.

Explanation
Explanation: Buckets in all regions except US-East-1 have a maximum length of 63 characters for the bucket name. US-East-1 allows up to 256 characters for the bucket name. Bucket names cannot contain capital letters. *Please note that the US-East-1 naming limit may change soon - "While the US Standard region currently allows non-compliant DNS bucket naming, we are moving to the same DNS-compliant bucket naming convention for the US Standard region in the coming months."*

77) Since S3 object are stored lexicographically, by introducing "randomness" to your S3 names it helps S3 storage distribute the I/O load across more than one partition. Given the following examples, how could you add a hashed prefix to the naming convention to increase I/O performance? bucket/2010-26-05-15-00-00/myfolder234234/photo1.jpg bucket/2010-26-05-15-00-00/myfolder3857422/photo2.jpg
= bucket/8761-2010-26-05-15-00-00/myfolder234234/photo1.jpg

Explanation
http://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadComplete.html: Amazon S3 maintains an index of object key names in each AWS region. Object keys are stored lexicographically across multiple partitions in the index. That is, Amazon S3 stores key names in alphabetical order. The key name dictates which partition the key is stored in. Using a sequential prefix, such as time-stamp or an alphabetical sequence, increases the likelihood that Amazon S3 will target a specific partition for a large number of your keys, overwhelming the I/O capacity of the partition. If you introduce some randomness in your key name prefixes, the key names, and therefore the I/O load, will be distributed across more than one partition.

78) You are working with the S3 API and receive an error message: 409 Conflict. What is the possible cause of this error?
= You're attempting to remove a bucket without emptying the contents of the bucket first.

79) While working with the S3 API you receive the error: 403 forbidden. What is the most likely cause of this?
= AccessDenied

80) You have an Amazon S3 bucket that you use to store objects. You'd like to encrypt some of the new objects you upload to this bucket. What header do you need to use in order to request server-side encryption when using the REST API?
= x-amz-server-side-encryption

81) You need to announce an emergency downtime for a production AWS web application. This downtime notification will require different sets of instructions for different devices. All of the application users signed up to receive SNS notifications from the “mywebapp” topic when they began using the application and they are currently subscribed to this topic. What are appropriate ways for you to provide timely, device-specific instructions to end users when announcing this downtime?
= Send a single message, but customize the text in the SNS message field so that each device gets only the information that is appropriate for them

Explanation
A & B could work, but C is the quickest and easiest resolution. Using the SNS JSON message generator, you can choose the appropriate endpoint types and edit the generated code to send different text to the different endpoint types.

82) While working with the S3 API, you receive the following error: 409 Conflict. What is the most likely cause?
= BucketAlreadyExists

Explanation
S3 error codes are handled with HTTP error responses. 409 conflict means there is a conflicting issue.

83) S3 names are stored lexicographically (alphabetical order).
= True

Explanation
http://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadComplete.html: Amazon S3 maintains an index of object key names in each AWS region. Object keys are stored lexicographically across multiple partitions in the index. That is, Amazon S3 stores key names in alphabetical order. The key name dictates which partition the key is stored in. Using a sequential prefix, such as time-stamp or an alphabetical sequence, increases the likelihood that Amazon S3 will target a specific partition for a large number of your keys, overwhelming the I/O capacity of the partition. If you introduce some randomness in your key name prefixes, the key names, and therefore the I/O load, will be distributed across more than one partition.

84) What would you set in your CloudFormation template to fire up different instance sizes based off of environment type? i.e. (If this is for prod, use m1.large instead of t1.micro)
= conditions

Explanation
Conditions allow you to cause different resources to be launched that are listed in the template. If a specific condition is met for the resource, then the resource is launched. Conditions are created in their own property section and then referenced in the resource declaration.

85) Your "forums" table has a primary key of "id". Using DynamoDB, you're able to query the data based on the id primary key. You need to be able to query the forums table by userId. What would you add to the table during table creation time?
= Create a secondary index.

86) A taxi company uses a mobile GPS application to track the location of each of their 60 cabs. The application records the taxi’s location to a DynamoDB table every 6 seconds. Each transmission is just under 1 KB, and throughput is spread evenly within that minute. How many units of write capacity should you specify for this table?
= 10

Explanation
60 seconds / one write per cab every 6 seconds =  10 writes per cab per minute. 60 cabs x 10 writes per cab per minute =  600 total writes per minute. 600 total writes per minute / 60 seconds =  10 writes per second.

87) DynamoDB supports cross table joins.
= False

Explanation
DynamoDB is a NoSQL database service and does not act like traditional relational databases. Relational databases allow for cross table joins. Due to the schema design of a NoSQL database, you cannot use cross table joins.

88) Your app is using SQS to create distributed applications. Your messages need to contain more information than the 256KB SQS limit size allowed. How could you solve this problem?
= Store the information in S3 and attach retrieval information to the message for the application to process

Explanation
SQS messages can contain up to 256KB of data. This data can include any information needed. In order to work around the limit issue, the message can contain information on how to access the larger dataset from another service such as S3 or DynamoDB.

89) The only SNS notification event supported by S3 is S3:ReducedRedundancyLostObject.
= False

Explanation
S3 provides the S3:ReducedRedundancyLostObject for objects that are using the Reduce Redundancy Storage class on Amazon S3. This notification is used with SNS and sends a JSON object notification to the subscribed SNS topics if an object is lost by Amazon S3. This allows you to create automation and be informed with RRS (99.9% durability storage) has an object data loss from one of your buckets. AWS now supports event notifications for object creation as well.

90) Which of the following is an incorrect S3 bucket name?
= 10.2.181.2, 1Linuxacademy.com

91) You are creating a CloudFormation template in the Singapore region which will create an S3 website bucket. You have created a parameter “LinuxAcademy” which is used to store the name of your S3 bucket, and you are hoping to create output from your template which will list the URL of the S3 website. Which of the following Join statements will provide the URL of your S3 website?
= "Fn::Join" : ["", [“http://”,{"Ref":"LinuxAcademy"},".s3-website-",{"Ref":"AWS::Region"},".amazonaws.com"]]

Explanation
The easiest way to return the URL of an S3 bucket in a CloudFormation template is “Fn::GetAtt” : [“logical name of your AWS::S3::Bucket”,”WebsiteURL”]. Of the choices above, however, Answer C is the only one with the correct Join syntax to return the valid URL of the bucket.

92) What is the default limit for CloudFormation templates per region?
= There are no limits to the number of templates

Explanation
There is no limit to the number of templates, however there is a limit of 200 stacks per AWS account.

93) You're using CloudFormation templates to build out staging environments. What section of the CloudFormation would you edit in order to allow the user to specify the PEM key-name at start time?
= Parameters Section

Explanation
Parameters property type in CloudFormation allows you to accept user input when starting the CloudFormation template. It allows you to reference the user input as variable throughout your CloudFormation template. Other examples might include asking the user starting the template to provide Domain admin passwords, instance size, pem key, region, and other dynamic options.

94) A benefit of multi-part upload is that you can upload a file as it is being created.
= True

Explanation
Multi-part upload API allows you to upload parts of an object once broken apart. As a file/object is being created, the multi-part upload API will allow you to upload the file to S3. Only after all parts of the object have been uploaded do you execute the CompleteMultipartUpload API call which completes a multi-part upload by assembling previously uploaded parts.

95) Why will the following CloudFormation template fail to deploy a stack? { "AWSTemplateFormatVersion" : "2010-09-09", "Parameters" : { "VPCId" : { "Type": "String", "Description" : "Enter current VPC Id" }, "SubnetId : { "Type": "String", "Description" : "Enter a subnet Id" } }, "Outputs" : { "InstanceId" : { "Value" : { "Ref" : "MyInstance" }, "Description" : "Instance Id" } } }
= A “Resources” section is mandatory but is not included

96) EC2 instances are launched from Amazon Machine Images (AMIs). A given public AMI:
= can only be used to launch EC2 instances in the same AWS region as the AMI is stored.

Explanation
AMIs cannot be launched into another region. In order to launch a given AMI that lives in one region, into another, you can copy the AMI from one region to another.

97) Which API call would you use to query an item by it's primary hash key?
= GetItem

Explanation
The GetItem operation returns a set of Attributes for an item that matches the primary key. If there is no matching item, GetItem does not return any data. It is suggested that you become familiar with the DynamoDB API calls.

98) By default, what event occurs if your CloudFormation receives an error during creation?
= ROLLBACK_IN_PROGRESS

99) What is one key difference between an Amazon EBS-backed and an instance-store backed instance?
= Amazon EBS - backed instances can be stopped and restarted.

Explanation
You can stop and restart your instance if it has an Amazon EBS volume as its root device. The instance retains its instance ID, but can change as described in the Overview section. When you stop an instance, we shut it down. We don't charge hourly usage for a stopped instance, or data transfer fees, but we do charge for the storage for any Amazon EBS volumes. Each time you restart a stopped instance, we charge a full instance hour, even if you make this transition multiple times within a single hour. While the instance is stopped, you can treat its root volume like any other volume, and modify it (for example, repair file system problems or update software). You just detach the volume from the stopped instance, attach it to a running instance, make your changes, detach it from the running instance, and then reattach it to the stopped instance. Make sure that you reattach it using the storage device name that's specified as the root device in the block device mapping for the instance. If you decide that you no longer need an instance, you can terminate it. As soon as the state of an instance changes to shutting-down or terminated, we stop charging for that instance.

100) You created three S3 buckets – “mydomain.com”, “downloads.mydomain.com”, and “www.mydomain.com”. You uploaded your files, enabled static website hosting, specified both of the default documents under the “enable static website hosting” header, and set the “Make Public” permission for the objects in each of the three buckets. All that’s left for you to do is to create the Route 53 Aliases for the three buckets. You are going to have your end users test your websites by browsing to http://mydomain.com/error.html, http://downloads.mydomain.com/index.html, and http://www.mydomain.com. What problems will your testers encounter?
= http://downloads.mydomain.com/index.html will not work because the “downloads” prefix is not a supported prefix for S3 websites using Route 53 aliases

Explanation
Explanation: The only allowed domain prefix when creating Route 53 Aliases for S3 static websites is the “www” prefix.

101) Which of these CloudFormation snippets of code will return an address that can be used to access our application from our browser if we're using a resource type of AWS::ElasticLoadBalancing::LoadBalancer with Logical ID "ElasticLoadBalancer"?
= "Fn::Join" : [ "", [ "http://", { "Fn::GetAtt" : [ "ElasticLoadBalancer", "DNSName" ]}]]

Explanation
The answer with "Ref" would return the Elastic Load Balancer physical ID The [ "ElasticLoadBalancer", "URL" ] is not a valid option (it should be EndpointURL instead)

102) Which of the following is NOT a common S3 API call?
= ReadObject

Explanation
ReadObject is not an S3 call. Getting a general overview of S3 API calls will help you on the exam.

103) You have items in your table that are 12KB in size and you want to have 10 strongly consistent reads per second. How many read capacity units would you need to provision?
= 30

Explanation
10 x (12/4) =  30

104) S3 bucket names may only contain only lower case letters, periods, numbers, and dashes but do not have to contain them all.
= True
