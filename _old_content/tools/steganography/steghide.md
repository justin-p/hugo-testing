---
title: "steghide"
description: "Steghide is a steganography program that is able to hide data in various kinds of image- and audio-files. "
date: 2020-03-06T13:37:43+01:00
draft: false
chapter: true
weight: 120
---

### steghide

#### get info

```bash
root@kali:/mnt/hgfs/_shared_folder# steghide  info hawking
"hawking":
  format: jpeg
  capacity: 3.3 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "flag.txt":
    size: 1.6 KB
    encrypted: rijndael-128, cbc
    compressed: yes
```

#### extract data

```bash
root@kali:/mnt/hgfs/_shared_folder# steghide --extract -sf hawking -p hawking
wrote extracted data to "flag.txt".
```
