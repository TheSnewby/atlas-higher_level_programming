#!/usr/bin/python3
"""
Load, add, save
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

p_list = sys.argv[1:]
try:
    f = load_from_json_file('add_item.json')
except Exception:
    f = []

save_to_json_file(p_list, 'add_item.json')
