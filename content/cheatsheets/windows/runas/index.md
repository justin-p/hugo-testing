---
### The title for the content.
title : "runas"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "runas"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "run programs as other users."
### The datetime assigned to this page.
date : 2021-09-01T22:06:23+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "runas"
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

## runas

### Usage

```bash
RUNAS [ [/noprofile | /profile] [/env] [/savecred | /netonly] ] /user:UserName program

RUNAS [ [/noprofile | /profile] [/env] [/savecred] ] /smartcard [/user:UserName] program

RUNAS /showtrustlevels

RUNAS /trustlevel:TrustLevel program
```

### Flags

```bash
/noprofile       Do not load the user's profile.
                 This causes the application to load more quickly, but
                 can cause some applications to malfunction.
/profile         Load the user's profile. (default)
/env             Use the current environment instead of user's.
/netonly         Use the credentials for remote access only.
/savecred        Use credentials previously saved by the user.
/smartcard       Load the credentials from a smartcard.
/user            UserName in the form USER@DOMAIN or DOMAIN\USER
/trustlevel Level  One of levels enumerated in /showtrustlevels.
                   RunAs is not able to launch an application with an elevated
                   access token.
program          The program to run.
```

### Examples

#### Run program as AD-user context for network tasks

```bash
runas /netonly /user:<DOMAIN>\<USER> program
```

### Also see

N/A