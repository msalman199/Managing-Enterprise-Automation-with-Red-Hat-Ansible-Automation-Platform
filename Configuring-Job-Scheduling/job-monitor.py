#!/usr/bin/env python3

import requests
import json
import time
import sys
from datetime import datetime

# AWX Configuration
AWX_HOST = "http://localhost"
AWX_USERNAME = "admin"
AWX_PASSWORD = "password"

class AWXJobMonitor:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.verify = False

    def get_job_status(self, job_id):
        """Get current status of a job"""
        url = f"{self.host}/api/v2/jobs/{job_id}/"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching job status: {e}")
            return None

    def poll_job_completion(self, job_id, poll_interval=10, timeout=3600):
        """Poll job until completion or timeout"""
        start_time = time.time()
        print(f"Starting to monitor job {job_id}")
        
        while time.time() - start_time < timeout:
            job_data = self.get_job_status(job_id)
            
            if not job_data:
                print("Failed to get job status")
                return False
            
            status = job_data.get('status')
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Job {job_id} status: {status}")
            
            if status in ['successful', 'failed', 'error', 'canceled']:
                print(f"Job {job_id} completed with status: {status}")
                self.print_job_summary(job_data)
                return status == 'successful'
            
            time.sleep(poll_interval)
        
        print(f"Job {job_id} monitoring timed out after {timeout} seconds")
        return False

    def print_job_summary(self, job_data):
        """Print job execution summary"""
        print("\n" + "="*50)
        print("JOB EXECUTION SUMMARY")
        print("="*50)
        print(f"Job ID: {job_data.get('id')}")
        print(f"Job Name: {job_data.get('name')}")
        print(f"Status: {job_data.get('status')}")
        print(f"Started: {job_data.get('started')}")
        print(f"Finished: {job_data.get('finished')}")
        print(f"Elapsed: {job_data.get('elapsed')} seconds")
        print("="*50)

    def get_recent_jobs(self, template_name=None, limit=5):
        """Get list of recent jobs"""
        url = f"{self.host}/api/v2/jobs/"
        params = {'page_size': limit, 'order_by': '-created'}
        
        if template_name:
            params['job_template__name'] = template_name
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json().get('results', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching recent jobs: {e}")
            return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 job-monitor.py <job_id>")
        print("   or: python3 job-monitor.py --recent [template_name]")
        sys.exit(1)
    
    monitor = AWXJobMonitor(AWX_HOST, AWX_USERNAME, AWX_PASSWORD)
    
    if sys.argv[1] == '--recent':
        template_name = sys.argv[2] if len(sys.argv) > 2 else None
        jobs = monitor.get_recent_jobs(template_name)
        
        print("Recent Jobs:")
        print("-" * 80)
        for job in jobs:
            print(f"ID: {job['id']:4} | Status: {job['status']:12} | "
                  f"Name: {job['name']:30} | Started: {job.get('started', 'N/A')}")
    else:
        job_id = int(sys.argv[1])
        success = monitor.poll_job_completion(job_id)
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
