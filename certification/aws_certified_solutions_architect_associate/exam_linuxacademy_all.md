1) Your supervisor asks you to create a decoupled application whose process includes dependencies on EC2 instances and servers located in your company’s on-premises datacenter. Which of these are you least likely to recommend as part of that process?
= SQS polling from an EC2 instance using IAM user credentials

Explanation
An EC2 IAM role should be used when deploying EC2 instances to grant permissions rather than storing IAM user credentials in EC2 instances

2) In the basic monitoring package for EC2, Amazon CloudWatch provides the following metrics:
= Hypervisor visible metrics, such as CPU utilization

3) You have 8 instances running on your VPC and all 10 of your users (5 production and 5 development) currently have access to all the instances. However, you have been told that because 4 of the instances are used for production and 4 are used for development you will need to set up access so that the 5 production people can only access the production server and the 5 development people can only access the development server. Using policies, which of the following would be the best way to accomplish this?
= Define the tags on the test and production servers and add a condition to the IAM policy which allows access to specific tags

4) When a snapshot is being taken against an EBS volume, the volume becomes unavailable and the instance no longer has the ability to communicate with the EBS volume until the snapshot is complete.
= False

5) Your EC2 instances are configured to run behind an Amazon VPC. You have assigned two web serves instances to an Elastic Load Balancer. However, the instances and the ELB are not reachable via URL to the elastic load balancer serving the web app data from the EC2 instances. How might you resolve the issue so that your instances are serving the web app data to the public Internet?
= Attach an Internet gateway to the VPC and route it to the subnet

6) You are a consultant tasked with migrating an on-premise application architecture to AWS. During your design process you have to give consideration to current on-premise security and determine which security attributes you are responsible for on AWS. Which of the following does AWS provide for you as part of the shared responsibility model?
= Physical network infrastructure , Vitualization infrastracture

7) After building an application that makes use of an Elastic Load Balancer over port 80, you notice that your instances, even though they are healthy as part of the health check, are not serving traffic when you go to the ELB DNS cname. What might be the cause of this issue?
= The ELB security group does not have port 80 open, The EC2 instances do not have port 80 open

Explanation
Remember that health checks do not have to be performed on port 80. This is the default, yes, but it can be changed. So in this case we could have a health check configured on a different port which is why it would be marked as healthy even though the ELB security group and/or the EC2 instance security group on port 80 could be closed. Even if this scenario does not sound very likely, it is possible. AWS likes to try and trick test takers by throwing in scenarios like these, which is why we included this tricky question.

8) You design an application that checks for new items in an S3 bucket once per hour. If new items exist, a message is added to an SQS queue. You have several EC2 instances which retrieve messages from the SQS queue, parse the file, and send you an email containing the relevant information from the file. You upload one test file to the bucket, wait a couple hours and find that you have hundreds of emails from the application. What is the most likely cause for this volume of email?
= Your application does not issue a delete command to the SQS queue after processing the message

Explanation
Many instances can poll a single queue, but to keep multiple instances from processing the same SQS message, your application must delete the SQS message after processing it. While SQS does not guarantee a message will be processed only once, the same message being processed many times is probably an indication that the message is not being deleted following processing.

9) To maintain compliance with HIPPA laws, all data being backed up or stored on Amazon S3 needs to be encrypted at rest. What is the best method for encryption for your data, assuming S3 is being used for storing the healthcare-related data?
= Enable SSE on an S3 bucket to make use of AES-256 encryption , Encrypt the data locally using your own encryption keys, then copy the data to Amazon S3 over HTTPS endpoints

10) One of your more important clients is a Telecom business who needs to process some real-time data in a distributed manner. They suggest to you that they think they should use either Amazon SQS or Amazon Kinesis to achieve this and they want you to tell them what would be the difference between the two. After some research you decide that they should use Kinesis and are trying to put together some reasons for this. One of the below statements is INCORRECT, regarding this. Which one?
= Kinesis cannot route related data records to the same record processor (as in streaming MapReduce).

11) Currently you're helping design and architect a highly available application. After building the initial environment, you've found that part of your application does not work correctly until port 443 is added to the security group. After adding port 443 to the appropriate security group, how much time will it take before the changes are applied and the application begins working correctly?
= Changes apply instantly to the security group, and the application should be able to respond to 443 requests

12) You have 5 CloudFormation templates. Each template is for a different application architecture. These architectures vary between your blog apps and your gaming apps. What determines the cost of using the CloudFormation templates?
= CloudFormation does not have a cost but you are charged for the underlying resources it builds

13) You manage a web application on EC2 instances. Your website occasionally experiences brief but large spikes in traffic that cause your EC2 instances’ resources to become overwhelmed and the application to freeze up and lose recently-submitted requests from end users. You use Auto Scaling to deploy additional resources to handle the load during spikes, but the new instances do not deploy fast enough to prevent the existing application servers from freezing. Assuming you cannot find a pattern to when these spikes occur, which of the following is likely to provide the most cost-effective solution to avoid losing recently submitted requests?
= Use an SQS queue to decouple the application components

Explanation
Because of the infrequency of the spikes in traffic, keeping extra EC2 resources always deployed is not cost-effective. Pre-warming is a process used when you are anticipating a spike in demand, but in this case, the spikes are unpredictable. The use of an SQS queue allows submitted requests to be retained as messages in the SQS queue until the application resumes normal operation and can process the requests.

14) You are consulting for a healthcare company that has strict compliance and auditing requirements. When architecting the application environment on AWS, which services or service features might you enable to take advantage of monitoring to ensure auditing the environment for compliance is easy and follows the strict healthcare compliance requirements?
= CloudTrail for security logs

15) If your organization is concerned about storing sensitive data in the cloud, you should _______.
= Encrypt the file system on an EBS volume using Linux tools, Enable EBS Encyption, Enable S3 Encryption

16) You recently purchased four reserved EC2 instances in the US-East-1 region’s Availability Zone 1. Your supervisor just informed you that she would like the instances distributed equally across US-East-1 region Availability Zones 1 and 2. Can you use the reserved instances you just purchased to deploy EC2 instances in Availability Zone 2?
= Yes, you can migrate the reserved instances to Availability Zone 2

Explanation
After recent AWS updates you can now migrate reserved instances without having to sell and repurchase.

17) The AMI ID used in an Auto Scaling policy is configured in the _______.
= Launch configuration

18) Your supervisor asks you to create a highly available website which serves static content from EC2 instances. Which of the following is not a requirement to accomplish this goal?
= An SQS queue

Explanation
While an SQS queue can be an important part of a multi-step decoupled web application, it is not necessary to host a highly available static website on EC2. An auto scaling group configured to deploy EC2 instances in multiple subnets located in multiple availability zones allows an application to remain online despite an instance or AZ failure.

19) You have been told that you need to set up a bastion host by your manager in the cheapest, most secure way, and that you should be the only person that can access it via SSH. Which of the following setups would satisfy your manager's request?
= A small EC2 instance and a security group which only allows access on port 22 via your IP address

20) Your company is posting a big article on the front page of your website tomorrow. It is expected that the demand could potentially overwhelm your infrastructure. In the event of a load failure, how can you set up DNS failover to a static website?
= Use Route 53 and the failover option to failover to a static S3 website bucket or CloudFront distribution in the event of an issue

21) Which of the following relational database servers are available on Amazon RDS?
= Aurora , MariaDB, MySQL

22) Data stored on EBS volumes are automatically and redundantly stored in multiple physical volumes in the same availability zone as part of the normal operations of the EBS service at no additional charge.
= True

23) You're building out an application on AWS that is running within a single region. However, you're designing with disaster recovery in mind. Your intention is to build the application so that if the current region becomes unavailable, you can failover to another region. Part of your application relies heavily on pre-built AMIs. In order to share those AMIs with the region you're using as a backup, what process would you take?
= Copy the AMI from the current region to another region, modify the Auto Scaling groups in the backup region to use the new AMI ID in the backup region

24) Which of the following will occur when an EC2 instance in a VPC with an associated Elastic IP is stopped and started?
= All data on instance-store devices will be lost, The underlying host for the instance can be changed

25) Your company requires that all the data on your EBS-backed EC2 volumes be encrypted. How would you go about doing this?
= AWS allows you to encrypt the file system on an EBS volume on EBS volume setup

26) You manage an application that uses EC2 instances and SQS to process requests from end users. Your application is working great, but your supervisor is concerned about the cost of the AWS resources it uses. Which of the following would not help address that concern?
= Increase the visibility timeout for messages in the SQS queue

27) You are working for a startup company that is building an application that receives large amounts of data. Unfortunately, current funding has left the start-up short on cash, cannot afford to purchase thousands of dollars of storage hardware, and has opted to use AWS. Which services would you implement in order to store a virtually unlimited amount of data without any effort to scale when demand unexpectedly increases?
= Amazon S3, because it provides unlimited amounts of storage data, scales automatically, is highly available, and durable

28) Company B provides an online image recognition service and utilizes SQS to decouple system components for scaleability. The SQS consumer's readers poll the image queue as often as possible to keep end-to-end throughput as high as possible. However, Company B is realizing that polling in tight loops is burning CPU cycles and increasing costs with empty responses. How can company B reduce the number of empty responses?
= Enable long polling by setting the ReceiveMessageWaitTimeSeconds to a number > 0

29) In AWS, when a request is made, the AWS service decides whether a given request should be allowed or denied. The distinction between a request being denied or allowed by default and an explicit deny in a policy is important. Which of the following statements best describes this distinction?
= By default, a request is denied, but this can be overridden by an allow. In contrast, if a policy explicitly denies a request, that deny can't be overridden.

30) Your supervisor calls you wanting to know why an SWF workflow you created has not made any progress in the last three weeks. What is the most likely explanation for the workflow’s behavior?
= SWF is awaiting human input from an activity task you assigned to your supervisor

Explanation
SWF task and workflow execution can last up to one year, and can include tasks to be performed by on-premises servers and humans.

31) What is the difference between an availability zone and an edge location?
= An availability zone is an Amazon resource within an AWS region; an edge location will deliver cached content to the closest location to reduce latency

32) Which of the following is true of an SQS message?
= SQS messages are guaranteed to be delivered at least once

33) Your organization has been using a HSM (Hardware Security Module) for secure key storage. It is only used for generating keys for your EC2 instances. Unfortunately, the HSM has been zeroized after someone attempted to log in as the administrator three times using an invalid password. This means that the encryption keys on it have been wiped. You did not have a copy of the keys stored anywhere else. How can you obtain a new copy of the keys that you had stored on HSM?
= You cannot; the keys are lost if you did not have a copy.

34) You've been contacted by a client who is having connectivity issues on their Amazon Virtual Private Cloud and EC2 instances. After logging into the environment, you notice that the customer is using four instances that all belong to a subnet with an attached internet gateway. The instances also belong to the same security group. However, one of the instances is not able to send or receive traffic like the other three. After logging into the internal network and investigating, you find that the instance is working as expected and determine it is not an operating system issue. Which of the following is missing from the environment and is preventing that single instance from connecting?
= The EC2 instance does not have a public IP address associated with it

35) Which of the following is not expected behavior from SQS and may indicate a problem with your application?
= Messages in JSON format fail to be created in the SQS queue

Explanation
JSON is an acceptable message format. Failure to create a message in JSON format may indicate a permissions issue or the message size may be larger than the 256 KB SQS maximum message size.

36) You create an SQS queue and decide to test it out by creating a simple application which looks for messages in the queue. When a message is retrieved, the application is supposed to delete the message. You create three test messages in your SQS queue and discover that messages 1 and 3 are quickly deleted but message 2 remains in the queue. What is a possible cause for this behavior?
= The order that messages are received in is not guaranteed in SQS, Your application is using short polling

Explanation
Short polling does not query all the servers that the SQS messages can reside on, so multiple queries of the queue may be needed to retrieve all messages in the queue.

37) Which statement is true about Amazon SQS?
= Amazon SQS (Simple Queue Service) guarantees delivery of AT LEAST 1 message but cannot guarantee it will not create duplicates, Amazon SQS guarantees delivery of AT LEAST 1 message but cannot guarantee message order, although does attempt to

38) In order to establish a successful site-to-site VPN connection from your on-premise network to the VPC (Virtual Private Cloud), which of the following needs to be configured inside of the VPC?
= A public IP address on the customer gateway for the on-premise network

Explanation
When you configure a VPN, you're configuring it from the VPC and from the on-premises network. You are taking information (the public IP) from the on-premises network and configuring it inside of the VPC.

39) While implementing a disaster recovery strategy in another region, you are attempting to move the data from one EBS volume to another in a separate region. What is the best way to do this? Keep in mind this is not a live production replication copy.
= Take a snapshot of the EBS volume and copy it to the desired region

40) You can deny the AWS root account to EC2 instances via IAM policy.
= False

Explanation
You can not apply permissions to the AWS root account.

41) Which of the following is not a legitimate concern?
= US-East-1 is does not support Multi-AZ RDS deployments.

Explanation
US-East-1 supports Multi-AZ RDS deployments.

42) You recently purchased and deployed four reserved EC2 instances in the US-East-1 region’s Availability Zone 1 for a new project. Your supervisor just informed you that this project only requires two EC2 instances. Rather than selling the reserved instances, she asked you to terminate the extra instances and convert two of the on-demand instances already running in Availability Zone 1 to reserved instances. Can this be done?
= Yes, you can terminate the reserved instances and AWS will automatically begin billing the two on-demand instances as reserved instances

Explanation
If you own three Reserved Instances with the same instance type and Availability Zone, the billing system checks each hour to see how many total instances you have running that match those parameters. If it is three or less, you will be charged the Reserved Instance rate for each instance running that hour.

43) Your AWS environment contains several reserved EC2 instances dedicated to a project that has just been cancelled. Your supervisor would like to recuperate cost for these reserved instances, but also does not want to lose the data just yet in case the project is revived next fiscal year. What can you do to minimize charges for these instances?
= Take snapshots of the EBS volumes and terminate the instances, Sell the instances on the AWS Reserved Instance Marketplace

Explanation
For a reserved instance that will not be needed for a long time (or maybe ever,) the best way to recuperate cost is to preserve the instance's data via snapshot, then sell the reserved instance. If the instance is required in the future, you can deploy a new instance using an EBS volume built from the snapshot you took of the original volume.

44) One of your instances is reporting an unhealthy system status check. However, this is not something you should have to monitor and repair on your own. How might you automate the repair of the system status check failure in an AWS environment?
= Create CloudWatch metrics that stop and start the instance based off of status check alarms

45) What is the difference between an availability zone and an edge location?
= An availability zone is an Amazon resource within an AWS region, whereas an edge location will deliver cached content to the closest location to reduce latency

46) Your application's usage peaks at 90% during the hours of 9 AM and 10 AM everyday. All other hours require only 10% of the peak resources. What is the best way to scale your application so you're only paying for max resources during peak hours?
= Proactive Cycle Scaling

47) Which of the following best describes what "bastion hosts" are?
= Bastion hosts are instances that sit within your public subnet and are typically accessed using SSH or RDP. Once remote connectivity has been established with a bastion host, it then acts as a ‘jump’ server, allowing you to use SSH or RDP to log into other instances (within private subnets) deeper within your network.

48) As part of your application architecture requirements, the company you are working for has requested the ability to run analytics against all combined log files from the Elastic Load Balancer. Which services are used together to collect logs and process log file analysis in an AWS environment?
= Amazon S3 for storing ELB log files and Amazon EMR for processing the log files in analysis

49) After migrating an application architecture from on-premise to AWS you will not be responsible for the ongoing maintenance of packages for the following AWS services that your application uses:
= RDS, DynamoDB

50) In the basic monitoring package for RDS, Amazon CloudWatch provides the following metrics:
= database visible metrics such as number of connections

51) Elasticity is a fundamental property of the cloud. What best describes elasticity?
= Power to scale computing resources up and down easily with minimal friction

52) Your company is building it's first deployment on AWS and is concerned about security in the cloud. There will be a lot of online payment transactions happening once the infrastructure is deployed. Your security officer has come to you and wants to know whether they should be using the Hardware Security Module (HSM) or AWS Key Management Service (KMS) for encryption. Which of the following would be the most correct response to give him?
= KMS is probably adequate unless additional protection is necessary for some applications and data that are subject to strict contractual or regulatory requirements for managing cryptographic keys, then HSM should be used

53) What is the minimum size of an S3 object?
= 0 Bytes

54) Amazon SQS (Simple Queue Service) guarantees delivery of AT LEAST 1 message but cannot guarantee it will not create duplicates.
= True

55) Which of the following statements is FALSE regarding the role of a bastion host?
= A Bastion host should be on a private subnet and never a public subnet due to security concerns

56) You are asked to evaluate a company’s AWS environment to find ways to reduce cost. You discover they are running three production web server reserved EC2 instances with EBS-backed root volumes. These instances have a consistent CPU load of 80%. Traffic is being distributed to these instances by an Elastic Load Balancer. They also have production and development Multi-AZ RDS MySQL databases. What recommendation would you make to reduce cost in this environment without affecting availability of mission-critical systems?
= Consider not using a Multi-AZ RDS deployment for the development database

Explanation
Multi-AZ RDS databases minimize downtime, provide high availability, and reduce performance impact during backups, so they are highly recommended for production systems. Development systems may be able to get by with a standard RDS deployment, since uptime and performance requirements may be lower in a development environment.

57) What URL might you query on an EC2 instance to find the public AND private IP address of an instance?
= http://169.254.169.254/latest/meta-data/

58) While running an EC2 instance, you've been storing data on one of the instance's volumes. However, to save money, you shut down the instance for the weekend. The following week, after starting the instance, you notice that all your work has been lost and is no longer available on the EC2 instance. What might be the cause of this?
= The EC2 instance was using instance store volumes, which are ephemeral and only live for the life of the instance

59) You are testing an application that uses EC2 instances to poll an SQS queue. At this stage of testing, you have verified that the EC2 instances can retrieve messages from the queue, but your coworkers are complaining about not being able to manually retrieve any messages from the queue from their on-premises workstations. What is the most likely source of this problem?
= Your coworkers may not have permission to the SQS queue

Explanation
Short polling may fail to retrieve messages sometimes, but if no messages can be retrieved after multiple attempts, permissions are the more likely cause.

60) Amazon Glacier is designed for:
= Infrequently accessed data, Data archives

61) Which of the following services allow the administrator access to the underlying operating system?
= Amazon EC2, Amazon EMR

62) Which is an operational process performed by AWS for data security?
= Decommissioning of storage devices using industry-standard practices

63) Which of the following is an invalid VPC peering configuration?
= You have a VPC peering connection between VPC A and VPC B. VPC A also has a VPN connection to a corporate network. You use VPC A to extend the peering relationship to exist between VPC B and the corporate network so that traffic from the corporate network can directly access VPC B by using the VPN connection to VPC A

64) A colleague would like a new subnet configured in AWS for a database cluster she is building. She expects that the subnet will never need more than six IP addresses. Which of the following will likely be the most appropriate choice for this subnet?
= A /28 private subnet

Explanation
Databases generally do not require public access from the Internet, so a private subnet is likely the better choice from a security perspective. /28 is the smallest possible subnet in an AWS VPC.

65) Auto Scaling is a tool used for creating elastic and self-healing applications.
= True

66) Which region ID is the US Standard region?
= us-east-1

67) A user needs access to Elastic Load Balancing. This is the first and possibly only time that they will require this access. Which of the following choices would be the best way to allow this access?
= Delegate access to the ELB using an IAM role

68) You are using IOT sensors to monitor the movement of a group of hikers on a three day trek and send the information into an Kinesis Stream. They each have a sensor in their shoe and you know for certain that there is no problem with mobile coverage so all the data is getting back to the stream. You have used default settings for the stream. At the end of the third day the data is sent to an S3 bucket. When you go to interpret the data in S3 there is only data for the last day and nothing for the first 2 days. Which of the following is the most probable cause of this?
= Data records are only accessible for a default of 24 hours from the time they are added to a stream.

69) Given the following region design, what is the bare minimum for configuring high availability and why? Two availability zones within a region, az-a and az-b.
= Create an ELB that serves traffic to two instances, one instance in each availability zone, and enable cross-zone load balancing on the ELB, then create an Auto Scaling Group, because this applies high availability if a single availability zone is no longer available

Explanation
We need to use Auto Scaling to meet minimum requirements because otherwise, if an availability zone fails and takes an instance down with it, the only remaining instance would receive double the amount of requests (it's original amount, plus what was being distributed to the other instance). This not only creates a single point of failure, but it can also overwhelm that single instance. Instead, by having an Auto Scaling group, another instance gets automatically created to replace the unresponsive one and to continue distributing requests between two separate instances.

70) After deciding that, due to to strict contractual requirements, the latest AWS VPC that you deploy will need to incorporate AWS CloudHSM as an encryption solution, where within your AWS infrastructure would be the best place to physically locate the HSM appliances and why?
= Locating HSM appliances near your EC2 instances decreases network latency, which can improve application performance

71) To protect S3 data from both accidental deletion and accidental overwriting, you should:
= Enable S3 versioning on the bucket

72) The KPL is an easy-to-use, highly configurable library that helps you write to an Amazon Kinesis stream. It acts as an intermediary between your producer application code and the stream's API actions. One of its key concepts is aggregation. Which of the following best describes aggregation as it relates to the KPL?
= It refers to the storage of multiple records in a stream's record and allows customers to increase the number of records sent per API call, which effectively increases producer throughput

73) Your company wants to backup the onsite file server to AWS but does not want to serve the files from S3 to your office network when files need accessed. Which service and setup would you use to accomplish this task?
= Use Amazon Storage Gateway and gateway-stored volumes to store the data locally and asynchronously backup point-in-time snapshots to S3

74) To prevent in-flight tampering, all requests sent with API keys over REST or Query API should be sent over HTTPS connection.
= True

75) Your company is moving their entire 20 TB data warehouse to the cloud. With your current bandwidth it would take 2 months to transfer the data. Which service would allow you to quickly get your data into AWS?
= Amazon Import/Export

76) Your supervisor asks you to create a decoupled application using EC2 instances polling an SQS queue. Which of the following is not necessary to accomplish this goal?
= An Elastic Load Balancer to distribute traffic from EC2 instances to the SQS queue

Explanation
While an Elastic Load Balancer is often used to handle incoming web traffic requests in a highly available web application solution, it is not required for a decoupled application's EC2 instances to poll SQS. A decoupled application requires that one component of the application can fail without the entire environment failing. Using multiple EC2 instances that have been launched with a role granting SQS queue permissions and using code to poll an SQS queue allows an EC2 instance to fail, even if it has already begun processing a job because another instance is able to process the job when the message is returned to the queue.

77) When designing a cloud service based on AWS and you choose to use RRS on S3 instead of S3 standard storage type, what type of trade offs do you have to build your application around?
= RRS only has 99.99% durability and you have to design automation around replacing lost objects

78) Amazon Auto Scaling is not meant to handle instant load spikes but is built to grow with a gradual increase in usage over a short time period.
= True

79) Your supervisor asks you to create a highly available, decoupled web application. Which of the following does not help you accomplish this goal?
= IAM user credentials on EC2 instances to grant permissions to modify an SQS queue

Explanation
Elastic Load Balancers, Auto Scaling, and SQS can all play a part in a highly available, decoupled web application. IAM user credentials should not be stored on a EC2 instance.

80) When reviewing the Auto Scaling events, it is noticed that an application is scaling up and down multiple times within the hour. What design change could you make to optimize cost while preserving elasticity?
= Change the scale down CloudWatch metric to a higher threshold

81) You own an image manipulation application. Your users take a picture, upload it to your app, and request filters to be added to the image. You need to decouple the application so your users are not waiting for the image processing to take place. How would you go about doing this?
= Use Amazon SQS to store the requests using metadata and JSON in the message, use S3 to store the image, and Auto Scaling to determine when to fire off more worker instances based on queue size

82) You've been tasked with building out a duplicate environment in another region for disaster recovery purposes. Part of your environment relies on EC2 instances with preconfigured software. What steps would you take to configure the instances in another region?
= Create an AMI of the EC2 instance and copy the AMI to the desired region

83) Your company is concerned with EBS volume backup on Amazon EC2 and wants to ensure they have proper backups and that the data is durable. What solution would you implement and why?
= Write a cronjob that uses the AWS CLI to take a snapshot of production EBS volumes. The data is durable because EBS stapshots are stored on the Amazon S3 standard storage class

84) You are the system administrator for your company's AWS account of approximately 200 IAM users. A new company policy has just been introduced that will change the access of 50 of the IAM users to have unlimited access to S3 buckets. How can you implement this effectively so that there is no need to apply the policy at the individual user level?
= Use the IAM groups and add users, based upon their role, to different groups and apply the policy to group

85) Which of the following is not a benefit of a decoupled architecture using EC2, Auto Scaling, and SQS?
= An application does not become unavailable due to the deletion of a single SQS queue

Explanation
Deletion of an SQS queue used in an application will cause the application to fail.

86) You are asked to perform a security audit on a company’s AWS environment. You log in to their AWS account with the root user credentials and discover that they are using a VPN to connect to and manage their private EC2 instances. Upon further inspection, you find that they are not regularly patching their RDS instances. Finally, you notice that they are using IAM policies rather than bucket policies to manage access to their S3 buckets. What do you cite as the most critical security risk in your report?
= The company allows people to log in with their AWS account’s root user

Explanation
A bastion host is not more secure than a VPN as a means of connecting to private instances. IAM policies and S3 bucket policies are both acceptable means of controlling S3 bucket access. It is AWS's responsibility to patch RDS instances. After initial account setup, AWS account administration should be performed by IAM users rather than the root user account.

87) Which statements are true about Amazon S3?
= Provides %99.999999999 durability to S3 objects, Provides %99.99 availability to S3 objects

88) If an instance that belongs to an Elastic Load Balancer's health check fails, what occurs to the instance that fails?
= The ELB will de-register the instance and stop sending traffic to the unhealthy instance

89) Does S3 provide read-after-write consistency for new objects?
= Yes, for all regions

Explanation
This changed in June 2015 where read after write consistency is now available in all regions; however, only eventual consistency for overwrite PUTS and DELETES.

90) Your AWS environment contains several reserved EC2 instances dedicated to a project that has just been cancelled. Your supervisor wants to stop incurring charges for these reserved instances immediately and recuperate as much of the reserved instance cost as possible. What can you do to avoid being charged for them?
= Terminate the instances as soon as possible, Sell the reserved instances on the AWS Reserved Instance Marketplace

Explanation
You should terminate the instance to avoid any data transfer charges that the instance might incur if left running and sell the reserved instance in the AWS Reserved Instance Marketplace to recuperate cost.

91) Your company has moved a legacy application from an on-premise data center to the cloud. The legacy application requires a static IP address hard-coded into the backend, which prevents you from deploying the application with high availability and fault tolerance using the ELB. Which steps would you take to apply high availability and fault tolerance to this application?
= Ensure that the instance it's using has an elastic IP address assigned to it, Write a custom script that pings the health of the instance, and, if the instance stops responding, switches the elastic IP address to a standby instance

92) Your company has an application that requires access to a NoSQL database. Your IT department has no desire to manage the NoSQL servers. Which Amazon service provides a fully-managed and highly available NoSQL service?
= DynamoDB

93) You are consulting for a company with a limited budget for on-premise hardware. However, they need to store large amounts of data that is easily accessible through a network share with on-premise employees. Which AWS solution would you implement for this company?
= Configure storage gateway with Gateway-Cached Volumes

Explanation
Gateway-Stored volumes use S3 to backup the data but store locally, which means we're limited to the amount of space we allocate to the VM. With the Gateway-Cache volumes, you aren't limited in that way since you're storing all of the data on S3 and simply caching frequently-used data locally.

94) Which of the following AWS services allow you access to the underlying operating system?
= Amazon EMR, Amazon Elastic Beanstalk

95) You are consulting for a finance company that has specific backup and archiving policies. This company's RTO for all financial documents created in the past 6 months is 1 hour. The second requirement is to configure a setup that allows for all documents that are 6 months or older to be sent automatically for archiving in a lower-cost but highly durable archive environment. Given that the company is using the storage gateway, gateway-stored configuration, which of the following would be the best setup to reach the objectives?
= Enable S3 versioning with a lifecycle policy that sends objects older than 6 months to Amazon Glacier

96) You create an SQS queue with the default settings for a new application your company is deploying. While new messages are added to the queue throughout the week, management has indicated that the application which retrieves the messages should only be run during your company’s weekly Sunday evening maintenance window. It is quickly noticed on Monday morning that several messages were not processed the previous evening and the messages are no longer in the queue. What is a likely cause for this issue?
= The messages surpassed the retention period for the queue

Explanation
The default message retention period for an SQS queue is four days, so messages older than four days would have been deleted.

97) You recently purchased hardware to run a decoupled application in your on-premises datacenter. The application is working great, but has seen an increased workload in recent weeks that makes you concerned that your hardware cannot handle the load. Your supervisor asks you to analyze the possibility of expanding the application using cloud resources. You cannot completely migrate the application to AWS because of the investment you have already made in on-premises hardware. What items will most likely be included in your analysis?
= You can leverage SQS to utilize both on-premises servers and EC2 instances for your decoupled application, You can leverage SWF to utilize both on-premises servers and EC2 instances for your decoupled application

98) What is the maximum size of a general SSD EBS volume?
= 16TiB

99) For basic monitoring on AWS, which metrics are not included as part of the basic monitoring package?
= Free memory, Free swap

100) Ten students have just been employed by your company for one week and it is your task to provide them with access to AWS, through IAM. Your supervisor has come to you and said that he wants to be able to track these students as a group, rather than individually. Because of this, he has requested for them to all have the same login ID but completely different passwords. Which of the following is the best way to achieve this?
= It isn't possible to have the same login ID for multiple IAM users of the same account

101) Your supervisor is upset that a client’s purchase from your website was processed twice. You find out that the order process involves EC2 instances processing messages from an SQS queue. What action would you recommend to ensure this does not happen again?
= Modify the order process to use SWF

Explanation
The only way to ensure that a duplicate will not occur in a process is to use Amazon SWF instead of SQS. The other options can decrease the chances of duplicates in SQS, but will not eliminate them entirely.

102) After setting up your first VPC peering connection between you and one of your clients, the client requests to be able to send traffic between instances in the peered VPCs using private IP addresses. What must you do to make this possible?
= Add a route to a route table that's associated with your VPC

103) You are designing a global application that takes advantage of multiple regions. As part of your application, the need to synchronize from one region to another is required to ensure your application is serving the same data when employing latency-based Route 53 DNS records. To ensure this happens, you have determined that using the AWS CLI to sync files from the primary storage servers to S3 is the best method. How might you implement AWS CLI authentication against the S3 service?
= Create an EC2 IAM role and assign it to each EC2 instance that utilizes the AWS CLI to sync the data

104) You manage a web application on EC2 instances. Incoming requests are saved as messages in an SQS queue with the maximum message retention period. You return from a week and a half vacation to find that the part of the application which processes received requests is hung and the queue has grown to 1,000 messages. While you are working on resolving the application issue, you need to post an update to end users. What information should that update include?
= An apology for the delay in processing requests, assurance that the application will be operational shortly, and a note that all received requests will be processed at that time.

Explanation
Use of an SQS queue to decouple the application means that a virtually unlimited number of received requests can be stored in the SQS queue for a maximum of 14 days and can be processed when the portion of the application that is responsible for processing received requests becomes operational again.

105) The AMI ID used in an Auto Scaling policy is configured in the _______.
= Launch configuration

106) After building out a new VPC from scratch, you have attached an Internet gateway to the only route table within your VPC. This means all instances currently belong to a public subnet. While trying to connect to one of the instances over the Internet gateway, you are experiencing connectivity issues preventing any communication from your machine to the instance over the Internet. After investigating, you notice that the security group has proper permissions and the route table is currently as follows: 10.0.0.0/16 local 0.0.0.0/16 igw-xxxx58d8	What might be the issue?
= Change the route table Destination for the IGW to be 0.0.0.0/0

107) You are building a system to distribute confidential training videos to employees. Using CloudFront, what method would be used to serve content that is stored in S3, but not publicly accessible from S3 directly?
= Create an Origin Access Identify (OAI) for CloudFront and grant access to the objects in your S3 bucket to that OAI

108) When designing an application architecture utilizing EC2 instances and the ELB, to determine the instance size required for your application what questions might be important?
= Determining the minimum memory requirements for an application, Determine the required I/O operations

109) Your web application front end consists of multiple EC2 instances behind an Elastic Load Balancer. You configured the ELB to perform health checks on these EC2 instances. If an instance fails to pass health checks, which statement is true?
= The ELB stops sending traffic to the instance that failed its health check.

110) Your AWS environment contains several on-demand EC2 instances dedicated to a project that has just been cancelled. Your supervisor does not want to incur charges for these on-demand instances, but also does not want to lose the data just yet because there is a chance the project may be revived in the next few days. What should you do to minimize charges for these instances in the meantime?
= Stop the instances as soon as possible

Explanation
You should not terminate an instance that you may need to place back into production in a few days. The best way to minimize charges is to stop the instances to avoid any data transfer charges that the instance might incur if left running.

111) An EC2 instance retrieves a message from an SQS queue, begins processing the message, then crashes. What happens to the message?
= When the message visibility timeout expires, the message becomes available for processing by other EC2 instances

Explanation
112) You and a colleague create an SQS queue and create several messages in it. You both test your ability to manually poll the queue by using the command-line API calls. After testing, you find that your colleague’s polling attempt retrieved messages 1, 3, and 5. Your polling attempt retrieved messages 4, 6, and 8. Nether of your attempts retrieved messages 2 or 7. What is a possible cause for this behavior?
= You and your colleague did not see the same messages because of the visibility timeout, You and your colleague used short polling

Explanation
When a message is retrieved, that message is hidden from other polling attempts until the message is deleted or the visibility timeout expires. Short polling does not query all the servers that the SQS messages can reside on, so multiple queries of the queue may be needed to retrieve all messages in the queue.

113) You are setting up a VPC peering connection with another VPC. This is the first time that you have done this, and you are not that familiar with the limitations and rules. When reading up on this, you discover that there seems to be a lot of limitations and rules when it comes to VPC peering. Which of the following is NOT one of those limitations or rules?
= A placement group cannot span peered VPCs

114) An AWS VPC (Virtual Private Cloud) allows you to _______.
= Connect your cloud resources to your own encrypted IPSec VPN connections

115) By default is data in S3 encrypted?
= No, but it can be when the right APIs are called for SSE

116) You are asked to review a plan that your company has made to create a new application that makes use of SQS, EC2, Auto Scaling and CloudWatch. Which of the following action items should you advise your company not to implement?
= Utilize short polling with a wait time of 20 seconds to reduce the number of empty responses from the SQS queue

Explanation
Polling executed with a wait time of greater than 0 seconds is called long polling.

117) You are planning on creating an EC2 instance that will create S3 objects and modify CloudWatch alarms. What is the best way to deploy this instance?
= Assign an S3 policy and a CloudWatch policy to a single IAM role. Assign the IAM role to the instance at deployment time

Explanation
EC2 instances should use IAM roles, rather than IAM user credentials, to perform actions on AWS resources. An EC2 instance can only be assigned one role.
