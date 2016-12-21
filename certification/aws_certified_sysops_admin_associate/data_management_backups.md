Services that have automated backups
-RDS
-elasticache (redis only)
-redshift

Services that don't have automated backups
-ec2
-can take snapshots of EC2, but manual process

************
RDS Backups
************
-MySQL, need InnoDB
-performance hit if multi-az not enabled
-automated backups deleted if instance deleted
-manual DB snapshots are not deleted
-during restore, can change engine type
-stored on S3

*******************
Elasticache backups
*******************
-reddis cache cluster only
-entire cluster is snap shotted
-snapshot will degrade performance (take backup during non busy part of daily)
-stored in S3

****************
Redshift backups
****************
-default automated backups are 1 day retention period
-only backups data that has changed
-stored in S3

***
EC2
***
-no automated backups
-snapshot will degrade performance (take backup during non busy part of daily)
-stored in S3
-automated backups required using cmd line or python
-snapshots are incremental
-only charged for incremental storage
-each snapshot still contains the base snapshot data
