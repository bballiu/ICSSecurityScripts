#! /usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient
timeout=0.1

def putHigh(c,i):
    c.write_coil(i,1)

## MAIN SHOW ##    
c = ModbusTcpClient(host="123.145.120.102", port=502, auto_open=True)
print("Turning on outputs")
for x in range(0,16):
        putHigh(c,x)

c.close()
