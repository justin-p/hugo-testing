---
title: "SSH SHA256 to public key"
description: "Find out which public key was used to logon"
date: 2020-03-06T11:12:09+01:00
draft: false
weight: 50
---

```bash
Accepted publickey for beheer from 10.0.0.1 port 17073 ssh2: RSA SHA256:13456798132456789123
```

```bash
ssh-keygen -lf ~/.ssh/authorized_keys
9999 SHA256:13456798132456789123 JustinPerdok@some-PC (RSA)
```
