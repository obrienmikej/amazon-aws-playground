#!/bin/bash

aws dynamodb create-table --attribute-definitions AttributeName=Name,AttributeType=S --table-name Forum --key-schema AttributeName=Name,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
