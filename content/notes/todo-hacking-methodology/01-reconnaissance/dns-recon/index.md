---
### The title for the content.
title : "DNS-Recon"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "dns"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "DNS-Recon, if you don't know where stuff is its gonna get hard to hack it."
### The datetime assigned to this page.
date : 2020-03-10T16:43:44+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "dns"
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

## dns

## External services

| Service                                            | info                                            |
|----------------------------------------------------|-------------------------------------------------|
| [dnsdumpster](https://dnsdumpster.com/)            | dns recon & research, find & lookup dns records |
| [cert.sh](https://cert.sh)                         | Certficate fingerprint search engine            |

## [PSDNSDumpsterAPI](https://github.com/justin-p/PSDNSDumpsterAPI)

### Return the results from dnsdumpster as a PSObject

```powershell
$DomainInfo=Invoke-PSDnsDumpsterAPI -Domains 'justin-p.me'
```

## [sublist3r](https://github.com/aboul3la/Sublist3r)

### Enumerate subdomains of specific domain

```bash
sublist3r -d example.com
```

### Show only subdomains which have ports 80 and 443 open

```bash
sublist3r -d example.com -p 80,443
```

### Save results in txt file

```bash
sublist3r -d example.com -o ~/output/file.txt
```

## [OWASP Amass](https://github.com/OWASP/Amass/blob/master/doc/user_guide.md)

### The most basic use of the tool for subdomain enumeration

```bash
amass enum -d example.com
```

### Typical parameters for DNS enumeration

```bash
amass enum -v -src -ip -brute -min-for-recursive 2 -d example.com
```
