#!/bin/bash

TABLE_NAME=ProductCatalog

aws dynamodb create-table --attribute-definitions AttributeName=Id,AttributeType=N --table-name $TABLE_NAME --key-schema AttributeName=Id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
