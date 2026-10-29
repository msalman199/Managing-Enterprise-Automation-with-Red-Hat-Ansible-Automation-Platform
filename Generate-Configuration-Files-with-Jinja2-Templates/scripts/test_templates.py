#!/usr/bin/env python3

import os
import sys
import re
import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import argparse

class TemplateValidator:
    def __init__(self, template_dir, data_dir, output_dir):
        self.template_dir = template_dir
        self.data_dir = data_dir
        self.output_dir = output_dir

        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def validate_template_syntax(self, template_name):
        try:
            self.env.get_template(template_name)
            print(f"[OK] Template {template_name} syntax is valid")
            return True
        except Exception as e:
            print(f"[FAIL] Template {template_name} syntax error: {e}")
            return False

    def test_template_with_data(self, template_name, data_file):
        try:
            template = self.env.get_template(template_name)

            data_path = os.path.join(self.data_dir, data_file)
            with open(data_path, 'r') as file:
                data = yaml.safe_load(file)

            data['generation_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            config = template.render(data)

            base_name = os.path.splitext(data_file)[0]
            template_base = os.path.splitext(template_name)[0]
            output_file = f"{base_name}_{template_base}.txt"

            output_path = os.path.join(self.output_dir, output_file)
            with open(output_path, 'w') as file:
                file.write(config)

            print(f"[OK] Rendered {template_name} with {data_file} -> {output_file}")
            return True, output_file

        except Exception as e:
            print(f"[FAIL] Error rendering {template_name} with {data_file}: {e}")
            return False, None

    def analyze_template_variables(self, template_name):
        try:
            template_path = os.path.join(self.template_dir, template_name)
            with open(template_path, 'r') as file:
                content = file.read()

            variables = set()

            var_pattern = r'\{\{\s*([^}]+)\s*\}\}'
            for match in re.findall(var_pattern, content):
                var_name = match.split('|')[0].split('.')[0].strip()
                if var_name not in ('loop', 'item'):
                    variables.add(var_name)

            for_pattern = r'\{%\s*for\s+\w+\s+in\s+([^%]+)\s*%\}'
            for match in re.findall(for_pattern, content):
                variables.add(match.strip())

            print(f"Variables referenced in {template_name}:")
            for var in sorted(variables):
                print(f"  - {var}")

            return variables

        except Exception as e:
            print(f"Error analyzing template {template_name}: {e}")
            return set()

    def run_comprehensive_test(self):
        print("JINJA2 TEMPLATE TESTING SUITE")
        print("=" * 60)

        test_combinations = [
            ('cisco_switch.j2', 'switch_data.yaml'),
            ('cisco_switch.j2', 'dist_switch_data.yaml'),
            ('cisco_router.j2', 'router_data.yaml'),
            ('cisco_router.j2', 'branch_router_data.yaml'),
        ]

        results = []

        print("\n1. TEMPLATE SYNTAX VALIDATION")
        print("-" * 40)
        templates = sorted(set(combo[0] for combo in test_combinations))
        for template in templates:
            self.validate_template_syntax(template)

        print("\n2. TEMPLATE VARIABLE ANALYSIS")
        print("-" * 40)
        for template in templates:
            print(f"\n{template}:")
            self.analyze_template_variables(template)

        print("\n3. TEMPLATE RENDERING TESTS")
        print("-" * 40)
        for template, data_file in test_combinations:
            success, output_file = self.test_template_with_data(template, data_file)
            results.append({
                'template': template,
                'data': data_file,
                'success': success,
                'output': output_file
            })

        print("\n4. TEST SUMMARY")
        print("-" * 40)
        successful = sum(1 for r in results if r['success'])
        total = len(results)
        print(f"Successful tests: {successful}/{total}")

        if successful < total:
            print("\nFailed tests:")
            for result in results:
                if not result['success']:
                    print(f"  FAIL: {result['template']} + {result['data']}")

        print(f"\nGenerated files are in: {self.output_dir}")

        return successful == total

def main():
    parser = argparse.ArgumentParser(description='Test Jinja2 templates')
    parser.add_argument('--template', help='Specific template to test')
    parser.add_argument('--data', help='Specific data file to use')
    args = parser.parse_args()

    base_dir = os.path.expanduser("~/jinja2-lab")
    template_dir = os.path.join(base_dir, "templates")
    data_dir = os.path.join(base_dir, "data")
    output_dir = os.path.join(base_dir, "output")

    os.makedirs(output_dir, exist_ok=True)

    validator = TemplateValidator(template_dir, data_dir, output_dir)

    if args.template and args.data:
        success, output_file = validator.test_template_with_data(args.template, args.data)
        if success:
            print(f"Test successful. Output: {output_file}")
        else:
            print("Test failed")
            sys.exit(1)
    else:
        if validator.run_comprehensive_test():
            print("\nAll tests passed.")
        else:
            print("\nSome tests failed")
            sys.exit(1)

if __name__ == "__main__":
    main()
