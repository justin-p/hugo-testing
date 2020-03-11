---
title: "08. Fail2ban"
description: "Setting up a Fail2Ban, a package that will automatically ban brute forcing IPs."
date: 2020-03-06T11:48:23+01:00
draft: false
weight: 90
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
