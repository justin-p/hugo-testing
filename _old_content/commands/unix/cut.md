---
title: "cut"
description: " "
date: 2020-03-06T11:25:03+01:00
draft: false
weight: 60
---

### Usage

```bash
cut OPTION FILE
```

### Flags

```bash
-b, --bytes=LIST
    select only these bytes

-c, --characters=LIST
    select only these characters

-d, --delimiter=DELIM
    use DELIM instead of TAB for field delimiter

-f, --fields=LIST
    select only these fields; also print any line that contains no delimiter character, unless the -s option is specified

-n
    with -b: dont split multibyte characters

--complement
    complement the set of selected bytes, characters or fields


-s, --only-delimited
    do not print lines not containing delimiters

--output-delimiter=STRING
    use STRING as the output delimiter the default is to use the input delimiter

--help
    display this help and exit

--version
    output version information and exit

Use one, and only one of -b, -c or -f. Each LIST is made up of one range, or many ranges separated by commas. Selected input is written in the same order that it is read, and is written exactly once. Each range is one of:

N
    N th byte, character or field, counted from 1
N-
    from N th byte, character or field, to end of line
N-M
    from N th to M th (included) byte, character or field
-M
    from first to M th (included) byte, character or field

With no FILE, or when FILE is -, read standard input.
```

### Examples

```bash
echo "a string" | cut -d " " -f 1
a
```

```bash
echo "a string" | cut -d " " -f 2
string
```

```bash
echo "a string" | cut -d " " -f 3
```

### Also see

N/A
