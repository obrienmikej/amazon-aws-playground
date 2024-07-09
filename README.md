# Overview
Playground for preparing for AWS certification.

## prerequisites
1. from ~aws git clone https://github.com/obrienmikej/amazon-aws-playground.gitamazon-aws-playground
2. aws cli setup with credentials and region set to us-east-1

## Create VPC with Cloud Formation
1. run aws cloudformation create-stack --stack-name myvpc --template-body file://myvpc.json
2. run aws cloudformation create-stack --stack-name myvpc --template-body file://myvpc.yaml

## Delete CPC with Cloud Formation
1. run aws cloudformation delete-stack --stack-name myvpc
2. run aws cloudformation delete-stack --stack-name myvpc

# AWS CDK

Plarground for using the AWS CDK with python

## prerequisites

- AWS CLI
- AWS CDK
- PIP

## vscode

- Create a virtual environment and activate it to use the repo within VSCode.
- Install the dependencies via the `requirements.txt` file using.
- Active the environment
```commandline
source .venv/bin/activate
```

