Regional failover

2 ELB in 2 regions
2 EC2 instance in 2 regions
instance "In Service" in each ELB
Route53 health check
failure Threshold = low to test/fail quickly
2 record sets in Route53 (primary & secondary)

FIVE Routing Policies 
(F)Failover
(G)Geolocation
(L)Latency
(S)Simple Routing
(W)Weighted

********************
Route53 Health Check
********************
Route 53 health checks monitor the health and performance of your application's servers, or endpoints, from a network of health checkers in locations around the world. You can specify either a domain name or an IP address and a port to create HTTP, HTTPS, and TCP health checks that check the health of the endpoint.

Amazon Route 53 health checks monitor the health and performance of your web applications, web servers, and other resources. At regular intervals that you specify, Amazon Route 53 submits automated requests over the Internet to your application, server, or other resource to verify that it's reachable, available and functional.

You can configure a health check to make requests similar to those that your users make, such as requesting a web page from a specific URL. You can also view the current and recent status of health checks. If you want to receive a notification when an application or a resource becomes unavailable, you can configure an Amazon CloudWatch alarm for each health check. For information about creating health checks, see Creating, Updating, and Deleting Health Checks. For information about viewing health check status and receiving notifications, see Monitoring Health Check Status and Getting Notifications.

If you have multiple resources that perform the same function, for example, web servers or email servers, and you want Amazon Route 53 to route traffic only to the resources that are healthy, you can configure DNS failover by associating health checks with your resource record sets. If a health check determines that the underlying resource is unhealthy, Amazon Route 53 routes traffic away from the associated resource record set. For more information, see Configuring DNS Failover.

*********************
Simple Routing Policy
*********************
Use a simple routing policy when you have a single resource that performs a given function for your domain, for example, one web server that serves content for the example.com website. In this case, Amazon Route 53 responds to DNS queries based only on the values in the resource record set, for example, the IP address in an A record.

***********************
Weighted Routing Policy
***********************
Use the weighted routing policy when you have multiple resources that perform the same function (for example, web servers that serve the same website) and you want Amazon Route 53 to route traffic to those resources in proportions that you specify (for example, one quarter to one server and three quarters to the other). For more information about weighted resource record sets, see Weighted Routing.

**********************
Latency Routing Policy
**********************
Use the latency routing policy when you have resources in multiple Amazon EC2 data centers that perform the same function and you want Amazon Route 53 to respond to DNS queries with the resources that provide the best latency. For example, you might have web servers for example.com in the Amazon EC2 data centers in Ireland and in Tokyo. When a user browses to example.com, Amazon Route 53 chooses to respond to the DNS query based on which data center gives your user the lowest latency. For more information about latency resource record sets, see Latency-Based Routing.

**************************************************
Failover Routing Policy (Public Hosted Zones Only)
**************************************************
Use the failover routing policy when you want to configure active-passive failover, in which one resource takes all traffic when it's available and the other resource takes all traffic when the first resource isn't available. For more information about failover resource record sets, see Configuring Active-Passive Failover by Using Amazon Route 53 Failover and Failover Alias Resource Record Sets. For information about creating failover resource record sets in a private hosted zone, see Configuring Failover in a Private Hosted Zone.

**************************
Geolocation Routing Policy
**************************
Use the geolocation routing policy when you want Amazon Route 53 to respond to DNS queries based on the location of your users. For more information about geolocation resource record sets, see Geolocation Routing.

****************
Weighted Routing
****************
Weighted resource record sets let you associate multiple resources with a single DNS name. This can be useful for a variety of purposes, including load balancing and testing new versions of software. To create a group of weighted resource record sets, you create two or more resource record sets that have the same combination of DNS name and type, and you assign each resource record set a unique identifier and a relative weight.

When processing a DNS query, Amazon Route 53 searches for a resource record set or a group of resource record sets that have the specified name and type. For weighted resource record sets, Amazon Route 53 selects one from the group. The probability of any one resource record set being selected depends on its weight as a proportion of the total weight for all resource record sets in the group:


For example, suppose you create three resource record sets for www.example.com. The three A records have weights of 1, 1, and 3 (sum = 5). On average, Amazon Route 53 selects each of the first two resource record sets one-fifth of the time, and returns the third resource record set three-fifths of the time.

*********************
Latency-Based Routing
*********************
If your application is hosted on Amazon EC2 instances in multiple Amazon EC2 regions, you can reduce latency for your users by serving their requests from the Amazon EC2 region for which network latency is lowest. Amazon Route 53 latency-based routing lets you use DNS to route user requests to the Amazon EC2 region that will give your users the fastest response.

To use latency-based routing, you create a latency resource record set for the Amazon EC2 resource in each region that hosts your application. When Amazon Route 53 receives a query for the corresponding domain, it selects the latency resource record set for the Amazon EC2 region that gives the user the lowest latency. Amazon Route 53 then responds with the value associated with that resource record set.

For example, suppose you have ELB classic or application load balancers in the US West (Oregon) region and in the Asia Pacific (Singapore) region, and that you've created a latency resource record set in Amazon Route 53 for each load balancer. A user in London enters the name of your domain in a browser, and DNS routes the request to an Amazon Route 53 name server. Amazon Route 53 refers to its data on latency between London and the Singapore region and between London and the Oregon region. If latency is lower between London and the Oregon region, Amazon Route 53 responds to the user's request with the IP address of your load balancer in the Amazon EC2 data center in Oregon. If latency is lower between London and the Singapore region, Amazon Route 53 responds with the IP address of your load balancer in the Amazon EC2 data center in Singapore.
