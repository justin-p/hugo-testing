---
### The title for the content.
title : "tar"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "tar"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "an archiving utility."
### The datetime assigned to this page.
date : 2020-03-10T16:38:53+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "tar"
### Aliases can be used to create redirects to your page from other URLs.
# aliases : [""]
### Display name of this page modifier. If set, it will be displayed in the footer.
# LastModifierDisplayName : ""
### Email of this page modifier. If set with LastModifierDisplayName, it will be displayed in the footer
# LastModifierEmail : ""
### Table of content (toc) is enabled by default. Set this parameter to true to disable it.
# disableToc : true
### Set the page as a chapter, changing the way it's displayed
# chapter : true
### Hide a menu entry by setting this to true
# hidden : true
### If true, the content will not be rendered unless the --buildDrafts flag is passed to the hugo command.
# draft : true
### Used for ordering your content in lists. Lower weight gets higher precedence. So content with lower weight will come first.
### 0 does nothing !
weight : 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
# tags : [""]
---

## tar

### Usage

```bash
tar [FLAGS] FILE.tar.gz
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
