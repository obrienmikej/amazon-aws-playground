FOUR important things to look at
1.CPU utilization
2.Swap Usage
3.Evictions
4.Concurrent connections

***************
CPU utilization
***************
Memcached
-multi threaded
-Ok up to 90% load
-add more nodes to cluster when CPU load > 90%

Reddis
-not multi threaded
-when to scale : take 90 & divide by number of cores (i.e. 90 / 4 cores = 22.5%)

**********
Swap Usage
**********
-the amount of the swap file that is used
-swap/paging file is the amount of disk reserved if computer runs out of memory
-typical to have swap = size of the RAM

Memcached
-should be around 0 most of the time
-should not exceed 50mb
memcached_connections_overhead defines the amount of memory to be reserved for memcached connections and other overheard
-if > 50mb increase memcached_connections_overhead

Reddis
-no SwapUsage metric
-use reserved-memory

*********
Evictions
*********
An eviction occurs when a new item is added and an old item must be removed due to lack of free space in the system

Memcached
-no recommended setting
-set threshold based on application
-scale up (increase memory of existing nodes)
OR
-scale out (add more nodes)

Reddis
-no recommended setting
-set threshold based on application
-scale out (add read replicas)

**********************
Concurrent connections
**********************
-no recommended setting
-set threshold based on application
-set alarm on concurrent connections for elasticache 
-if large or sustained spike in number of concurrent connections
1.large traffic spike
OR
2.application not releasing connections
