***************************
Simple Storage Service (S3)
***************************

Object based storage
Files 0 byte to 5TB
Max buckets per account = 100
Unlimited Storage
Largest single put object = 5GB
Files stored in alphabetical order
Max # of buckets per AWS account = 100

Important S3 Limits:
-Unlimited Number of Objects in S3 or Archives in Glacier
-100 S3 buckets per account per region [Contact AWS to increase limit]
-1000 Glacier Vaults per account per region

-0 byte to  5 TB size of Objects in S3.
-1 byte to 40 TB size of Archives in Glacier.
-5 GB is Max size in one PUT in S3.
-100 MB or more Recommended (5 GB or more Mandatory) for MultiPart Upload. 5MB - 5 TB
-1000 keys limit for Multi Object Delete
-100 Max no of CORS rules allowed

Rules for buckets
3 to 63 characters
CAN BE
-lowercase letters, numbers, and hyphens
-be separated by .

CAN'T
-contain an ip address
-contain download in the name 
-start with .
-start with -
-end with a .

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
-Objects stored in your bucket before you set the versioning state have a version ID of null

Replication
-Cross region replication requires version to be enabled

Access
When new bucket created, DEFAULT behavior = private
Controlled by
-Bucket policy
-Access control list

Bucket ownership is not transferable; however, if a bucket is empty, you can delete it. After a bucket is deleted, the name becomes available to reuse, but the name might not be available for you to reuse for various reasons.

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

************************************
Cross Origin Resource Sharing (CORS)
************************************

-Remove need for proxy server
-Allow Site X to talk/use resources in Site Y i.e Java Script, HTML5
-Cross reference resources in services EC2/S3

***************************
Elastic Block Storage (EBS)
***************************

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

***************
Storage Gateway
***************

Connects an on-premises software appliance with cloud-based storage to provide seamless and secure integration between your on-premises IT environment and the AWS storage infrastructure in the cloud.

Gateway Stored Volume
-Data on site (private cloud)
-Backed up to S3

Gateway Cached Volume
-Data in S3
-Frequently accessed date on site (private cloud)

Gateway Virtual Library (VTL)
-For backups in AWS using NetBackup, Backup Exec..

***********
Cloud Front
***********

-Can read & write to edge locations
-Objects cached for life of TTL in edge location
-Can clear cached objects, but will  be charged

Edge location = where content is cached

Origin = where all files are located & can have multiple origins
-S3
-EC2
-ELB
-Route53

Distribution = Name of CDN

Types
-Web distribution = website
-RTMP = media
