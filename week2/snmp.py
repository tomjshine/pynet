#!/usr/bin/env python

import pysnmp
from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY = 'galileo'
IP = '50.76.53.27'
SNMP_PORT = '7961'

def snmp(a_device, oid):
    snmp_data = snmp_get_oid(a_device, oid)
    return snmp_extract(snmp_data)

def main():

    a_device = (IP, COMMUNITY, SNMP_PORT)
    OID = '1.3.6.1.2.1.1.5.0'

    output = snmp(a_device, oid=OID)

    print output

if __name__ == "__main__":
    main()
