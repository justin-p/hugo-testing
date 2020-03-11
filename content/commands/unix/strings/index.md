---
### The title for the content.
title : "strings"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "strings"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "strings description."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "strings"
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

## strings

### Usage

```bash
strings OPTIONS FILE
```

### Flags

```bash
-a --all -
    Do not scan only the initialized and loaded sections of object files; scan the whole files.

-f --print-file-name
    Print the name of the file before each string.

--help
    Print a summary of the program usage on the standard output and exit.

-min-len -n min-len --bytes=min-len
    Print sequences of characters that are at least min-len characters long, instead of the default 4.

-o
    Like -t o. Some other versions of strings have -o act like -t d instead. Since we can not be compatible with both ways, we simply chose one.

-t radix --radix=radix
    Print the offset within the file before each string. The single character argument specifies the radix of the offset---o for octal, x for hexadecimal, or d for decimal.

-e encoding --encoding=encoding
    Select the character encoding of the strings that are to be found. Possible values for encoding are: s = single-7-bit-byte characters ( ASCII , ISO 8859, etc., default), S = single-8-bit-byte characters, b = 16-bit bigendian, l = 16-bit littleendian, B = 32-bit bigendian, L = 32-bit littleendian. Useful for finding wide character strings. (l and b apply to, for example, Unicode UTF-16/UCS-2 encodings).

-T bfdname --target=bfdname
    Specify an object code format other than your systems default format.
-v -V --version
    Print the program version number on the standard output and exit.

@file
    Read command-line options from file. The options read are inserted in place of the original @file option. If file does not exist, or cannot be read, then the option will be treated literally, and not removed.
    Options in file are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The file may itself contain additional @file options; any such options will be processed recursively.
```

### Examples

```bash
cat data.bin | strings
```

### Also see

N/A
