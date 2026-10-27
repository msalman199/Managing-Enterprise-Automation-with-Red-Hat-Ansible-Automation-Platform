#!/usr/bin/env python3

from flask import Flask, request, jsonify
import json
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/webhook-receiver.log'),
        logging.StreamHandler()
    ]
)

@app.route('/webhook/job-status', methods=['POST'])
def job_status_webhook():
    try:
        data = request.get_json()
        
        # Log the received webhook
        logging.info(f"Received webhook: {json.dumps(data, indent=2)}")
        
        # Extract job information
        job_id = data.get('id')
        job_name = data.get('name')
        job_status = data.get('status')
        job_url = data.get('url')
        
        # Process different job statuses
        if job_status == 'successful':
            handle_successful_job(job_id, job_name, data)
        elif job_status == 'failed':
            handle_failed_job(job_id, job_name, data)
        elif job_status == 'running':
            handle_running_job(job_id, job_name, data)
        
        return jsonify({'status': 'received', 'job_id': job_id}), 200
        
    except Exception as e:
        logging.error(f"Error processing webhook: {e}")
        return jsonify({'error': str(e)}), 500

def handle_successful_job(job_id, job_name, data):
    """Handle successful job completion"""
    logging.info(f"Job {job_id} ({job_name}) completed successfully")
    
    # Write success report
    with open(f'/tmp/job-success-{job_id}.log', 'w') as f:
        f.write(f"Job Success Report\n")
        f.write(f"==================\n")
        f.write(f"Job ID: {job_id}\n")
        f.write(f"Job Name: {job_name}\n")
        f.write(f"Completed: {datetime.now()}\n")
        f.write(f"Status: {data.get('status')}\n")

def handle_failed_job(job_id, job_name, data):
    """Handle failed job"""
    logging.error(f"Job {job_id} ({job_name}) failed!")
    
    # Write failure report
    with open(f'/tmp/job-failure-{job_id}.log', 'w') as f:
        f.write(f"Job Failure Report\n")
        f.write(f"==================\n")
        f.write(f"Job ID: {job_id}\n")
        f.write(f"Job Name: {job_name}\n")
        f.write(f"Failed: {datetime.now()}\n")
        f.write(f"Status: {data.get('status')}\n")
        f.write(f"Result Traceback: {data.get('result_traceback', 'N/A')}\n")

def handle_running_job(job_id, job_name, data):
    """Handle running job notification"""
    logging.info(f"Job {job_id} ({job_name}) is now running")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
