---
title: "curl"
description: " "
date: 2020-03-06T11:25:00+01:00
draft: false
weight: 50
---

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

[DevHints](https://devhints.io/curl)
