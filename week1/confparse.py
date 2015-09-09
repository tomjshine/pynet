#!/usr/share/env python

from ciscoconfparse import CiscoConfParse

conf = CiscoConfParse("cisco_ipsec.txt")

intf = conf.find_objects(r"^interface")

print "\nInterfaces with no IP address:"
for i in intf:
    for c in i.children:
        if  "no ip address" in c.text:
            print i.text

desc_list = []
print "\nInterfaces with description:"
for i in intf:
    for c in i.children:
        if  "description"  in c.text:
            desc_list.append(i.text + ": " + c.text)
for i in desc_list:
    print i


