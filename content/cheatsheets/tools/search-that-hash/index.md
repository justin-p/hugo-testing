---
### The title for the content.
title : "Search-That-Hash"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "search that hash"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Search-That-Hash searches the most popular hash cracking sites and automatically inputs your hash(s) for cracking."
### The datetime assigned to this page.
date : 2021-09-02T20:02:34+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "Search-That-Hash"
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

## Search-That-Hash

### Installation

```bash
pip3 install search-that-hash 
```

### Usage

```bash
sth [OPTIONS]
```

### Flags

```bash
-t, --text TEXT        Crack a single hash.
-f, --file FILENAME    The file of hashes, seperated by newlines.
-w, --wordlist TEXT    The wordlist you want to use for Hashcat.
--timeout INTEGER      Choose timeout in seconds.
-g, --greppable        Prints as JSON, use this to grep.
--hashcat_binary TEXT  Location of hashcat folder (if using windows).
-o, --offline          Use offline mode. Does not search for hashes in APIs.
-v, --verbose          Turn on debugging logs. -vv for max.
--accessible           Makes the output accessible.
--no-banner            Doesn't print banner.
--help                 Show this message and exit.
```

### Examples

#### Search on all resources using text input

```bash
sth --text "5f4dcc3b5aa765d61d8327deb882cf99"
```

#### Search on all resources using file input

```bash
sth --file hashes.txt
```

#### Search on all resources using text input, if it's not found run hashcat with wordlist

```bash
sth --text "5f4dcc3b5aa765d61d8327deb882cf99" -w /path/to/wordlist.txt
```

#### Only run hashcat with wordlist using text input

```bash
sth --text "5f4dcc3b5aa765d61d8327deb882cf99" -w /path/to/wordlist.txt -o
```

### Related pages

{{< related_pages_table tag="password-cracking" >}}

### Also see

[Github Project](https://github.com/HashPals/Search-That-Hash)