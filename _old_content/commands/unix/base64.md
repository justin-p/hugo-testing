---
title: "base64"
description: "base64 encode/decode data and print to standard output"
date: 2020-03-06T11:24:34+01:00
draft: false
weight: 20
---

### Usage

```bash
base64 OPTION FILE
```

### Flags

```bash
-w, --wrap=COLS
    Wrap encoded lines after COLS character (default 76). Use 0 to disable line wrapping.
-d, --decode
    Decode data.
-i, --ignore-garbage
    When decoding, ignore non-alphabet characters.
--help
    display this help and exit
--version
    output version information and exit
```

### Examples

#### Encode

```bash
echo EncodeMe | base64 -e
```

#### Decode

```bash
echo RW5jb2RlTWU= | base64 -d
```

#### Encode file

```bash
base64 file1 > encodedfile1
```

#### Decode file

```bash
base64 -d encodedfile1 > file1
```

### Also see

N/A
