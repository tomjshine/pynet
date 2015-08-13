#!/usr/bin/env python

# import modules needed
from pprint import pprint as pp
import json, yaml

# initialize list and dict
my_list = []
my_dict = {'key1': 'val1','key2': 'val2', 'key3': {'subkey1': 'subval1', 'subkey2': 'subval2'}}
my_list = range(10)
my_list.append(my_dict)

# dump to json
with open('json.txt', 'w') as f:
    json.dump(my_list, f, sort_keys=True, indent=4)

# dump to yaml
with open('yaml.txt', 'w') as f:
    yaml.dump(my_list, f)
