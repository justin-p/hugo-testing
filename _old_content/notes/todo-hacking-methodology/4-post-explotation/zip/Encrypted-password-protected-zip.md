---
title: "Encrypted/Password protected zip"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---

## zip2john

extract zip hash

```
zip2john crackme.zip > crackeziphash.txt
ver 2.0 efh 5455 efh 7875 crackme.zip/DoNotTouch PKZIP Encr: 2b chk, TS_chk, cmplen=335181, decmplen=884736, crc=E8183254
```

### hashcat format

remove zipfilename

```
zip2john crackme.zip | cut -d ":" -f 2 > ziphash.txt
ver 2.0 efh 5455 efh 7875 crackme.zip/DoNotTouch PKZIP Encr: 2b chk, TS_chk, cmplen=335181, decmplen=884736, crc=E8183254
```


## fcrackzip

```
root@kali:~# fcrackzip -u -D -p /usr/share/wordlists/rockyou.txt zipfile.
```