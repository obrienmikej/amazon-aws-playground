***************************
Virtual Private Cloud (VPC)
***************************

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
