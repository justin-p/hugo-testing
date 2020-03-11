---
title: "smbclient"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---


## protocol negotiation failed: NT_STATUS_IO_TIMEOUT

```bash
Resolution: On Kali, edit /etc/samba/smb.conf

Add the following under global:
   client min protocol = CORE
   client max protocol = SMB3
```

## list

```bash
smbclient -L \\\\10.10.10.10\\
```

## download all files

```
smbclient \\\\10.10.10.10\\share
mask ""
recurse ON
prompt OFF
cd "path\to\remote\dir"
lcd "~/path/to/download/to/"
mget *
``` 