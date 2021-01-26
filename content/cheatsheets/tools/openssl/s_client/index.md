---
### The title for the content.
title : "s_client"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "s_client"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "s_client description."
### The datetime assigned to this page.
date : 2020-03-10T16:36:30+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "s_client"
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

## s_client

### Usage

```bash
openssl s_client OPTIONS ARGUMENTS
```

### Examples

#### Check an SSL connection

```bash
openssl s_client -connect example.com:443
openssl s_client -host example.com -port 443
```

#### Make an SSL connection. Hide most info

```bash
openssl s_client --connect 127.0.0.1:30001 -quiet
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
```

#### show full certificate chain

```bash
openssl s_client -showcerts -host example.com -port 443 </dev/null
```

#### Extract the certificate

```bash
openssl s_client -connect example.com:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > certificate.pem
```

#### Test for TLS/SSL version cipher

```bash
openssl s_client -host example.com -port 443 -ssl3 2>&1 </dev/null
```

Options

```bash
-ssl2  
-ssl3  
-tls1  
-tls1_1  
-tls1_2
```

#### Test for specific cipher

```bash
openssl s_client -host example.com -port 443 -cipher        ECDHE-RSA-AES128-GCM-SHA256 2>&1 </dev/null
```

#### Measure SSL connection time without/with session reuse

```bash
openssl s_time -connect example.com:443 -new
openssl s_time -connect example.com:443 -reuse
```
