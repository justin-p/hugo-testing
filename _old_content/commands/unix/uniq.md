---
title: "uniq"
description: " "
date: 2020-03-06T11:27:29+01:00
draft: false
weight: 250
---

### Usage

```bash
uniq OPTIONS INPUT OUTPUT
```

### Flags

```bash
-c, --count
    prefix lines by the number of occurrences

-d, --repeated
    only print duplicate lines, one for each group

-D     print all duplicate lines

--all-repeated[=METHOD]
    like -D, but allow separating groups with an empty line;
    METHOD={none(default),prepend,separate}

-f, --skip-fields=N
    avoid comparing the first N fields

--group[=METHOD]
    show all items, separating groups with an empty line;
    METHOD={separate(default),prepend,append,both}

-i, --ignore-case
    ignore differences in case when comparing

-s, --skip-chars=N
    avoid comparing the first N characters

-u, --unique
    only print unique lines

-z, --zero-terminated
    line delimiter is NUL, not newline

-w, --check-chars=N
    compare no more than N characters in lines

--help
    display this help and exit

--version
    output version information and exit
```

### Examples

#### show each unique line

```bash
uniq file1
```

#### show how many times a line accurse

```bash
uniq -c file1
```

#### only print duplicate lines

```bash
uniq -D file1
```

#### only print non-repetitive lines

```bash
uniq -u file1
```

#### avoid comparing set number of initial characters

```bash
uniq -s 4 file1
```

#### limit comparison to set number of chars

```bash
uniq -w 3 file1
```

#### uniq comparison case insensitive

```bash
uniq -i file1
```

#### uniq output NUL-terminated

```bash
uniq -z file1
```

### Also see

N/A
