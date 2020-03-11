---
### The title for the content.
title : "cut"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "cut"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "remove sections from each line of files."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "cut"
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

## cut

### Usage

```bash
cut OPTION FILE
```

### Flags

```bash
-b, --bytes=LIST
    select only these bytes

-c, --characters=LIST
    select only these characters

-d, --delimiter=DELIM
    use DELIM instead of TAB for field delimiter

-f, --fields=LIST
    select only these fields; also print any line that contains no delimiter character, unless the -s option is specified

-n
    with -b: dont split multibyte characters

--complement
    complement the set of selected bytes, characters or fields


-s, --only-delimited
    do not print lines not containing delimiters

--output-delimiter=STRING
    use STRING as the output delimiter the default is to use the input delimiter

--help
    display this help and exit

--version
    output version information and exit

Use one, and only one of -b, -c or -f. Each LIST is made up of one range, or many ranges separated by commas. Selected input is written in the same order that it is read, and is written exactly once. Each range is one of:

N
    N th byte, character or field, counted from 1
N-
    from N th byte, character or field, to end of line
N-M
    from N th to M th (included) byte, character or field
-M
    from first to M th (included) byte, character or field

With no FILE, or when FILE is -, read standard input.
```

### Examples

```bash
echo "a string" | cut -d " " -f 1
a
```

```bash
echo "a string" | cut -d " " -f 2
string
```

```bash
echo "a string" | cut -d " " -f 3
```

### Also see

N/A
