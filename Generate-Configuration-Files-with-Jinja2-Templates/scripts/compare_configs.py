#!/usr/bin/env python3

import os
import sys
import difflib

class ConfigComparator:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def compare_files(self, file1, file2):
        try:
            file1_path = os.path.join(self.output_dir, file1)
            file2_path = os.path.join(self.output_dir, file2)

            with open(file1_path, 'r') as f1:
                lines1 = f1.readlines()

            with open(file2_path, 'r') as f2:
                lines2 = f2.readlines()

            diff = list(difflib.unified_diff(
                lines1, lines2,
                fromfile=file1,
                tofile=file2,
                lineterm=''
            ))

            if diff:
                print(f"\nDifferences between {file1} and {file2}:")
                print("-" * 60)
                for line in diff:
                    print(line)
            else:
                print(f"\nNo differences between {file1} and {file2}")

            return len(diff) == 0

        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
            return False
        except Exception as e:
            print(f"Error comparing files: {e}")
            return False

    def analyze_config_structure(self, filename):
        """
        Count structural statistics in a rendered configuration file.
        Handles both switch-style configs (vlan/interface) and
        router-style configs (interface/route/access-list) since the
        same tool is used across device types.
        """
        try:
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()

            stats = {
                'total_lines': len(lines),
                'comment_lines': 0,
                'blank_lines': 0,
                'interface_count': 0,
                'vlan_count': 0,
                'access_list_count': 0,
                'route_count': 0,
            }

            for raw_line in lines:
                line = raw_line.strip()

                if not line:
                    stats['blank_lines'] += 1
                    continue

                if line.startswith('!') or line.startswith('#'):
                    stats['comment_lines'] += 1
                    continue

                if line.startswith('interface '):
                    stats['interface_count'] += 1
                elif line.startswith('vlan '):
                    stats['vlan_count'] += 1
                elif line.startswith('access-list '):
                    stats['access_list_count'] += 1
                elif line.startswith('ip route ') or line.startswith('network '):
                    stats['route_count'] += 1

            return stats

        except FileNotFoundError:
            print(f"Error: File {filename} not found in {self.output_dir}")
            return None
        except Exception as e:
            print(f"Error analyzing {filename}: {e}")
            return None

    def display_stats(self, filename, stats):
        """Print a formatted summary of configuration statistics."""
        print(f"\nStructure analysis for {filename}:")
        print("-" * 60)
        if stats is None:
            print("  No statistics available (file could not be analyzed)")
            return

        print(f"  Total lines:       {stats['total_lines']}")
        print(f"  Comment lines:     {stats['comment_lines']}")
        print(f"  Blank lines:       {stats['blank_lines']}")
        print(f"  Interfaces:        {stats['interface_count']}")
        print(f"  VLANs:             {stats['vlan_count']}")
        print(f"  Access lists:      {stats['access_list_count']}")
        print(f"  Routes/networks:   {stats['route_count']}")

def main():
    base_dir = os.path.expanduser("~/jinja2-lab")
    output_dir = os.path.join(base_dir, "output")

    comparator = ConfigComparator(output_dir)

    print("=" * 60)
    print("CONFIGURATION STRUCTURE ANALYSIS")
    print("=" * 60)

    files_to_analyze = [
        'switch_data_cisco_switch.txt',
        'dist_switch_data_cisco_switch.txt',
        'router_data_cisco_router.txt',
        'branch_router_data_cisco_router.txt',
    ]

    for filename in files_to_analyze:
        stats = comparator.analyze_config_structure(filename)
        comparator.display_stats(filename, stats)

    print("\n" + "=" * 60)
    print("CONFIGURATION COMPARISON")
    print("=" * 60)

    comparator.compare_files(
        'switch_data_cisco_switch.txt',
        'dist_switch_data_cisco_switch.txt'
    )

    comparator.compare_files(
        'router_data_cisco_router.txt',
        'branch_router_data_cisco_router.txt'
    )

if __name__ == "__main__":
    main()
