---
title: "e-mail address gathering"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---

## External services

| Service                          | info                    |
|----------------------------------|-------------------------|
| [hunter.io](https://hunter.io)   | find email addresses    |
| [emailrep](https://emailrep.io/) | get e-mail 'reputation' |

## TheHarvester

### Basic Synatx

```bash
theHarvester -d [domain] -l [depth] -b [search engine name]
```

### Scan domain on google

```bash
theHarvester -d justin-p.me -l 500 -b google
```

### Save results in a HTML and XML file

```bash
theHarvester -d justin-p.me -l 500 -b google -f exportfile
```
