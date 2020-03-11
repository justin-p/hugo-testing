---
### The title for the content.
title: "08. Fail2ban"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "08 fail2ban"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Setting up a Fail2Ban, a package that will automatically ban brute forcing IPs."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "08-fail2ban"
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

## Fail2Ban

If you ever connected something to the public internet you might have noticed that within seconds people are knocking on your ports. To avoid people bruteforcing them self into your server you can setup Fail2Ban. Fail2Ban watches logfiles for incorrect logins and automatically bans IP's.

### Installing Fail2Ban

```bash
sudo apt update && sudo apt upgrade
sudo apt install fail2ban
```

Make sure you copy the default Fail2Ban configuration file to `jail.local`. Never edit the file `jail.conf`.

`sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local`

`sudo vim /etc/fail2ban/jail.local`

### Setup IP exclusions

You can configure Fail2Ban to exclude some IPs. You might want to add your own external IP here. Fail2Ban uses CIDR notations.

`ignoreip = 127.0.0.1/8 an.ip.address.here another.goes.here.yeah one.for.another.person`

### Setup for how long a IP will be banned

You can configure Fail2Ban how long IPs are banned. IF you excluded your own external IP i'd recommend setting up permanent bans.

use `bantime = -1`  for permanent bans, otherwise use `bantime = 21600`

### Apply settings

Restart Fail2Ban with the command: `sudo service fail2ban restart`
