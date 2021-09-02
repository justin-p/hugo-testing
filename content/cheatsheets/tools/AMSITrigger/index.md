---
### The title for the content.
title : "AMSITrigger"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "amsitrigger"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "AMSITrigger is a tool to identify malicious strings in PowerShell files."
### The datetime assigned to this page.
date : 2021-09-02T16:35:19+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "amsitrigger"
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

## AMSITrigger

### Installation

```bash
git clone https://github.com/RythmStick/AMSITrigger
# and build using visual studio
```

or download release from https://github.com/RythmStick/AMSITrigger/releases

{{% notice note %}}
Place the AMSITrigger.exe and the PS file you want to check in a whitelisted folder.
{{% /notice %}}


### Usage

```bash
.\AmsiTrigger_x64.exe [PowerShell File] [OPTIONS]
```

### Flags

```bash
-i, --inputfile=VALUE       Powershell filename
-u, --url=VALUE             URL eg. https://10.1.1.1/Invoke-NinjaCopy.ps1
-f, --format=VALUE          Output Format:
                              1 - Only show Triggers
                              2 - Show Triggers with Line numbers
                              3 - Show Triggers inline with code
                              4 - Show AMSI calls (xmas tree mode)
-d, --debug                 Show Debug Info
-m, --maxsiglength=VALUE    Maximum signature Length to cater for,
                              default=2048
-c, --chunksize=VALUE       Chunk size to send to AMSIScanBuffer,
                              default=4096
-h, -?, --help              Show Help
```

### Examples

#### Scan local file

```bash
.\AmsiTrigger_x64.exe -i virus.ps1
```

#### Scan remote file

```bash
.\AmsiTrigger_x64.exe -u https://raw.githubusercontent.com/BloodHoundAD/BloodHound/master/Collectors/SharpHound.ps1
```

### Related pages

{{< related_pages_table tag="AV bypass" >}}

### Also see

* [Github](https://github.com/RythmStick/AMSITrigger)