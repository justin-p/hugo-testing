---
title: "tr"
description: " "
date: 2020-03-06T11:27:25+01:00
draft: false
weight: 240
---

### Usage

```bash
```

### Flags

```bash
```

### Examples

#### replace lowercase letters with uppercase

```bash
cat file1 | tr "[a-z]" "[A-Z]"
cat file1 | tr "[:lower:]" "[:upper:]"
```

#### replace spaces with tabs

```bash
echo "file1 file2 file3" | tr [:space:] '\t'
```

#### remove specified characters

```bash
echo 'abcdefg' | tr -d 'a'
```

#### remove all the digits from the string

```bash
echo "123a467b890c" | tr -d [:digit:]
```

#### remove all characters except digest

```bash
echo "123a467b890c" | tr -cd [:digit:]
```

### Also see

N/A
