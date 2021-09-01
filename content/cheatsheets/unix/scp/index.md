---
### The title for the content.
title : "scp"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "scp"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "secure copy (remote file copy program)."
### The datetime assigned to this page.
date : 2020-03-10T16:38:53+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "scp"
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

## scp

### Usage

```bash
scp [OPTIONS] SOURCE_PATH DESTINATION_PATH
```

### Flags

#### transfer directory

```bash
-r
```

#### see the transfer details (verbose)

```bash
-v
```

#### copy files with compression

```bash
-C
```

#### limit bandwidth

```bash
-l 800
```

#### keep the original attributes

```bash
-p
```

#### quite

```bash
-q
```

### Examples

#### push a file to a remote system

```bash
scp file user@host:/path/to/file
```

#### pull a file from a remote system

```bash
scp user@host:/path/to/file /local/path/to/file
```

#### push multiple files to a remote system

```bash
scp file1 file2 user@host:/path/to/directory
```

#### push an entire directory to a remote system

```bash
scp -r /path/to/directory user@host:/path/to/directory
```

### See Also

* [SCP Cheatsheets](https://github.com/rstacruz/cheatsheets/blob/master/scp.md)
