#!/usr/bin/env python3

import csv
import json
import statistics
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def analyze_performance_logs():
    """Analyze performance test results"""
    
    # Read performance data
    performance_data = []
    
    try:
        with open('/tmp/performance_log.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    performance_data.append({
                        'timestamp': parts[0],
                        'test_type': parts[1],
                        'duration': float(parts[2]),
                        'host': parts[3]
                    })
    except FileNotFoundError:
        print("Performance log file not found. Run some tests first.")
        return
    
    # Analyze by test type
    test_types = {}
    for record in performance_data:
        test_type = record['test_type']
        if test_type not in test_types:
            test_types[test_type] = []
        test_types[test_type].append(record['duration'])
    
    # Generate statistics
    print("Performance Analysis Report")
    print("=" * 50)
    
    for test_type, durations in test_types.items():
        print(f"\n{test_type} Performance:")
        print(f"  Average Duration: {statistics.mean(durations):.2f} seconds")
        print(f"  Median Duration: {statistics.median(durations):.2f} seconds")
        print(f"  Min Duration: {min(durations):.2f} seconds")
        print(f"  Max Duration: {max(durations):.2f} seconds")
        print(f"  Standard Deviation: {statistics.stdev(durations):.2f} seconds")
        print(f"  Total Runs: {len(durations)}")
    
    # Identify performance issues
    print("\nPerformance Recommendations:")
    print("-" * 30)
    
    for test_type, durations in test_types.items():
        avg_duration = statistics.mean(durations)
        std_dev = statistics.stdev(durations) if len(durations) > 1 else 0
        
        if std_dev > avg_duration * 0.3:
            print(f"⚠️  {test_type}: High variability detected (std dev: {std_dev:.2f})")
            print("   Recommendation: Check for resource contention or network issues")
        
        if avg_duration > 60:
            print(f"⚠️  {test_type}: Long execution time (avg: {avg_duration:.2f}s)")
            print("   Recommendation: Consider optimization or parallel execution")
    
    return test_types

def analyze_system_performance():
    """Analyze system resource usage during tests"""
    
    try:
        df = pd.read_csv('/tmp/system_performance.csv')
        
        print("\nSystem Resource Analysis:")
        print("=" * 30)
        print(f"Average CPU Usage: {df['CPU_Usage'].mean():.2f}%")
        print(f"Peak CPU Usage: {df['CPU_Usage'].max():.2f}%")
        print(f"Average Memory Usage: {df['Memory_Usage'].mean():.2f}%")
        print(f"Peak Memory Usage: {df['Memory_Usage'].max():.2f}%")
        print(f"Average Load: {df['Load_Average'].mean():.2f}")
        print(f"Peak Load: {df['Load_Average'].max():.2f}")
        
        # Identify resource bottlenecks
        if df['CPU_Usage'].max() > 80:
            print("⚠️  CPU bottleneck detected during tests")
        if df['Memory_Usage'].max() > 80:
            print("⚠️  Memory bottleneck detected during tests")
        if df['Load_Average'].max() > 4:
            print("⚠️  High system load detected during tests")
            
    except FileNotFoundError:
        print("System performance log not found.")

if __name__ == "__main__":
    # Install required packages if not available
    try:
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError:
        print("Installing required packages...")
        import subprocess
        subprocess.run(["pip3", "install", "pandas", "matplotlib"])
        import pandas as pd
        import matplotlib.pyplot as plt
    
    analyze_performance_logs()
    analyze_system_performance()
