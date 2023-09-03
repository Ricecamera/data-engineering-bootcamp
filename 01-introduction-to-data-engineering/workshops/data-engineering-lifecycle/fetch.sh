#!/bin/bash

API_KEY='$2b$10$NxTo5tVOjcSqVS8MzQU3JOGC7QCkaS7Eud7wfZV6e7UivQkCG1LEK'
COLLECTION_ID='64cdf959b89b1e2299cbae02'

curl -XGET \
    -H "X-Master-key: $API_KEY" \
    "https://api.jsonbin.io/v3/c/$COLLECTION_ID/bins"
