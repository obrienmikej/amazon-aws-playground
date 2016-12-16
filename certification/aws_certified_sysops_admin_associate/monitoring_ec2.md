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
