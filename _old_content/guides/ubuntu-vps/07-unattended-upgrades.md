---
title: "07. Unattended Upgrades"
description: "Automating security updates and reboots."
date: 2020-03-06T11:48:05+01:00
draft: false
weight: 80
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
