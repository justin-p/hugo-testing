---
### The title for the content.
title : "Web"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "gobuster"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Web"
### The datetime assigned to this page.
date : 2020-03-10T16:43:44+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "gobuster"
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



## gobuster

## General scan

```bash
./go/bin/gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt -t 40 -e
```

## Bigger wordlist and extensions

```bash
gobuster dir -u http://example.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html,sql -t 40 -e
```

## run trough burpsuite

```
~/go/bin/gobuster dir -u http://192.168.56.101:12380 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,sql,html,txt  -t 40 -e -p http://127.0.0.1:8080
```

## kadimus

LFI Scan & Exploit Tool (@hc0d3r - P0cL4bs Team)

## general scan, through burp and save results

```
kadimus -u http://192.168.56.103/?page=login --proxy http://127.0.0.1:8080 --output outputfile
```

## get file

```
kadimus -u http://192.168.56.103/?page=login --parameter page --get-source --filename "login" --proxy http://127.0.0.1:8080
``` 


## nikto

## General scan

```bash
nikto -h [hostname/ip]
```

## Output to file

```bash
nikto -h [hostname/ip] -output [filename]
```


## run trough burpsuite

`LW_SSL_ENGINE=SSLeay`

```bash
nikto -h [hostname/ip] -useproxy http://localhost:8080/
```


## wpscan

## General scan (mostly passive)

get all vuln plugins/themes, get Timthumbs, config backups, Medias and users

`wpscan --url https://192.168.56.101:12380/blogblog/ --disable-tls-checks --enumerate vp,vt,tt,cb,dbe,u,m`

## General scan + WPVulnDB API

`wpscan --url https://192.168.56.101:12380/blogblog/ --disable-tls-checks --enumerate vp,vt,tt,cb,dbe,u,m --api-token TOKEN `

## Aggressive scan + WPVulnDB API (go ham)

`wpscan --url https://192.168.56.101:12380/blogblog/ --disable-tls-checks --enumerate ap,at,tt,cb,dbe,u,m --detection-mode aggressive --plugins-detection aggressive --plugins-version-detection aggressive --api-token TOKEN`
