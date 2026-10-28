#!/bin/bash

JOB_ID=$1
AWX_TOKEN=$2
AWX_HOST=$3

if [ -z "$JOB_ID" ] || [ -z "$AWX_TOKEN" ] || [ -z "$AWX_HOST" ]; then
    echo "Usage: $0 <job_id> <token> <host>"
    exit 1
fi

echo "Monitoring job $JOB_ID..."

while true; do
    RESPONSE=$(curl -s -H "Authorization: Bearer $AWX_TOKEN" \
                    -H "Content-Type: application/json" \
                    "$AWX_HOST/api/v2/jobs/$JOB_ID/")
    
    STATUS=$(echo "$RESPONSE" | jq -r '.status')
    ELAPSED=$(echo "$RESPONSE" | jq -r '.elapsed')
    
    echo "$(date): Status: $STATUS, Elapsed: ${ELAPSED}s"
    
    if [[ "$STATUS" == "successful" ]] || [[ "$STATUS" == "failed" ]] || [[ "$STATUS" == "error" ]] || [[ "$STATUS" == "canceled" ]]; then
        echo "Job completed with status: $STATUS"
        break
    fi
    
    sleep 5
done
