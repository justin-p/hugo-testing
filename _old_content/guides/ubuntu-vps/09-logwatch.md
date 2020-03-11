---
title: "09. Logwatch"
description: "Setting up Logwatch, a package that parses logs files on your system and sends over a report."
date: 2020-03-06T11:48:40+01:00
draft: false
weight: 100
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
