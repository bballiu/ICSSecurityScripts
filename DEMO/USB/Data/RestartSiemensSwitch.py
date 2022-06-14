#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error,  http.client, http.cookiejar, os
def showBanner():    
    os.system('cls' if os.name == 'nt' else 'clear')    
    print ("")

showBanner()
ipaddress = '10.20.2.5'
username = 'admin'
password = 'Onderzoekb211'
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.1'
oCj = http.cookiejar.CookieJar()
webPage = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(oCj))
login_data = urllib.parse.urlencode({'log':'in','name':username,'code':password,'_':505037}).encode("utf-8")
response = webPage.open('http://'+ipaddress+'/login.mwp', login_data).read()
print(response)
respArr = response.split(b',')
sResp = respArr[0].split(b':')[1].replace(b'"',b'')
print(sResp.decode())
if sResp.decode() == 'OK':    
    sCode = respArr[2].split(b':')[1].replace(b'"',b'').replace(b'}',b'')    
    print(sCode)
    print(('Generated Login Code '+sCode.decode()))    
    webPage2 = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(oCj))    
    post_data = urllib.parse.urlencode({'pageMode':'action','button':'BWbmGeneralRestartSystem_0','_':sCode.decode()+'99999'}).encode()
    try:
        response = webPage.open('http://'+ipaddress+'/restart.mwp', post_data).read()
        print(response)
    except (http.client.IncompleteRead) as e:
        response = e.partial

    print(sResp)
    sResp = response.split(b',')[0].split(b':')[1].replace(b'"',b'')    
    print(response)
    if sResp == 'OK':      
        print('Looks fine, switch should be restarting')
