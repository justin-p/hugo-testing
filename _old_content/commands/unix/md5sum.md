---
title: "md5sum"
description: " "
date: 2020-03-06T11:26:06+01:00
draft: false
weight: 130
---

### Usage

```bash
md5sum OPTIONS FILE
```

### Flags

```bash
-b, --binary
    read in binary mode

-c, --check
    read MD5 sums from the FILEs and check them

--tag  create a BSD-style checksum

-t, --text
    read in text mode (default)

-z, --zero
    end each output line with NUL, not newline, and disable file
    name escaping

The following five options are useful only when verifying checksums:

--ignore-missing
       dont fail or report status for missing files

--quiet
       dont print OK for each successfully verified file

--status
       dont output anything, status code shows success

--strict
       exit non-zero for improperly formatted checksum lines

-w, --warn
       warn about improperly formatted checksum lines

--help display this help and exit

--version
       output version information and exit
```

### Examples

#### display the hash value

```bash
md5sum file1
```

#### validate multiple files

```bash
md5sum file1 file2 file3 > hashes
md5sum --check hashes
```

#### display only modified files

```bash
md5sum --quiet --check hashes
```

#### identify invalid hash values

```bash
md5sum --warn --check hashes
```

### Also see

N/A
