---
### The title for the content.
title: "09. Logwatch"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "09 logwatch"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Setting up Logwatch, a package that parses logs files on your system and sends over a report."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "09-logwatch"
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

## Logwatch

Logwatch is a package that parses logs files on your system and sends over a report. This is a useful way to monitor whats going on and ensure you can spot issues more timely and easily.

### Update and upgrade your packges

`sudo apt update && sudo apt upgrade`

### Installing Logwatch

`sudo apt install logwatch`

### Configuring Logwatch

#### default.conf/logwatch.conf

`sudo vim /usr/share/logwatch/default.conf/logwatch.conf`

I'd recommend setting following parameters as below:

```bash
Output = mail
Format = html
MailTo = support@domain.tld
MailFrom = logwatch@fqdn-of-the-server-here
Range = Today
Detail = 10
Service = All
```

#### dist.conf/logwatch.conf

`sudo vim /usr/share/logwatch/dist.conf/logwatch.conf`

I'd recommend setting following parameters as below:

`MailFrom = logwatch@fqdn-of-the-server-here`

#### main.cf

`sudo vim /etc/postfix/main.cf`

I'd recommend setting following parameters as below:

`mydestination = $myhostname, FQDN of the server here, localhost.localdomain, localhost`

### Testing Logwatch

`logwatch --mailto your-email@domain.tld`

It is likely that the e-mails sent from the server are getting blocked by spamfilters. Make sure to have a public A-record for your FQDN. Also check your spam filter and/or configure things like MX, SPF, DKIM and
