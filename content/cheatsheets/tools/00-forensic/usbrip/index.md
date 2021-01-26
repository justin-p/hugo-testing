---
### The title for the content.
title : "usbrip"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "usbrip"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "usbrip description."
### The datetime assigned to this page.
date : 2020-03-10T16:36:31+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "usbrip"
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

## usbrip

usbrip is a small piece of software which analyzes Linux log data for constructing USB event history tables.

### Install

```bash
pip3 install --upgrade usbrip
```

### Usage

```bash
usbrip MODULE SUBMODULE FLAGS
```

### Examples

#### show history

```bash
root@kali:/mnt/hgfs/_shared_folder/# usbrip events history

         _     {{4}}    {v2.1.4-7}
 _ _ ___| |_ ___[e]___
| | |_ -| . |  _[N] . |
|___|___|___|_| [5]  _|
               x[!]_|   https://github.com/snovvcrash/usbrip


[*] Started at 2020-01-09 23:09:28
[23:09:28] [INFO] Trying to run journalctl...
[23:09:28] [INFO] Successfully runned journalctl
[23:09:28] [INFO] Reading journalctl output
100%|████████████████████████████████▉| 3848/3849 [00:00<00:00, 115044.31line/s]
[?] How would you like your event history list to be generated?

    1. Terminal stdout
    2. JSON-file

[>] Please enter the number of your choice (default is 1): 1
[23:09:30] [INFO] Preparing gathered events
[23:09:30] [INFO] Representation: Table

┌USB-History-Events───┬──────┬──────┬──────┬───────────────────────────┬──────────────────────────────────┬───────────────┬───────┬─────────────────────┐
│           Connected │ User │  VID │  PID │                   Product │                     Manufacturer │ Serial Number │  Port │        Disconnected │
├─────────────────────┼──────┼──────┼──────┼───────────────────────────┼──────────────────────────────────┼───────────────┼───────┼─────────────────────┤
│ 2020-01-08 •••••••• │ −−−− │ −−−− │ −−−− │ −−−−−−−−−−−−−−−−−−−−−−−−− │ −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− │ −−−−−−−−−−−−− │ −−−−− │ −−−−−−−−−−−−−−−−−−− │
│ 2020-01-08 16:01:58 │ kali │ 1d6b │ 0002 │      EHCI Host Controller │ Linux 5.3.0-kali3-amd64 ehci_hcd │  0000:02:03.0 │  usb1 │                   ∅ │
│ 2020-01-08 16:01:58 │ kali │ 1d6b │ 0001 │      UHCI Host Controller │ Linux 5.3.0-kali3-amd64 uhci_hcd │  0000:02:00.0 │  usb2 │                   ∅ │
│ 2020-01-08 16:01:58 │ kali │ 0e0f │ 0003 │  VMware Virtual USB Mouse │                           VMware │             ∅ │   2-1 │                   ∅ │
│ 2020-01-08 16:01:58 │ kali │ 0e0f │ 0002 │    VMware Virtual USB Hub │                                ∅ │             ∅ │   2-2 │                   ∅ │
│ 2020-01-08 16:01:58 │ kali │ 0e0f │ 0008 │ Virtual Bluetooth Adapter │                           VMware │  000650268328 │ 2-2.1 │                   ∅ │
└─────────────────────┴──────┴──────┴──────┴───────────────────────────┴──────────────────────────────────┴───────────────┴───────┴─────────────────────┘
[*] Shut down at 2020-01-09 23:09:30
[*] Time taken: 0:00:01.911036
```

#### search for violations

```bash
usbrip events violations auth.json -f syslog

         _     {{4}}    {v2.1.4-7}
 _ _ ___| |_ ___[E]___
| | |_ -| . |  _[n] . |
|___|___|___|_| [s]  _|
               x[!]_|   https://github.com/snovvcrash/usbrip


[*] Started at 2020-01-09 23:03:24
[23:03:31] [INFO] Reading "/mnt/hgfs/_shared_folder/syslog"
100%|██████████████████████████████| 900000/900000 [00:36<00:00, 24803.74line/s]
[23:04:09] [INFO] Opening authorized device list: "/mnt/hgfs/_shared_folder//auth.json"
[23:04:11] [INFO] Searching for violations
```

### Also see

* [Github](https://github.com/snovvcrash/usbrip)
