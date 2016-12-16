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

EBS
-root device volume terminated by DEFAULT when EC2 instance terminated
-other volumes preserved if instance deleted
-ebs backed instance can be stopped

overide
GUI = unselect Delete on Termination
API = deleteontermination

Instance store
-root device volume terminated by DEFAULT when EC2 instance terminated.  Can't stop this
-other volumes deleted if instance deleted automatically
-instance store backed instance can NOT be stopped.  Can only be rebooted or terminated.
