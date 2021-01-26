---
### The title for the content.
title : "cron"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "cron"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "daemon to execute scheduled commands."
### The datetime assigned to this page.
date : 2020-03-10T16:38:53+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "cron"
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

## cron

### Usage

```bash
Min  Hour Day  Mon  Weekday  Command
*    *    *    *    *        command to be executed
┬    ┬    ┬    ┬    ┬
│    │    │    │    └─  Weekday  (0=Sun .. 6=Sat)
│    │    │    └──────  Month    (1..12)
│    │    └───────────  Day      (1..31)
│    └────────────────  Hour     (0..23)
└─────────────────────  Minute   (0..59)
```

### Examples

| Example | Description |
| :--- | :--- |
| `0 * * * *` | every hour |
| `*/15 * * * *` | every 15 mins |
| `0 */2 * * *` | every 2 hours |
| `0 0 * * 0` | every Sunday midnight |
| `@reboot` | every reboot |

### Crontab

#### Adding tasks easily

```bash
echo "@reboot echo hi" | crontab
```

#### Open in editor

```bash
crontab -e
```

#### List tasks

```bash
crontab -l [-u user]
```

### Also see

N/A
