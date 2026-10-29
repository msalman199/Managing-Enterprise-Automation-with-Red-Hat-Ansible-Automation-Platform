#!/usr/bin/env python3

import os
import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class ConfigGenerator:
    def __init__(self, template_dir, data_dir, output_dir):
        self.template_dir = template_dir
        self.data_dir = data_dir
        self.output_dir = output_dir

        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def load_yaml_data(self, yaml_file):
        try:
            with open(yaml_file, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: Data file {yaml_file} not found")
            return None
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file {yaml_file}: {e}")
            return None

    def generate_config(self, template_name, data_file, output_file):
        try:
            template = self.env.get_template(template_name)

            data = self.load_yaml_data(os.path.join(self.data_dir, data_file))
            if data is None:
                return False

            data['generation_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            config = template.render(data)

            output_path = os.path.join(self.output_dir, output_file)
            with open(output_path, 'w') as file:
                file.write(config)

            print(f"[OK] Generated {output_file} successfully")
            return True

        except Exception as e:
            print(f"[FAIL] Error generating {output_file}: {e}")
            return False

    def generate_all_configs(self):
        """
        Generates the two primary, first-pass configurations:
        one switch and one router. This is a smoke test to confirm
        templates render correctly before the full multi-device
        test suite in Task 3 exercises every template/data pair.
        """
        configs = [
            {
                'template': 'cisco_switch.j2',
                'data': 'switch_data.yaml',
                'output': 'switch_config.txt'
            },
            {
                'template': 'cisco_router.j2',
                'data': 'router_data.yaml',
                'output': 'router_config.txt'
            }
        ]

        print("Generating primary network configurations...")
        print("=" * 50)

        success_count = 0
        for config in configs:
            if self.generate_config(config['template'], config['data'], config['output']):
                success_count += 1

        print("=" * 50)
        print(f"Generated {success_count}/{len(configs)} configurations successfully")

        return success_count == len(configs)

def main():
    base_dir = os.path.expanduser("~/jinja2-lab")
    template_dir = os.path.join(base_dir, "templates")
    data_dir = os.path.join(base_dir, "data")
    output_dir = os.path.join(base_dir, "output")

    os.makedirs(output_dir, exist_ok=True)

    generator = ConfigGenerator(template_dir, data_dir, output_dir)

    if generator.generate_all_configs():
        print("\nPrimary configurations generated successfully.")
        print(f"Check the output directory: {output_dir}")
        print("Run scripts/test_templates.py in Task 3 to test all device combinations.")
    else:
        print("\nSome configurations failed to generate")
        sys.exit(1)

if __name__ == "__main__":
    main()
