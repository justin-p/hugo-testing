---
title: "find"
description: " "
date: 2020-03-06T11:25:47+01:00
draft: false
weight: 90
---

### Usage

```bash
find PATH CONDITIONS ACTIONS
```

### Conditions

#### search for things that contain '.c'

```bash
-name "*.c"
```

#### search for things owned by user 'jonathan'

```bash
-user jonathan
```

#### search for things with no user that corresponds to file's numeric user ID

```bash
-nouser
```

#### Search for specific type

search for things that are files

```bash
-type f
```

search for things that are directories

```bash
-type d
```

search for things that are symlinks

```bash
-type l
```

#### search only 2 folders deep

```bash
-maxdepth 2
```

#### search with a regex pattern

```bash
-regex PATTERN
```

#### search for specific file sizes

Exactly 8 512-bit blocks

```bash
-size 8
```

Smaller than 128 bytes

```bash
-size -128c
```

Exactly 1440KiB

```bash
-size 1440k
```

Larger than 10MiB

```bash
-size +10M
```

Larger than 2GiB

```bash
-size +2G
```

#### search for files modified more recently then file.txt

```bash
-newer file.txt
```

`m`odified newer than file.txt

```bash
-newerm file.txt
```

`c`hange, `m`odified, `B`create

```bash
-newerX file.txt
```

`t`imestamp

```bash
-newerXt "1 hour ago"
```

### Actions

execute rm on found items

```bash
-exec rm {} \;
```

print found items

```bash
-print
```

delete found items

```bash
-delete
```

### Examples

#### Find all files ending in '.jpg' and remove them

```bash
find . -name '*.jpg' -exec rm {} \;
```

#### Find all files created 24 hours ago

```bash
find . -newerBt "24 hours ago"
```

#### Specific command 1

In the current folder, find files that are readable, executable have a size of 1033 bytes, then send the files found over to cat.

```bash
find . -type f -readable ! -executable -size 1033c -exec cat {} \;
```

#### Specific command 2

In the current folder, find everything that has a size of 33 bytes, is owned by group bandit6 and user bandit7, redirect errors to /dev/null and send the stuff found over to cat.

```bash
find . -size 33c -group bandit6 -user bandit7 2> /dev/null -exec cat {} \;
```

### Also see

* [DevHints](https://devhints.io/find)
