#!/usr/bin/env python3

import time
import logging
from job_monitor import AWXJobMonitor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/awx-monitor.log'),
        logging.StreamHandler()
    ]
)

def main():
    monitor = AWXJobMonitor("http://localhost", "admin", "password")
    
    while True:
        try:
            # Check for running jobs
            jobs = monitor.get_recent_jobs(limit=10)
            running_jobs = [job for job in jobs if job['status'] == 'running']
            
            for job in running_jobs:
                logging.info(f"Monitoring running job: {job['id']} - {job['name']}")
            
            time.sleep(60)  # Check every minute
            
        except Exception as e:
            logging.error(f"Error in monitoring loop: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
