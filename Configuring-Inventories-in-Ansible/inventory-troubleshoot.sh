#!/bin/bash

echo "=== Ansible Inventory Troubleshooting ==="
echo

echo "1. Checking Ansible version:"
ansible --version
echo

echo "2. Testing static inventory parsing:"
ansible-inventory -i static-inventory.yml --list > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Static inventory parsed successfully"
else
    echo "✗ Static inventory parsing failed"
    ansible-inventory -i static-inventory.yml --list
fi
echo

echo "3. Testing host connectivity (static):"
ansible -i static-inventory.yml all -m ping --one-line 2>/dev/null || echo "✗ Some hosts unreachable"
echo

echo "4. Checking group definitions:"
echo "Available groups in static inventory:"
ansible-inventory -i static-inventory.yml --list | jq -r 'keys[]' | grep -v "_meta" | sort
echo

echo "5. Testing dynamic inventory:"
if [ -f "aws_ec2_inventory.py" ]; then
    ./aws_ec2_inventory.py --list > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "✓ Dynamic inventory script working"
    else
        echo "✗ Dynamic inventory script failed"
    fi
else
    echo "✗ Dynamic inventory script not found"
fi
echo

echo "6. Checking SSH connectivity:"
echo "Testing SSH key permissions:"
ls -la ~/.ssh/id_rsa 2>/dev/null || echo "✗ SSH private key not found"
echo

echo "=== Troubleshooting Complete ==="
