---
### The title for the content.
title: "05. SSH Keys"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "05 ssh keys"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Generating and setting up SSH Keys."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "05-ssh-keys"
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

## SSH Keys

SSH keys allow you to connect to servers with a secret key AND password. If configured correctly, without the key a person would not be able to authenticate itself through SSH, even if it somehow got possession of your a user accounts password.

### Generating and using SSH keys

As a example in this guide we will use `PuTTY` for generating and using SSH keys. If you do not have PuTTY installed on your own system and want to follow along, click [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/) to download it.

If you do have `PuTTY` installed, make sure `PuTTYgen` is installed as well.

We will use PuTTYgen to generate the keypair. Start up PuTTYgen and press the `Generate` button.

![Generate](/img/guides/ubuntu-vps/05-ssh-keys-PuTTYgen.jpg)

Move your mouse over the `Key` area untill the progress bar it is completely filled up. PuTTYgen uses the mouse movements to collect randomness.

When complete, the public key should appear in the Window.  You can now specify a passphrase for the key. I recommended using a passphrase for private key files intended for interactive use.

Save your private key on your own system by pressing the `Save private key` button within PuTTYgen. The private key should be kept to yourself and is used to authenticate yourself against the public key that we placed on the server.

ave your private key on your own system by pressing the `Save private key` button within PuTTYgen. This text will be added to a SSH `authorized_keys` file on servers that you want to use this Public-Private key paring on.

Now you need to add this key paring on your server. Todo so login on your Linux server and run the the following commands:

```bash
mkdir ~/.ssh
chmod 0700 ~/.ssh
touch ~/.ssh/authorized_keys
chmod 0644 ~/.ssh/authorized_keys
```

Then edit file `~/.ssh/authorized_keys` using the following command:

`sudo vim ~/.ssh/authorized_keys`

Press the `i` key on your keyboard once to enter `input-mode` within vim. Paste the public key in this file. Save the file by pressing `ESC`, then typing `:wq!` and pressing `ENTER`.

To ensure everything is setup correctly you can run the commands below to adjust the file owner, permissions and group on the `.ssh` folder and `authorized_keys` file.

```bash
chown beheer:beheer ~/.ssh -R
chmod 0700 ~/.ssh
chmod 0644 ~/.ssh/authorized_keys
```

### Also see

* [Understanding public key private key concepts](http://blakesmith.me/2010/02/08/understanding-public-key-private-key-concepts.html)
