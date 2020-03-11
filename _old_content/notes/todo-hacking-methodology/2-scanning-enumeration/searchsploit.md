---
title: "searchsploit"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---


## Search

```bash
searchsploit "Samba < 2."
```

## show web url instead of local

```bash
searchsploit -w "Samba < 2."
```

## open exploit in editor

```bash
searchsploit -x exploits/linux/remote/16321.rb
```

## copy exploit to current folder

```bash
searchsploit -m exploits/linux/remote/16321.rb
```
