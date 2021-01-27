---
### The title for the content.
title : "encrypted password protected zip"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "encrypted password protected zip"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Show me the hidden goods."
### The datetime assigned to this page.
date : 2020-03-10T16:43:46+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "encrypted-password-protected-zip"
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

## encrypted password protected zip


During your work you might stumble upon an password protected zip. It's possible to extract a password hash that can be cracked with hashcat/john. 

## zip2john

extract zip hash

```
zip2john crackme.zip > crackeziphash.txt
ver 2.0 efh 5455 efh 7875 crackme.zip/DoNotTouch PKZIP Encr: 2b chk, TS_chk, cmplen=335181, decmplen=884736, crc=E8183254
```

### hashcat format

remove zipfilename

```
zip2john crackme.zip | cut -d ":" -f 2 > ziphash.txt
ver 2.0 efh 5455 efh 7875 crackme.zip/DoNotTouch PKZIP Encr: 2b chk, TS_chk, cmplen=335181, decmplen=884736, crc=E8183254
```


## fcrackzip

```
root@kali:~# fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt zipfile.
```