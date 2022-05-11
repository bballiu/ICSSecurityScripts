#! /usr/bin/env python
## Requires one thing in Linux and two things in Windows:
## pip install pyModbusTCP
## And in Windows: also
## pip install win_inet_pton
from pyModbusTCP.client import ModbusClient
from win_inet_pton import *
import time

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

## MAIN SHOW ##    
#c = ModbusClient(host="172.20.2.30", port=502, auto_open=True, auto_close=True)
c = ModbusClient(host="123.145.120.102", port=502, auto_open=True)

print("Will now start the LED walk")
ledWalkLeft(c)
ledWalkRight(c)
ledWalkLeft(c)
ledWalkRight(c)
ledWalkLeft(c)
ledWalkRight(c)
c.write_single_coil(0,0)
c.close()
