import random
import csv
import json
import pathlib

def load_file(filePath):
    suffix = pathlib.Path(filePath).suffix
    if suffix == ".csv":
        with open(filePath, mode="r") as file:
            return [row for row in csv.DictReader(file)]
    if suffix == ".json":
        return json.load(open(filePath))

def extract_10_random_items(items):
    return random.sample(items, 10)

def pretty_show_items(items):
    organized_items = json.dumps(sort_keys=True, indent=4, obj=items)
    print(organized_items)
    return organized_items