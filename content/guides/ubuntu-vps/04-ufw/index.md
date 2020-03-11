---
### The title for the content.
title: "04. UFW"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "04 ufw"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Setting up a basic firewall files using the commandline."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "04-ufw"
### Aliases can be used to create redirects to your page from other URLs.
# aliases : [""]
### Display name of this page modifier. If set, it will be displayed in the footer.
# LastModifierDisplayName : ""
### Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
# LastModifierEmail : ""
### Table of content (toc) is enabled by default. Set this parameter to true to disable it.
# disableToc : true
### Set the page as a chapter, changing the way it's displayed
# chapter : true
### Hide a menu entry by setting this to true
# hidden : true
### If true, the content will not be rendered unless the --buildDrafts flag is passed to the hugo command.
# draft : true
### Used for ordering your content in lists. Lower weight gets higher precedence. So content with lower weight will come first.
### 0 does nothing !
weight : 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
# tags : [""]
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
