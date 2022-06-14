#########################################################
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#           Created by Benoit.balliu@howest.be          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#########################################################

# Simple script that takes an IP address as argument and lets
# you print and then cut off whatever you can type aka imitates netcat

import sys
import re
import socket

# 'netcat implementation' that only sends data to target and does not wait for an answer
def netcat(_ip, _port, _content):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((_ip,_port))
    sock.sendall(_content)
    sock.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)
    sock.close()

# Look for IP address in argument
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


try:
    if validate_ip_address(sys.argv[1]) is False:
        sys.exit(1)
except IndexError:
    print("Please provide an IP address as argument")
    sys.exit(1)

## var ##
ip = sys.argv[1]
port = 9100
shouldClose = False

print("Start entering text:")
print("Close connection by entering: exit")

## read every line from input (if not exit) and send that to the printer
try:
    while 1:
        buf =""
        inp = input(":. ")

        if (inp == "exit"):
                shouldClose = True
        buf += inp + "\n"
        
        if(shouldClose):
             break

        netcat(ip,port,buf.encode())
    
    # send cut command to printer after exit
    print("Cutting label...")
    netcat(ip, port, "\x1B@\x1DV1".encode())     

# Nices error message
except(ConnectionRefusedError):
    print("Target refused communication, make sure the provided IP belongs to an Epson printer")
    sys.exit(1)

