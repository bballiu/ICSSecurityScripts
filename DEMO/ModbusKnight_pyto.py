#! /usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient
import time 
timeout=0.1

def putHighAndLow(c,i):
    c.write_coil(i,1)
    time.sleep(timeout)
    c.write_coil(i,0)

def ledWalkLeft(c):
    for x in range(0, 9):
        putHighAndLow(c,x)
    c.write_coil(9,1)
    time.sleep(timeout)

def ledWalkRight(c):
    time.sleep(timeout)
    c.write_coil(9,0)
    for x in range(8,0,-1):
        putHighAndLow(c,x)
    c.write_coil(0,1)
    time.sleep(timeout)

def putDblHighAndLow(c,y,z):
    c.write_coil(y,1)
    c.write_coil(z,1)
    time.sleep(timeout)
    c.write_coil(y,0)
    c.write_coil(z,0)

def ledWalkDblLeft(c):
    for x in range(0,8):
        putDblHighAndLow(c,x,(8+x))



## MAIN SHOW ##    
c = ModbusTcpClient(host="123.145.120.102", port=502, auto_open=True)


print("Will now start the LED walk")
ledWalkLeft(c)
ledWalkRight(c)
ledWalkLeft(c)
ledWalkRight(c)
ledWalkLeft(c)
ledWalkRight(c)
ledWalkDblLeft(c)
ledWalkDblLeft(c)
ledWalkDblLeft(c)
ledWalkDblLeft(c)
c.close()
