# CVE-2022-35568
A proof of concept for TP-LINK router AC1750 v2 Buffer Overflow.

## Intro
In July 2022 I found a new vulnerability in the TP-LINK router. 

<img src="https://raw.githubusercontent.com/gscamelo/TP-Link-AC1750-v2/main/images/02.jpeg" width=50% height=50%>

A buffer overflow in the httpd daemon on TP-Link Archer C7 v2 (firmware version 3.15.3 Build 180114) devices allows an authenticated remote attacker to execute arbitrary code via a malicious Folder Sharing request to /userRpm/NasFolderSharingRpm.htm.

To exploit the vulnerability simple adding a new folder request could be abused to achieve a classic RCE bug, after playing around with the parameters I found sending a long string inside the parameter "shareFolderName" produced that the application gets stuck, and the web interface stops responding to requests and even the WIFI AP stop working.

## PoC
```
python xpl.py 
[#] Trying to obtein a valid Session!
[#] A session was obteined!
[#] Crafting Payload
[#] Triggering the Bug
```

![Crash](/images/01.jpeg)


## Timeline

+ July 01, 2022 - Vulnerability identified
+ July 07, 2022 - Vulnerability reported
+ August 19, 2022 - Mitre Reserved CVE-2022-35568

## LINKS

https://www.tp-link.com/en/support/download/archer-c7/v2/
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-35568

