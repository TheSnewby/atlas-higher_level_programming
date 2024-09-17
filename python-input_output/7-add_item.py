#!/usr/bin/python3
"""
Load, add, save
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = sys.argv[1:]
try:
    file_list = load_from_json_file('add_item.json')
except Exception:
    file_list = []
file_list.extend(arg_list)
save_to_json_file(file_list, 'add_item.json')
