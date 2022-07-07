#! /usr/bin/env python
##  Simple version for IOS Pyto demo
from pyModbusTCP.client import ModbusClient
import time


timeout=5
timeout2=1

## MAIN SHOW ##    
#c = ModbusClient(host="172.20.2.30", port=502, auto_open=True, auto_close=True)

# 01000110 01001100 01000001 01000111 00101101 00110000 00110001 00111000 00110011 00110011 00110010 00110100 00111000 00001010
print("ModbusRiderLed.py")

c = ModbusTcpClient(host="123.145.120.102", port=502, auto_open=True)

print("Will now start the LED walk")
def putLow(c,i):
    c.write_coil(i,0)

for x in range(0,16):
        putLow(c,x)
 #01000110 01001100 01000001 01000111 00101101 00110000 00110001 00111000 00110011 00110011 00110010 00110100 00111000 00001010
 #98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432 98765432
 # little endian + 2

while(1):
    c.write_coil(3,1)
    c.write_coil(4,1)
    c.write_coil(8,1)
    time.sleep(timeout)
    c.write_coil(3,0)
    c.write_coil(4,0)
    c.write_coil(8,0)
    time.sleep(timeout2)
    #01001100
    c.write_coil(4,1)
    c.write_coil(5,1)
    c.write_coil(8,1)
    time.sleep(timeout)
    c.write_coil(4,0)
    c.write_coil(5,0)
    c.write_coil(8,0)
    time.sleep(timeout2)
    #01000001

    c.write_coil(2,1)
    c.write_coil(8,1)
    time.sleep(timeout)
    c.write_coil(2,0)
    c.write_coil(8,0)
    time.sleep(timeout2)

    c.write_coil(2,1)
    c.write_coil(3,1)
    c.write_coil(8,1)
    c.write_coil(4,1)
    time.sleep(timeout)
    c.write_coil(4,0)
    c.write_coil(3,0)
    c.write_coil(2,0)
    c.write_coil(8,0)
    time.sleep(timeout2)

    c.write_coil(7,1)
    c.write_coil(5,1)
    c.write_coil(2,1)
    c.write_coil(4,1)
    time.sleep(timeout)
    c.write_coil(4,0)
    c.write_coil(7,0)
    c.write_coil(5,0)
    c.write_coil(2,0)
    time.sleep(timeout2)

    c.write_coil(7,1)
    c.write_coil(6,1)
    time.sleep(timeout)
    c.write_coil(7,0)
    c.write_coil(6,0)
    time.sleep(timeout2)

    c.write_coil(7,1)
    c.write_coil(6,1)
    c.write_coil(2,1)
    time.sleep(timeout)
    c.write_coil(7,0)
    c.write_coil(6,0)
    c.write_coil(2,0)
    time.sleep(timeout2)


    c.write_coil(7,1)
    c.write_coil(6,1)
    c.write_coil(5,1)
    time.sleep(timeout)
    c.write_coil(7,0)
    c.write_coil(6,0)
    c.write_coil(5,0)
    time.sleep(timeout2)

    c.write_coil(7,1)
    c.write_coil(6,1)
    c.write_coil(3,1)
    c.write_coil(2,1)
    time.sleep(timeout)
    c.write_coil(7,0)
    c.write_coil(6,0)
    c.write_coil(3,0)
    c.write_coil(2,0)
    time.sleep(timeout2)

    c.write_coil(7,1)
    c.write_coil(6,1)
    c.write_coil(3,1)
    time.sleep(timeout)
    c.write_coil(7,0)
    c.write_coil(6,0)
    c.write_coil(3,0)
    time.sleep(timeout2)

    c.write_coil(7,1)
    c.write_coil(6,1)
    c.write_coil(4,1)
    time.sleep(timeout)
    c.write_coil(7,0)
    c.write_coil(6,0)
    c.write_coil(4,0)
    time.sleep(timeout2)

    c.write_coil(7,1)
    c.write_coil(6,1)
    c.write_coil(5,1)
    time.sleep(timeout)
    c.write_coil(7,0)
    c.write_coil(6,0)
    c.write_coil(5,0)
    time.sleep(timeout2)

    c.write_coil(5,1)
    c.write_coil(3,1)
    time.sleep(timeout)
    c.write_coil(5,0)
    c.write_coil(3,0)

c.close()
