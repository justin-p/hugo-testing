---
title: "06. Setup sshd"
description: "Hardening the SSH Deamon."
date: 2020-03-06T11:47:43+01:00
draft: false
weight: 70
---

## Setup sshd

### Only give access to specific users and groups

You can tell your server which users are allowed to connect to your server through SSH and who are not. You can do this with the the `AllowUsers` keyword in the SSHD configuration file.Todo so, edit the configuration file \(`/etc/ssh/sshd_config`\). The same can be done for groups using the `AllowGroups` keyword.

In the example below we tell our system that only the user `beheer` is allowed to authenticate using SSH.

`AllowUsers beheer`

### Do not allow the user root to access the server over SSH

The `root` is the a account that has _all_ the permissions on the system, if someone with bad intentions is able to logon with root its game-over.
In the SSH-configuration file there is a options to enable/disable root logon. You will see the following rule/line: `PermitRootLogin value`

Make sure to adjust it to the following: `PermitRootLogin no`

### Only allow authentication with private keys

To further secure the server we are going to only allow SSH logins on the server with SSH keys.

```bash
PubkeyAuthentication yes
PasswordAuthentication no
```

In order to process the made changes we need to restart the ssh deamon. You can use the following command todo so: `sudo service sshd restart`
