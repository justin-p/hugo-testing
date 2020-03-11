---
### The title for the content.
title: "06. Setup sshd"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "06 setup sshd"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Hardening the SSH Deamon."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "06-setup-sshd"
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
