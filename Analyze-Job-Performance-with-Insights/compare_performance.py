#!/usr/bin/env python3

import csv
import json
import statistics
from datetime import datetime

def read_performance_data(filename):
    """Read performance data from log file"""
    data = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    data.append({
                        'timestamp': parts[0],
                        'test_type': parts[1],
                        'duration': float(parts[2]),
                        'host': parts[3]
                    })
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return data

def compare_performance():
    """Compare original vs optimized performance"""
    
    original_data = read_performance_data('/tmp/performance_log.txt')
    optimized_data = read_performance_data('/tmp/performance_log_optimized.txt')
    
    print("Performance Comparison Report")
    print("=" * 50)
    
    # Group data by test type
    original_by_type = {}
    optimized_by_type = {}
    
    for record in original_data:
        test_type = record['test_type']
        if test_type not in original_by_type:
            original_by_type[test_type] = []
        original_by_type[test_type].append(record['duration'])
    
    for record in optimized_data:
        test_type = record['test_type'].replace('_OPTIMIZED', '')
        if test_type not in optimized_by_type:
            optimized_by_type[test_type] = []
        optimized_by_type[test_type].append(record['duration'])
    
    # Compare performance
    for test_type in original_by_type.keys():
        if test_type in optimized_by_type:
            orig_avg = statistics.mean(original_by_type[test_type])
            opt_avg = statistics.mean(optimized_by_type[test_type])
            improvement = ((orig_avg - opt_avg) / orig_avg) * 100
            
            print(f"\n{test_type}:")
            print(f"  Original Average: {orig_avg:.2f} seconds")
            print(f"  Optimized Average: {opt_avg:.2f} seconds")
            print(f"  Improvement: {improvement:.1f}%")
            
            if improvement > 0:
                print(f"  ✅ Performance improved by {improvement:.1f}%")
            else:
                print(f"  ❌ Performance degraded by {abs(improvement):.1f}%")

def generate_insights_report():
    """Generate a comprehensive insights report"""
    
    report = {
        'timestamp': datetime.now().isoformat(),
        'recommendations': [],
        'performance_metrics': {},
        'optimization_results': {}
    }
    
    # Add recommendations based on analysis
    report['recommendations'].extend([
        {
            'category': 'Connection Optimization',
            'recommendation': 'Enable SSH pipelining and connection multiplexing',
            'impact': 'High',
            'implementation': 'Update ansible.cfg with pipelining=True'
        },
        {
            'category': 'Parallel Execution',
            'recommendation': 'Use strategy: free for independent tasks',
            'impact': 'Medium',
            'implementation': 'Add strategy: free to playbook'
        },
        {
            'category': 'Fact Gathering',
            'recommendation': 'Disable fact gathering when not needed',
            'impact': 'Medium',
            'implementation': 'Set gather_facts: no in playbook'
        },
        {
            'category': 'Resource Management',
            'recommendation': 'Monitor system resources during execution',
            'impact': 'High',
            'implementation': 'Implement continuous monitoring'
        }
    ])
    
    # Save report
    with open('/tmp/insights_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\nInsights Report Generated:")
    print("-" * 30)
    for rec in report['recommendations']:
        print(f"• {rec['category']}: {rec['recommendation']}")
        print(f"  Impact: {rec['impact']}")
        print(f"  Implementation: {rec['implementation']}\n")

if __name__ == "__main__":
    compare_performance()
    generate_insights_report()
