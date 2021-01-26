---
### The title for the content.
title : "curl"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "curl"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "transfer a URL."
### The datetime assigned to this page.
date : 2020-03-10T16:38:52+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "curl"
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

## curl

### Usage

```bash
curl OPTIONS URL
```

### Flags

#### write to file

```bash
-o <file>
--output <file>
```

#### Authentication

```bash
https://devhints.io/curl
-u <user>:<pass>
--user <user>:<pass>
```

#### Verbose

```bash
-v
--verbose
```

#### Very Verbose

```bash
-vv
```

#### Silent

```bash
-s
--silent
```

#### Headers only

```bash
-I
--head
```

#### Request

```bash
-X POST
--request POST
```

#### follow link if page redirects

```bash
-L
```

### Data

HTTP post data, URL encoded (eg, status="Hello")

```bash
-d 'data'
--data 'data'
```

#### data via file

```bash
-d @file
--data @file
```

#### send data via GET

```bash
-G
--get
```

### Headers

#### user-agent

```bash
-A <str>
--user-agent <str>
```

#### cookie

```bash
-b name=val
--cookie name=val
```

#### cookie via file

```bash
-b FILE
--cookie FILE
```

#### Custom header

```bash
-H "X-Foo: y"
--header "X-Foo: y"
```

#### Use deflate/gzip

```bash
--compressed
```

### SSL/TLS

```bash
--cacert <file>
--capath <dir>
```

#### Client cert file

```bash
-E <cert>
--cert <cert>
```

#### Cert type

```bash
--cert-type <der/pem/eng>
```

#### Ignore SSL

```bash
-k
--insecure
```

### Examples

#### Post data

```bash
curl -d password=x http://x.com/y
```

#### Auth/data

```bash
curl -u user:pass -d status="Hello" http://twitter.com/statuses/update.xml
```

#### multipart file upload

```bash
curl -v -include --form key1=value1 --form upload=@localfilename URL
```

### Also see

* [DevHints](https://devhints.io/curl)
