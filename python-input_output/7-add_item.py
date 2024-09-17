#!/usr/bin/python3
"""Load, add, save"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file


p_list = sys.argv[1:]
load_from_json_file('add_item.json')
for i in range(len(p_list)):
    # consider if not created, create it
    save_to_json_file(p_list[i], 'add_item.json')

