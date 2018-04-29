#Overview
Playground for preparing for AWS certification.

## prerequisites
1. amazon-aws-playground in ~aws/amazon-aws-playground
2. aws cli setup with credentials and region set to us-east-1

## Create VPC with Cloud Formation
1. run aws cloudformation create-stack --stack-name myvpc --template-body file://myvpc.json
or
2. run aws cloudformation create-stack --stack-name myvpc --template-body file://myvpc.yaml

## Delete CPC with Cloud Formation
1. run aws cloudformation delete-stack --stack-name myvpc --template-body file://myvpc.json
or
2. run aws cloudformation delete-stack --stack-name myvpc --template-body file://myvpc.yaml
