---
title: "02. Managing of packages"
description: "Managing packages using the commandline."
date: 2020-03-06T11:39:47+01:00
draft: false
weight: 30
---

## Managing of packages

Nearly all Linux distributions come preinstalled with a packet manager. A packet manager is an application that pulls software packages from a software library and installs them on the system.

### Why a package manager is awesome

If you want to install a web server on Windows, you will first need to manually perform several steps to download the installer and install it on your system.

On Linux \(Ubuntu in this example\), only a simple command is required: `apt install nginx`. The package manager \(APT\) makes sure that nginx gets downloaded from a trusted source and is properly installed on your system.

APT also has many other functionalities, like:

* Searching for available software packages in all software libraries.
* Updating old software packages.
* Updating your operating system \(system upgrade\).

**Warning:** On older Linux versions, you are possible required to extend the `apt` command to `apt-get`.

#### Examples of using apt

Performing updates on all installed packages `apt update && apt upgrade`

Searching for a package called nginx in the package library `apt search nginx`

### Useful packages

Below are several packages that will make your life managing a server much more easy. I recommended to install these applications on every server by default.

`apt install htop ranger tmux ncdu`  

### Also see

* [HTOP explained visually](https://codeahoy.com/2017/01/20/hhtop-explained-visually/)
* [Check disk space usage on linux using ncdu](https://www.ostechnix.com/check-disk-space-usage-linux-using-ncdu/)
* [Official Ranger user guide](https://github.com/ranger/ranger/wiki/Official-user-guide)
* [A quick and easy guide to tmux](http://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)
* [Tmux Cheatsheet](https://gist.github.com/MohamedAlaa/2961058)
