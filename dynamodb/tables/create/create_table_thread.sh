#!/bin/bash

aws dynamodb create-table --attribute-definitions AttributeName=ForumName,AttributeType=S AttributeName=Subject,AttributeType=S --table-name Thread --key-schema AttributeName=ForumName,KeyType=HASH AttributeName=Subject,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
