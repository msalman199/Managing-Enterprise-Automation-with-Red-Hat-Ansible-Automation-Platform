#!/usr/bin/env python3

import json
import boto3
import sys
from botocore.exceptions import ClientError

def get_ec2_instances():
    """Retrieve EC2 instances and organize them into Ansible inventory format"""
    
    try:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        
        inventory = {
            '_meta': {
                'hostvars': {}
            },
            'all': {
                'children': ['ungrouped']
            },
            'ungrouped': {
                'hosts': []
            }
        }
        
        # Group hosts by tags and instance state
        groups = {}
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] != 'running':
                    continue
                
                # Get instance details
                instance_id = instance['InstanceId']
                private_ip = instance.get('PrivateIpAddress', '')
                public_ip = instance.get('PublicIpAddress', '')
                instance_type = instance['InstanceType']
                
                # Use public IP if available, otherwise private IP
                host_ip = public_ip if public_ip else private_ip
                
                if not host_ip:
                    continue
                
                # Add to hostvars
                inventory['_meta']['hostvars'][host_ip] = {
                    'ansible_host': host_ip,
                    'ec2_instance_id': instance_id,
                    'ec2_instance_type': instance_type,
                    'ec2_private_ip': private_ip,
                    'ec2_public_ip': public_ip,
                    'ec2_state': instance['State']['Name']
                }
                
                # Process tags for grouping
                tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                
                # Group by Name tag
                if 'Name' in tags:
                    name_group = f"tag_Name_{tags['Name'].replace(' ', '_').replace('-', '_')}"
                    if name_group not in groups:
                        groups[name_group] = []
                    groups[name_group].append(host_ip)
                
                # Group by Environment tag
                if 'Environment' in tags:
                    env_group = f"env_{tags['Environment']}"
                    if env_group not in groups:
                        groups[env_group] = []
                    groups[env_group].append(host_ip)
                
                # Group by Role tag
                if 'Role' in tags:
                    role_group = f"role_{tags['Role']}"
                    if role_group not in groups:
                        groups[role_group] = []
                    groups[role_group].append(host_ip)
                
                # Group by instance type
                type_group = f"type_{instance_type.replace('.', '_')}"
                if type_group not in groups:
                    groups[type_group] = []
                groups[type_group].append(host_ip)
                
                # Add tags to hostvars
                for key, value in tags.items():
                    inventory['_meta']['hostvars'][host_ip][f'ec2_tag_{key}'] = value
        
        # Add groups to inventory
        for group_name, hosts in groups.items():
            inventory[group_name] = {
                'hosts': hosts
            }
            
        return inventory
        
    except ClientError as e:
        print(f"Error connecting to AWS: {e}", file=sys.stderr)
        return {'_meta': {'hostvars': {}}}
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return {'_meta': {'hostvars': {}}}

def main():
    """Main function to handle command line arguments"""
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        inventory = get_ec2_instances()
        print(json.dumps(inventory, indent=2))
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        # Return empty dict for host-specific vars (we use _meta)
        print(json.dumps({}))
    else:
        print("Usage: aws_ec2_inventory.py --list")
        print("       aws_ec2_inventory.py --host <hostname>")
        sys.exit(1)

if __name__ == '__main__':
    main()
