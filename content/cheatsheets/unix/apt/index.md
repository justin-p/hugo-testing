---
### The title for the content.
title : "apt"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "apt"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "A commandline package manager and provides commands for searching and managing as well as querying information about packages."
### The datetime assigned to this page.
date : 2021-09-01T15:38:25+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "apt"
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

## apt

### Usage

```bash
apt [options] [command]
```

### Flags

```bash
list - list packages based on package names
search - search in package descriptions
show - show package details
install - install packages
reinstall - reinstall packages
remove - remove packages
autoremove - Remove automatically all unused packages
update - update list of available packages
upgrade - upgrade the system by installing/upgrading packages
full-upgrade - upgrade the system by removing/installing/upgrading packages
edit-sources - edit the source information file
satisfy - satisfy dependency strings
```

### Examples

#### Update local repositories

```bash
apt update
```

#### Install all updates

```bash
apt update
```

#### Update specific package

```bash
apt --only-upgrade install <package>
```

#### Fix dependencies

```bash
apt --fix-broken install
```

#### Remove program and dependencies

```bash
apt install -f <package>.deb
```

### Also see

N/A