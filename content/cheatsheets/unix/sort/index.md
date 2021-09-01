---
### The title for the content.
title : "sort"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "sort"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "sort lines of text files."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "sort"
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

## sort

### Usage

```bash
sort [OPTIONS] [FILE]
```

### Flags

```bash
-b, --ignore-leading-blanks
    ignore leading blanks

-d, --dictionary-order
    consider only blanks and alphanumeric characters

-f, --ignore-case
    fold lower case to upper case characters

-g, --general-numeric-sort
    compare according to general numerical value

-i, --ignore-nonprinting
    consider only printable characters

-M, --month-sort
    compare (unknown) < 'JAN' < ... < 'DEC'

-h, --human-numeric-sort
    compare human readable numbers (e.g., 2K 1G)

-n, --numeric-sort
    compare according to string numerical value

-R, --random-sort
    shuffle, but group identical keys.  See shuf(1)

--random-source=FILE
    get random bytes from FILE

-r, --reverse
    reverse the result of comparisons

--sort=WORD
    sort according to WORD: general-numeric -g, human-numeric -h,
    month -M, numeric -n, random -R, version -V

-V, --version-sort
    natural sort of (version) numbers within text

Other options:

--batch-size=NMERGE
    merge at most NMERGE inputs at once; for more use temp files

-c, --check, --check=diagnose-first
    check for sorted input; do not sort

-C, --check=quiet, --check=silent
    like -c, but do not report first bad line

--compress-program=PROG
    compress temporaries with PROG; decompress them with PROG -d

--debug
    annotate the part of the line used to sort, and warn about
    questionable usage to stderr

--files0-from=F
    read input from the files specified by NUL-terminated names in
    file F; If F is - then read names from standard input

-k, --key=KEYDEF
    sort via a key; KEYDEF gives location and type

-m, --merge
    merge already sorted files; do not sort

-o, --output=FILE
    write result to FILE instead of standard output

-s, --stable
    stabilize sort by disabling last-resort comparison

-S, --buffer-size=SIZE
    use SIZE for main memory buffer

-t, --field-separator=SEP
    use SEP instead of non-blank to blank transition

-T, --temporary-directory=DIR
    use DIR for temporaries, not $TMPDIR or /tmp; multiple options
    specify multiple directories

--parallel=N
    change the number of sorts run concurrently to N

-u, --unique
    with -c, check for strict ordering; without -c, output only
    the first of an equal run

-z, --zero-terminated
    line delimiter is NUL, not newline

--help display this help and exit

--version
    output version information and exit
```

### Examples

#### sort by 5th column

```bash
ls -al | sort -n -k5
```

#### sort numerically by column two

```bash
ps auxw | sort -nk2
```

#### reverse sort numerically by column two

```bash
ps auxw | sort -rnk2
```

#### sort a file contents to file

```bash
sort file1 > file1.sorted
```

#### scramble instead of sort

```bash
sort -R file1
sort -R
```

### Also see

N/A
