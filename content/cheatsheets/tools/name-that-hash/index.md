---
### The title for the content.
title : "Name-That-Hash"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "name that hash"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "The Modern Hash Identification System."
### The datetime assigned to this page.
date : 2021-09-02T19:51:37+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "name-that-hash"
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
tags : ["Tools","hashes","password-cracking"]
---

## name-that-hash

### Installation

```bash
pip3 install name-that-hash
```

### Usage

```bash
nth [OPTIONS]
```

### Flags

```bash
Options:
  -t, --text TEXT      Check one hash, use single quotes ' as inverted commas
                       " messes up on Linux.

  -f, --file FILENAME  Checks every hash in a newline separated file.
  -g, --greppable      Are you going to grep this output? Prints in JSON
                       format.

  -b64, --base64       Decodes hashes in Base64 before identification. For
                       files with mixed Base64 & non-encoded it attempts
                       base64 first and then falls back to normal hash
                       identification per hash.

  -a, --accessible     Turn on accessible mode, does not print ASCII art. Also
                       does not print very large blocks of text, as this can
                       cause some pains with screenreaders. This reduces the
                       information you get. If you want the least likely
                       feature but no banner, use --no-banner.

  -e, --extreme        Searches for hashes within a string. This mode will get
                       5d41402abc4b2a76b9719d911017c592 from
                       ####5d41402abc4b2a76b9719d911017c592###

  --no-banner          Removes banner from startup.
  --no-john            Don't print John The Ripper Information.
  --no-hashcat         Don't print Hashcat Information.
  -v, --verbose        Turn on debugging logs. -vvv for maximum logs.
  --help               Show this message and exit.
```

### Examples

#### Text as input

```bash
nth --text 5f4dcc3b5aa765d61d8327deb882cf99
```

#### File as input

```bash
nth --file unknownhash.txt
```

#### Decode hashes in Base64 before identification

```bash
nth --text 5f4dcc3b5aa765d61d8327deb882cf99 -b64
```

#### Output as JSON

```bash
nth --text 5f4dcc3b5aa765d61d8327deb882cf99 -g 
```

#### Hide the banner

```bash
nth --text 5f4dcc3b5aa765d61d8327deb882cf99 --no-banner 
```

#### Hide the banner and only show Most likely

```bash
nth --text 5f4dcc3b5aa765d61d8327deb882cf99 --accessible 
```

### Related pages

{{< related_pages_table tag="password-cracking" >}}

### Also see

[Github Project](https://github.com/HashPals/Name-That-Hash)