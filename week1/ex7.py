#!/usr/bin/env python

from pprint import pprint as pp
import json, yaml

my_dict = {}
my_dict_yaml = {}

with open('json.txt', 'r') as f:
    my_dict[0] = json.load(f)

with open('yaml.txt', 'r') as f:
    my_dict[1] = yaml.load(f)


pp(my_dict)
