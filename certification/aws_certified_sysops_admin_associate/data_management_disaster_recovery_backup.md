recovery time objective (RTO)
-targeted duration of time and a service level within which a business process must be restored after a disaster (or disruption) in order to avoid unacceptable consequences associated with a break in business continuity

recovery point objective (RPO)
-maximum targeted period in which data might be lost from an IT service due to a major incident. The RPO gives systems designers a limit to work to. For instance, if the RPO is set to four hours, then in practice, off-site mirrored backups must be continuously maintained
–a daily off-site backup on tape will not suffice. Care must be taken to avoid two common mistakes around the use and definition of RPO. Firstly, business continuity staff use business impact analysis to determine RPO for each service
–RPO is not determined by the existent backup regime. Secondly, when any level of preparation of off-site data is required, rather than at the time the backups are offsited, the period during which data is lost very often starts near the time of the beginning of the work to prepare backups which are eventually offsited.

FOUR DR Scenarios

******************
Backup and Restore
******************
-DR scenario where data backed up to tape and stored off site.  Use tapes to restore service
-S3 ideal destination for backup when need quick acccess
-could use AWS import/export to transfer large data sets
-Glacier could be used for longer term storage where retrieval times are longer

Key steps:
1.select appropriate tool/method to backup data
2.ensure appropriate retention policy
3.ensure security measures, like encryption and access policies
4.test recovery/restoration process

Fail Back
1.freeze data changes to DR site
2.take backup
3.restore the backup to the primary site
4.repoints users to the primary site
5.unfreeze the changes

***********
Pilot Light
***********
-DR scenario where minimal version of environment is always running
-able to rapidly provision full scale production environment when needed
-include critical core parts of system (think RDS, db server, active directory)
-use preconfigured AMI's to quickly provision remaining parts of infrastructure
-use pre-allocated elastic IP addressed and associate them with instances when invoking DR
-can use pre-allocated elastic network interfaces (ENI's) with pre allocated MAC addressed for apps with special licensing requirements

use ELB to distribute traffic to multiple instances
-then update DNS to points to ECS instances
or
-point to ELB using using a CNAME

Fail Back
1.establish reverse mirroring/replication from DR site to primary, once the primary site has caught up with the changes
2.freeze data changes to the DR site
3.repoint users to the primary site
4.unfreeze the changes

************
Warm Standby
************
-DR scenario whee scaled down version of a fully functional environment is always running
-everything running, but on minimum sized fleet of ec2 instances
-will no handle full production load, but is fully functional
-could also be used for non production work (test, internal use)
-in disaster scenario, system scaled up quickly to handle production load

Key steps:
1.setup EC2 instances to replicate or mirror data
2.create & maintain AMI's
3.run system using minimal footprint (smallest EC2 instances)
4.patch/update software and config to match production environment

Recovery key steps:
1.increase size of ec2 instances in service with elb (horizontal scaling)
2.start app on larger ec2 instances (vertical scaling)
3.
manually change DNS records
or
use route 53 automated health checks to route traffic
4.consider auto scaling to right size fleet

In AWS, achieve by
-adding more instances to ELB
-resize instances to larger instance types

Fail Back
1.establish reverse mirroring/replication from DR site to primary, once the primary site has caught up with the changes
2.freeze data changes to the DR site
3.repoint users to the primary site
4.unfreeze the changes

**********
Multi Site
**********
-active\active configuration
-can use route 53 to root traffic to both sites either symmetrically or asymmetrically

in disaster scenario
-adjust DNS weighting and reroute traffic
-use auto scaling to automate process to scale out
-might need app logic to detect failure for db service and cut over to parallel db service

Key steps
1.duplicate production environment
2.setup dns weighting to distribute incoming requests to both sites
3.configure automated failover to re-route traffic

Key steps preparation
1.manual or with DNS failover
2.have app logic for failover
3.consider auto scaling to right size fleet

Fail Back
1.establish reverse mirroring/replication from DR site to primary, once the primary site has caught up with the changes
2.freeze data changes to the DR site
3.repoint users to the primary site
4.unfreeze the changes


Exam TIP:
-horizontal scaling is preferred over vertical scaling
-can have ENI with preconfigured MAC addresses
