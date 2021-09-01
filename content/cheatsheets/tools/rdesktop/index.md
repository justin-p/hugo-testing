---
### The title for the content.
title : "Rdesktop"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "rdesktop"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "A Remote Desktop Protocol client."
### The datetime assigned to this page.
date : 2021-09-01T23:07:10+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "rdesktop"
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

## rdesktop

### Installation

```bash
apt install rdesktop
```

### Usage

```bash
rdesktop [options] server[:port]
```

### Flags

```bash
-u: user name
-d: domain
-s: shell / seamless application to start remotely
-c: working directory
-p: password (- to prompt)
-n: client hostname
-k: keyboard layout on server (en-us, de, sv, etc.)
-g: desktop geometry (WxH[@DPI][+X[+Y]])
-i: enables smartcard authentication, password is used as pin
-f: full-screen mode
-b: force bitmap updates
-L: local codepage
-A: path to SeamlessRDP shell, this enables SeamlessRDP mode
-V: tls version (1.0, 1.1, 1.2, defaults to negotiation)
-B: use BackingStore of X-server (if available)
-e: disable encryption (French TS)
-E: disable encryption from client to server
-m: do not send motion events
-M: use local mouse cursor
-C: use private colour map
-D: hide window manager decorations
-K: keep window manager key bindings
-S: caption button size (single application mode)
-T: window title
-t: disable use of remote ctrl
-N: enable numlock synchronization
-X: embed into another window with a given id.
-a: connection colour depth
-z: enable rdp compression
-x: RDP5 experience (m[odem 28.8], b[roadband], l[an] or hex nr.)
-P: use persistent bitmap caching
-r: enable specified device redirection (this flag can be repeated)
      '-r comport:COM1=/dev/ttyS0': enable serial redirection of /dev/ttyS0 to COM1
          or      COM1=/dev/ttyS0,COM2=/dev/ttyS1
      '-r disk:floppy=/mnt/floppy': enable redirection of /mnt/floppy to 'floppy' share
          or   'floppy=/mnt/floppy,cdrom=/mnt/cdrom'
      '-r clientname=<client name>': Set the client name displayed
          for redirected disks
      '-r lptport:LPT1=/dev/lp0': enable parallel redirection of /dev/lp0 to LPT1
          or      LPT1=/dev/lp0,LPT2=/dev/lp1
      '-r printer:mydeskjet': enable printer redirection
          or      mydeskjet="HP LaserJet IIIP" to enter server driver as well
      '-r sound:[local[:driver[:device]]|off|remote]': enable sound redirection
                  remote would leave sound on server
                  available drivers for 'local':
                  alsa:      ALSA output driver, default device: default
      '-r clipboard:[off|PRIMARYCLIPBOARD|CLIPBOARD]': enable clipboard
                   redirection.
                   'PRIMARYCLIPBOARD' looks at both PRIMARY and CLIPBOARD
                   when sending data to server.
                   'CLIPBOARD' looks at only CLIPBOARD.
      '-r scard[:"Scard Name"="Alias Name[;Vendor Name]"[,...]]
       example: -r scard:"eToken PRO 00 00"="AKS ifdh 0"
                "eToken PRO 00 00" -> Device in GNU/Linux and UNIX environment
                "AKS ifdh 0"       -> Device shown in Windows environment 
       example: -r scard:"eToken PRO 00 00"="AKS ifdh 0;AKS"
                "eToken PRO 00 00" -> Device in GNU/Linux and UNIX environment
                "AKS ifdh 0"       -> Device shown in Microsoft Windows environment 
                "AKS"              -> Device vendor name                 
-0: attach to console
-4: use RDP version 4
-5: use RDP version 5 (default)
-o: name=value: Adds an additional option to rdesktop.
        sc-csp-name        Specifies the Crypto Service Provider name which
                           is used to authenticate the user by smartcard
        sc-container-name  Specifies the container name, this is usually the username
        sc-reader-name     Smartcard reader name to use
        sc-card-name       Specifies the card name of the smartcard to use
-v: enable verbose logging
```

### Examples

#### Verify if Network Level Authentication (NLA) is enabled

```bash
rdesktop -u '' <target>
```

### Also see

* [Rdesktop Github](https://github.com/rdesktop/rdesktop)
