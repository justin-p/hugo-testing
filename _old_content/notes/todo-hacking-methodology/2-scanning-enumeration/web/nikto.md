---
title: "nikto"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---

## General scan

```bash
nikto -h [hostname/ip]
```

## Output to file

```bash
nikto -h [hostname/ip] -output [filename]
```


## run trough burpsuite

`LW_SSL_ENGINE=SSLeay`

```bash
nikto -h [hostname/ip] -useproxy http://localhost:8080/
```