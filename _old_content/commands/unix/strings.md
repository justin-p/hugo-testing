---
title: "strings"
description: " "
date: 2020-03-06T11:27:11+01:00
draft: false
weight: 200
---

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
