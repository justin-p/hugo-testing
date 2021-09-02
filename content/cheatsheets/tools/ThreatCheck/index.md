---
### The title for the content.
title : "ThreatCheck"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "threatcheck"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Modified version of Matterpreter's DefenderCheck. Takes a binary as input (either from a file on disk or a URL), splits it until it pinpoints that exact bytes that the target engine will flag on and prints them to the screen. "
### The datetime assigned to this page.
date : 2021-09-02T17:03:44+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "threatcheck"
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
tags : ["Tools","AV bypass"]
---

## ThreatCheck

### Installation

```bash
git clone https://github.com/rasta-mouse/ThreatCheck
# and build using visual studio
```

### Usage

```bash
ThreatCheck.exe [FILE] [OPTIONS]
```

Determine the line(s) of code that are being flagged by Defender.

Obfuscate the detected line(s) of code so it is no longer flagged by Defender.

### Flags

```bash
  -e, --engine    (Default: Defender) Scanning engine. Options: Defender, AMSI
  -f, --file      Analyze a file on disk
  -u, --url       Analyze a file from a URL
  --help          Display this help screen.
  --version       Display version information.
```

### Examples

#### Check local covenant grunt with AMSI

Only uses in-memory script scanning engine.

```bash
ThreatCheck.exe -f Downloads\Grunt.bin -e AMSI
```

#### Check local covenant grunt with Defender

Temporarily writes file to disk.

```bash
ThreatCheck.exe -f Downloads\Grunt.bin -e Defender
```

### Related pages

{{< related_pages_table tag="AV bypass" >}}

### Also see

N/A