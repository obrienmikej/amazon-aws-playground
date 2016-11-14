#!/bin/bash

aws dynamodb create-table --attribute-definitions AttributeName=Id,AttributeType=S AttributeName=ReplyDateTime,AttributeType=S --table-name Reply --key-schema AttributeName=Id,KeyType=HASH AttributeName=ReplyDateTime,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

# SYNOPSIS
#            create-table
#          --attribute-definitions <value>
#          --table-name <value>
#          --key-schema <value>
#          [--local-secondary-indexes <value>]
#          [--global-secondary-indexes <value>]
#          --provisioned-throughput <value>
#          [--stream-specification <value>]
#          [--cli-input-json <value>]
#          [--generate-cli-skeleton]
