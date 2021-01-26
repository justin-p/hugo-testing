---
### The title for the content.
title : "awk"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "awk"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "awk is a complete pattern scanning and processing language, it is most commonly used as a Unix command-line filter to reformat the output of other commands."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "awk"
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

## awk

### Usage

```bash
awk OPTIONS PROGRAM FILE
```

### Flags

```bash
-F fs
--field-separator fs
    Use fs for the input field separator (the value of the FS predefined variable).
-v var=val
--assign var=val
    Assign the value val to the variable var, before execution of the program begins. Such variable values are available to the BEGIN block of an AWK program.
-f program-file
--file program-file
    Read the AWK program source from the file program-file, instead of from the first command line argument. Multiple -f (or --file) options may be used.
-mf NNN
-mr NNN
    Set various memory limits to the value NNN. The f flag sets the maximum number of fields, and the r flag sets the maximum record size. These two flags and the -m option are from an earlier version of the Bell Laboratories research version of UNIX awk. They are ignored by gawk, since gawk has no pre-defined limits. (Current versions of the Bell Laboratories awk no longer accept them.)
-O
--optimize
    Enable optimizations upon the internal representation of the program. Currently, this includes just simple constant-folding. The gawk maintainer hopes to add additional optimizations over time.
-W compat
-W traditional
--compat
--traditional
    Run in compatibility mode. In compatibility mode, gawk behaves identically to UNIX awk; none of the GNU -specific extensions are recognized. The use of --traditional is preferred over the other forms of this option. See GNU EXTENSIONS, below, for more information.
-W copyleft
-W copyright
--copyleft
--copyright
    Print the short version of the GNU copyright information message on the standard output and exit successfully.
-W dump-variables[=file]
--dump-variables[=file]
    Print a sorted list of global variables, their types and final values to file. If no file is provided, gawk uses a file named awkvars.out in the current directory.
    Having a list of all the global variables is a good way to look for typographical errors in your programs. You would also use this option if you have a large program with a lot of functions, and you want to be sure that your functions dont inadvertently use global variables that you meant to be local. (This is a particularly easy mistake to make with simple variable names like i, j, and so on.)
-W exec file
--exec file
    Similar to -f, however, this is option is the last one processed. This should be used with #! scripts, particularly for CGI applications, to avoid passing in options or source code (!) on the command line from a URL. This option disables command-line variable assignments.
-W gen-po
--gen-po
    Scan and parse the AWK program, and generate a GNU .po format file on standard output with entries for all localizable strings in the program. The program itself is not executed. See the GNU gettext distribution for more information on .po files.
-W help
-W usage
--help
--usage
    Print a relatively short summary of the available options on the standard output. (Per the GNU Coding Standards, these options cause an immediate, successful exit.)
-W lint[=value]
--lint[=value]
    Provide warnings about constructs that are dubious or non-portable to other AWK implementations. With an optional argument of fatal, lint warnings become fatal errors. This may be drastic, but its use will certainly encourage the development of cleaner AWK programs. With an optional argument of invalid, only warnings about things that are actually invalid are issued. (This is not fully implemented yet.)
-W lint-old
--lint-old
    Provide warnings about constructs that are not portable to the original version of Unix awk.
-W non-decimal-data
--non-decimal-data
    Recognize octal and hexadecimal values in input data. Use this option with great caution!
-W posix
--posix
    This turns on compatibility mode, with the following additional restrictions:
    - \x escape sequences are not recognized.
    - Only space and tab act as field separators when FS is set to a single space, newline does not.
    - You cannot continue lines after ? and :.
    - The synonym func for the keyword function is not recognized.
    - The operators ** and **= cannot be used in place of ^ and ^=.
    - The fflush() function is not available.
-W profile[=prof_file]
--profile[=prof_file]
    Send profiling data to prof_file. The default is awkprof.out. When run with gawk, the profile is just a "pretty printed" version of the program. When run with pgawk, the profile contains execution counts of each statement in the program in the left margin and function call counts for each user-defined function.
-W re-interval
--re-interval
    Enable the use of interval expressions in regular expression matching (see Regular Expressions, below). Interval expressions were not traditionally available in the AWK language. The POSIX standard added them, to make awk and egrep consistent with each other. However, their use is likely to break old AWK programs, so gawk only provides them if they are requested with this option, or when --posix is specified.
-W source program-text
--source program-text
    Use program-text as AWK program source code. This option allows the easy intermixing of library functions (used via the -f and --file options) with source code entered on the command line. It is intended primarily for medium to large AWK programs used in shell scripts.
-W use-lc-numeric
--use-lc-numeric
    This forces gawk to use the locales decimal point character when parsing input data. Although the POSIX standard requires this behavior, and gawk does so when --posix is in effect, the default is to follow traditional behavior and use a period as the decimal point, even in locales where the period is not the decimal point character. This option overrides the default behavior, without the full draconian strictness of the --posix option.
-W version
--version
    Print version information for this particular copy of gawk on the standard output. This is useful mainly for knowing if the current copy of gawk on your system is up to date with respect to whatever the Free Software Foundation is distributing. This is also useful when reporting bugs. (Per the GNU Coding Standards, these options cause an immediate, successful exit.)
```

### Examples

#### Print N columns from all rows

Print the first column from all rows:

```bash
awk '{print $1}'
```

Print the first and third columns from all rows:

```bash
awk '{print $1, $3}'
```

The comma between the column parameters in the previous command will put a space between the outputted columns. However, you can change this behavior and use your own formatting:

```bash
awk '{print $1 " --- " $3}'
```

#### Change the field delimiter and print the second column

By default, awk will parse a row into columns using a space as the delimiter. The delimiter can be changed with the -F command line switch.

For example, change the delimiter to a semicolon:

```bash
awk -F: '{print $2}'
```

The field delimiter could be anything such as an equal sign, -F=, or a period, -F..

#### Print the last column from all rows

There are plenty of situations where you might need to print the last column from a given row, but you do not know how many columns are on that given row. The built-in variable NF can be used to solve this.

```bash
awk '{print $NF}'
```

#### Print the last column from the first row

Another built-in variable is NR which always contains the current row number. This can be used to do such things as printing the last column from only the first row:

```bash
awk 'NR==1 {print $NF}'
```

#### Print the first column from all rows matching a regular expression

If you want to print particular columns only from rows that match certain conditions, you can pass a regular expression:

```bash
awk '/regular-expression-to-match/ {print $1}'
```

#### Print the first column from all rows except rows matching a regular expression

You can also invert your regular expression match by putting an exclamation mark outside of the search field:

```bash
awk '!/regular-expression-to-match/ {print $1}'
```

### Also see

* [awk commands cheatsheet](https://thornelabs.net/posts/awk-commands-cheat-sheet.html)
