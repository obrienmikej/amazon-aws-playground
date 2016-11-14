#!/bin/bash

TABLE_NAME=Forum
READ_UNITS=1
WRITE_UNITS=1

aws dynamodb create-table --attribute-definitions AttributeName=Name,AttributeType=S --table-name $TABLE_NAME --key-schema AttributeName=Name,KeyType=HASH --provisioned-throughput ReadCapacityUnits=$READ_UNITS,WriteCapacityUnits=$WRITE_UNITS
