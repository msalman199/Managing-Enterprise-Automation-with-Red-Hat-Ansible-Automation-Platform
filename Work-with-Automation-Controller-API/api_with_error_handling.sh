#!/bin/bash

AWX_TOKEN=$1
AWX_HOST=$2

make_api_call() {
    local method=$1
    local endpoint=$2
    local data=$3
    
    if [ -n "$data" ]; then
        response=$(curl -s -w "\n%{http_code}" -X "$method" \
                       -H "Authorization: Bearer $AWX_TOKEN" \
                       -H "Content-Type: application/json" \
                       -d "$data" \
                       "$AWX_HOST$endpoint")
    else
        response=$(curl -s -w "\n%{http_code}" -X "$method" \
                       -H "Authorization: Bearer $AWX_TOKEN" \
                       -H "Content-Type: application/json" \
                       "$AWX_HOST$endpoint")
    fi
    
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n -1)
    
    if [[ $http_code -ge 200 && $http_code -lt 300 ]]; then
        echo "Success: $http_code"
        echo "$body" | jq '.' 2>/dev/null || echo "$body"
        return 0
    else
        echo "Error: HTTP $http_code"
        echo "$body" | jq '.' 2>/dev/null || echo "$body"
        return 1
    fi
}

# Test with a valid endpoint
echo "Testing valid endpoint:"
make_api_call "GET" "/api/v2/ping/"

echo
echo "Testing invalid endpoint:"
make_api_call "GET" "/api/v2/nonexistent/"
