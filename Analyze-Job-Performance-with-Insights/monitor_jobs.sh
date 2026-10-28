#!/bin/bash

# Monitor system resources during job execution
echo "Monitoring system performance..."

# Create log file with headers
echo "Timestamp,CPU_Usage,Memory_Usage,Load_Average,Active_Jobs" > /tmp/system_performance.csv

while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    memory_usage=$(free | grep Mem | awk '{printf "%.2f", $3/$2 * 100.0}')
    load_avg=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}' | tr -d ',')
    
    # Count active ansible processes
    active_jobs=$(ps aux | grep -c '[a]nsible-playbook')
    
    echo "$timestamp,$cpu_usage,$memory_usage,$load_avg,$active_jobs" >> /tmp/system_performance.csv
    
    sleep 30
done
