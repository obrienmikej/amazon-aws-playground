****************************
Security Token Service (STS)
****************************

grants users limited and temporary access to AWS resources

Users can come from 3 sources
1.federation
2.federation with mobile apps
3.cross account access i.e. other AWS accounts

Federation:
-combine/join list of users between domains i.e. IAM with active directory or Facebook
-typically Active Directory (AD)
-uses Security Assertion Markup Language (SAML)
-grants temporary access based off the (AD) credentials
-do NOT need to be a users in IAM
-single sign on allows users to login to AWS console without assigning IAM credentials

Identity Broker:
-service that allows you to take an identity from point A and join with point B
-federate it
-customer has to develop own identity Broker

Identity Store:
Services like active directory, Facebook, google

Identity:
A user of a service

Scenarios

ONE
1.develop identity broker with LDAP & AWS STS
2.identity broker authenticates with LDAP FIRST, then STS
3.app gets temporary access to AWS

TWO
1.develop identity broker with LDAP & AWS STS
2.identity broker authenticates with LDAP FIRST, gets a IAM role
3.app then authenticates with STS & assumes IAM role
4.app uses IAM role to interact with AWS resources

***************
AWS Credentials
***************

Passwords
String of characters 6-128
1.AWS root account
2.IAM user

Multi Factor Authentication (MFA)
6 digit single use code + password
1.AWS root account
2.IAM user

Access Keys
access id + secret access key
-Digital signed request
-AWS sdk, cli, rest/query API

Key Pairs
1024 bit ssh-2 RSA key
-ssh login to compute
-cloud front signed url's

x-509
SOAP only for S3
-digitally signed SOAP requests to AWS api's
-SSL server certificates for HTTPS

***********************
Storage Decommissioning
***********************
When storage device reaches end of life, AWS procedures include decommissioning process to prevent customer data from being exposed.  scrub disks, wipe, zero out

1.DoD 5220.22-M national industrial security program operating manual
2.NIST 800-88 guidelines for media sanitation

****************
Network security
****************

Can use a IPSC virtual Private Network (VPN) device to provide encrypted tunnel between AWS VPC & private cloud

Network monitoring & protection from AWS
1.DDOS
2.Man in the Middle attack (MIM)
3.IP spoofing
-you must request a vulnerability scan in advance
-AWS controlled, host based firewall will not permit an instance to send traffic with a source IP or MAC address other than it's own
4.Port scanning
5.Packet sniffing by other tenants

*****************************
Security Responsibilities
*****************************
AWS responsible for protecting global infrastructure
Comprised of hardware, software, networking & facilities that run AWS services

AWS responsible for security configuration of managed services.  Examples
DynamoDB
RDS
Redshift
EMR
Workspace

Customer responsible for services under their control.  Customer performs all necessary security configuration and management tasks.  Examples
EC2
VPC
S3

******************
Instance Isolation
******************
-xen hypervisor isolates different instances running on the same physical machine
-aws firewall resides within the hypervisor layer between the physical network interface and the instance's virtual interface.  
-all packets pass through this layer - instance neighbor's have no more access to the instance.  can be treated as separate physical hosts
-physical RAM separated using similar mechanisms
-no access to raw disk devices; have access to virtualized disks
-new memory allocations not available until scrubbing is complete

Guest Operating System (OS)
-completely controlled by customers with full root access
-aws does not have any access rights to customers instances or guest OS

Encryption
-good security practice for sensitive data via AES-256
-can encrypt EBS volumes
-can encrypt EBS snapshots
-limited to more powerful EC2 instance types (i.e. M3, C3, R3, G2)

Firewall
-ec2 provides complete firewall solution
-mandatory and configured in deny all mode by default
-customers must explicitly open ports to all inbound traffic

Elastic Load Balancing
-SSL termination on elb supported

Compliance
-SOC1
-SOC2
-SOC3
-FISMA, DIACAP, FEDRAMP
-PCI
-ISO 27001
-ISO 9001
-ITAR
-FIPS
-HIPPA
-CSA
-MPAA
