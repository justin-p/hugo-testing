---
### The title for the content.
title : "Hydra"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "hydra"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Bruteforce logins."
### The datetime assigned to this page.
date : 2020-03-10T16:43:45+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "hydra"
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
tags : ["Tools","bruteforce","password-spraying"]
---

## Hydra

### Installation

```bash
apt install apt-get install libssl-dev libssh-dev libidn11-dev libpcre3-dev libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev firebird-dev libmemcached-dev libgpg-error-dev libgcrypt11-dev libgcrypt20-dev
git clone https://github.com/vanhauser-thc/thc-hydra
cd thc-hydra
./configure
make
make install
```

### Usage

```bash
hydra [[[-l LOGIN|-L FILE] [-p PASS|-P FILE]] | [-C FILE]] [-e nsr] [-o FILE] [-t TASKS] [-M FILE [-T TASKS]] [-w TIME] [-W TIME] [-f] [-s PORT] [-x MIN:MAX:CHARSET] [-c TIME] [-ISOuvVd46] [-m MODULE_OPT] [service://server[:PORT][/OPT]]
```

### Flags

Flags

```bash
-R        restore a previous aborted/crashed session
-I        ignore an existing restore file (don't wait 10 seconds)
-S        perform an SSL connect
-s PORT   if the service is on a different default port, define it here
-l LOGIN or -L FILE  login with LOGIN name, or load several logins from FILE
-p PASS  or -P FILE  try password PASS, or load several passwords from FILE
-x MIN:MAX:CHARSET  password bruteforce generation, type "-x -h" to get help
-y        disable use of symbols in bruteforce, see above
-r        use a non-random shuffling method for option -x
-e nsr    try "n" null password, "s" login as pass and/or "r" reversed login
-u        loop around users, not passwords (effective! implied with -x)
-C FILE   colon separated "login:pass" format, instead of -L/-P options
-M FILE   list of servers to attack, one entry per line, ':' to specify port
-o FILE   write found login/password pairs to FILE instead of stdout
-b FORMAT specify the format for the -o FILE: text(default), json, jsonv1
-f / -F   exit when a login/pass pair is found (-M: -f per host, -F global)
-t TASKS  run TASKS number of connects in parallel per target (default: 16)
-T TASKS  run TASKS connects in parallel overall (for -M, default: 64)
-w / -W TIME  wait time for a response (32) / between connects per thread (0)
-c TIME   wait time per login attempt over all threads (enforces -t 1)
-4 / -6   use IPv4 (default) / IPv6 addresses (put always in [] also in -M)
-v / -V / -d  verbose mode / show login+pass for each attempt / debug mode 
-O        use old SSL v2 and v3
-K        do not redo failed attempts (good for -M mass scanning)
-q        do not print messages about connection errors
-U        service module usage details
-m OPT    options specific for a module, see -U output for information
-h        more command line options (COMPLETE HELP)
server    the target: DNS, IP or 192.168.0.0/24 (this OR the -M option)
service   the service to crack (see below for supported protocols)
OPT       some service modules support additional input (-U for module help)
```

### Examples

#### known username, password list on ssh

root with passwordlist, null password, login as pass and reversed login as pass.

```bash
hydra -v -V -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt 192.168.88.129 ssh -t 8 -e nsr
```

#### user list, password list on ssh

userlist with passwordlist, null password, login as pass and reversed login as pass looped around users.

```bash
hydra -v -V -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/metasploit/unix_passwords.txt 192.168.88.129 ssh -t 8 -e nsr -u
```

#### Basic auth brute-force + password list

```bash
hydra -l admin -P <passwords.txt> -s 443 -f domain.tld https-get /   
```

#### Basic auth brute-force + username & password list

```bash
hydra -L <users.txt> -P <passwords.txt> -s 443 -f domain.tld https-get /   
```

### Related pages

{{< related_pages_table tag="password-spraying" >}}

### Also see

[Github Project](https://github.com/vanhauser-thc/thc-hydra)