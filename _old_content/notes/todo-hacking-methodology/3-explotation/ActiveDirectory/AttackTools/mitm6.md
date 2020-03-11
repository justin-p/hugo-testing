---
title: "mitm6"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---

## Basic command

Command below will send out IPv6 RA and catch DNS requests for lab.justin-p.me.

```bash
sudo mitm6 -i eth0 -d lab.justin-p.me 
```
