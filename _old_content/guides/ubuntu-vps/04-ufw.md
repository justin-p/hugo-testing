---
title: "04. UFW"
description: "Setting up a basic firewall files using the commandline."
date: 2020-03-06T11:46:11+01:00
draft: false
weight: 50
---

## UFW

UFW stands for uncomplicated firewall. UFW actually is not a firewall itself, instead it is a configuration program for iptables.

First of all, make sure that UFW is installed on the server with the following command: `sudo apt install ufw`

### Default settings

In the most cases firewalls are configured to block all incoming traffic and allow all outgoing traffic by default. If this is your first time i'd recommend configuring it like just like that. Todo this run the following 2 commands:

`sudo ufw default deny incoming`

`sudo ufw default allow outgoing`

### Some allow rules

Now that we blocked all incoming traffic we should ensure that where still able to manage this machine after enabling the firewall. This means we need to allow SSH. In most cases, HTTP and HTTPS traffic is crucial as well. You can allow these 3 services by running the commands below.

`sudo ufw allow ssh`

`sudo ufw allow http`

`sudo ufw allow https`

### Enable UFW

Now we need to make sure we enable the firewall. Todo so this run `sudo ufw enable`

Afterwords you can check your config by running `sudo ufw status verbose`

### Also see

For more information on UFW and on how to use it see the following pages:

* [UFW Essentials](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)
* [How to setup a firewall with ufw](https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server)
* [Advanced UFW setups](https://www.cyberciti.biz/faq/howto-configure-setup-firewall-with-ufw-on-ubuntu-linux/)
