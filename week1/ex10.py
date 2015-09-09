#!/usr/share/env python

from ciscoconfparse import CiscoConfParse

conf = CiscoConfParse("cisco_ipsec.txt")

crypto = conf.find_objects(r"crypto map CRYPTO")


#print crypto

print "\nCRYPTO MAP ENTRIES NOT USING AES:"
for c in crypto:
    for chil in c.children:
        if "transform" in chil.text and "AES" not in chil.text:
            map_entry = c.text.split()
            ts_name = chil.text.split()
            print("Entry \"{0}\" is not using AES").format(map_entry[3])
            print("Its transform set is called \"{0}\"").format(ts_name[2])
print ""
