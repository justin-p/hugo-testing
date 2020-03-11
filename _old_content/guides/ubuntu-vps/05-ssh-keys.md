---
title: "05. SSH Keys"
description: "Generating and setting up SSH Keys."
date: 2020-03-06T11:46:49+01:00
draft: false
weight: 60
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
