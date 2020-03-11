---
### The title for the content.
title: "02. Managing of packages"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "02 packges"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Managing packages using the commandline."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "02-packges"
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
