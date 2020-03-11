---
title: "scp"
description: " "
date: 2020-03-06T11:27:03+01:00
draft: false
weight: 170
---

### Usage

```bash
scp OPTIONS SOURCE_PATH DESTINATION_PATH
```

### Flags

#### transfer directory

```bash
-r
```

#### see the transfer details (verbose)

```bash
-v
```

#### copy files with compression

```bash
-C
```

#### limit bandwidth

```bash
-l 800
```

#### keep the original attributes

```bash
-p
```

#### quite

```bash
-q
```

### Examples

#### push a file to a remote system

```bash
scp file user@host:/path/to/file
```

#### pull a file from a remote system

```bash
scp user@host:/path/to/file /local/path/to/file
```

#### push multiple files to a remote system

```bash
scp file1 file2 user@host:/path/to/directory
```

#### push an entire directory to a remote system

```bash
scp -r /path/to/directory user@host:/path/to/directory
```

### See Also

* [SCP Cheatsheets](https://github.com/rstacruz/cheatsheets/blob/master/scp.md)
