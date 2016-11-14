#!/bin/bash

aws dynamodb batch-write-item --request-items file://product_catalog.json
