#!/usr/bin env python

from snmp_helper import snmp_get_oid, snmp_extract

IP = '50.76.53.27'

router_1 = (IP, 'galileo', 7961)
router_2 = (IP, 'galileo', 8061)


sysName = '1.3.6.1.2.1.1.5.0'
sysDescr = '1.3.6.1.2.1.1.1.0'

def snmp_output(dev, oid): 
        snmp_data = snmp_get_oid(dev, oid)
        output = snmp_extract(snmp_data)
        return output


print '\nRouter 1:'
print snmp_output(router_1, sysName)
print snmp_output(router_1, sysDescr)

print '\nRouter 2:'
print snmp_output(router_2, sysName)
print snmp_output(router_2, sysDescr)

print '\n' 
