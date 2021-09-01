---
### The title for the content.
title : "WPAD"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "wpad"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "WPAD description."
### The datetime assigned to this page.
date : 2020-03-10T16:43:46+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "wpad"
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

## WPAD

Windows can use a upstream proxy. To make configuring this proxy easier WPAD can be used. Web Proxy Auto-Discovery Protocol (WPAD) is a method used by clients to locate the URL of a configuration file using DHCP and/or DNS. 

A attacker can serve a fake WPAD server and respond to client WPAD name resolutions. The client then requests the wpad.dat file from this fake WPAD Server. Responder creates an authentication screen and asks clients to enter the username and password they use in the domain.

## Attacking

[responder](https://github.com/lgandx/Responder) + [ntlmrelayx](https://github.com/SecureAuthCorp/impacket)

[mitm6](https://github.com/fox-it/mitm6) + [ntlmrelayx](https://github.com/SecureAuthCorp/impacket) + ([getSP.py](https://github.com/SecureAuthCorp/impacket) + ) [secretsdump.py](https://github.com/SecureAuthCorp/impacket)
