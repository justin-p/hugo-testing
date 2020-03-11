---
title: "touch"
description: " "
date: 2020-03-06T11:27:22+01:00
draft: false
weight: 230
---

### Usage

```bash
touch OPTION FILE
```

### Flags

```bash
-a
    change only the access time

-c, --no-create
    do not create any files

-d, --date=STRING
    parse STRING and use it instead of current time

-f
    (ignored)

-h, --no-dereference
    affect each symbolic link instead of any referenced file (useful only on systems that can change the timestamps of a symlink)

-m
    change only the modification time

-r, --reference=FILE
    use this files times instead of current time

-t STAMP
    use [[CC]YY]MMDDhhmm[.ss] instead of current time

--time=WORD
    change the specified time: WORD is access, atime, or use: equivalent to -a WORD is modify or mtime: equivalent to -m

--help
    display this help and exit

--version
    output version information and exit
```

### Examples

#### create a empty file

```bash
touch file1
```

#### update timestamp and modification

```bash
touch -am file
```

#### use timestamp of file4 on file 5

```bash
touch -r file4 file5
```

#### make file7 30 seconds older than file6

```bash
touch -r file6 -B 30 file7
```

#### set timestamp to specific timestamp

```bash
touch -d '1 May 2005 10:22' file8
touch -d '14 May' file9
touch -d '14:24' file9
```

#### avoid creating new file

```bash
touch -c file10
```

### Also see

N/A
