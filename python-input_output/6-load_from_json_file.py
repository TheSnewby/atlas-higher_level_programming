#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Ojbect from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
