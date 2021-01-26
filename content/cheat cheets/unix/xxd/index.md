---
### The title for the content.
title : "xxd"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "xxd"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "make a hexdump or do the reverse."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "xxd"
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

## xxd

### Usage

```bash
xxd OPTIONS INFILE OUTFILE
```

### Flags

```bash

-a  -autoskip
    toggle autoskip: A single '*' replaces nul-lines. Default off.

-b  -bits
    Switch to bits (binary digits) dump, rather than hexdump. This option writes octets as eight digits "1"s and "0"s instead of a normal hexadecimal dump. Each line is preceded by a line number in hexadecimal and followed by an ascii (or ebcdic) representation. The command line switches -r, -p, -i do not work with this mode.

-c cols  -cols cols
    format <cols> octets per line. Default 16 (-i: 12, -ps: 30, -b: 6). Max 256.

-E  -EBCDIC
    Change the character encoding in the righthand column from ASCII to EBCDIC. This does not change the hexadecimal representation. The option is meaningless in combinations with -r, -p or -i.

-g bytes  -groupsize bytes
    separate the output of every <bytes> bytes (two hex characters or eight bit-digits each) by a whitespace. Specify -g 0 to suppress grouping. <Bytes> defaults to 2 in normal mode and 1 in bits mode. Grouping does not apply to postscript or include style.

-h  -help
    print a summary of available commands and exit. No hex dumping is performed.

-i  -include
    output in C include file style. A complete static array definition is written (named after the input file), unless xxd reads from stdin.

-l len  -len len
    stop after writing <len> octets.

-p  -ps  -postscript  -plain
    output in postscript continuous hexdump style. Also known as plain hexdump style.

-r  -revert
    reverse operation: convert (or patch) hexdump into binary. If not writing to stdout, xxd writes into its output file without truncating it. Use the combination -r -p to read plain hexadecimal dumps without line number information and without a particular column layout. Additional Whitespace and line-breaks are allowed anywhere.

-seek offset
    When used after -r: revert with <offset> added to file positions found in hexdump.

-s [+][-]seek
    start at <seek> bytes abs. (or rel.) infile offset. + indicates that the seek is relative to the current stdin file position (meaningless when not reading from stdin). - indicates that the seek should be that many characters from the end of the input (or if combined with +: before the current stdin file position). Without -s option, xxd starts at the current file position.

-u
    use upper case hex letters. Default is lower case.

-v  -version
    show version string.
```

### Examples

#### Create a hexdump

```bash
xxd data.txt >> data.hex
```

#### Reverse a hexdump

```bash
xxd -r data.hex >> data.txt
```

#### skip to line 0x30

```bash
xxd -s 0x30 data.txt

00000030: 6961 7c59 0a0a 3034 7c43 6869 6e61 7c4e  ia|Y..04|China|N
00000040: 0a30 357c 5275 7373 6961 7c59 0a30 367c  .05|Russia|Y.06|
00000050: 4a61 7061 6e7c 590a 0a30 377c 5369 6e67  Japan|Y..07|Sing
00000060: 7061 6f72 657c 590a 3038 7c53 6f75 7468  paore|Y.08|South
00000070: 204b 6f72 6561 7c4e 0a30 397c 4669 6e61   Korea|N.09|Fina
00000080: 6c61 6e64 7c59 0a31 307c 4972 656c 616e  land|Y.10|Irelan
00000090: 647c 590a                                d|Y.
```

#### dump until line x30

```bash
xxd -l 0x30 data.txt

00000000: 4e6f 2e7c 436f 756e 7472 797c 5965 732f  No.|Country|Yes/
00000010: 4e6f 0a30 317c 496e 6469 617c 590a 3032  No.01|India|Y.02
00000020: 7c55 537c 590a 3033 7c41 7573 7472 616c  |US|Y.03|Austral
```

#### set column length

```bash
xxd -c 5 data.txt

00000000: 4e6f 2e7c 43  No.|C
00000005: 6f75 6e74 72  ountr
0000000a: 797c 5965 73  y|Yes
0000000f: 2f4e 6f0a 30  /No.0
00000014: 317c 496e 64  1|Ind
00000019: 6961 7c59 0a  ia|Y.
0000001e: 3032 7c55 53  02|US
00000023: 7c59 0a30 33  |Y.03
00000028: 7c41 7573 74  |Aust
0000002d: 7261 6c69 61  ralia
00000032: 7c59 0a0a 30  |Y..0
00000037: 347c 4368 69  4|Chi
0000003c: 6e61 7c4e 0a  na|N.
00000041: 3035 7c52 75  05|Ru
00000046: 7373 6961 7c  ssia|
0000004b: 590a 3036 7c  Y.06|
00000050: 4a61 7061 6e  Japan
```

#### Create binary dump

```bash
xxd -b data.txt
```

### Also see

N/A
