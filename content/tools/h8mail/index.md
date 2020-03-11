---
### The title for the content.
title : "h8mail"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "h8mail"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Password Breach Hunting & Email OSINT tool, locally or using premium services. Supports chasing down related email."
### The datetime assigned to this page.
date : 2020-03-11T11:56:31+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "h8mail"
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
tags : ["Credential Gathering"]
---

## h8mail

h8mail is an email OSINT and breach hunting tool using different breach and reconnaissance services, or local breaches such as Troy Hunt's "Collection1" and the infamous "Breach Compilation" torrent.

### Installation

```python
pip3 install h8mail
```

### Usage

```bash
usage: h8mail [-h] [-t USER_TARGETS [USER_TARGETS ...]]
              [-u USER_URLS [USER_URLS ...]] [-q USER_QUERY] [--loose]
              [-c CONFIG_FILE [CONFIG_FILE ...]] [-o OUTPUT_FILE]
              [-bc BC_PATH] [-sk] [-k CLI_APIKEYS [CLI_APIKEYS ...]]
              [-lb LOCAL_BREACH_SRC [LOCAL_BREACH_SRC ...]]
              [-gz LOCAL_GZIP_SRC [LOCAL_GZIP_SRC ...]] [-sf]
              [-ch [CHASE_LIMIT]] [--power-chase] [--hide] [--debug]
              [--gen-config]
```

### Flags

```bash
optional arguments:
  -h, --help            show this help message and exit
  -t USER_TARGETS [USER_TARGETS ...], --targets USER_TARGETS [USER_TARGETS ...]
                        Either string inputs or files. Supports email pattern
                        matching from input or file, filepath globing and
                        multiple arguments
  -u USER_URLS [USER_URLS ...], --url USER_URLS [USER_URLS ...]
                        Either string inputs or files. Supports URL pattern
                        matching from input or file, filepath globing and
                        multiple arguments. Parse URLs page for emails.
                        Requires http:// or https:// in URL.
  -q USER_QUERY, --custom-query USER_QUERY
                        Perform a custom query. Supports username, password,
                        ip, hash, domain. Performs an implicit "loose" search
                        when searching locally
  --loose               Allow loose search by disabling email pattern
                        recognition. Use spaces as pattern seperators
  -c CONFIG_FILE [CONFIG_FILE ...], --config CONFIG_FILE [CONFIG_FILE ...]
                        Configuration file for API keys. Accepts keys from
                        Snusbase, WeLeakInfo, Leak-Lookup, HaveIBeenPwned,
                        Emailrep, Dehashed and hunterio
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        File to write CSV output
  -bc BC_PATH, --breachcomp BC_PATH
                        Path to the breachcompilation torrent folder. Uses the
                        query.sh script included in the torrent
  -sk, --skip-defaults  Skips HaveIBeenPwned and HunterIO check. Ideal for
                        local scans
  -k CLI_APIKEYS [CLI_APIKEYS ...], --apikey CLI_APIKEYS [CLI_APIKEYS ...]
                        Pass config options. Supported format: "K=V,K=V"
  -lb LOCAL_BREACH_SRC [LOCAL_BREACH_SRC ...], --local-breach LOCAL_BREACH_SRC [LOCAL_BREACH_SRC ...]
                        Local cleartext breaches to scan for targets. Uses
                        multiprocesses, one separate process per file, on
                        separate worker pool by arguments. Supports file or
                        folder as input, and filepath globing
  -gz LOCAL_GZIP_SRC [LOCAL_GZIP_SRC ...], --gzip LOCAL_GZIP_SRC [LOCAL_GZIP_SRC ...]
                        Local tar.gz (gzip) compressed breaches to scans for
                        targets. Uses multiprocesses, one separate process per
                        file. Supports file or folder as input, and filepath
                        globing. Looks for 'gz' in filename
  -sf, --single-file    If breach contains big cleartext or tar.gz files, set
                        this flag to view the progress bar. Disables
                        concurrent file searching for stability
  -ch [CHASE_LIMIT], --chase [CHASE_LIMIT]
                        Add related emails from hunter.io to ongoing target
                        list. Define number of emails per target to chase.
                        Requires hunter.io private API key
  --power-chase         Add related emails from ALL API services to ongoing
                        target list. Use with --chase. Requires a private API
                        key
  --hide                Only shows the first 4 characters of found passwords
                        to output. Ideal for demonstrations
  --debug               Print request debug information
  --gen-config, -g      Generates a configuration file template in the current
                        working directory & exits. Will overwrite existing
                        h8mail_config.ini file
```

### Examples

#### Query for a single target

```bash
h8mail -t target@example.com
```

#### Query for list of targets, indicate config file for API keys, output to `pwned_targets.csv`

```bash
h8mail -t targets.txt -c config.ini -o pwned_targets.csv
```

#### Query a list of targets without making API calls against local copy of the Breach Compilation

```bash
h8mail -t targets.txt -bc ../Downloads/BreachCompilation/ -sk
```

#### Search every .gz file for targets found in targets.txt locally

```bash
h8mail -t targets.txt -gz /tmp/Collection1/ -sk
```

### Also see

- [Github](https://github.com/khast3x/h8mail)
