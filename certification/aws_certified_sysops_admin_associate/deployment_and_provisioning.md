Services with root/admin access to O/S
1.Elastic Beanstalk
2.Elastic MapReduce
3.Opswork
4.EC2

************************************
Elastic Load Balancer Configurations
************************************
-Can     :configure across different AZ's in same region
-Can NOT :configure with different VPC's
-Can NOT :configure with different regions

TWO different types of ELB's
1.External ELB with external DNS names
2.Internal ELB with internal DNS names

***************
ELB healthcheck
***************
Ping Protocol
-The protocol to use to connect with the instance.  
-Valid values: TCP, HTTP, HTTPS, and SSL

Ping Port
-The port to use to connect with the instance, as a protocol:port pair.
-If the load balancer fails to connect with the instance at the specified port within the configured response timeout period, the instance is considered unhealthy.
-Ping protocols: TCP, HTTP, HTTPS, and SSL

Ping Path
-The destination for the HTTP or HTTPS request.
-An HTTP or HTTPS GET request is issued to the instance on the ping port and the ping path. If the load balancer receives any response other than "200 OK" within the response timeout period, the instance is considered unhealthy. If the response includes a body, your application must either set the Content-Length header to a value greater than or equal to zero, or specify Transfer-Encoding with a value set to 'chunked'.
-Default: /index.html

Response Timeout
-The amount of time to wait when receiving a response from the health check, in seconds.
-Valid values: 2 to 60

HealthCheck Interval
-The amount of time between health checks of an individual instance, in seconds.
-Valid values: 5 to 300

Unhealthy Threshold
-The number of consecutive failed health checks that must occur before declaring an EC2 instance unhealthy.
-Valid values: 2 to 10

Healthy Threshold
-The number of consecutive successful health checks that must occur before declaring an EC2 instance healthy.
-Valid values: 2 to 10

***************
Sticky sessions
***************
-enables the elb to lock user down to a specific web server (ec2 instance)
-also known as session affinity
-not enabled by default

TWO types
****************
1.Duration based
****************
edit stickiness = enable load balancer generated cookie stickiness
-most common
-elb creates the session cookie
-if no cookie, elb send traffic to app  
-once assigned to elb, done through stickness
instance failure = elb stops routing to that instance
-time set = elb

******************************
2.Application controlled based
******************************
edit stickiness = enable application generated cookie stickiness
-elb uses a special cookie to associate the session with the original server that handled request
-follows the lifetime of app generated cookie
-elb only inserts new stickiness cookie if app response include new app cookie
-time set = app

***************
Pre-warming ELB
***************
HOW = contact AWS prior to expected event
-start/end dates
-expect request rate per seconds
-total size
