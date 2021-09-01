---
### The title for the content.
title: "DNS Recon"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "dns"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "DNS Recon, if you don't know where stuff is its gonna get hard to hack it."
### The datetime assigned to this page.
date: 2020-03-10T16:43:44+01:00
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
weight: 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
tags: ["DNS Recon"]
---

## DNS Recon

When targeting an orgianization you want to know where their resources live. Apart from getting to know where their assets are most of the times these days there is a proxy infront of web applications that require the correct vhost (DNS hostname) to access them.

### DNS Bruteforce

[Seclists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS) has great wordlists for DNS bruteforce.

Try to find commonalities between domains and iterating names. Think about web01.domain.tld and web02.domain.tld, try web03,04,05 etc.

### MX/SPF

Looking at SPF/MX records can give you additional hostnames/ip addresses. Try to preform reverse lookups on these IPs.

## External services

| Service                                     | info                                                                                     |
| ------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [dnsdumpster](https://dnsdumpster.com/)     | dns recon & research, find & lookup dns records                                          |
| [threatcrowd](https://www.threatcrowd.org/) | ThreatCrowd is a system for finding and researching artefacts relating to cyber threats. |
| [RIPE](https://apps.db.ripe.net/db-web-ui/query) & [ARIN](https://whois.arin.net/ui/) whois | search the registration database of RIPE and ARIN |

## Related tools

{{< related_pages_table tag="DNS Recon" >}}
