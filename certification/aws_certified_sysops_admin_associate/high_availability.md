**********
Elasticity
**********
-think rubber band
-allows you to stretch out & retract infrastructure
-only pay for what you use
-used during short periods (hours or days)

***********
Scalability
***********
-think pyramid
-used over longer time periods (weeks, days, months)
-build out infrastructure to meet long term demands

EC2
elasticity = more instances
scalability = increase instance size

DynamoDB
elasticity = more IOPS
scalability = unlimited storage

RDS
elasticity = not
scalability = increase instance size

Lambda = good example of automated elasticity

ScaleUp = more processors, RAM, storage
ScaleOut = add more resources (ec2 instances, web servers)

Exam Tips
network problems - resolve network bottle necks by scaling up
if network related, best to scale up
if problem is not enough resources, best to scale out

Remember
scaling out, you can scale back
scaling up is easy, scaling down is not so easy

*********************
RDS multi AZ failover
*********************
-safeguard data in the event of a DB instance failure or loss of AZ
-fail over, DNS name does not change
-with failure, aws will take care of pointing to RDS endpoint

MySQL, Oracle, PostgreSQL
-synchronous physical replication
-standby

SQL Server
-synchronous logical replication
-native mirroring

advantages
-high availability
-backup/restore take from secondary to avoid IO suspension

Reboot RDS instance to force failover
-console
-API = RebootDBInstance

not a scaling solution
read replicas are used to scale

*****************
RDS Read Replicas
*****************
-read only copy of db
-can have multiple read replicas
-use to elastically scale out beyond capacity constraints
-gets new DNS address
-can be promoted to primary db, but will break replication
-can have read replicas of replicas
-automated backups not taken of read replicas
API = CreateDBInstanceReadReplica

Read Replica Support
MySQL 5.6 (innodb tables only)
PostgreSQL 9.3.5

Create Read Replica
multi az NOT enabled : snapshot primary db, IO hit
multi az enabled     : snapshot secondary az

Exam Tips
MySQL
-can have 5 read replicas
-can have read replica in different region
-replication = asynchronous

PostgreSQL
-can have 5 read replicas
-same region only
-replication = asynchronous

Key Cloud Watch metric = Replica Lag

************
Bastion Host
************
high availability = multiple instances, route53, elastic IP's, separate subnets

*********************************
Instances and auto scaling groups
*********************************
why instances might not launch
-auto scaling group    : config problem
-auto scaling service  : not enabled in account
-az                    : not supported
-drive                 : invalid EBS device mapping
-drive                 : attempt to attach EBS block device to instance store ami
-instance type         : not supported in az
-key pair              : does not exist
-security group        : does not exist
