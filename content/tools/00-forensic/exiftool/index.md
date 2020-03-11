---
### The title for the content.
title : "exiftool"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "exiftool"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "exiftool description."
### The datetime assigned to this page.
date : 2020-03-10T16:36:31+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "exiftool"
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

## exiftool

### Usage

```bash
exiftool OPTIONS FILE
```

### Flags

```bash
Tag operations

-TAG or --TAG                    Extract or exclude specified tag
-TAG[+-]=[VALUE]                 Write new value for tag
-TAG[+-]<=DATFILE                Write tag value from contents of file
-TAG[+-]<SRCTAG                  Copy tag value (see -tagsFromFile)

-tagsFromFile SRCFILE            Copy tag values from file
-x TAG      (-exclude)           Exclude specified tag

Input-output text formatting

-args       (-argFormat)         Output data as exiftool arguments
-b          (-binary)            Output data in binary format
-c FMT      (-coordFormat)       Set format for GPS coordinates
-charset [[TYPE=]CHARSET]        Specify encoding for special characters
-d FMT      (-dateFormat)        Set format for date/time values
-D          (-decimal)           Show tag ID numbers in decimal
-E, -ex     (-escape(HTML|XML))  Escape values for HTML (-E) or XML (-ex)
-f          (-forcePrint)        Force printing of all specified tags
-g[NUM...]  (-groupHeadings)     Organize output by tag group
-G[NUM...]  (-groupNames)        Print group name for each tag
-h          (-htmlFormat)        Use HMTL formatting for output
-H          (-hex)               Show tag ID number in hexadecimal
-htmlDump[OFFSET]                Generate HTML-format binary dump
-j          (-json)              Use JSON output format
-l          (-long)              Use long 2-line output format
-L          (-latin)             Use Windows Latin1 encoding
-lang [LANG]                     Set current language
-n          (--printConv)        Disable print conversion
-p FMTFILE  (-printFormat)       Print output in specified format
-s          (-short)             Short output format
-S          (-veryShort)         Very short output format
-sep STR    (-separator)         Set separator string for list items
-struct                          Enable output of structured information
-t          (-tab)               Output in tab-delimited list format
-T          (-table)             Output in tabular format
-v[NUM]     (-verbose)           Print verbose messages
-w[!] EXT   (-textOut)           Write output text files
-X          (-xmlFormat)         Use RDF/XML output format

Processing control

-a          (-duplicates)        Allow duplicate tags to be extracted
-e          (--composite)        Do not calculate composite tags
-ee         (-extractEmbedded)   Extract information from embedded files
-ext EXT    (-extension)         Process files with specified extension
-F[OFFSET]  (-fixBase)           Fix the base for maker notes offsets
-fast[NUM]                       Increase speed for slow devices
-fileOrder [-]TAG                Set file processing order
-i DIR      (-ignore)            Ignore specified directory name
-if EXPR                         Conditionally process files
-m          (-ignoreMinorErrors) Ignore minor errors and warnings
-o OUTFILE  (-out)               Set output file or directory name
-overwrite_original              Overwrite original by renaming tmp file
-overwrite_original_in_place     Overwrite original by copying tmp file
-P          (-preserve)          Preserve date/time of original file
-password PASSWD                 Password for processing protected files
-q          (-quiet)             Quiet processing
-r          (-recurse)           Recursively process subdirectories
-scanForXMP                      Brute force XMP scan
-u          (-unknown)           Extract unknown tags
-U          (-unknown2)          Extract unknown binary tags too
-z          (-zip)               Read/write compressed information

Special features

-geotag TRKFILE                  Geotag images from specified GPS log
-use MODULE                      Add features from plug-in module

Utilities

-delete_original[!]              Delete "_original" backups
-restore_original                Restore from "_original" backups

Other options

-@ ARGFILE                       Read command-line arguments from file
-k          (-pause)             Pause before terminating
-list[w|f|wf|g[NUM]|d|x]         List various exiftool attributes
-ver                             Print exiftool version number

Advanced options

-common_args                     Define common arguments
-config CFGFILE                  Specify configuration file name
-execute                         Execute multiple commands on one line
-srcfile FMT                     Set different source file name
-stay_open FLAG                  Keep reading -@ argfile even after EOF
```

### Examples

#### Searching for Files

##### Find images in a directory that don't have a DateTimeOriginal

```bash
exiftool -filename -filemodifydate -createdate -r -if '(not $datetimeoriginal) and $filetype eq "JPEG"' .
```

##### See files File Modify Date recursively in a directory who don't have datetimeoriginal set

```bash
exiftool -filemodifydate -r -if '(not $datetimeoriginal or ($datetimeoriginal eq "0000:00:00 00:00:00")) and ($filetype eq "JPEG")' .
```

#### Modifying Files

##### Create Captions From a Filename

```bash
exiftool '-Comment<BaseName' '-UserComment<BaseName' .
```

##### Change JPG to jpg and MOV to mov in filenames

```bash
for i in *.JPG; do mv "$i" "${i%%.JPG}.jpg"; done; !#:gs/JPG/MOV/:gs/jpg/mov/
```

Recursively

```bash
find /path/to/directory -name *JPG -exec sh -c 'mv "$0" "${0%%.JPG}.jpg"; echo "Moved $0 to ${0%%.JPG}.jpg"' {} \;
```

##### Change last created and modified for files in a directory

The date syntax has to be YYYY:MM:DD HH:MM:SS

Option 1:

```bash
find . -name "*.jpg" | while read filename;
    exiftool "-AllDates=1986:11:05 12:00:00" "$filename";
done
```

Option 2:

```bash
exiftool "-AllDates=1986:11:05 12:00:00" -if '$filetype eq "JPEG"' .
```

##### [Timeshift Photos by One Year](https://exiftool.org/Shift.html)

```bash
exiftool "-AllDates+=1:0:0 0" .
```

##### Rename files to datestamp

Filename looks like 2014-01-01 12:00:00.jpg and will append -NUM if DateTimeOriginal is the same for multiple files

```bash
exiftool '-FileName<DateTimeOriginal' -d "%Y-%m-%d %H.%M.%S%%-c.%%e" .
```

##### [Rename Files to With Milliseconds](https://exiftool.org/forum/index.php?topic=2736.0)

_Good for burst photos where the seconds are all the same. If milliseconds are only out to 2 digits, use `${SubSecCreateDate}` instead_

Found at

```bash
exiftool -v '-Filename<${datetimeoriginal}${subsectimeoriginal;$_.=0 x(3-length)}.%e' -d %Y%m%d_%H%M%S .
```

##### Update any photo that doesn't have DateTimeOriginal to have it based on file modify date

```bash
exiftool '-datetimeoriginal<filemodifydate' -if '(not $datetimeoriginal or ($datetimeoriginal eq "0000:00:00 00:00:00")) and ($filetype eq "JPEG")' .
```

##### Set DateTimeOriginal to Any Arbitrary Timestamp

```bash
exiftool '-datetimeoriginal=2015:01:18 12:00:00' .
```

#### Moving/Copying Files

##### Copy directory recursively into organized folder

```bash
exiftool -o ~/dummy/ -if '$filesize# > 300000' '-Directory<CreateDate' -d ~/Desktop/old_photos2/%Y/%m\ %B -r ~/Desktop/iPhoto\ Library/
```

`-o ~/dummy` This flag is to copy, not move. The directory is a fallback if the flag isn't available on the given photo. Good if using something like DateTimeOriginal

`-if '$filesize# > 300000'` gets files that are over 300kB. I was parsing an iPhoto library where there were thumbnails. The `#` turns the value to a number. you can use the flag `-n` to turn all values to numbers

`'-Directory<CreateDate'` Create directories based on the CreateDate of the photos

`-d ~/Desktop/old_photos/%Y/%m\ %B` Create folders with the given date format.

`-r` Run recursively

### Also see

- [Cheatsheet source](https://gist.githubusercontent.com/rjames86/33b9af12548adf091a26/raw/6fcdbfab8b2a08e0001a03bae6d524fefad7b925/My%2520Exiftool%2520Cheatsheet.md)
- [Timeshift Photos by One Year](https://exiftool.org/Shift.html)
- [Rename Files to With Milliseconds](https://exiftool.org/forum/index.php?topic=2736.0)
