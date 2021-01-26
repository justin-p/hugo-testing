---
### The title for the content.
title : "Markdown"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "markdown"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Markdown description."
### The datetime assigned to this page.
date : 2020-03-10T16:43:50+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "markdown"
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

## Markdown

### Headers

```text
# h1
## h2
### h3
```

```text
Header 1
========
```

```text
Header 2
--------
```

### Emphasis

```text
*italic*
_italic_
```

```text
**bold**
__bold__
```

```text
`code`
```

### Lists

```text
* Item 1
* Item 2
```

```text
- Item 1
- Item 2
```

### Links

```text
[link](http://google.com)
```

```text
[link][google]
```

```text
<http://google.com>
```

### Images

```text
![Image alt text](/path/to/img.jpg)
![Image alt text](/path/to/img.jpg "title")
![Image alt text][img]
```

### Code

```text
    4 space indent
    makes a code block
```

code fences

```text
```js
codeFences.withLanguage()
```

```text
# Blockquotes

```text
> This is
> a blockquote
>
> > Nested
> > Blockquote
```

### Horizontal line

```text
----
```

```text
****
```

### Tables

```text
| Column 1 Heading | Column 2 Heading |
| ---------------- | ---------------- |
| Some content     | Other content    |
```

```text
Column 1 Heading | Column 2 Heading
--- | ---
Some content | Other content
```
