***************************
Virtual Private Cloud (VPC)
***************************

Limits:
-5 VPCs per account per region
-1 Default VPC per account
-200 Subnets per VPC
-1 Internet Gateway per VPC
-10 IPSEC Connections per VPC

Security Group                       | Network ACL
at instance level                    | at subnet level
all rules only                       | allow & deny rules
stateful                             | stateless
return traffic automatically allowed | return traffic must be explicitly allowed
evaluate rules, the proceed          | process rules in order
instances in security group          | all instances in subnet
                                     | Every subnet must have an ACL
                                     | Can associate ACL with multiple subnets
                                     | Subnet can only have 1 ACL
                                     | default ACL allow all out/in
                                     | new ACL deny all out/in

**************
Direct Connect
**************

Connection between private cloud and AWS

Benefits
-Reduce Cost
-Increase bandwidth
-Consistent network experience

****************************
Elastic Load Balancers (ELB)
****************************

Not free - charged by hour & GB

Supported protocols
-http
-https (secure http)
-tcp
-ssl (secure tcp)

********
Route 53
********

Supports the following Record Sets:
-A
-AAAA (IpV6)
-CNAME(Canonical Name Record)
-MX
-NAPTR
-NS
-PTR
-SOA
-SPF
-SRV
-TXT
-ALIAS - Maps Resource Records in Hosted Zones to S3, Elastic BeanStalk, ELB, CloudFront. Similar to CNAME that map one DNSName
			like www.example.com to another DNS Name like elb1234.amazonaws.com. But difference is its not Visible to resolvers. Also
			Alias route to S3, CloudFront, ELB, BeanStalk is Free but you pay for CNAME.

* Route 53 can map Apex Domain Names like example.com to S3, ELB, Elastic BeanStalk and CloudFront using Alias
* Route 53 supports ipv6 using AAAA (forward) and PTR (reverse) records.
* Route 53 supports Weighted Round Robin (WRR) and Latency Based Routing (LBR) Features.
		WRR - Assign "weights" to different record sets for A/B testing. So If you assign a "weight" of 3 to Record Set 1 and "weight"
			  of 1 for Record set 2, 75% of the time Route 53 will return Record Set 1 and 25% of time it will return Record Set 2
		LBR - If you run your application in multiple regions, Route 53 will route users to the region that provides lowest latency.
* Private DNS lets you have authoritative DNS within a VPC without exposing your DNS records.
  Private DNS you can host private HostesZones. Route 53 will only return these records from calls WITHIN VPC
* Route 53 Pricing : Pay for what you use.No upfront prices or overcharge.Pay for usage of HostedZones,Queries,Health Checks and DomainNames
* Q. Does Amazon Route 53 use an anycast network?
  Yes - Anycast is a networking and routing technology that helps DNS queries get answered from optimal Route
