**************************
Simple Queue Service (SQS)
**************************

= Short timeframe

First AWS service
Message orientated API
Messages can be delivered multiple times
Messages can be in any order
Need to implement app level tracking
Messages can be 256kb
Billed in 64kb chunks (4 chunks = 256)

Visibility/timeout default = 30 seconds
Visibility/timeout max = 12 hours
Message retention period = 1 minute to 14 days

Max long polling timeout = 20 seconds
-burn cpu cycles with no messages
-will wait long poll timeout
-inexpensive, save money
-pull queue once every 20 seconds

ReceiveMessageWaitTimeSeconds = set this for long polling

Fanning out
-SNS Topic -> Create/Subscribe multiple SQS queues
-deliver message to all queues

*****************************
Simple Workflow Service (SWF)
*****************************

= Long timeframe

Easily coordinate work across distributed applications
Task orientated API
Task only assigned once and never duplicated
Tracks all tasks and events

Max workflow = 1 year

Sample
Verify order, change credit card, ship order, record done

Domain = think collection of everything
-Workflow
-Activity types
-Workflow execution
Think collection of everything

(W) Worker
-Get tasks, process tasks, return results

(D) Decider
-Controls coordination of tasks

Workers/Deciders
-Do not track execution state
-Could run on an EC2 instance

*********************************
Simple Notification Service (SNS)
*********************************

publish - subscribe model, SNS notifies the message, and hence push based approach
Inexpensive pay as you go
CloudWatch or Autoscaling triggers SNS
SNS messages are stored redundantly to multiple AZs

SNS can notify
-Email
-Text / SMS
-SQS or any HTTP end point.

protocols:
-HTTP
-HTTPS
-EMAIL
-EMAIL-JSON
-SQS
-Application - messages can be customized for each protocol

SNS Dataformat - JSON (Subject, Message, TopicArn, MessageId, unsubscribeURL etc..)

********************************
Identity Access Management (IAM)
********************************

(U) User = individual
(G) Groups = collection of users with set of permissions
(R) Roles = can be applied to
-users
-services i.e EC3, Lambda

Security Assertion Markup Language (SAML)
https://signin.aws.amazon.com/saml

workflow
1.Authenticate against identity provider FIRST
2.Obtain temp security credentials (AssumeRoleWithWebIdentity)

AssumeRoleWithSAML against active directory

WebIdentityFederation
-Allow apps/mobile users to access AWS resources i.e save something to S3
-Apps sign in with known identity provider i.e facebook
-Receive token and exchange for aws credentials
-Temporary credentials from social media provider

***********
AWS Regions
***********

Code           | Name
us-east-1      | US East (N. Virginia)
us-east-2      | US East (Ohio)
us-west-1      | US West (N. California)
us-west-2      | US West (Oregon)
eu-west-1      | EU (Ireland)
eu-central-1   | EU (Frankfurt)
ap-northeast-1 | Asia Pacific (Tokyo)
ap-northeast-2 | Asia Pacific (Seoul)
ap-southeast-1 | Asia Pacific (Singapore)
ap-southeast-2 | Asia Pacific (Sydney)
ap-south-1     | Asia Pacific (Mumbai)
sa-east-1      | South America (São Paulo)

***************
Trusted Advisor
***************

(C) Cost Optimization
(P) Performance
(F) Fault Tolerance
(S) Security

***************
Storage Gateway
***************

Gateway Stored Volume
-Data on site (private cloud)
-Backed up to S3

Gateway Cached Volume
-Data in S3
-Frequently accessed date on site (private cloud)

Gateway Virtual Library (VTL)
-For backups in AWS using NetBackup, Backup Exec..

**************
Direct Connect
**************

Connection between private cloud and AWS

Benefits
-Reduce Cost
-Increase bandwidth
-Consistent network experience

***********
Elasticache
***********

-In memory cache in the cloud
-Improve web performance
-Get data from cache vs database query

Solutions
-Memcached
-Redis

Cross Origin Resource Sharing (CORS)

-Remove need for proxy server
-Allow Site X to talk/use resources in Site Y i.e Java Script, HTML5
-Cross reference resources in services EC2/S3

*********************************
Relational Database Service (RDS)
*********************************

DB Engines
-MariaDB
-Postgre SQL
-Amazon Aurora
-MySQL
-Oracle
-Microsoft SQL server

Online Transaction Processing (OLTP)
-Query data for order 1234 including name, date, address

Online Analytics Processing (OLAP)
-Query data for net profits in a region & product

***************************
Database Management Service
***************************

-Migrate existing DB to AWS
-Data type transformations, compression, transfer
-AWS schema conversion tool

***********
Cloud Front
***********

-Can read & write to edge locations
-Objects cached for life of TTL in edge location
-Can clear cached objects, but will  be charged

Edge location = where content is cached

Origin = where all files are located & can have multiple origins
-S23
-EC2
-ELB
-Route53

Distribution = Name of CDN

Types
-Web distribution = website
-RTMP = media

****************************
Elastic Load Balancers (ELB)
****************************

Not free - charged by hour & GB

Supported protocols
-http
-https (secure http)
-tcp
-ssl (secure tcp)

***************************
Simple Storage Service (S3)
***************************

Object based storage
Files 0 byte to 5TB
Unlimited Storage
Largest single put object = 5GB
Files stored in alphabetical order

Consistency
-Read after write consistency for PUTS of new objects
-Eventual consistency for overwrite PUTS & DELETES
Any new object put on S3 will be able to be read
With update or delete, then try to access immediately access, may get old version

S3      : durable, immediately available, frequently accessed
S3-IA   : durable, immediately available, infrequently accessed
S3-RA   : reduced storage, data easily reproducible
Glacier : archived data, wait 3-5 hours before accessing

S3
-key (name)
-value (data)
-version ID
-metadata
-access control list

Versioning
-can't disable once enabled
-stores all objects - can get expensive since every version of file is saved

Replication
-Cross region replication requires version to be enabled

Access
When new bucket created, DEFAULT behavior = private
Controlled by
-Bucket policy
-Access control list

Encryption | in transit
-ssl/tls i.e via https

Encryption | at rest | server side
SSE-S3  : amazon S3-managed key
SSE-KMS : amazon KMS managed key (benefits i.e. envelope key)
SSE-C   : Customer provided keys

Encryption | client side
secure at client
customer encrypts data and uploads encrypted data

URL examples

bucket  : https://s3-eu-west-1.amazon.com/bucketname
website : https://websitename.s3-website-eu-west-1.amazon.com

*********************
Elastic Compute (EC2)
*********************

Every AMI uses the XEN hypervisor on bare metal
XEN offers
-HVM
-PV

Amazon recommends HVM over PV

Paravirtual (PV)
-boot with special boot loader (PV_CRUB)
-lighter format of virtualization
-fast near native speed

Hardware Virtual Machine (HVM)
-best performance
-fully virtualized and not aware of sharing processing

Instances | On Demand
-pay by hour

Instances | Spot
-bid price, if met get instance
-instance terminated if price goes up
-good for after hour compute or compute doesn't always have to be on

Instances | Reserved
-lock in price via contract
-cheapest way to consume compute

Elastic Block Storage (EBS)

General Purpose  SSD : to 10,000 IOPS
Provisioned IOPS     : > 10,000 IOS
Magnetic             : cheap


Can't mount EBS volume to multiple EC2 Instances
By default, Amazon EBS-backed instance root volumes have the DeleteOnTermination flag set to true

            | EBS-Backed                       | Instance Store-Backed
Boot time   | Usually less than 1 minute       | Usually less than 5 minutes
Size limit  | 16 TiB                           | 10 GiB
Upgrading   | can change instance when stopped | no changes

Data persistence - EBS-Backed  
-By default, the root volume is deleted when the instance terminates.
-Data on any other Amazon EBS volumes persists after instance termination by default.

Data persistence - Instance Store-Backed
-Data on any instance store volumes persists only during the life of the instance.

Stopped state - EBS-Backed
Can be placed in stopped state where instance is not running, but the root volume is persisted in Amazon EBS

Stopped state - Instance Store-Backed
Cannot be in stopped state; instances are running or terminated

***************************
Virtual Private Cloud (VPC)
***************************

Security Group                       | Network ACL
at instance level                    | at subnet level
all rules only                       | allow & deny rules
stateful                             | stateless
return traffic automatically allowed | return traffic must be explicitly allowed
evaluate rules, the proceed          | process rules in order
instances in security group          | all instances in subnet
                                     | Every subnet must have an ACL
                                     | Can associate ACL with multiple subnets
                                     | Subnet can only have 1 ACL
                                     | default ACL allow all out/in
                                     | new ACL deny all out/in

********
DynamoDB
********

fast - flexible No sql database - single digit ms latency, fully managed, supports document and key-value (web, gaming, ad-tech, IOT)..

(T) table
(I) item (row)
(A) attribute (key - value)

Eventual Consistent Reads vs Strongly Consistent Reads

Read Capacity Units, Write Capacity Units (can be scaled up) - push button scalability

\Writes are written to 3 different location / facilities/ datacenter (synchronous) - Amazon DynamoDB synchronously replicates data across three facilities in an AWS Region, giving you high availability and data durability.

Two types of primary key

Single Attribute (think unique id)
Partition Key (Hash Key) composted of 1 attribute (no nesting allowed here) - Partition key will help determine the physical location of data.

Composite key (think unique id and range)
Partition Key(Hash Key) & Sort Key (Range key - e.g date) - composed of 2 attributes - if two data have same partition key (same location) it must have a different sort key, and they will be stored together on single location.

Secondary Indexes

Local Secondary Index - Same Partion Key + Different Sort Key ( can only be created while creating the table, cannot be added/removed or modified later)

Global Secondary Index - Different Partition Key + Different Sort Key ( can be created during the table creation or can be added later or removed / modified later)

DynamoDB Streams

use to capture any kinda modification to the dynamo db table, Lambda can capture events and push notifications thru SES

Table can be exported to csv (either select all items )

Query vs Scan

Query operation finds item in a table using only primary key attribute values , must provide partition attribute name and the value to search for, you can optionally provide a sort key attribute name and value to refine search results (e.g. all the forums with this ID since last 7 days). By default Query returns all the data attributes for those items with specified primary keys. You can further use ProjectionExpression parameter to only return a selected attributes.

Query results are always sorted by the sort key (ascending for both numbers and string by default). To reverse the sort order set the ScanIndexForward parameter to false

By Default Queries are going to be Eventually consistent but can be changed to StronglyConsistent.

Scan operation is basically examines every item - e.g. dumping the entire table, by default Scan returns all the data attributes but we could use ProjectionExpression parameter to only return a selected attributes.

Query operation is more efficient than scan operation

For quick response time design your table in a way that you can use Query Get or BatchGetItem API (read multiple items - can get upto 100 items or up to 1MB of data) ,

Alternatively design your application to use scan operation in a way that minimize impact of your table’s request rate since it can use up the entire table’s provisioned throughput in a single scan operation

When you exceed your maximum allowed provisioned throughput for a table or one or more global secondary index you will get 400 HTTP Status code - ProvisionedThroughputExceededException

AssumeRolewithWebIdentity role

Idempotent conditional write

Atomic counters - always need to increment so its not idempotent

if data is critical and no margin of error then must use Idempotent conditional write.

Only Tables(256 table per region) and ProvisionedThroughput(80 K read, 80K write per account for US east, 20K for other regions) limits can be increased
