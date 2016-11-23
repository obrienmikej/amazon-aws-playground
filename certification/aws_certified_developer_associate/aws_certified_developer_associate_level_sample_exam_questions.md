Which of the following statements about SQS is true?
A. Messages will be delivered exactly once and messages will be delivered in First in, First out order
B. Messages will be delivered exactly once and message delivery order is indeterminate
C. Messages will be delivered one or more times and messages will be delivered in First in, First out order
D. Messages will be delivered one or more times and message delivery order is indeterminate
ANSWER = D

EC2 instances are launched from Amazon Machine Images (AMIs). A given public AMI:
A. can be used to launch EC2 instances in any AWS region
B. can only be used to launch EC2 instances in the same country as the AMI is stored
C. can only be used to launch EC2 instances in the same AWS region as the AMI is stored
D. can only be used to launch EC2 instances in the same AWS availability zone as the AMI is stored
ANSWER = C

Company B provides an online image recognition service and utilizes SQS to decouple system
components for scalability. The SQS consumers poll the imaging queue as often as possible to keep endto-end
throughput as high as possible. However, Company B is realizing that polling in tight loops is
burning CPU cycles and increasing costs with empty responses. How can Company B reduce the number
of empty responses?
A. Set the imaging queue VisibilityTimeout attribute to 20 seconds
B. Set the imaging queue ReceiveMessageWaitTimeSeconds attribute to 20 seconds
C. Set the imaging queue MessageRetentionPeriod attribute to 20 seconds
D. Set the DelaySeconds parameter of a message to 20 seconds
ANSWER = B

Which operation could return temporarily inconsistent results?
A. Getting an object from Amazon S3 after it was deleted
B. Getting an object from Amazon S3 after it was initially created
C. Selecting a row from an Amazon RDS database after it was inserted
D. Selecting a row from an Amazon RDS database after it was deleted
ANSWER = A

You have reached your account limit for the number of CloudFormation stacks in a region. How do you
increase your limit?
A. Make an API call
B. Contact AWS
C. Use the console
D. You cannot increase your limit
ANSWER = B

Which statements about DynamoDB are true? (Pick 2 correct answers)
A. DynamoDB uses a pessimistic locking model
B. DynamoDB uses optimistic concurrency control
C. DynamoDB uses conditional writes for consistency
D. DynamoDB restricts item access during reads
E. DynamoDB restricts item access during writes
ANSWER = B,C

What is one key difference between an Amazon EBS-backed and an instance-store backed instance?
A. Instance-store backed instances can be stopped and restarted
B. Auto scaling requires using Amazon EBS-backed instances
C. Amazon EBS-backed instances can be stopped and restarted
D. Virtual Private Cloud requires EBS backed instances
ANSWER = C

A corporate web application is deployed within an Amazon VPC, and is connected to the corporate data
center via IPSec VPN. The application must authenticate against the on-premise LDAP server. Once
authenticated, logged-in users can only access an S3 keyspace specific to the user.
Which two approaches can satisfy the objectives?
A. The application authenticates against LDAP. The application then calls the IAM Security Service to login
to IAM using the LDAP credentials. The application can use the IAM temporary credentials to access the
appropriate S3 bucket.
B. The application authenticates against LDAP, and retrieves the name of an IAM role associated with the
user. The application then calls the IAM Security Token Service to assume that IAM Role. The application
can use the temporary credentials to access the appropriate S3 bucket.
C. The application authenticates against IAM Security Token Service using the LDAP credentials. The
application uses those temporary AWS security credentials to access the appropriate S3 bucket.
D. Develop an identity broker which authenticates against LDAP, and then calls IAM Security Token Service
to get IAM federated user credentials. The application calls the identity broker to get IAM federated user
credentials with access to the appropriate S3 bucket.
E. Develop an identity broker which authenticates against IAM Security Token Service to assume an IAM
Role to get temporary AWS security credentials. The application calls the identity broker to get AWS
temporary security credentials with access to the appropriate S3 bucket.
ANSWER = B, D

You run an ad-supported photo sharing website using S3 to serve photos to visitors of your site. At some
point you find out that other sites have been linking to the photos on your site, causing loss to your
business. What is an effective method to mitigate this?
A. Use CloudFront distributions for static content.
B. Remove public read access and use signed URLs with expiry dates.
C. Block the IPs of the offending websites in Security Groups.
D. Store photos on an EBS volume of the web server.
ANSWER = B

Your application is trying to upload a 6 GB file to Simple Storage Service and receive a "Your proposed
upload exceeds the maximum allowed object size." error message. What is a possible solution for this?
A. None, Simple Storage Service objects are limited to 5 GB
B. Use the multi-part upload API for this object
C. Use the large object upload API for this object
D. Contact support to increase your object size limit
E. Upload to a different region
ANSWER = B
