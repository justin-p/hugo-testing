---
title: "sed"
description: " "
date: 2020-03-06T11:27:05+01:00
draft: false
weight: 180
---

### Usage

```bash
sed OPTIONS FILE
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
