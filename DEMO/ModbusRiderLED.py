#! /usr/bin/env python
## Requires one thing in Linux and two things in Windows:
## pip install pyModbusTCP
## And in Windows: also
## pip install win_inet_pton
from pyModbusTCP.client import ModbusClient
import os
import sys
if os.name == 'nt':
    from win_inet_pton import *
import time
import re

timeout=0.1

def putHighAndLow(c,i):
    c.write_single_coil(i,1)
    time.sleep(timeout)
    c.write_single_coil(i,0)

def ledWalkLeft(c):
    #for x in range(8, 15):
    for x in range(0, 9):
        putHighAndLow(c,x)
    c.write_single_coil(9,1)
    time.sleep(timeout)

def ledWalkRight(c):
    time.sleep(timeout)
    c.write_single_coil(9,0)
    for x in range(8,0,-1):
        putHighAndLow(c,x)
    c.write_single_coil(0,1)
    time.sleep(timeout)

def validate_ip_address(address):
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    if bool(match) is False:
        print("IP address {} is not valid".format(address))
        sys.exit(1)
        return False

    for part in address.split("."):
        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            sys.exit(1)
            return False

    print("IP address {} is valid".format(address))
    return True 


## MAIN SHOW ##    
#c = ModbusClient(host="172.20.2.30", port=502, auto_open=True, auto_close=True)
print("ModbusRiderLed.py")
try:
    if validate_ip_address(sys.argv[1]) is False:
        sys.exit(1)
except IndexError:
    print("Please provide an IP address as argument")
    sys.exit(1)

print("Opening connection...")

c = ModbusClient(host=sys.argv[1], port=502, auto_open=True)

print("Will now start the LED walk")
ledWalkLeft(c)
ledWalkRight(c)
ledWalkLeft(c)
ledWalkRight(c)
ledWalkLeft(c)
ledWalkRight(c)
c.close()
