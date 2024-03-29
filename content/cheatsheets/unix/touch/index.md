---
### The title for the content.
title : "touch"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "touch"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "change file timestamps."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "touch"
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

## touch

### Usage

```bash
touch [OPTION] [FILE]
```

### Flags

```bash
-a
    change only the access time

-c, --no-create
    do not create any files

-d, --date=STRING
    parse STRING and use it instead of current time

-f
    (ignored)

-h, --no-dereference
    affect each symbolic link instead of any referenced file (useful only on systems that can change the timestamps of a symlink)

-m
    change only the modification time

-r, --reference=FILE
    use this files times instead of current time

-t STAMP
    use [[CC]YY]MMDDhhmm[.ss] instead of current time

--time=WORD
    change the specified time: WORD is access, atime, or use: equivalent to -a WORD is modify or mtime: equivalent to -m

--help
    display this help and exit

--version
    output version information and exit
```

### Examples

#### create a empty file

```bash
touch file1
```

#### update timestamp and modification

```bash
touch -am file
```

#### use timestamp of file4 on file 5

```bash
touch -r file4 file5
```

#### make file7 30 seconds older than file6

```bash
touch -r file6 -B 30 file7
```

#### set timestamp to specific timestamp

```bash
touch -d '1 May 2005 10:22' file8
touch -d '14 May' file9
touch -d '14:24' file9
```

#### avoid creating new file

```bash
touch -c file10
```

### Also see

N/A
