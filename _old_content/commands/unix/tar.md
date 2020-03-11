---
title: "tar"
description: " "
date: 2020-03-06T11:27:16+01:00
draft: false
weight: 210
---

### Usage

```bash
tar FLAGS FILE.tar.gz
```

### Flags

```bash
-z : Work on gzip compression automatically when reading archives.
-x : Extract tar.gz archive.
-v : Produce verbose output i.e. display progress and extracted file list on screen.
-f : Read the archive from the archive to the specified file. In this example, read backups.tar.gz archive.
-t : List the files in the archive.
-r : Append files to the end of the tarball.
--delete (GNU/Linux tar only) : Delete files from the tarball.
```

### Examples

#### extracting tar.gz file

```text
tar -zxvf file1.tar.gz
```

#### extract file2 from file.tar.gz tarball

```text
tar -zxvf file1.tar.gz file1
```

#### list files

```text
tar -tvf file1.tar.gz
```

#### create a tarball

```text
tar -cvf file.tar file1 file2 file3
```

#### add files to an existing tarball

```text
tar -rf file.tar file4
```

#### delete files from a tarball

```text
tar -f file.tar --delete file4
```

### Also see

N/A
