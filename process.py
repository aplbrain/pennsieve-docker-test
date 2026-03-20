# process.py
# Basic script to load a set of CSV files and convert them to JSON files

import csv
import json
import os

input_dir = os.environ["INPUT_DIR"]
output_dir = os.environ["OUTPUT_DIR"]

for filename in os.listdir(input_dir):

    # Check to make sure that file is of type CSV
    if not filename.lower().endswith('.csv'):
        print(f"Skipping file {filename} because not a .csv file")
        continue

    # Read CSV
    data = []
    input_file = os.path.join(input_dir, filename)
    with open(input_file, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)

    # Write JSON
    output_file = os.path.join(output_dir, filename.replace(".csv",".json"))
    with open(output_file, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Successfully converted {input_file} → {output_file}")
