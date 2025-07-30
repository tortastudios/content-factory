#!/usr/bin/env python3
import yaml
import os
import sys
from pathlib import Path

def extract_keys_recursive(data, current_path=''):
    """Recursively extract all keys from a YAML structure."""
    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            new_path = f"{current_path}.{key}" if current_path else key
            if isinstance(value, (dict, list)):
                result[key] = extract_keys_recursive(value, new_path)
            else:
                result[key] = ""
        return result
    elif isinstance(data, list):
        if data and isinstance(data[0], dict):
            # If it's a list of dicts, return the structure of the first item
            return [extract_keys_recursive(data[0], current_path)]
        else:
            # If it's a list of simple values, return empty list
            return []
    else:
        return ""

def process_yaml_file(input_path, output_path):
    """Process a single YAML file and extract only keys."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if data is None:
            print(f"Warning: {input_path} is empty or invalid")
            return
        
        keys_only = extract_keys_recursive(data)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(keys_only, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print(f"Processed: {input_path} -> {output_path}")
        
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    source_dir = "/Users/cthor/Dev/bakery/content-factory"
    output_dir = "/Users/cthor/Dev/bakery/temp-content-factory/context-profiles"
    
    # Find all YAML files in the source directory
    yaml_files = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                yaml_files.append(os.path.join(root, file))
    
    print(f"Found {len(yaml_files)} YAML files")
    
    for yaml_file in yaml_files:
        # Create relative path from source directory
        rel_path = os.path.relpath(yaml_file, source_dir)
        output_file = os.path.join(output_dir, rel_path)
        
        process_yaml_file(yaml_file, output_file)

if __name__ == "__main__":
    main()