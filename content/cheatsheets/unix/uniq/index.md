---
### The title for the content.
title : "uniq"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "uniq"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "report or omit repeated lines."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "uniq"
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

## uniq

### Usage

```bash
uniq [OPTIONS] INPUT OUTPUT
```

### Flags

```bash
-c, --count
    prefix lines by the number of occurrences

-d, --repeated
    only print duplicate lines, one for each group

-D     print all duplicate lines

--all-repeated[=METHOD]
    like -D, but allow separating groups with an empty line;
    METHOD={none(default),prepend,separate}

-f, --skip-fields=N
    avoid comparing the first N fields

--group[=METHOD]
    show all items, separating groups with an empty line;
    METHOD={separate(default),prepend,append,both}

-i, --ignore-case
    ignore differences in case when comparing

-s, --skip-chars=N
    avoid comparing the first N characters

-u, --unique
    only print unique lines

-z, --zero-terminated
    line delimiter is NUL, not newline

-w, --check-chars=N
    compare no more than N characters in lines

--help
    display this help and exit

--version
    output version information and exit
```

### Examples

#### show each unique line

```bash
uniq file1
```

#### show how many times a line accurse

```bash
uniq -c file1
```

#### only print duplicate lines

```bash
uniq -D file1
```

#### only print non-repetitive lines

```bash
uniq -u file1
```

#### avoid comparing set number of initial characters

```bash
uniq -s 4 file1
```

#### limit comparison to set number of chars

```bash
uniq -w 3 file1
```

#### uniq comparison case insensitive

```bash
uniq -i file1
```

#### uniq output NUL-terminated

```bash
uniq -z file1
```

### Also see

N/A
