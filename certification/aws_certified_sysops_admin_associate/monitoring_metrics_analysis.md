**********
CloudWatch
**********

Host level metrics consist of:
(C) CPU
(C) Status Check
(D) Disk
(N) Network

Default interval = 5 minutes
Can change interval = 1 minute
Metrics stored for 2 weeks

GetMetricStatistics = use API for older data

Can retrieve data from terminated EC2 & ELB instances
RAM utilization is a custom metric

**********************
Centralized Monitoring
**********************
-Usually involve 3rd party tool and installing agent on servers
-agent report metrics back to server

protocol
-depends on what is being monitored
-most basic monitoring is going to use ICMP
-cloud be SQL (1433) or MySQL (3306)

For exam
Allow ICMP|ports access to
-IP address OR Range of IP address'
-Create new security group with ICMP access
-whitelist IP address

Internet Control Message Protocol (ICMP)
Supporting protocol in the Internet protocol suite. It is used by network devices, like routers, to send error messages and operational information indicating, for example, that a requested service is not available or that a host or router could not be reached.

ICMP differs from transport protocols such as TCP and UDP in that it is not typically used to exchange data between systems, nor is it regularly employed by end-user network applications (with the exception of some diagnostic tools like ping and trace route.)

********************
Consolidated Billing
********************
You can receive a single bill for multiple AWS Accounts. Your Consolidated Bill will show overall costs and also breakdowns by account. By combining usage across multiple accounts, you can more quickly reach lower-priced volume tiers.

Set in console
Name : My Billing Dashboard : Consolidated Billing

*************
Billing alarm
*************
create alarm in CloudWatch
billing metrics (have to use n.virginia)

*****************
EC2 Status Checks
*****************
System Status Check = physical HOST
-loss of network connectivity
-loss of system power
-software or  issue on the physical host
RESOlVE = stop/start VM (will start VM on new physical host)

Instance Status Check = VM
-failed system status check
-misconfigured networking or startup config
-exhausted memory
-corrupted file system
-incompatible kernel
RESOLVE = reboot instance or modify OS
