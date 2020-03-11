---
### The title for the content.
title : "Python"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "python"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Python description."
### The datetime assigned to this page.
date : 2020-03-10T16:33:40+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "python"
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
### a map of Front Matter keys whose values are passed down to the page’s descendants unless overwritten by self or a closer ancestor’s cascade. 
cascade:
    tags: ['Python']
---

## Python

### Onelinersoneliners

#### HTTP

Start a webserver that hosts the current pwd.

| Python2                         | Python3                     |
|---------------------------------|-----------------------------|
| `Python -m SimpleHTTPServer 8000` | `Python3 -m http.server 8000` |

#### FTP

Start a ftp that hosts the current pwd.

| Python2                         | Python3                     |
|---------------------------------|-----------------------------|
| `Python -m pyftpdlib`             | `Python3 -m pyftpdlib`        |

#### unicode character

Print a unicode character

| Python2                         | Python3                      |
|---------------------------------|------------------------------|
| `Python -c "print unichr(234)"`   | `Python3 -c "print(chr(234))"` |


### Handystuff

#### get current function name

```python
functionname = inspect.stack()[0][3]
```

#### get callers name of current function

```python
functionname = inspect.stack()[1][3]
```
