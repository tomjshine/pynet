#!/usr/share/env python

from ciscoconfparse import CiscoConfParse

conf = CiscoConfParse("cisco_ipsec.txt")

crypto = conf.find_objects(r"crypto map CRYPTO")


#print crypto

print "\nCRYPTO MAPS THAT CONTAIN 'set pfs group2':"
for c in crypto:
    for chil in c.children:
        if 'set pfs group2' in chil.text:
            print "!"
            print c.text
            print chil.text

print "\n"
