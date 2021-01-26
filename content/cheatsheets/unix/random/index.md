---
### The title for the content.
title : "random"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "random"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "random description."
### The datetime assigned to this page.
date : 2020-03-10T16:38:53+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "random"
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

## random

### Usage of dash \(-\) in place of a filename

Using - as a filename to mean stdin/stdout is a convention that a lot of programs use. It is not a special property of the filename. The kernel does not recognize - as special so any system calls referring to - as a filename will use - literally as the filename.

With bash redirection, - is not recognized as a special filename, so bash will use that as the literal filename.

When cat sees the string - as a filename, it treats it as a synonym for stdin. To get around this, you need to alter the string that cat sees in such a way that it still refers to a file called -. The usual way of doing this is to prefix the filename with a path - ./-, or /home/Tim/-. This technique is also used to get around similar issues where command line options clash with filenames, so a file referred to as ./-e does not appear as the -e command line option to a program, for example.

```bash
cat ./-
```

### Also see

N/A
