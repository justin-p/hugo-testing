---
### The title for the content.
title : "sed"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "sed"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "stream editor for filtering and transforming text."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "sed"
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

## sed

### Usage

```bash
sed [OPTIONS] [FILE]
```

### Flags

```bash
-n, --quiet, --silent
    suppress automatic printing of pattern space

--debug
    annotate program execution

-e script, --expression=script
    add the script to the commands to be executed

-f script-file, --file=script-file
    add the contents of script-file to the commands to be executed

--follow-symlinks
    follow symlinks when processing in place

-i[SUFFIX], --in-place[=SUFFIX]
    edit files in place (makes backup if SUFFIX supplied)

-l N, --line-length=N
    specify the desired line-wrap length for the 'l' command

--posix
    disable all GNU extensions.

-E, -r, --regexp-extended
    use extended regular expressions in the script (for
    portability use POSIX -E).

-s, --separate
    consider files as separate rather than as a single, continuous
    long stream.

--sandbox
    operate in sandbox mode (disable e/r/w commands).

-u, --unbuffered
    load minimal amounts of data from the input files and flush
    the output buffers more often

-z, --null-data
    separate lines by NUL characters

--help
    display this help and exit

--version
    output version information and exit
```

### Examples

#### Printing lines

Print all with "abc"

```bash
/abc/p
```

Print all without "abc"

```bash
/abc/!p
```

#### Deleting

Delete all with "abc"

```bash
/abc/d
```

Delete all without "abc"

```bash
/abc/!d
```

#### Select a block

```bash
/start/,/end/!d
```

#### Conditional replace

```bash
/abc/{s/def/ghi)}
```

#### Appending lines

Append 'Hallo' after each line

```bash
aHallo
```

Append 'Hallo' after line #5

```bash
5 aHallo
```

Append 'Hallo' to end of file

```bash
$ aHallo
```

#### Pre-pending lines

```bash
sed -i '1s;^;new line 1\nanother new line 2\n;' <file>
```

#### In-place Editing

To edit file use the -i option this safely changes the file contents without any output redirection needed.

```bash
sed -i 's/abc/ABC/' myfile.txt
sed -i '/deleteme/d' *
```

#### Drop grep

Often grep and sed are used together. In all those cases grep can be dropped. For example

```bash
grep "pattern" file | sed "s/abc/def/"
```

can be written as

```bash
sed -n "/pattern/p; s/abc/def/"
```

#### Grouping with sed

Always use single quotes!

```bash
sed 's/^.*\(pattern\).*/\1/'
```

#### Single Quoting Single Quotes

If you want to do extraction and need a pattern based on single quotes use \x27 instead of trying to insert a single quote. For example:

```bash
sed 's/.*var=\x27\([^\x27]*\)\x27.*/\1/'
```

to extract "some string" from "var='some string'". Or if you don't know about the quoting, but know there are quotes

```bash
sed 's/.*var=.\([^"\x27]*\)..*/\1/'
```

#### Conditional Replace with sed

```bash
sed '/conditional pattern/{s/pattern/replacement/g}'
```

#### Prefix files with a boilerplate using sed

```bash
sed -i '1s/^/# DO NOT TOUCH THIS FILE!\n\n/' *
```

#### Removing Newlines with sed

The only way to remove new line is this:

```bash
sed ':a;N;$!ba;s/\n//g' file
```

#### Selecting Blocks

```bash
sed '/first line/,/last line/!d' file
```

### See Also

* [sed CheatSheet](https://lzone.de/cheat-sheet/sed)
