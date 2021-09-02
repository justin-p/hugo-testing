---
### The title for the content.
title : "ntp"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "ntp"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Network Time Protocol"
### The datetime assigned to this page.
date : 2021-09-01T17:31:24+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "ntp"
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

## ntp

### Usage

```bash
ntpq [-flags] [-flag [value]] [--option-name[[=| ]value]] [ host ...]
```

### Flags

```bash
Flg Arg Option-Name    Description
   -4 no  ipv4           Force IPv4 name resolution
                                - prohibits the option 'ipv6'
   -6 no  ipv6           Force IPv6 name resolution
                                - prohibits the option 'ipv4'
   -c Str command        run a command and exit
                                - may appear multiple times
   -d no  debug-level    Increase debug verbosity level
                                - may appear multiple times
   -D Num set-debug-level Set the debug verbosity level
                                - may appear multiple times
   -i no  interactive    Force ntpq to operate in interactive mode
                                - prohibits these options:
                                command
                                peers
   -n no  numeric        numeric host addresses
      no  old-rv         Always output status line with readvar
   -p no  peers          Print a list of the peers
                                - prohibits the option 'interactive'
   -r KWd refid          Set default display type for S2+ refids
   -w no  wide           Display the full 'remote' value
      opt version        output version information and exit
   -? no  help           display extended usage information and exit
   -! no  more-help      extended usage information passed thru pager
   -> opt save-opts      save the option state to a config file
   -< Str load-opts      load options from a config file
                                - disabled as '--no-load-opts'
                                - may appear multiple times
```

### Examples

#### Check for mode 6

```bash
ntpq -c rv <IP>
```

### Also see

N/A