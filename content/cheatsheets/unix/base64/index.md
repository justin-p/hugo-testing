---
### The title for the content.
title : "base64"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "base64"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "base64 encode/decode data and print to standard output."
### The datetime assigned to this page.
date : 2020-03-10T16:38:53+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "base64"
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

## base64

### Usage

```bash
base64 [OPTION] [FILE]
```

### Flags

```bash
-w, --wrap=COLS
    Wrap encoded lines after COLS character (default 76). Use 0 to disable line wrapping.
-d, --decode
    Decode data.
-i, --ignore-garbage
    When decoding, ignore non-alphabet characters.
--help
    display this help and exit
--version
    output version information and exit
```

### Examples

#### Encode

```bash
echo EncodeMe | base64 -e
```

#### Decode

```bash
echo RW5jb2RlTWU= | base64 -d
```

#### Encode file

```bash
base64 file1 > encodedfile1
```

#### Decode file

```bash
base64 -d encodedfile1 > file1
```

### Also see

N/A
