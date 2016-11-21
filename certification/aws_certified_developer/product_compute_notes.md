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

EC2 APIs
-RunInstances			  : Runs the instances using an AMI and returns the DNS names of the instances
-StartInstances		  : Starts an instance that you have previously stopped
-StopInstances			: Stop the instances (EBS backed only. Instance Store Backed cannot be stopped and will throw an error when attempting to stop)
-TerminateInstances	: Terminate the instances
-DescribeInstances 	: Gives the status of the instances
-CreateVolume			  : Create a Volume, either NEW from restore from SNAPSHOT
-AttachVolume			  : Attaches an EBS volume to a running or stopped instance
-CreateSnapshot		  : Creates a snapshot from an EBS Volume and stores it in S3
-CopySnapshot			  : Copies a point-in-time Snapshot and stores it in S3. Can copy to S3 in the same region or a different region
-DescribeSnapshots	: Describes one or more EBS snapshots available to you
