---
### The title for the content.
title: "07. Unattended Upgrades"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "07 unattended upgrades"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Automating security updates and reboots."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "07-unattended-upgrades"
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


## Unattended Upgrades

Updates are important. But where all lazy, so we want to automate some of this process. To ensure our server is always using the latest important security updates we are going to configure Unattended upgrades.

_Normally this is installed by default, but some hosting providers might use custom images which strip some packages from the default installation._

### Install unattended-upgrades

```bash
sudo apt-get install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

### Configure unattended-upgrades

`sudo vim /etc/apt/apt.conf.d/50unattended-upgrades`

#### Auto reboot

Some updates require a restart after installing, kernel updates being one of them. On ubuntu if you don't reboot the server the new kernel will not be loaded. To ensure you are running on the latest kernel version you can configure unattended-upgrades to auto reboot at a specific time.

```bash
// Automatically reboot *WITHOUT CONFIRMATION*
//  if the file /var/run/reboot-required is found after the upgrade
Unattended-Upgrade::Automatic-Reboot "true";

// If automatic reboot is enabled and needed, reboot at the specific
// time instead of immediately
//  Default: "now"
Unattended-Upgrade::Automatic-Reboot-Time "04:00";
```

#### Mail

The file `50unattended-upgrades` can be manually adjusted to send mails if unattended upgrades fail on the server.

```bash
// Send email to this address for problems or packages upgrades
// If empty or unset then no email is sent, make sure that you
// have a working mail setup on your system. A package that provides
// 'mailx' must be installed. E.g. "user@example.com"
Unattended-Upgrade::Mail "user@example.com";

// Set this value to "true" to get emails only on errors. Default
// is to always send a mail if Unattended-Upgrade::Mail is set
Unattended-Upgrade::MailOnlyOnError "true";
```

It is likely that the e-mails sent from the server are getting blocked by spamfilters. Make sure to have a public A-record for your FQDN. Also check your spam filter and/or configure things like MX, SPF, DKIM and DMARC.
