#!/bin/bash

AWX_TOKEN=$1
AWX_HOST=$2

if [ -z "$AWX_TOKEN" ] || [ -z "$AWX_HOST" ]; then
    echo "Usage: $0 <token> <host>"
    exit 1
fi

echo "=== Automation Controller Job Dashboard ==="
echo

# Get recent jobs
echo "Recent Jobs (Last 10):"
echo "======================"
curl -s -H "Authorization: Bearer $AWX_TOKEN" \
     -H "Content-Type: application/json" \
     "$AWX_HOST/api/v2/jobs/?page_size=10&order_by=-created" | \
     jq -r '.results[] | "\(.id) | \(.name) | \(.status) | \(.created) | \(.elapsed)s"' | \
     column -t -s '|'

echo
echo "Running Jobs:"
echo "============="
curl -s -H "Authorization: Bearer $AWX_TOKEN" \
     -H "Content-Type: application/json" \
     "$AWX_HOST/api/v2/jobs/?status=running" | \
     jq -r '.results[] | "\(.id) | \(.name) | \(.status) | \(.elapsed)s"' | \
     column -t -s '|'

echo
echo "Failed Jobs (Last 5):"
echo "====================="
curl -s -H "Authorization: Bearer $AWX_TOKEN" \
     -H "Content-Type: application/json" \
     "$AWX_HOST/api/v2/jobs/?status=failed&page_size=5" | \
     jq -r '.results[] | "\(.id) | \(.name) | \(.status) | \(.created)"' | \
     column -t -s '|'
