---
title: "nmap"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---


## General scan

```bash
nmap -T4 -A -oA outputfolder 10.10.10.10
```

## Scan for all TCP ports

```bash
nmap -T4 -p- -A 10.10.10.10
```

## General UDP scan

```bash
nmap -T4 -p -sU 10.10.10.10
```

## ARP scan

```bash
nmap -n -sn -PR 10.10.10.0/24
```

## Host discovery

ARP,ICMP,SYN 443/tcp, ACK 80/tcp

```bash
nmap -n -sn 10.10.10.10
```
