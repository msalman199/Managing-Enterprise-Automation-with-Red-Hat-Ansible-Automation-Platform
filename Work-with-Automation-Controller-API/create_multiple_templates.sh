#!/bin/bash

AWX_TOKEN=$1
AWX_HOST=$2
PROJECT_ID=$3
INVENTORY_ID=$4

for i in {1..3}; do
    cat > bulk_template_$i.json << EOF
{
  "name": "Bulk-Template-$i",
  "description": "Bulk created template $i",
  "job_type": "run",
  "inventory": $INVENTORY_ID,
  "project": $PROJECT_ID,
  "playbook": "lamp_simple/site.yml",
  "verbosity": 1
}
