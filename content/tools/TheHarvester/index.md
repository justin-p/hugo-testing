---
### The title for the content.
title : "theHarvester"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "theharvester"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "theHarvester gathers emails, names, subdomains, IPs and URLs using multiple public data sources."
### The datetime assigned to this page.
date : 2020-03-11T15:28:04+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "theharvester"
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

## theHarvester

### Installation

```bash
git clone https://github.com/laramies/theHarvester
cd theHarvester
python3 -m pip install -r requirements/base.txt
python3 theHarvester.py -h 
```

### Usage

```bash
theHarvester -d [domain] -l [depth] -b [search engine name]
```

### Flags

```bash
-d: Domain to search or company name
-b: data source: baidu, bing, bingapi, dogpile, google, googleCSE,
                 googleplus, google-profiles, linkedin, pgp, twitter, vhost,
                 virustotal, threatcrowd, crtsh, netcraft, yahoo, all
-s: start in result number X (default: 0)
-v: verify host name via dns resolution and search for virtual hosts
-f: save the results into an HTML and XML file (both)
-n: perform a DNS reverse query on all ranges discovered
-c: perform a DNS brute force for the domain name
-t: perform a DNS TLD expansion discovery
-e: use this DNS server
-p: port scan the detected hosts and check for Takeovers (80,443,22,21,8080)
-l: limit the number of results to work with(bing goes from 50 to 50 results,
     google 100 to 100, and pgp doesn't use this option)
-h: use SHODAN database to query discovered hosts
```

### Examples

#### Scan domain on google

```bash
theHarvester -d justin-p.me -l 500 -b google
```

#### Save results in a HTML and XML file

```bash
theHarvester -d justin-p.me -l 500 -b google -f exportfile
```

### Also see

* [Github](https://github.com/laramies/theHarvester)
