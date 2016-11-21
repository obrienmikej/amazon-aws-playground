***************
Trusted Advisor
***************

(C) Cost Optimization
(P) Performance
(F) Fault Tolerance
(S) Security

***************
Cloud Formation
***************

enables you to create and provision AWS infrastructure deployments predictably and repeatedly
limited to a maximum of 200 stacks
Template, Parameter, Output, and Resource description fields are limited to 4096 characters.
up to 60 parameters and 60 outputs in a template

Five Elements
1.optional - parameters (input values supplied at stack creation time)
2.optional - output values (e.g. the complete URL to a web application)
3.optional - data tables used to lookup static configuration values (e.g., AMI names)
4.list of AWS resources and their configuration values
5.file format version number

Stacks : Some useful CLI based commands on stacks:
create-stack          : "aws cloudformation create-stack --stack-name mystack --template-body file://c:/mytemplate.json" (gets uploaded to s3 bucket)
list-stacks           : "aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE (lists and can filter stacks by status, deleted ones upto 90 days)
list-stack-resources  : "aws cloudformation list-stack-resources -stack-name mystack" (lists all resources created in mystack)
describe-stacks       : "aws cloudformation describe-stacks --stack-name mystack" (describes running stack instances)
decribe-stack-events  : "aws cloudformation describe-stack-events --stack-name mystack" (describes the list of events in reverse chronological order)
delete-stack          : "aws cloudformation delete-stack --stack-name mystack" (deletes the stack mystack)
update-stack          : "aws cloudformation update-stack --stack-name mystack --template-url <path> --parameters ..." (directly updates stack)
get-template          : "aws cloudformation get-template --stack-name mystack" (outputs the template body only.)
validate-template     : "aws cloudformation validate-template --template-url <path> (checks syntax of the template. wont check if an a property exists.)

****************************
Intrinsic Function Reference
****************************

AWS CloudFormation provides several built-in functions that help you manage your stacks. Use intrinsic functions in your templates to assign values to properties that are not available until runtime.

Note
You can use intrinsic functions only in specific parts of a template. Currently, you can use intrinsic functions in resource properties, metadata attributes, and update policy attributes.
Topics

Fn::Base64
Condition Functions
Fn::FindInMap
Fn::GetAtt
Fn::GetAZs
Fn::ImportValue
Fn::Join
Fn::Select
Fn::Sub
Ref
