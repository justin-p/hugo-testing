---
### The title for the content.
title : "md5sum"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "md5sum"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "compute and check MD5 message digest."
### The datetime assigned to this page.
date : 2020-03-10T16:38:53+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "md5sum"
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

## md5sum

### Usage

```bash
md5sum OPTIONS FILE
```

### Flags

```bash
-b, --binary
    read in binary mode

-c, --check
    read MD5 sums from the FILEs and check them

--tag  create a BSD-style checksum

-t, --text
    read in text mode (default)

-z, --zero
    end each output line with NUL, not newline, and disable file
    name escaping

The following five options are useful only when verifying checksums:

--ignore-missing
       dont fail or report status for missing files

--quiet
       dont print OK for each successfully verified file

--status
       dont output anything, status code shows success

--strict
       exit non-zero for improperly formatted checksum lines

-w, --warn
       warn about improperly formatted checksum lines

--help display this help and exit

--version
       output version information and exit
```

### Examples

#### display the hash value

```bash
md5sum file1
```

#### validate multiple files

```bash
md5sum file1 file2 file3 > hashes
md5sum --check hashes
```

#### display only modified files

```bash
md5sum --quiet --check hashes
```

#### identify invalid hash values

```bash
md5sum --warn --check hashes
```

### Also see

N/A
