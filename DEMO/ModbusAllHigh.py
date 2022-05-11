#! /usr/bin/env python
## Requires one thing in Linux and two things in Windows:
## pip install pyModbusTCP
## And in Windows: also
## pip install win_inet_pton
from pyModbusTCP.client import ModbusClient
from win_inet_pton import *
import time

timeout=0.1

def putHigh(c,i):
    c.write_single_coil(i,1)
    
## MAIN SHOW ##    
#c = ModbusClient(host="172.20.2.30", port=502, auto_open=True, auto_close=True)
c = ModbusClient(host="123.145.120.102", port=502, auto_open=True)

for x in range(0,16):
        putHigh(c,x)

c.close()
