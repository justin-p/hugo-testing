---
### The title for the content.
title : "file"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "file"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "determine file type."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "file"
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

## file

### Usage

```bash
FILE OPTIONS file
```

### Flags

```bash
-b, --brief

    Do not prepend filenames to output lines (brief mode).

-C, --compile
    Write a magic.mgc output file that contains a pre-parsed version of the magic file or directory.

-c, --checking-printout
    Cause a checking printout of the parsed form of the magic file. This is usually used in conjunction with the -m flag to debug a new magic file before installing it.

-e, --exclude testname
    Exclude the test named in testname from the list of tests made to determine the file type. Valid test names are:

    apptype
    EMX application type (only on EMX).

    text Various types of text files (this test will try to guess the text encoding, irrespective of the setting of the encoding option).

    encoding
    Different text encodings for soft magic tests.

    tokens Looks for known tokens inside text files.

    cdf Prints details of Compound Document Files.

    compress
    Checks for, and looks inside, compressed files.

    elf Prints ELF file details.

    soft Consults magic files.

    tar Examines tar files.

-F, --separator separator
    Use the specified string as the separator between the filename and the file result returned. Defaults to ':'.

-f, --files-from namefile
    Read the names of the files to be examined from namefile (one per line) before the argument list. Either namefile or at least one filename argument must be present; to test the standard input, use '-' as a filename argument.

-h, --no-dereference
    option causes symlinks not to be followed (on systems that support symbolic links). This is the default if the environment variable POSIXLY_CORRECT is not defined.

-i, --mime
    Causes the file command to output mime type strings rather than the more traditional human readable ones. Thus it may say 'text/plain; charset=us-ascii' rather than 'ASCII text'. In order for this option to work, file changes the way it handles files recognized by the command itself (such as many of the text file types, directories etc), and makes use of an alternative 'magic' file. (See the FILES section, below).

--mime-type, --mime-encoding
    Like -i, but print only the specified element(s).

-k, --keep-going
    Dont stop at the first match, keep going. Subsequent matches will be have the string '\012- ' prepended. (If you want a newline, see the '-r' option.)

-L, --dereference
    option causes symlinks to be followed, as the like-named option in ls(1) (on systems that support symbolic links). This is the default if the environment variable POSIXLY_CORRECT is defined.

-m, --magic-file magicfiles
    Specify an alternate list of files and directories containing magic. This can be a single item, or a colon-separated list. If a compiled magic file is found alongside a file or directory, it will be used instead.

-N, --no-pad
    Dont pad filenames so that they align in the output.

-n, --no-buffer
    Force stdout to be flushed after checking each file. This is only useful if checking a list of files. It is intended to be used by programs that want filetype output from a pipe.

-p, --preserve-date
    On systems that support utime(2) or utimes(2), attempt to preserve the access time of files analyzed, to pretend that file never read them.

-r, --raw
    Dont translate unprintable characters to \ooo. Normally file translates unprintable characters to their octal representation.

-s, --special-files
    Normally, file only attempts to read and determine the type of argument files which stat(2) reports are ordinary files. This prevents problems, because reading special files may have peculiar consequences. Specifying the -s option causes file to also read argument files which are block or character special files. This is useful for determining the filesystem types of the data in raw disk partitions, which are block special files. This option also causes file to disregard the file size as reported by stat(2) since on some systems it reports a zero size for raw disk partitions.

-v, --version
    Print the version of the program and exit.

-z, --uncompress
    Try to look inside compressed files.

-0, --print0
    Output a null character '\0' after the end of the filename. Nice to cut(1) the output. This does not affect the separator which is still printed.

--help
    Print a help message and exit.
```

### Examples

#### show file type

```bash
file file1
```

#### show types for all files in directory

```bash
file *
```

#### change the delimiter

```bash
file -F - *
```

#### show mime-types

```bash
file -i file1
```

### Also see

N/A
