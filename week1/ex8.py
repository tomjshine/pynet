#!/usr/share/env python

from ciscoconfparse import CiscoConfParse

conf = CiscoConfParse("cisco_ipsec.txt")

crypto = conf.find_objects(r"crypto map CRYPTO")


#print crypto

print "\nCRYPTO MAPS:"
for c in crypto:
    print "!\n" + c.text
    for chil in c.children:
        print chil.text

print "\n"
