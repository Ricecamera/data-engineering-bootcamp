#!/bin/bash

API_KEY='$2b$10$NxTo5tVOjcSqVS8MzQU3JOGC7QCkaS7Eud7wfZV6e7UivQkCG1LEK'
COLLECTION_ID='64cdf959b89b1e2299cbae02'

curl -XPOST \
    -H "Content-type: application/json" \
    -H "X-Master-Key: $API_KEY" \
    -H "X-Collection-Id: $COLLECTION_ID" \
    -d @dogs.json \
    "https://api.jsonbin.io/v3/b"
