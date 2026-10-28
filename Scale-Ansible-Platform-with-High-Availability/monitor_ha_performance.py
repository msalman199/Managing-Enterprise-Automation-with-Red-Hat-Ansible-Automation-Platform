#!/usr/bin/env python3
# monitor_ha_performance.py

import requests
import time
from datetime import datetime
import threading

class HAMonitor:
    def __init__(self, base_url, check_interval=5):
        self.base_url = base_url
        self.check_interval = check_interval
        self.monitoring = True
        self.results = []
        self.lock = threading.Lock()

    def check_health(self):
        """Perform a single health check against the load balancer endpoint."""
        try:
            response = requests.get(
                f"{self.base_url}/api/v2/ping/",
                timeout=5
            )
            return {
                'timestamp': datetime.now().isoformat(),
                'status': 'healthy' if response.status_code == 200 else 'unhealthy',
                'response_time': response.elapsed.total_seconds(),
                'status_code': response.status_code
            }
        except requests.exceptions.RequestException as e:
            return {
                'timestamp': datetime.now().isoformat(),
                'status': 'error',
                'response_time': None,
                'status_code': None,
                'error': str(e)
            }

    def monitor_loop(self):
        """Continuously poll the health endpoint until monitoring is stopped."""
        while self.monitoring:
            result = self.check_health()
            with self.lock:
                self.results.append(result)

            rt = f"{result['response_time']:.3f}s" if result['response_time'] is not None else "N/A"
            print(f"[{result['timestamp']}] status={result['status']} response_time={rt}")

            time.sleep(self.check_interval)

    def start_monitoring(self, duration=300):
        """Start monitoring for the given duration in seconds, then report."""
        print(f"Starting HA monitoring against {self.base_url} for {duration} seconds...")

        monitor_thread = threading.Thread(target=self.monitor_loop)
        monitor_thread.start()

        time.sleep(duration)
        self.monitoring = False
        monitor_thread.join()

        self.generate_report()

    def generate_report(self):
        """Generate a summary report of collected results."""
        print("\n=== HA MONITORING REPORT ===")

        total = len(self.results)
        healthy = len([r for r in self.results if r['status'] == 'healthy'])
        uptime_pct = (healthy / total) * 100 if total > 0 else 0

        print(f"Total checks: {total}")
        print(f"Healthy checks: {healthy}")
        print(f"Uptime: {uptime_pct:.2f}%")

        response_times = [r['response_time'] for r in self.results if r['response_time'] is not None]
        if response_times:
            avg_response = sum(response_times) / len(response_times)
            max_response = max(response_times)
            min_response = min(response_times)
            print(f"Average response time: {avg_response:.3f}s")
            print(f"Min response time: {min_response:.3f}s")
            print(f"Max response time: {max_response:.3f}s")
        else:
            print("No successful responses were recorded.")


if __name__ == "__main__":
    monitor = HAMonitor(base_url="http://192.168.56.40", check_interval=5)
    monitor.start_monitoring(duration=300)
