#!/usr/bin/env python

import time
import telnetlib

IP = '50.76.53.27'
PORT = 23
TIMEOUT = 5

username = 'pyclass'
password = '88newclass'

def telnet_connect(ip_addr):
    return telnetlib.Telnet(IP, PORT, TIMEOUT)
    
def login(remote_conn):
    output = remote_conn.read_until('sername:', TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until('ssword:', TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def send_command(cmd):
    remote_conn.write(cmd + "\n")
    time.sleep(1)
    return remote_conn.read_very_eager()
    
ip_addr = '50.76.53.27'
cmd = 'show ip int brief'

remote_conn = telnet_connect(ip_addr)
output = login(remote_conn)


output = send_command(cmd)

print output

