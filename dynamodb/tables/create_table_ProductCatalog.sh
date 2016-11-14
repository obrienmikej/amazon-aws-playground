#!/bin/bash

aws dynamodb create-table --attribute-definitions AttributeName=Id,AttributeType=N --table-name ProductCatalog  --key-schema AttributeName=Id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
