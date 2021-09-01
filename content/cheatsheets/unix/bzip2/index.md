---
### The title for the content.
title : "bzip2"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "bzip2"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "a block-sorting file compressor."
### The datetime assigned to this page.
date : 2020-03-10T16:38:53+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "bzip2"
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

## bzip2

### Usage

```bash
bzip2 [OPTIONS] [FILE]
```

### Flags

```bash
-c --stdout
    Compress or decompress to standard output.

-d --decompress
    Force decompression. bzip2, bunzip2 and bzcat are really the same program, and the decision about what actions to take is done on the basis of which name is used. This flag overrides that mechanism, and forces bzip2 to decompress.

-z --compress
    The complement to -d: forces compression, regardless of the invocation name.

-t --test
    Check integrity of the specified file(s), but dont decompress them. This really performs a trial decompression and throws away the result.

-f --force
    Force overwrite of output files. Normally, bzip2 will not overwrite existing output files. Also forces bzip2 to break hard links to files, which it otherwise wouldnt do.
    bzip2 normally declines to decompress files which dont have the correct magic header bytes. If forced (-f), however, it will pass such files through unmodified. This is how GNU gzip behaves.

-k --keep
    Keep (dont delete) input files during compression or decompression.

-s --small
    Reduce memory usage, for compression, decompression and testing. Files are decompressed and tested using a modified algorithm which only requires 2.5 bytes per block byte. This means any file can be decompressed in 2300k of memory, albeit at about half the normal speed.
    During compression, -s selects a block size of 200k, which limits memory use to around the same figure, at the expense of your compression ratio. In short, if your machine is low on memory (8 megabytes or less), use -s for everything. See MEMORY MANAGEMENT below.

-q --quiet
    Suppress non-essential warning messages. Messages pertaining to I/O errors and other critical events will not be suppressed.

-v --verbose
    Verbose mode -- show the compression ratio for each file processed. Adding more -v increase the verbosity level, spewing out lots of information which is primarily of interest for diagnostic purposes.

-L --license -V --version
    Display the software version, license terms and conditions.

-1 (or --fast) to -9 (or --best)
    Set the block size to 100 k, 200 k .. 900 k when compressing. Has no effect when decompressing. See MEMORY MANAGEMENT below. The --fast and --best aliases are primarily for GNU gzip compatibility. In particular, --fast doesnt make things significantly faster. And --best merely selects the default behaviour.

--
    Treats all subsequent arguments as file names, even if they start with a dash. This is so you can handle files with names beginning with a dash, for example: bzip2 -- -myfilename.

--repetitive-fast --repetitive-best
    These flags are redundant in versions 0.9.5 and above. They provided some coarse control over the behaviour of the sorting algorithm in earlier versions, which was sometimes useful. 0.9.5 and above have an improved algorithm which renders these flags irrelevant.
```

### Examples

#### compress a file

```bash
bzip2 file1
```

#### decompress a file

```bash
bzip2 -d file1.bz2
```

#### compress a single file and keep the original

```bash
bzip2 -c file1 > file1.bz
```

#### fast compression

```bash
bzip2 -1 file1
```

#### best compression

```bash
bzip2 -9 file1
```

### Also see

N/A
