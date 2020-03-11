---
title: "s_client"
description: "OpenSSL comes with a client tool that you can use to connect to a secure server. The tool is similar to telnet or nc, in the sense that it handles the SSL/TLS layer but allows you to fully control the layer that comes next."
date: 2020-03-06T11:26:37+01:00
draft: false
weight: 142
---

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
