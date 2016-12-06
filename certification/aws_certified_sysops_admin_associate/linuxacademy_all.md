1) When managing our VPC in an AWS region, we want to give other teams access to create their own instances and modify the security groups inside subnets dedicated to their teams. We have to make sure the development team can NOT do anything in their subnets that could allow their instances to impact production instances in the production subnets. What can we do to separate out our VPC so that instances that the dev team can access can never interfere or interact with the ones within our production?
Correct answer
We can create NACLs that restrict which subnets can talk to each other

2) True or False: By default, there is no route between the subnets in a VPC.
Correct answer
False

3) Your company is ready to start migrating its application over to the cloud, but you cannot afford any downtime. Your manager asks you to come up with a plan of action. She also wants a solution that offers the flexibility to test the application on AWS with only a subset of users, but with the ability to increase the number of users over time. Which of these options are you most likely to recommend?
Correct answer
Implement a Route53 weighted routing policy that distribute the traffic between your on-premises application and the AWS application depending on weight.

Explanation
This option works great because we can modify the weight of one record set over the other to increase or decrease the amount of traffic. If the application on AWS is behaving properly, we can slowly increase the number of users that get routed to that application and slowly phase out the on-premises application. Otherwise, we can revert back to the on-premises application.

4) True or False: Read replicas can be created from a read replica of another read replica.
Correct answer
True

5) Your applications in AWS need to authenticate against LDAP credentials that are in your on-premises data center. You need low latency between the AWS app authenticating and your on- premises network. How can you achieve this?
Correct answer
If you don’t already have a secure tunnel, create a VPN between your on-premises data center and AWS. You can then spin up a secondary LDAP server that replicates from the on-remises LDAP server.

6) Your company has decided to deploy a “Pilot Light” AWS environment to keep minimal resources in AWS with the intention of rapidly expanding the environment in the event of a disaster in your on-premises Datacenter. Which of the following services will you likely not make use of?
Correct answer
A Gateway-Cached implementation of Storage Gateway for storing snapshot copies of on-premises data

Explanation
A Gateway-Cached implementation of Storage Gateway stores all of your data in AWS and caches your frequently-accessed data on premises. Keeping all data in AWS is not a minimal AWS implementation. A Gateway-Stored implementation of Storage Gateway would be preferred for a “Pilot Light” AWS environment, as it would allow you retain your data on-premises but take snapshot copies of the data to AWS, so it could be accessed in the event of an on-premises disaster.

7) You want to run a web application in which application servers on EC2 instances are in an Auto Scaling group spread across two Availability Zones. After monitoring for six months, we notice that only one of our web servers is needed to handle our minimum load. During our core utilization hours (8:00am-8:00pm Monday-Friday), five to six web servers are needed to handle the minimum load. Four to five days a year, the number of web servers required can go up to 18 servers. What choice would reduce our costs the most while providing the highest availability?
Correct
Correct answer
Five Reserved Instances (heavy utilization), the rest covered by on-demand instances

Explanation
Different levels of utilization for reserved instances (heavy, medium, light) have been phased out. This might still show up on the exam, however, so it's a good idea to be familiar with the concept.

8) True or False: RDS Read Replicas are synchronous in their replications.


Correct answer
False

Explanation
They are asynchronous

9) You patch the operating system on an EC2 instance and issue a reboot command from inside the instance’s OS. After disconnecting from the instance and waiting several minutes, you notice that you still cannot successfully ping the instance’s public IP address. What is the most likely reason for this?


Correct answer
Changes made during OS patching caused a problem with the instance’s NIC driver.

10) True or False: Read replicas can have Multi Availability Zone enabled.


Correct answer
False

11) Your website is hosted on 10 EC2 instances in five regions around the globe, with two instances per region. How could you configure your site to maintain availability with minimum downtime if one of the five regions was to lose network connectivity for an extended period?
Correct

Correct answer
Create a Route 53 Latency Based Routing Record Set that resolves to an Elastic Load Balancer in each region and has the Evaluate Target Health flag set to true.

12) You notice that several of your AWS environment’s CloudWatch metrics consistently have a value of zero. Which of these are you most likely to be concerned about and take action on?


Correct answer
RDS DatabaseConnections

Explanation
Zero connections to a database for a long period of time may mean you are paying for a database that is not in use. If you cannot find anyone with a legitimate use case for the database, you may want to consider taking a snapshot of it and terminating it. Zero is an ideal value for the other metrics listed.

13) You are uploading 3 gigabytes of data every night to S3 from your on-premises data center. It takes 3 hours to upload and you are uploading it to Amazon S3. You are only using half of your available bandwidth through your internet provider. How might you decrease the amount of time to back up that 3GB of data from your on-premises data center to S3?


Correct answer
You can use multipart upload to speed up the upload process, You could establish a Direct Connect connection between your on-premises data center and AWS VPC

14) We have a customer with a web application that uses cookie-based sessions to see if users are logged in. This uses the Amazon Elastic Load Balancer and Auto Scaling. When the load on the application increases, Auto Scaling launches new instances so that the load on the other instances does not increase too much. However, all of the existing users still experience slow response time. What could be the cause of this?


Correct answer
The ELB is continuing to send the request to the web app with the previously established connections in the same backend instances rather than spreading them to the new instances.

15) True or False: You can configure an internal elastic load balancer to load balance internal traffic.
Correct

Correct answer
True

16) You are running an application on an EC2 instance that needs access to stored images on Amazon S3. What would be the best practice for allowing API access from the EC2 instance to Amazon S3?
Correct

Correct answer
Launch the EC2 instances using AWS IAM roles that restrict API access for the instance

Explanation
When available, it is best practice to use IAM roles for communicating with the AWS API. You should never store API credentials on an AMI. If roles are unavailable, your next best option would be to pass the API credentials to the instance at runtime.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/66/lesson/6/module/12

17) A deny overrides an allow in which circumstances?


Correct answer
An explicit allow is set in an IAM policy governing S3 access and an explicit deny is set on an S3 bucket via an S3 bucket policy.

18) True or False: When taking a snapshot of an EBS volume there can be a performance issue: We might see a decrease in performance due to an increase in I/O operations.
Correct

Correct answer
True

19) Which of the following statements is true?


Correct answer
You can customize your AWS deployments using the Ruby programming language with OpsWorks templates., You can customize your AWS deployments using JSON templates in CloudFormation.

20) Which of the following is a security best practice for an AWS environment?


Correct answer
Enable MFA on the root user for your AWS account and use IAM users rather than the root user for administrative tasks.

Explanation
IAM user accounts should not be used for executing automated scheduled tasks on EC2 instances, and automated tasks do not use MFA. The default VPC is built for ease of use, not security. IAM user credentials should not be stored on AMIs; EC2 instances that need permission to perform actions on AWS resources should use IAM roles.

21) True or False: Multi-AZ RDS replications use asynchronous data replication.


Correct answer
False

Explanation
Data replication is synchronous

22) We have a two-tiered application with the following components. We have an ELB, three web and application servers on EC2, and one MySQL RDS database. When our load grows, the database queries take longer and slow down the overall response time for the user request. Which three options would we choose to speed up performance?
Partially Correct

Correct answer
We can shard the database and distribute the load between shards, We can create an RDS read-replica and redirect half of the database read requests to it, We can cache our database queries with ElastiCache

23) What happens during a failover process in a Multi-AZ deployment with AWS RDS instance?


Correct answer
The DNS record of the DB instance changes from the primary to the standby DB instance

Explanation
The Multi-AZ failover process does not require any action from the SysOps admin. The DNS on the backend of AWS will change from the primary to the secondary instance. This occurs during time periods such as DB failure and DB updates by AWS.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/182/lesson/2/module/12

24) You maintain an application on AWS to provide development and test platforms for your developers. Currently, both environments consist of an m1.small EC2 instance. Your developers notice performance degradation as they increase network load in the test environment. How would you mitigate these performance issues in the test environment?


Correct answer
Upgrade the m1.small to a larger instance type

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/181/lesson/3/module/12

25) Your infrastructure does not have an Internet Gateway attached to any of the subnets. What might you do in order to SSH into your EC2 instances? All other configurations are correct.


Correct answer
Create a VPN connection

26) What item, when attached to a subnet, will allow the internal subnet to communicate to external networks? (Choose two)


Correct answer
Internet Gateway (IGW), Virtual Private Gateway

27) You need to establish a secure backup and archiving solution for your company, using AWS. Documents should be immediately accessible for three months and available for five years for compliance reasons. Which AWS service fulfills these requirements in the most cost-effective way?


Correct answer
Upload data to S3 and use lifecycle policies to move the data into Glacier for long-term archiving.

28) You see an increased load on an EC2 instance that is used as a web server. You decide to place the server behind an Elastic Load Balancer and deploying an additional instance to help meet this increased demand. You deploy the ELB, configure it to listen for traffic on port 80, bring up a second EC2 instance, move both instances behind the load balancer, and provide customers with the ELB’s URL - https://mywebapp-1234567890.us-west-2.elb.amazonaws.com. You immediately begin receiving complaints that customers cannot connect to the web application via the ELB’s URL. Why?


Correct answer
You specified https:// in the ELB’s URL, but the ELB is not configured to listen on port 443.

Explanation
Specifying https:// directs web traffic to port 443. If you only configured a listener for port 80 on the ELB, traffic on port 443 will not be accepted.

29) What would be a reason you would upgrade to Direct Connect instead of a traditional VPN connection?
Correct

Correct answer
You gain higher bandwidth and consistent network connectivity

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/162/lesson/2/module/12

30) Which of the following will cause a noticeable performance impact on an RDS Multi-AZ deployment?


Correct answer
None of these

31) If we want to be able to monitor billing and cost metrics, what AWS configuration do we need to enable and use?


Correct answer
Billing Alerts in Account Preferences

Explanation
CloudWatch is used to monitor billing and cost metrics, BUT we are required to enable Billing Alerts in our Account Preferences before being able to create billing alerts with CloudWatch.

32) Which of the following could be a procedure for disaster recovery as it relates to RDS?


Correct answer
Create a read replica in a different region. In the event of a failover, promote the read replica as the primary and change the DNS for your application to point to the new primary and then enable Multi AZ.

33) Which option below is part of the failover process for a Multi-AZ deployment with an RDS instance?


Correct answer
The DNS for the primary DB instance is switched to the standby DB instance

34) You are running an EC2 instance serving a website with an SSL certificate. Your CPU utilization is constantly high. How might you resolve this issue?
Correct

Correct answer
Offload the SSL cert from the EC2 instance and configure it on the Elastic Load Balancer

35) A colleague noticed that CloudWatch was reporting that there has not been any connections to one of your MySQL databases for several months. You decided to terminate the database. Two months after the database was terminated, you get a phone call from a very upset user who needs information from that database to run end-of-year reports. What can you do?
Correct

Correct answer
If you took a manual snapshot of the database, you can restore the database from that snapshot.

Explanation
Manual snapshots persist even after a database is terminated. There is not an expiration period for manual snapshots. While automated backups do have a maximum retention period of 35 days, they are deleted at the time a database is terminated.

36) Which of the following would you be likely to schedule during a maintenance window (rather than during business hours) when working in a Multi-AZ RDS environment?


Correct answer
All of these

Explanation
While patches and upgrades can be performed with minimal downtime in a Multi-AZ environment, any work that requires a failover of the database or functional changes to the database or underlying OS can still impact connectivity and should be performed during a maintenance window.

Further Reading
http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html

37) You have been tasked by your manager to build a tiered storage setup for database backups and their logs. These backups must be archived to a durable solution. After 10 days, the backups can then be archived to a lower priced storage tier. The data, however, must be retained for compliance policies. Which tiered storage solution would help you save cost, and still meet this compliance policy?


Correct answer
Set up an independent EBS volume where we can store daily backups and then copy these files over to S3, where we configure a bucket that has a lifecycle policy to archive files older than 10 days to AWS Glacier

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/79/lesson/4/module/12

38) You are running a legacy application that has a hardcoded IP address in your application. How might you apply high availability to the instance running that application?
Correct

Correct answer
Assign an elastic IP address to the EC2 instance, have a backup instance running. In the event of failure, move the Elastic IP from the primary instance to the backup instance.

39) What would we need to attach to a Bastion host or NAT host for high availability in the event that the primary host went down and that we needed to send traffic to a secondary host?


Correct answer
Elastic IP Address

Explanation
EIPs can be detached from the primary host and attached to the secondary host

40) You have multiple AWS users with access to an Amazon S3 bucket. These users have permission to add and delete objects. If you wanted to prevent accidental deletions, what might you do to prevent these users from performing accidental deletions of an object?


Correct answer
You can use MFA to prevent accidental deletions of an object

41) What is the most likely reason you are being charged for an instance you launched from a free-tier eligible AMI?
Correct

Correct answer
Your account has passed the one-year trial period

42) We need to run a business intelligence application against our production database. This application requires near real time data from the database. How might we configure our RDS setup so that our application does not increase I/O load against our production database?


Correct answer
Create a read replica from the production instance and point the application to the read replica

43) Your RDS instance is consistently maxed out on its resource utilization. What are multiple ways to solve this issue? (Choose three)
Partially Correct

Correct answer
Fire up an ElastiCache cluster in front of your RDS instance., Increase RDS instance size., Offload read-only activity to a read replica if the application is read-intensive.

44) You have an Elastic Load Balancer with an Auto Scaling group for your application. You also have 4 running instances and you have Auto Scaling enabled. Some of those instances are running in one Availability Zone, and others are in a different Availability Zone. Some instances within one of the zones are not available to the ELB. What could be the cause?


Correct answer
The ELB isn’t configured for that Availability Zone

45) Your AWS application is set up to use Auto Scaling with an ELB. To be sure that your application is performing its best and the page loads quickly, what, precisely, could you monitor in CloudWatch?
Correct

Correct answer
Monitor your ELB latency using CloudWatch metrics

Explanation
CloudWatch provides latency metrics which monitor the time it takes for the request to go from the Elastic Load Balancer to the instance and back. Latency is a good metric to determine if our Elastic Load Balancer is healthy.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/177/lesson/7/module/12

46) Assuming you have kept the default settings and are using the automated backup services provided by AWS, which of the following will retain automated backups?


Correct answer
None of these

Explanation
Automated backups of RDS databases are deleted when an RDS instance is terminated. Only manual snapshots of an RDS database remain after the RDS instance is terminated. The same goes for EBS volumes, but on top of that, AWS does not offer an automated backup solution for volumes attached to EC2 instances.

47) What is the result of the following bucket policy? { "Statement": [ { "Sid": "Sid1", "Action": "s3:*", "Effect": "Allow", "Resource": "arn:aws:s3:::mybucket/*.", "Principal": { {"AWS": ["arn:aws:iam::5555555555:user/jeff"]} } }, { "Sid": "Sid2", "Action": "s3:*", "Effect": "Deny", "Resource": "arn:aws:s3:::mybucket/*", "Principal": { "AWS": [ "*" ] } } ] }


Correct answer
It will deny all access to the bucket mybucket

Explanation
Explicit denies override allows

48) What might be the cause of an EC2 instance not launching in an auto-scaling group?
Partially Correct

Correct answer
The Availability zone is no longer supported, Invalid EBS device mapping, The key pair associated with EC2 instance does not exist

49) In your infrastructure, you are running a corporate application using a T2.Small instance. You are also using a NAT instance so that your private instances can reach out to the internet without being publicly available. What is one thing that we should do to speed up bandwidth and performance?


Correct answer
Increase your T2.Small instance to a M3.Small or M3.Medium

Explanation
Instance size has a direct influence on the amount of data your instance can send and receive. If your AWS environment has many instances using NAT availability, a network bottleneck could occur. Increasing the instance size will increase the available network throughput.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/181/lesson/2/module/12

50) In your LAMP application, you have some developers that say they would like access to your logs. However, since you are using an AWS Auto Scaling group, your instances are constantly being re-created. What would you do to make sure that these developers can access these log files?


Correct answer
Set up a central logging server that you can use to archive your logs; archive these logs to an S3 bucket for developer-access.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/79/lesson/3/module/12

51) Your company’s website is hosted on several EC2 instances behind an Elastic Load Balancer. Every time the development team deploys a new upgrade to the web application, the support desk begins receiving calls from customers being disconnected from their sessions. Customers’ session data is very important, as it contains their shopping cart information, and this information is lost when the customers’ sessions are disconnected. Which of the following steps can be taken to prevent customers’ shopping cart data from being lost without affecting website availability? (Choose Two)


Correct answer
Use ElastiCache to store session state., Enable connection draining and remove instances from the Elastic Load Balancer prior to upgrading the application on those instances.

Explanation
Storing session state in ElastiCache will allow an instance to become unavailable without losing session data. Removing instances from the Elastic Load Balancer prior to upgrading them will prevent users from establishing new sessions on instances that are about to receive the application upgrade.

52) Select all that apply: Per the AWS Acceptable Use Policy, penetration testing of EC2 instances:


Correct answer
may be performed by the customer against their own instances with prior authorization from AWS

53) Your company is being audited by a third party IT auditing service; they have asked you for details about the physical network and virtualization infrastructure. What do you tell them?


Correct answer
You go to your AWS rep and AWS will give that information to the third party in charge of doing your audit

54) You are managing a large magazine application inside of Amazon Web Services. Your company posts an article that gets picked up internationally, causing millions of visitors to hit your application. Such a large increase in traffic causes strain on your DB server which is dynamically servicing the blog content. How might you quickly resolve this issue and make the blog post infinitely scaleable?


Correct answer
Create a static HTML page using S3 and use Route 53 to point the DNS to the static S3 bucket.

55) Which features can be used to restrict access to data in S3? (Choose 3)
Partially Correct

Correct answer
Create a CloudFront distribution for the bucket, Set an S3 bucket policy, Set an S3 ACL on the bucket or the object

56) Your company's compliance department mandates that within your multi-national organization, all data for customers in the UK must never leave UK servers and networks. Similarly, US data must never leave US servers and networks without explicit authorization first. What do we have to do to comply with this requirement in our web-based applications running on AWS in EC2? The user has already set up a user profile that states their geographic location.


Correct answer
We can run EC2 instances in multiple regions, and leverage a third-party data provider to determine whether a user should be redirected to the appropriate region based on that user’s profiles.

57) Which of the following can be overridden at the EC2 instance level?


Correct answer
The choice to not use dedicated tenancy at the VPC level., An IAM policy explicitly allowing a user the right to terminate all EC2 instances.

Explanation
The default option for a VPC is to not use dedicated tenancy, but that can be overridden at the instance level. If the option to use dedicated tenancy is explicitly set at the VPC level, however, it cannot be overridden at the instance level. Explicit denies in IAM policies always trump explicit allows, so a user who is allowed to terminate all EC2 instances in an account can be denied the permission to terminate a particular instance.

58) Assuming you have kept the default settings and have taken manual snapshots, which of the following manual snapshots will be retained?


Correct answer
A snapshot of an EBS root volume when the EC2 instance is terminated, A snapshot of an RDS database when the RDS instance is terminated

Explanation
Manual snapshots of RDS databases and EBS volumes persist after instance termination. You cannot snapshot an EC2 instance store volume.

59) In order for reserved instances to reduce the cost of running instances, those instances must match the exact specifications of the reserved instance including: Region, Availability Zone, and instance type.
Correct

Correct answer
True

60) What AWS services give you access to the underlying operating system? (Choose three)
Correct

Correct answer
EC2, Amazon EMR, Elastic Beanstalk

61) You have enabled a CloudWatch metric on your Memcached ElastiCache cluster. Your alarm is triggered due to an increased amount of evictions. How might you go about solving the increased eviction errors from the ElastiCache cluster? (Choose Two)


Correct answer
Increase the node size, Add a node to the cluster

62) Instance A and instance B are running in two different subnets, A and B, of a VPC. Instance A is not able to ping instance B. What are two possible reasons for this?


Correct answer
The security group attached to instance B does not allow inbound ICMP traffic, The NACL on subnet B does not allow outbound ICMP traffic

Explanation
Every route table contains a local route that enables communication within a VPC. This route cannot be modified or deleted, so that eliminates the routing issue. "The NACL on subnet B does not allow outbound ICMP traffic" is one of the correct answers because NACL is stateless - return traffic has to be explicitly allowed by rules. Because we are not allowing outbound ICMP traffic, the ping from instance A never gets a response.

63) If you configure a VPC with an Internet gateway that has a private and a public subnet, with each subnet in a different Availability Zone. The VPC also has a dual-tunnel VPN between the Virtual Private Gateway and the router in the private data center. You want to make sure that you do not have a potential single point of failure in this design. What could you do to make sure we achieve this above environment?


Correct answer
You set up a secondary router in your private data center to establish another dual-tunnel VPN connection with your Virtual Private Gateway.

64) You manage a popular blog website on EC2 instances in an Auto Scaling group. You notice that between 8:00 am and 8:00 pm, you see a 50% increase in traffic to your website. In addition, there are occasional random 1 to 2-hour spikes in traffic and some users are seeing timeouts when trying to load the index page during those spikes. What is the least cost-effective way to manage this Auto Scaling group?


Correct answer
Use reserved instances for the instances needed to handle the load during traffic spikes

Explanation
Reserved instances become cost-effective when they are in use for greater than 30% of the time. Using reserved instances to handle the brief spikes in traffic would not be cost effective.

65) You have been tasked with identifying an appropriate storage solution for a NoSQL database that requires random I/O reads of greater than 10,000 4kB IOPS. Which EC2 option will meet this requirement?


Correct answer
EBS provisioned IOPS, EBS optimized instances

Explanation
EBS volumes only allow you to provision up to 4,000k IOPS per volume. EBS optimized instances have greater IOPs and can go up to 16K. Provisioned IOPS can also achieve 10,000 IOPS at 200GiB. Combining EBS optimized with PIOPS can give you reliable performance.

Further Reading
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html

66) For which of the following reasons would you not contact AWS?


Correct answer
Request consolidated billing for multiple AWS accounts owned by your company

67) We are preparing for our regularly scheduled security assessment. What two configuration management practices should our organization have implemented?


Correct answer
Determine that our remote administrative access is performed securely, Make sure that S3 bucket policies and ACLs correctly implement our security policies

68) Your supervisor sends you a list of several processes in your AWS environment that she would like you to automate via scripts. Which of the following list items should you set as the highest priority?
Correct

Correct answer
Implement CloudWatch alerts for EC2 instances’ memory usage

69) You manage EC2 instances in two different VPCs and you would like instances in both VPCs to be able to easily communicate with each other. You are considering using VPC peering. Will this work? (Choose Two)


Correct answer
Yes, as long as the VPC’s are in the same region., Yes, as long as the VPCs’ CIDR blocks don’t overlap.

Further Reading
http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-peering.html

70) True or False: By using NACLs at the subnet level, you can create security entries to ensure that other applications such as development applications do not accidentally have any malicious effects against your primary application.
Correct

Correct answer
True

Explanation
NACLs allow you to block/allow traffic at the subnet level. NACLs can be used to prevent any "accidental" traffic from affecting other AWS apps in your environment.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/66/lesson/4/module/12

71) Your RDS database is experiencing high levels of read requests during the business day and performance is slowing down. You have already verified that the source of the congestion is not from backups taking place during the business day, as automatic backups are not enabled. Which of the following is the first step you can take toward resolving the issue?


Correct answer
Enable automated backups of the database.

Explanation
A read replica of the database cannot be created until automated backups are enabled. Your first step should be to enable automated backups. Once automated backups are enabled, you can proceed with creating a read replica of the database and offloading some client read requests to .

72) What is the result of the following bucket policy? { "Statement": [ { "Sid": "SID1", "Effect": "Allow", "Principal": { "AWS": "*" }, "Action": "s3:*", "Resource": "arn:aws:s3:::mybucket/*", "Condition": { "IpAddress": { "aws:SourceIp": "50.97.0.0/32" } } } ] }


Correct answer
It will deny all access to the S3 mybucket bucket except for requests coming from the IP 50.97.0.0

73) You notice that several of your AWS environment’s CloudWatch metrics are hovering near a value of 100. Which of these are you least concerned about?


Correct answer
ElastiCache CurrConnections

Explanation
A high number of connections is not necessarily a bad thing, if there are adequate resources to service those connections. 100% usage of resources for the other options typically means they are strained under a heavy load. A high SpilloverCount for an Elastic Load Balancer is also bad, as you do not want requests to be rejected.

74) You manage a technology blog website on EC2 instances in an Auto Scaling group behind an Elastic Load Balancer. Traffic volume to the site is consistently low, except during several weeks of the year when major technology conferences are occurring, when traffic increases 300 percent. What is the least advisable way to manage this environment?


Correct answer
Upgrade the reserved instances that handle the typical load for the website to larger reserved instances during technology conference weeks.

Explanation
Upgrading the size of reserved instances means you incur a cost to reserve resources for the entire period of the reservation, which at a minimum of one year, is much more commitment than is needed for a few week-long conferences. It's better to keep the reserved instances sized properly to handle the typical load and use on-demand instances to handle the spikes.

75) How might you assign permissions to an EC2 instance so that the EC2 custom CloudWatch metric scripts can send the required data to Amazon CloudWatch?


Correct answer
Assign an IAM role to the EC2 instance at creation time with permissions to write to CloudWatch

76) True or False: In a Network ACL an explicit Deny always overrides an explicit Allow.


Correct answer
False

Explanation
Rules are evaluated in order depending on the rule number. As soon as a matching rule is found, it is applied, even if there is another rule contradicting the first rule.

77) Which one of the below setups would need a custom CloudWatch metric in order to be able to monitor it?


Correct answer
Disk usage percentage of an Elastic Block Store volume

78) You have enabled a CloudWatch metric on your Redis ElastiCache cluster. Your alarm is triggered due to an increased amount of evictions. How might you go about solving the increased eviction errors from the ElastiCache cluster?


Correct answer
Increase the size of your node

79) Your EC2 instance has a system static check error with an error message of loss of network connectivity. What is the best way to attempt to resolve the EC2 instance status check error? (Choose two)


Correct answer
Attempt to change the physical host that the instance is on by stopping and starting the instance , Terminate the instance and build a new one

80) How would you restore an EBS snapshot to an EC2 instance?
Correct

Correct answer
Create a new volume from the snapshot, attach the volume to the EC2 instance, pre-warm the volume and mount it to the device

81) Which of the following services have automated backups?
Partially Correct

Correct answer
RDS, Redshift, ElastiCache

82) Your company is setting up an application that is used to share files. Because these files are important to the sales team, the application must be highly available. Which AWS-specific storage option would you set up for low cost, reliability, and security?


Correct answer
Use Amazon S3, which can be accessed by end users with signed URLs.

83) A colleague noticed that CloudWatch was reporting that there has not been any connections to one of your MySQL databases for several months. You decided to terminate the database. Two months after the database was terminated, you get a phone call from a very upset user who needs information from that database to run end-of-year reports. You are hopeful that you can restore the database to full functionality from a snapshot, but your database administrator is not quite as confident. Why?


Correct answer
The MySQL database was not using a transactional database engine such as InnoDB and may not restore properly.

84) We have terminated an instance which had a root EBS volume attached to it. What do we do now if we need to access the important data that was on this volume if we created this instance with the default storage options?


Correct answer
If we did not first take a snapshot of the EBS volume we will not be able to access the data after an instance termination because the volume was deleted

Explanation
By default, EBS root volumes are configured to terminate upon instance termination; however, when creating an EC2 instance we have the option to un-select the volume deletion option. We must also create snapshots of the EBS volume which we can restore the data from.

85) You run a stateless web application with the following components: an Elastic Load Balancer, three Web/Application servers on EC2, and a MySQL RDS database with 5000 Provisioned IOPS. Average response time for users is increasing. Looking at CloudWatch, you observe 95% CPU usage on the Web/Application servers and 20% CPU usage on the database. The average number of database disk operations varies between 2000 and 2500. How would you improve performance? (Choose Two)


Correct answer
Choose a different EC2 instance type for the Web/Application servers with a more appropriate CPU/Memory ratio, Use Auto Scaling to add additional Web/Application servers based on CPU load threshold

86) Which of the following CloudWatch metrics require a custom monitoring script to populate the metric?
Correct

Correct answer
Swap Usage, Available Disk Space

87) You manage a social media website on EC2 instances in an Auto Scaling group. You have configured your Auto Scaling group to deploy one new EC2 instance when CPU utilization is greater than 90% for 3 consecutive periods of 10 minutes. You notice that between 6:00 pm and 10:00 pm every night, you see a gradual increase in traffic to your website. Although Auto Scaling launches several new instances every night, some users complain they are seeing timeouts when trying to load the index page during those hours. What is the least cost-effective way to resolve this problem?
Correct

Correct answer
Increase the minimum number of instances in the AutoScaling group

Explanation
Increasing the minimum number of instances in the AutoScaling group will keep more instances running around the clock, thus making it a very inefficient way to manage cost. The other options all increase the AutoScaling group's sensitivity to an increase in load and enable it to respond quicker to increased load by spinning up instances as soon as they become necessary.

88) Best practice is to pre-warm:


Correct answer
EBS volumes newly created from snapshots. Pre-warm by accessing each block once.

Explanation
The read and write back method is used to pre-warm EBS volumes created from a snapshot. Fresh EBS volumes do require read or write back during pre-warming. Elastic load balancers should be pre-warmed prior to an anticipated large spike in traffic, but this is done by contacting AWS to provision additional back-end resources, not by a read and write back command.

89) You have an Amazon VPC that has a private subnet and a public subnet in which you have a NAT instance server. You have created a group of EC2 instances that configure themselves at startup by downloading a bootstrapping script from S3 that deploys an application via GIT. Which one of the following setups would give us the highest level of security?
Correct

Correct answer
EC2 instances in our private subnet, no EIPs, route outgoing traffic via the NAT

Explanation
EC2 instances in this example do not need to be in the public subnet, because the private subnet has access to resources in the public subnet, and therefore can access the NAT instance. That way, we can make sure those EC2 instances are hidden from public access.

90) You have been asked to maintain a small AWS environment consisting of five on-demand EC2 web server instances. Traffic from the Internet is distributed to these servers via an Elastic Load Balancer. Your supervisor is not pleased with a recent AWS bill. Assuming a consistent, moderately high load on the web servers, what option should you recommend to reduce the cost of this environment without negatively affecting availability?
Correct

Correct answer
Use reserved EC2 instances rather than on-demand instances.

Explanation
Auto Scaling can often save money in environments with variable load, but would likely not help reduce costs in an environment with a consistent high load spread across all servers. Reserved instances are recommended for instances with a consistently high load. Removing the ELB or using spot instances would save money, but could decrease availability.

91) You support a website with a large user base concentrated on the east coast, but very few users outside of that region. Traffic load is much heavier on the site during business hours so you are planning to implement Auto Scaling to optimize the number of running EC2 instances to meet the traffic load throughout the day. You are also looking for a solution to distribute traffic evenly among those instances. Which of the following solutions will distribute traffic most evenly among the EC2 instances hosting this website in the US-East-1 region?
Correct

Correct answer
Place the instances behind an Elastic Load Balancer with stickiness disabled.

Explanation
Elastic Load Balancers with sticky sessions configured may not distribute traffic equally between EC2 instances. Latency-based routing won’t evenly distribute the load among all instances, since the users are not evenly distributed and all the instances are in the same region.

92) Your supervisor is concerned about losing read access to your RDS database in the unlikely event of an AWS regional failure. You design a plan to create a read replica of the database in another region, but your supervisor sees a problem with this plan. What problem does he see?


Correct answer
Your database is using PostgreSQL, which does not support cross-region replication.

Explanation
Note: PostgreSQL on RDS now supports cross-region read replicas since June 2016, but please keep in mind that the exam probably won't be updated for a while. Read replicas are supported in different regions than the source RDS database, but only when using MySQL 5.6. You cannot synchronous replication between the two regions because, while latency is an important metric, read replicas use asynchronous replication, not synchronous replication. You cannot VPC peer between VPCs in different regions and because replication does not require VPC peering.

93) We have developed a mobile application that gets downloaded several hundred times a week. What authentication method should we enable for the mobile clients to access images that are stored in an AWS S3 bucket that provides us with the highest flexibility and rotates credentials?
Correct

Correct answer
Identity Federation based on AWS STS using an AWS IAM policy for the respective S3 bucket

94) We have a web application that is using Auto Scaling and an ELB. We would like to monitor the application to make sure that it maintains a good quality of service for our customers, defined by the application’s page load time. What metic within CloudWatch can we use for this?


Correct answer
The latency that is reported by the ELB

95) Given the following IAM policy: { "Version": "2014-19-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:Get*", "s3:List*" ], "Resource": "*" }, { "Effect": "Allow", "Action": "s3:PutObject", "Resource": "arn:aws:s3:::corporate_bucket/*" } ] } What does the IAM policy allow?


Correct answer
The user is allowed to read objects from the bucket named ‘corporate_bucket’, The user is allowed to write objects into the bucket named ‘corporate_bucket’

96) True or False: If Multi-AZ is enabled and automated backups occur on your instance, your application will experience performance issues due to the increased I/O operations caused by the automated backup.


Correct answer
False

Explanation
Automated backups are performed on the backup instance instead of the source database instance in order to avoid this performance degradation.

97) You have decided to extend your on-site data center to Amazon Web Servers by creating a VPC. You already have multiple DNS servers on-premises. You are using these DNS servers to host DNS records for your internal applications. You have a corporate security network policy that says that a DNS name for an internal application can only be resolved internally and never publicly over the internet. Your existing on-premises data center is already connected to your VPC using IPSec VPN. You are deploying new applications within your AWS service that need to resolve these new applications by name. How might you set up the scalable DNS architecture?
Correct

Correct answer
Create a DNS option set that includes both the DHCP options with domain-name-servers=AmazonProvidedDNS and your internal DNS servers

98) What sort of host might you set up in your AWS environment that can be used as a way to “hop” into your environment to gain access to secure servers within a private subnet?


Correct answer
Bastion host

99) In the shared responsibility model at AWS, what two options are you responsible for in the case of an audit? (Pick two)
Correct answer
The operating systems' administrators group, An application that you have running within AWS EC2

100) What is the result of the following bucket policy? { "Statement": [ { "Sid": "Sid2", "Action": "s3:*", "Effect": "Allow", "Resource": "arn:aws:s3:::mybucket/*.", "Condition": { "ArnEquals": { "s3:prefix": "finance_" } }, "Principal": { "AWS": [ "*" ] } } ] }
Correct answer
It will allow all actions only against objects with the prefix finance_

101) What are some steps you can take to optimize costs on AWS? (Choose three)
Partially Correct

Correct answer
Purchase reserved instances, Detach underutilized EBS volumes and take a snapshot of the EBS volume and then delete the EBS volume, For RDS DB instances that consistently have 0 connections, take a snapshot of the instance and terminate the instance

102) You have created an application that utilizes Auto Scaling behind an Elastic Load Balancer. You notice that user's sessions are not evenly distributed on the newly spun up instances. What could be a reason that your users' web sessions are stuck on one instance and not using others?
Correct answer
Your ELB is sending all the sessions to the old instance and not evenly sending sessions to all new instances that are spun up during Auto Scaling because of sticky sessions

Explanation
If sticky sessions are enabled on the Elastic Load Balancer then the load balancer will "remember" what instance that request was sent to and will continue to send that request to the same instance.

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/181/lesson/5/module/12

103) True or False: AWS is solely responsible for the security on the guest operating system.
Correct answer
False

104) Rule 100 in a NACL associated with subnets A and B denies HTTP traffic from 0.0.0.0/0. Rule 105 in the same NACL allows HTTP traffic from 0.0.0.0/0. EC2 Instances in subnet A are associated with a security group that allows HTTP traffic from 192.168.0.0/24. EC2 Instances in subnet B are associated with a security group that denies HTTP traffic from 128.168.0.0/24. Which of the following statements are true?
Correct answer
HTTP traffic from the internet will be denied to EC2 instances in both subnets due to the NACL rules.

Explanation
Rule 105 is the higher number rule and will not be evaluated. NACL rules are evaluated in order from lowest to highest so HTTP traffic from the internet will be denied to instances in subnet B.

105) When working with Amazon RDS, by default, AWS is responsible for implementing which two management-related activities?
Correct answer
Installing and periodically patching the database software, If automated backups are enabled, creating and maintaining automated database backups with a point-in-time recovery of up to five minutes

Further Reading
https://linuxacademy.com/cp/courses/lesson/course/79/lesson/3/module/12

106) A successful systems administrator does not need to create a script for:
Correct answer
Automating backups of RDS databases

Explanation
AWS offers automated backups of RDS, thus it is not a requirement to script this task.
