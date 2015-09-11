#!/usr/bin/env python

import time
import telnetlib
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        print sys.exit("Connection timed out")
    
def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnet_connect(ip_addr)
    login(remote_conn, username, password)
    
    time.sleep(1)
    output = remote_conn.read_very_eager()    

    send_command(remote_conn, "terminal length 0")
    cmd = "show version"
    output = send_command(remote_conn, cmd).lstrip(cmd)
    print output

    remote_conn.close()

if __name__ == "__main__":
    main() 
