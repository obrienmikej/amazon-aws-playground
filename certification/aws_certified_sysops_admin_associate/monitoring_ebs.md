****************
EBS Volume Types
****************
General Purpose (SSD)
-System boot volumes
-virtual desktops
-small to medium db's
-dev/test environments
-volume size = 1 GiB - 16 TiB
-max throughput = 160 MIB/s
-3 IOPS per GB see i/o credits

Provisioned IOPS (SSD)
-critical business apps that require sustained IOPS
-require more than 10,000 IOPS
-large db workloads (mongodb, sql server, mysql, oracle, postgresql)
-volume size = 4 GiB - 16 TiB
-max throughput = 320 MIB/s
-performance = up to 20,000 IOPS

Magnetic
-cold workloads where data is infrequently accessed
-lowest storage cost is important
-volume size = 1 GiB - 1 TiB
-max throughput = 40-90 MIB/s
-performance = averages 100 IOPS

I/O Credits
when volume requires more than baseline, use I/O credits in balance to burst (to max of 3,000 IOPS)
earn credits when not over provisioned I/O
each volume receives an initial I/O credit of 5,400,000
-this credit can sustain max burst of 3,000 IOPS for 30 minutes

***********************
Pre-Warming EBS volumes
***********************
Volumes are available immediately when back end storage blocks are allocated

Penalty
-new volumes      : must be wiped clean
-restored volumes : instantiated from snap shop

Applies to all EBS volumes (SSD, IOPS, magnetic)
can cause 5-50% loss of IOPS first time each block is accessed
performance restored after data is accessed once

pre-warming = read or write to volume before use
writing to blocks is preferred
can't write to volume if restored from snapshot (would overwrite restored data)
if restored volume, read all blocks first

**********************
EBS CloudWatch Metrics
**********************
VolumeReadBytes
VolumeWriteBytes

VolumeReadOps
VolumeWriteOps

VolumeTotalReadTime
VolumeTotalWriteTime

VolumeIdleTime

VolumeQueueLength
-Number of read & write operation requests waiting to be completed
-want this to be zero

VolumeThroughputPercentage

VolumeConsumedReadWriteOps

********************
Volume Status Checks
********************
OK
normal = volume performance is as expected

WARNING
degraded = volume performance is below expectations
severely degraded =  volume performance is well below expectations

IMPAIRED
stalled = volume performance is severely impacted
not available = unable to determine I/O performance because I/O is disabled

INSUFFICIENT-DATA
insufficient data

degraded or severely degraded = WARNING
stalled or not available = Impaired
