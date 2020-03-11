---
### The title for the content.
title : "Discover Open Ports"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "2 scanning enumeration"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "SCAN ALL THE THINGS!"
### The datetime assigned to this page.
date : 2020-03-10T16:33:38+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "2-scanning-enumeration"
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
### a map of Front Matter keys whose values are passed down to the page’s descendants unless overwritten by self or a closer ancestor’s cascade. 
cascade:
    tags: ['Scanning and Enumeration']
---

## Discover Open Ports

### netdiscover


```bash
netdiscover -r 192.168.1.0/24
```


### masscan

#### scan all ports

```bash	
masscan 10.11.0.0/16
```

#### scan port range

```bash
masscan 10.11.0.0/16 -p22-25 --rate 1000
```

#### Scan 'n' Number of nmap‘s Top Ports

```bash
masscan 10.11.0.0/16 ‐‐top-ports 100 --rate 1000
```

#### Output to file

```bash
-oX filename: Output to filename in XML.
-oG filename: Output to filename in Grepable format.
-oJ filename: Output to filename in JSON format.
```

### nmap

#### General scan

```bash
nmap -T4 -A -oA outputfolder 10.10.10.10
```

#### Scan for all TCP ports

```bash
nmap -T4 -p- -A 10.10.10.10
```

#### General UDP scan

```bash
nmap -T4 -p -sU 10.10.10.10
```

#### ARP scan

```bash
nmap -n -sn -PR 10.10.10.0/24
```

#### Host discovery

ARP,ICMP,SYN 443/tcp, ACK 80/tcp

```bash
nmap -n -sn 10.10.10.10
```
