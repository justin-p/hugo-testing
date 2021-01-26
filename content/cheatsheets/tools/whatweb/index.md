---
### The title for the content.
title : "whatweb"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "whatweb"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "WhatWeb identifies websites."
### The datetime assigned to this page.
date : 2020-03-11T16:20:49+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "whatweb"
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
tags : ["Identify Website Technologies"]
---

## whatweb

### Installation

```bash

```

### Usage

```bash
whatweb [options] <URLs>
```

### Flags

```bash
TARGET SELECTION:
  <TARGETs>             Enter URLs, hostnames, IP addresses, filenames or
                        IP ranges in CIDR, x.x.x-x, or x.x.x.x-x.x.x.x
                        format.
  --input-file=FILE, -i Read targets from a file. You can pipe
                        hostnames or URLs directly with -i /dev/stdin.

TARGET MODIFICATION:
  --url-prefix          Add a prefix to target URLs.
  --url-suffix          Add a suffix to target URLs.
  --url-pattern         Insert the targets into a URL. Requires --input-file,
                        eg. www.example.com/%insert%/robots.txt 

AGGRESSION:
  The aggression level controls the trade-off between speed/stealth and
  reliability.
  --aggression, -a=LEVEL Set the aggression level. Default: 1.
  Aggression levels are:
  1. Stealthy   Makes one HTTP request per target. Also follows redirects.
  3. Aggressive If a level 1 plugin is matched, additional requests will be
      made.
  4. Heavy      Makes a lot of HTTP requests per target. Aggressive tests from
      all plugins are used for all URLs.

HTTP OPTIONS:
  --user-agent, -U=AGENT Identify as AGENT instead of WhatWeb/0.5.1.
  --header, -H          Add an HTTP header. eg "Foo:Bar". Specifying a default
                        header will replace it. Specifying an empty value, eg.
                        "User-Agent:" will remove the header.
  --follow-redirect=WHEN Control when to follow redirects. WHEN may be 'never',
                        `http-only', `meta-only', `same-site', or `always'.
                        Default: always.
  --max-redirects=NUM   Maximum number of contiguous redirects. Default: 10.

AUTHENTICATION:
  --user, -u=<user:password> HTTP basic authentication.
  --cookie, -c=COOKIES  Provide cookies, e.g. 'name=value; name2=value2'.
  --cookiejar=FILE      Read cookies from a file.

PROXY:
  --proxy           <hostname[:port]> Set proxy hostname and port.
                    Default: 8080.
  --proxy-user      <username:password> Set proxy user and password.

PLUGINS:
  --list-plugins, -l            List all plugins.
  --info-plugins, -I=[SEARCH]   List all plugins with detailed information.
                                Optionally search with keywords in a comma
                                delimited list.
  --search-plugins=STRING       Search plugins for a keyword.
  --plugins, -p=LIST  Select plugins. LIST is a comma delimited set of 
                      selected plugins. Default is all.
                      Each element can be a directory, file or plugin name and
                      can optionally have a modifier, eg. + or -
                      Examples: +/tmp/moo.rb,+/tmp/foo.rb
                      title,md5,+./plugins-disabled/
                      ./plugins-disabled,-md5
                      -p + is a shortcut for -p +plugins-disabled.

  --grep, -g=STRING|REGEXP      Search for STRING or a Regular Expression. Shows 
                                only the results that match.
                                Examples: --grep "hello"
                                --grep "/he[l]*o/"
  --custom-plugin=DEFINITION\tDefine a custom plugin named Custom-Plugin,
  --custom-plugin=DEFINITION  Define a custom plugin named Custom-Plugin,
                        Examples: ":text=>'powered by abc'"
                        ":version=>/powered[ ]?by ab[0-9]/"
                        ":ghdb=>'intitle:abc \"powered by abc\"'"
                        ":md5=>'8666257030b94d3bdb46e05945f60b42'"
  --dorks=PLUGIN        List Google dorks for the selected plugin.

OUTPUT:
  --verbose, -v         Verbose output includes plugin descriptions. Use twice
                        for debugging.
  --colour,--color=WHEN control whether colour is used. WHEN may be 'never',
                        'always', or 'auto'.
  --quiet, -q           Do not display brief logging to STDOUT.
  --no-errors           Suppress error messages.

LOGGING:
  --log-brief=FILE        Log brief, one-line output.
  --log-verbose=FILE      Log verbose output.
  --log-errors=FILE       Log errors.
  --log-xml=FILE          Log XML format.
  --log-json=FILE         Log JSON format.
  --log-sql=FILE          Log SQL INSERT statements.
  --log-sql-create=FILE   Create SQL database tables.
  --log-json-verbose=FILE Log JSON Verbose format.
  --log-magictree=FILE    Log MagicTree XML format.
  --log-object=FILE       Log Ruby object inspection format.
  --log-mongo-database    Name of the MongoDB database.
  --log-mongo-collection  Name of the MongoDB collection. Default: whatweb.
  --log-mongo-host        MongoDB hostname or IP address. Default: 0.0.0.0.
  --log-mongo-username    MongoDB username. Default: nil.
  --log-mongo-password    MongoDB password. Default: nil.  
  --log-elastic-index     Name of the index to store results. Default: whatweb 
  --log-elastic-host      Host:port of the elastic http interface. Default: 127.0.0.1:9200
  
PERFORMANCE & STABILITY:
  --max-threads, -t       Number of simultaneous threads. Default: 25.
  --open-timeout          Time in seconds. Default: 15.
  --read-timeout          Time in seconds. Default: 30.
  --wait=SECONDS          Wait SECONDS between connections.
                          This is useful when using a single thread.

HELP & MISCELLANEOUS:
  --short-help            Short usage help.
  --help, -h              Complete usage help.
  --debug                 Raise errors in plugins.
  --version               Display version information. (WhatWeb 0.5.1).
```

### Examples

```bash
whatweb https://justin-p.me
```

### Also see

* [Github](https://github.com/urbanadventurer/WhatWeb)
