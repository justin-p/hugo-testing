---
### The title for the content.
title : "find"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "find"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "search for files in a directory hierarchy."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "find"
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

## find

### Usage

```bash
find PATH CONDITIONS ACTIONS
```

### Conditions

#### search for things that contain '.c'

```bash
-name "*.c"
```

#### search for things owned by user 'jonathan'

```bash
-user jonathan
```

#### search for things with no user that corresponds to file's numeric user ID

```bash
-nouser
```

#### Search for specific type

search for things that are files

```bash
-type f
```

search for things that are directories

```bash
-type d
```

search for things that are symlinks

```bash
-type l
```

#### search only 2 folders deep

```bash
-maxdepth 2
```

#### search with a regex pattern

```bash
-regex PATTERN
```

#### search for specific file sizes

Exactly 8 512-bit blocks

```bash
-size 8
```

Smaller than 128 bytes

```bash
-size -128c
```

Exactly 1440KiB

```bash
-size 1440k
```

Larger than 10MiB

```bash
-size +10M
```

Larger than 2GiB

```bash
-size +2G
```

#### search for files modified more recently then file.txt

```bash
-newer file.txt
```

`m`odified newer than file.txt

```bash
-newerm file.txt
```

`c`hange, `m`odified, `B`create

```bash
-newerX file.txt
```

`t`imestamp

```bash
-newerXt "1 hour ago"
```

### Actions

execute rm on found items

```bash
-exec rm {} \;
```

print found items

```bash
-print
```

delete found items

```bash
-delete
```

### Examples

#### Find all files ending in '.jpg' and remove them

```bash
find . -name '*.jpg' -exec rm {} \;
```

#### Find all files created 24 hours ago

```bash
find . -newerBt "24 hours ago"
```

#### Specific command 1

In the current folder, find files that are readable, executable have a size of 1033 bytes, then send the files found over to cat.

```bash
find . -type f -readable ! -executable -size 1033c -exec cat {} \;
```

#### Specific command 2

In the current folder, find everything that has a size of 33 bytes, is owned by group bandit6 and user bandit7, redirect errors to /dev/null and send the stuff found over to cat.

```bash
find . -size 33c -group bandit6 -user bandit7 2> /dev/null -exec cat {} \;
```

### Also see

* [DevHints](https://devhints.io/find)
