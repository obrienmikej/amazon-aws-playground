Review notes on AWS Storage Gateway - 3 configs
Review notes on EC2 types (ebs & instance store)

****
Logs
****
Can monitor environment by

1.3rd party tools (splunk, Zennos) and store logs in S3
2.CloudWatch logs
3.Access Logging in S3 (s3 only)

*******
Backups
*******
Best place to save logs is probably S3 because
1.durability
2.life cycle management
3.archive to glacier
4.tier backup solution

***
EC2
***

***********
Root volume
***********
-root volume = where OS is installed
-can be EBS or instance store

max size root device volume
instance store = 10GB
EBS = 1 or 2 TB

additional volumes
-windows (d:\, e:\, f:\)
-linux (dev/sdb, dev/sbc, dev/sbd)

Instance termination
-ec2 instances can be terminated

overide
GUI = unselect Delete on Termination
API = deleteontermination

***
EBS
***
-root device volume terminated by DEFAULT when EC2 instance terminated
-other volumes preserved if instance deleted
-ebs backed instance can be stopped

**************
Instance store
**************
-root device volume terminated by DEFAULT when EC2 instance terminated.  Can't stop this
-other volumes deleted if instance deleted automatically
-instance store backed instance can NOT be stopped.  Can only be rebooted or terminated
