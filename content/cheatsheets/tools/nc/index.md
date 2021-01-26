---
### The title for the content.
title : "nc"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "nc"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "nc description."
### The datetime assigned to this page.
date : 2020-03-10T16:36:30+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "nc"
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

## nc


### Usage

```bash
nc OPTIONS HOST PORT
```

### Flags

```bash
-4     Forces nc to use IPv4 addresses only.
-6     Forces nc to use IPv6 addresses only.
-b     Allow broadcast.
-C     Send CRLF as line-ending.
-D     Enable debugging on the socket.
-d     Do not attempt to read from stdin.
-h     Prints out nc help.
-I length     Specifies the size of the TCP receive buffer.
-i interval     Specifies a delay time interval between lines of text sent and received. Also, causes a delay time between connections to multiple ports.
-k     Forces nc to stay listening for another connection after its current connection is completed. It is an error to use this option without the -l option.
-l     Used to specify that nc should listen for an incoming connection rather than initiate a connection to a remote host. It is an error to use this option in conjunction with the -p, -s, or -z options. Additionally, any timeouts specified with the -w option are ignored.
-n     Do not do any DNS or service lookups on any specified addresses, hostnames or ports.
-O length     Specifies the size of the TCP send buffer.
-P proxy_username     Specifies a username to present to a proxy server that requires authentication. If no username is specified then authentication will not be attempted. Proxy authentication is only supported for HTTP CONNECT proxies at present.
-p source_port     Specifies the source port nc should use, subject to privilege restrictions and availability.
-q seconds     after EOF on stdin, wait the specified number of seconds and then quit. If seconds is negative, wait forever.
-r     Specifies that source or destination ports should be chosen randomly instead of sequentially within a range or in the order that the system assigns them.
-S     Enables the RFC 2385 TCP MD5 signature option.
-s source     Specifies the IP of the interface that is used to send the packets. For UNIX-domain datagram sockets, specifies the local temporary socket file to create and use so that datagrams can be received. It is an error to use this option in conjunction with the -l option.
-T toskeyword     Change IPv4 TOS value. toskeyword may be one of critical, inetcontrol, lowcost, lowdelay, netcontrol, throughput, reliability, or one of the DiffServ Code Points: ef, af11 ... af43, cs0 ... cs7; or a number in either hex or decimal.
-t     Causes nc to send RFC 854 DON'T and WON'T responses to RFC 854 DO and WILL requests. This makes it possible to use nc to script telnet sessions.
-U     Specifies to use UNIX-domain sockets.
-u     Use UDP instead of the default option of TCP. For UNIX-domain sockets, use a datagram socket instead of a stream socket. If a UNIX-domain socket is used, a temporary receiving socket is created in /tmp unless the -s flag is given.
-V rtable     Set the routing table to be used. The default is 0.
-v     Have nc give more verbose output.
-w timeout     Connections which cannot be established or are idle timeout after timeout seconds. The -w flag has no effect on the -l option, i.e. nc will listen forever for a connection, with or without the -w flag. The default is no timeout.
-X proxy_protocol     Requests that nc should use the specified protocol when talking to the proxy server. Supported protocols are "4" (SOCKS v.4), "5" (SOCKS v.5) and "connect" (HTTPS proxy). If the protocol is not specified, SOCKS version 5 is used.
-x proxy_address[:port]     Requests that nc should connect to destination using a proxy at proxy_address and port. If port is not specified, the well-known port for the proxy protocol is used (1080 for SOCKS, 3128 for HTTPS).
-Z     DCCP mode.
-z     Specifies that nc should only scan for listening daemons, without sending any data to them. It is an error to use this option in conjunction with the -l option.
```

### Examples

#### Netcat listening on port 567/TCP

```bash
nc -l -p 567
```

#### Connecting to that port from another machine

```bash
nc 1.2.3.4 5676
```

#### pipe a text file to the listener

```bash
cat infile | nc 1.2.3.4 567 -q 10
```

#### save a received text file

```bash
nc -l -p 567 > textfile
```

#### transfer a directory

first at the receiving end set up

```bash
nc -l -p 678 | tar xvfpz
```

Then send the directory

```bash
tar zcfp - /path/to/directory | nc -w 3 1.2.3.4 678
```

#### send a message to your syslog server

```bash
"echo '<0>message' | nc -w 1 -u syslogger 514"
```

#### Setting up a remote shell listener

```bash
nc -v -e '/bin/bash' -l -p 1234 -t
```

or

```bash
nc l p 1234 e "c\windows\system32\cmd.exe"
```

Then telnet to port 1234 from elsewhere to get the shell.

#### Using netcat to make an HTTP request

```bash
echo -e "GET http//www.google.com HTTP/1.0nn" | nc -w 5 www.google.com 80
```

#### Making a one-page webserver

```bash
cat homepage.txt | nc -v -l -p 80
```

### Also see

- [Netcat Commands](https://gist.githubusercontent.com/cmbaughman/c91f41ba7b2cf71106f1/raw/1d6e35f72817a81d0160517600c8a895217dd924/nc.md)
