#########################################################
#  __                    , _                            #
# / ()      ,   _       /|/ \ ,_  o      _|_   ,  |)    #
# >-   |/\_/ \_/ \_/|/|  |__//  | | /|/|  |   / \_|/\   #
# \___/|_/  \/ \_/  | |_/|      |/|/ | |_/|_/o \/ |  |  #
#     (|                                                #
#########################################################

# Simple script that takes an IP address as argument and lets
# you print and then cut off whatever you can type

import sys
import re
import socket



def netcat(_ip, _port, _content):
    #initilize connection

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((_ip,_port))

    sock.sendall(_content)
    sock.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while True:
        data = sock.recv(1024)
        if(not data):
            break
        res += data.decode()

    print(res)

    print("Connection closed.")
    sock.close()

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

ip = sys.argv[1]
port = 9100

print("Start entering text:")
print("Close connection by entering: exit")

try:
    while 1:
        buf =""
        shouldClose = False

        inp = input("")
        while inp != "":
            if (inp == "exit"):
                shouldClose = True
            buf += inp + "\n"
            inp = input("")
    
        buf += "\n"
        netcat(ip,port, buf.encode())
    
        if(shouldClose):
             break
except(ConnectionRefusedError):
    print("Target refused communication, make sure the provided IP belongs to an Epson printer")

print("Cutting label...")
netcat(ip, port, "\x1B@\x1DV1".encode)