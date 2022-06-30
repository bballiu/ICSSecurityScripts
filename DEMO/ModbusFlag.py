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

timeout=5



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

# 01000110 01001100 01000001 01000111 00101101 00110000 00110001 00111000 00110011 00110011 00110010 00110100 00111000 00001010
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
def putLow(c,i):
    c.write_single_coil(i,0)

for x in range(0,16):
        putLow(c,x)
 #01000110 01001100 01000001 01000111 00101101 00110000 00110001 00111000 00110011 00110011 00110010 00110100 00111000 00001010
 #98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432
 # little endian + 2
c.write_single_coil(3,1)
c.write_single_coil(4,1)
c.write_single_coil(8,1)
time.sleep(timeout)
c.write_single_coil(3,0)
c.write_single_coil(4,0)
c.write_single_coil(8,0)

#01001100
c.write_single_coil(4,1)
c.write_single_coil(5,1)
c.write_single_coil(8,1)
time.sleep(timeout)
c.write_single_coil(4,0)
c.write_single_coil(5,0)
c.write_single_coil(8,0)

#01000001

c.write_single_coil(2,1)
c.write_single_coil(8,1)
time.sleep(timeout)
c.write_single_coil(2,0)
c.write_single_coil(8,0)

c.write_single_coil(2,1)
c.write_single_coil(3,1)
c.write_single_coil(8,1)
c.write_single_coil(4,1)
time.sleep(timeout)
c.write_single_coil(4,0)
c.write_single_coil(3,0)
c.write_single_coil(2,0)
c.write_single_coil(8,0)

c.write_single_coil(7,1)
c.write_single_coil(5,1)
c.write_single_coil(2,1)
c.write_single_coil(4,1)
time.sleep(timeout)
c.write_single_coil(4,0)
c.write_single_coil(7,0)
c.write_single_coil(5,0)
c.write_single_coil(2,0)

c.write_single_coil(7,1)
c.write_single_coil(6,1)
time.sleep(timeout)
c.write_single_coil(7,0)
c.write_single_coil(6,0)

c.write_single_coil(7,1)
c.write_single_coil(6,1)
c.write_single_coil(2,1)
time.sleep(timeout)
c.write_single_coil(7,0)
c.write_single_coil(6,0)
c.write_single_coil(2,0)


c.write_single_coil(7,1)
c.write_single_coil(6,1)
c.write_single_coil(5,1)
time.sleep(timeout)
c.write_single_coil(7,0)
c.write_single_coil(6,0)
c.write_single_coil(5,0)

c.write_single_coil(7,1)
c.write_single_coil(6,1)
c.write_single_coil(3,1)
c.write_single_coil(2,1)
time.sleep(timeout)
c.write_single_coil(7,0)
c.write_single_coil(6,0)
c.write_single_coil(3,0)
c.write_single_coil(2,0)

c.write_single_coil(7,1)
c.write_single_coil(6,1)
c.write_single_coil(3,1)
time.sleep(timeout)
c.write_single_coil(7,0)
c.write_single_coil(6,0)
c.write_single_coil(3,0)

c.write_single_coil(7,1)
c.write_single_coil(6,1)
c.write_single_coil(4,1)
time.sleep(timeout)
c.write_single_coil(7,0)
c.write_single_coil(6,0)
c.write_single_coil(4,0)

c.write_single_coil(7,1)
c.write_single_coil(6,1)
c.write_single_coil(5,1)
time.sleep(timeout)
c.write_single_coil(7,0)
c.write_single_coil(6,0)
c.write_single_coil(5,0)

c.write_single_coil(5,1)
c.write_single_coil(3,1)
time.sleep(timeout)
c.write_single_coil(5,0)
c.write_single_coil(3,0)

c.close()
