---
### The title for the content.
title: "ipv4"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "ipv4"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "ipv4 description."
### The datetime assigned to this page.
date: 2020-03-10T16:43:49+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "ipv4"
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
weight: 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
# tags : [""]
---

## IPv4

### Subnetting

Netmask depends the range of the network. `1's` in the netmask lockdown the IP address.

Small mask = Large network  
Large mask = Small network

#### Binary - 255

| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |

#### Binary - 7

| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 1   | 1   | 1   |

#### CIDR - /32

| 255       | 255       | 255       | 255       |
| --------- | --------- | --------- | --------- |
| 1111 1111 | 1111 1111 | 1111 1111 | 1111 1111 |

#### CIDR - /24

| 255       | 255       | 255       | 0         |
| --------- | --------- | --------- | --------- |
| 1111 1111 | 1111 1111 | 1111 1111 | 0000 0000 |

#### CIDR - /22

| 255       | 255       | 252       | 0         |
| --------- | --------- | --------- | --------- |
| 1111 1111 | 1111 1111 | 1111 1100 | 0000 0000 |

#### school example

```txt
IP 192.168.1.0
Neem je masker 255.255.255.192
Het eerste groene getal pakken
Aftrekken van 256
256-192 = 64

128  64  32  16  8  4  2  1

De stappen van het eerste groene getal zullen 64 zijn

1e
192.168.1.0     NETID
192.168.1.1     LB
192.168.1.63     HB
192.168.1.64     BC

172.168.0.0
255.255.252.0
256-252=4

128  64  32  16  8  4  2  1

1e
172.168.0.0
172.168.0.1
172.168.4.254
172.168.4.255

IP        192.168.100.0
MASK      255.255.255.224

224 aftrekken 255
255.255.255.255
255.255.255.224 -
                         31


Trek een streep waar het vorige getal tussen past.
128      64     32|16     8    4    2    1


1 subnet
NETID    192.168.100.0
LB       192.168.100.1
HB       192.168.100.30
BC       192.168.100.31

2 subnet
NETID    192.168.100.32
LB       192.168.100.33
HB       192.168.100.62
BC       192.168.100.63

3 subnet
NETID    192.168.100.64
LB        192.168.100.65
HB        192.168.100.94
BC        192.168.100.95

4 subnet
NETID    192.168.100.96
LB        192.168.100.97
HB        192.168.100.126
BC        192.168.100.127

5 subnet
NETID    192.168.100.128
LB        192.168.100.129
HB        192.168.100.158
BC        192.168.100.159

6 subnet
NETID    192.168.100.160
LB        192.168.100.161
HB        192.168.100.190
BC        192.168.100.191

7 subnet
NETID    192.168.100.192
LB        192.168.100.193
HB        192.168.100.222
BC         192.168.100.223

8 subnet
NETID    192.168.100.224
LB        192.168.100.225
HB        192.168.100.253
BC        192.168.100.255
```

#### Table example

##### Subnet Table

| Octect | Subnet: 128 | Subnet: 192 | Subnet: 224 | Subnet: 240 | Subnet: 248 | Subnet: 252 | Subnet: 254 | subnet: 255 |
| ------ | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 1      | /1          | /2          | /3          | /4          | /5          | /6          | /7          | /8          |
| 2      | /9          | /10         | /11         | /12         | /13         | /14         | /15         | /16         |
| 3      | /17         | /18         | /19         | /20         | /21         | /22         | /23         | /24         |
| 4      | /25         | /26         | /27         | /28         | /29         | /30         | /31         | /32         |

##### Host Table

| Octect | Hosts:             | Hosts              | Hosts             | Hosts             | Hosts             | Hosts            | Hosts            | Hosts            |
| ------ | ------------------ | ------------------ | ----------------- | ----------------- | ----------------- | ---------------- | ---------------- | ---------------- |
| 1      | /1 <br> 2147483648 | /2 <br> 1073741824 | /3 <br> 536870912 | /4 <br> 268435456 | /5 <br> 134217728 | /6 <br> 67108864 | /7 <br> 33554432 | /8 <br> 16777216 |
| 2      | /9 <br> 8388608    | /10 <br> 4194304   | /11 <br> 2097152  | /12 <br> 1048576  | /13 <br> 524288   | /14 <br> 262144  | /15 <br> 131072  | /16 <br> 65536   |
| 3      | /17 <br> 32768     | /18 <br> 16384     | /19 <br> 8192     | /20 <br> 4096     | /21 <br> 2048     | /22 <br> 1024    | /23 <br> 512     | /24 <br> 256     |
| 4      | /25 <br> 128       | /26 <br> 64        | /27 <br> 32       | /28 <br> 16       | /29 <br> 8        | /30 <br> 4       | /31 <br> 2       | /32 <br> 1       |

##### Willdcard Mask Table

| Slash | Netmask         | Wildcard Mask   |
| ----- | --------------- | --------------- |
| /32   | 255.255.255.255 | 0.0.0.0         |
| /31   | 255.255.255.254 | 0.0.0.1         |
| /30   | 255.255.255.252 | 0.0.0.3         |
| /29   | 255.255.255.248 | 0.0.0.7         |
| /28   | 255.255.255.240 | 0.0.0.15        |
| /27   | 255.255.255.224 | 0.0.0.31        |
| /26   | 255.255.255.192 | 0.0.0.63        |
| /25   | 255.255.255.128 | 0.0.0.127       |
| /24   | 255.255.255.0   | 0.0.0.255       |
| /23   | 255.255.254.0   | 0.0.1.255       |
| /22   | 255.255.252.0   | 0.0.3.255       |
| /21   | 255.255.248.0   | 0.0.7.255       |
| /20   | 255.255.240.0   | 0.0.15.255      |
| /19   | 255.255.224.0   | 0.0.31.255      |
| /18   | 255.255.192.0   | 0.0.63.255      |
| /17   | 255.255.128.0   | 0.0.127.255     |
| /16   | 255.255.0.0     | 0.0.255.255     |
| /15   | 255.254.0.0     | 0.1.255.255     |
| /14   | 255.252.0.0     | 0.3.255.255     |
| /13   | 255.248.0.0     | 0.7.255.255     |
| /12   | 255.240.0.0     | 0.15.255.255    |
| /11   | 255.224.0.0     | 0.31.255.255    |
| /10   | 255.192.0.0     | 0.63.255.255    |
| /9    | 255.128.0.0     | 0.127.255.255   |
| /8    | 255.0.0.0       | 0.255.255.255   |
| /7    | 254.0.0.0       | 1.255.255.255   |
| /6    | 252.0.0.0       | 3.255.255.255   |
| /5    | 248.0.0.0       | 7.255.255.255   |
| /4    | 240.0.0.0       | 15.255.255.255  |
| /3    | 224.0.0.0       | 31.255.255.255  |
| /2    | 192.0.0.0       | 63.255.255.255  |
| /1    | 128.0.0.0       | 127.255.255.255 |
| /0    | 0.0.0.0         | 255.255.255.255 |

##### Example 1

```txt
Subnet to calculate 192.168.1.X/25

/25 is on row 4 of our subnet table, this means the first 3 octets of our netmask are locked down and the last octect is unknown.
255.255.255.?

Our unknown octet has the value 128 as seen on the header of the Subnet Table.
This means our netmask is 255.255.255.128.

There are 128 hosts using this netmask as seen in Host Table.
2 of those are not usable, the broadcast (BC) and Network ID(NETID), this means there are 126 usable hosts in this subnet. We start counting these hosts from 0.
To define our range of usable hosts we will use the Lowest Usable (LU) and the Highest Usable (HU). This means our LU in this case will be 192.168.1.1 and our HU will be 192.168.1.126.

First Subnet
NETID     192.168.1.0
LU         192.168.1.1
HU        192.168.1.126
BC        192.168.1.127

Second Subnet
NETID     192.168.1.128
LU         192.168.1.129
HU        192.168.1.254
BC        192.168.1.255
```

##### Example 2

```txt
Subnet to calculate 10.0.X.X/10

/10 is on row 2 of the subnet table, this means the first octet of our netmask are locked down to 255, the second octect is unknown and the rest are locked down to 0.
255.?.0.0

Our unknown octect has the value of 192 as seen in the header of the subnet table.
This means our netmask is 255.192.0.0.

There are 4194304 hosts using this netmask as seen in the host table.
2 of those are not usable, the broadcast (BC) and Network ID(NETID), this means there are 4194302 usable hosts in this subnet. We start counting these hosts from 0.
To define our range of usable hosts we will use the Lowest Usable (LU) and the Highest Usable (HU). Since this is a bigger range the Wildcard Mask can be used to make this easier.
To get our wildcard mask we inverse of our mask. Our wildcard mask is 0.63.255.255. See Wildcard Mask table.

This means our LU in this case will be 10.0.0.1 and our HU will be 10.63.255.254.

NETID     10.0.0.0
LU         10.0.0.1
HU        10.63.255.254
BC        10.63.255.255


NETID     10.64.0.0
LU         10.64.0.1
HU        10.127.255.254
BC        10.127.255.255

NETID     10.128.0.0
LU         10.128.0.1
HU        10.191.255.254
BC        10.191.255.255


NETID     10.192.0.0
LU         10.192.0.1
HU        10.255.255.254
BC        10.255.255.255
```

### Network Classes

[Source](https://gist.githubusercontent.com/inadarei/86968c7e5b8f322db260e56723e105ec/raw/407176bef50505055dd8a4f332e54d60c429495b/ipaddressclasses.md)

IP Addresses identify both a network as well as host on a network. Depending on the class of a network, certain amount of bits in the IP (32 bits overall) are allocated for network adressing and the rest is for: adressing the host on the network.

1. Class A: first octet is network, last three: host
2. Class B: first two octets are for network, last two: host
3. Class C: first three octets are for network, only last octet is for host.

Furthermore, looking at the IP itself, you can tell which class of IP it is, using the following rules:

|         Class         | Binary Prefix | First Octet of <br/> dotted-decimal must be | Excluded Addresses     |
| :-------------------: | ------------- | ------------------------------------------- | ---------------------- |
|           A           | 0             | 0 to 127                                    | 10.% and 127.%         |
|           B           | 10            | 128 to 191                                  | 172.16.% to 172.31.%   |
|           C           | 110           | 192 to 223                                  | 192.168.% to 192.168.% |
|  D<br/> (Multicast)   | 1110          | 224 to 239                                  |                        |
| E<br/> (Experimental) | 11110         | 240 to 254                                  |                        |

Additional, Special IP Rules:

1. All-zeros (in decimal) host is the network itself. E.g. 141.23.0.0 - is the network 141.23
2. All-ones (in decimal) is a broadcast address signaling to all hosts of the network, e.g. 141.23.255.255 is a broadcast address for the 141.23 network
   - Please note that `255.255.255.255` can also be used to broadcast on a current network.
3. 127.% are loopback IPs
4. [RFC1597](https://tools.ietf.org/html/rfc1597) reserves following ranges for private networks:
   1. `10.%`
   2. `172.16.%` - `172.31.%`
   3. `192.168.%` - `192.168.%`
5. Reserved for Autoconfiguration Range: `169.254.%` to `169.%`

### Classless Inter-Domain Routing (CIDR)

[Source](https://gist.githubusercontent.com/inadarei/86968c7e5b8f322db260e56723e105ec/raw/407176bef50505055dd8a4f332e54d60c429495b/ipaddressclasses.md)

CIDR notation indicates how many bits are taken in the mask by network + subnet. Remembering that overall there are 32 bits, the remaining bits can be used for host addresses. For instance: /25 indicates that 32-25 = 7 bits are available for the host portion, making 2^7=128 (in reality 128-2 = 126) host addresses available for assignment. The full CIDR address includes an IP (usually: lowest IP) of the range, e.g.: 192.168.100.14/24

##### Example CIDR -> IP Range Calculation

CIDR: `212.100.105.0/22`

Steps:

1. Figure-out netmask.

   Since 32-22 = 10, first two octets are all 1's, last one is all 0's and first six bits of the third octet are 1's. Calculating 128+64+32+16+8+4 = 252, the final netmask is: `255.255.252.0`. Obviously, here we remembered bit weights: 128,64,32,16,8,4,2,1 by heart, but if you don't, you just need to remember `128` is the high bit and the rest are sequence of dividing by 2 until 1.

2. Calculate IP range of the range.

   Knowing our netmask, we know that the lowest IP will have the same number in the first two octets as the example IP: 212.100.%. Since last octet is not masked, lowest IP will have it as zero, so we just need to figure-out lowest allowed number in the third octet. Third octet (252) in binary is: '1111 - 1100' which would enforce that the first six bits of the example IP are the same for all IPs in range. 105 in binary is: '0110 - 1001', therefore the lowest number with fixed six bits is: '**0110-10**00' (64+32+8=104) and highest is: '**0110 - 10**11' (64+32+8+2+1=107), where bolded-out part is the fixed part. Considering this, the final range is: 212.100.104.0 - 212.100.107.255.

There're also some really nice online calculators for these, e.g.: http://www.ipaddressguide.com/cidr

**Please note:** as a practical matter most commonly, CIDR ranges do indicate the lowest IP, since lowest IP is the network IP and the highest is broadcast IP, for that network. However, as we saw - we can calculate the proper range even if any other IP from the range is given (possibly: by mistake).

### NAT types

[source](https://github.com/pion/webrtc/wiki/Network-Address-Translation/)

An old version of the stun spec ([RFC3489](https://tools.ietf.org/html/rfc3489)) defined the following [NAT variations](https://tools.ietf.org/html/rfc3489#section-5):

**Full Cone:** A full cone NAT is one where all requests from the
same internal IP address and port are mapped to the same external
IP address and port. Furthermore, any external host can send a
packet to the internal host, by sending a packet to the mapped
external address.

**Restricted Cone:** A restricted cone NAT is one where all requests
from the same internal IP address and port are mapped to the same
external IP address and port. Unlike a full cone NAT, an external
host (with IP address X) can send a packet to the internal host
only if the internal host had previously sent a packet to IP
address X.

**Port Restricted Cone:** A port restricted cone NAT is like a
restricted cone NAT, but the restriction includes port numbers.
Specifically, an external host can send a packet, with source IP
address X and source port P, to the internal host only if the
internal host had previously sent a packet to IP address X and
port P.

**Symmetric:** A symmetric NAT is one where all requests from the
same internal IP address and port, to a specific destination IP
address and port, are mapped to the same external IP address and
port. If the same host sends a packet with the same source
address and port, but to a different destination, a different
mapping is used. Furthermore, only the external host that
receives a packet can send a UDP packet back to the internal host.

Additional research can be found in [RFC5780](https://tools.ietf.org/html/rfc5780)

[ccding/go-stun](https://github.com/ccding/go-stun) may be helpful to figure out your nat type(s).

##### NAT considerations

NAT bindings should not be considered to be deterministic:

- If an external port is already mapped to another host the NAT has to assign you another port.
- Some routers implement randomized port mapping.

##### Hole punching

Hole punching is an easy way to circumvent a NAT. Peers try to establish a direct connection by learning their respective public addresses using a 3rd party server. The 3rd party server is also used to keep the NAT binding alive.

The hole punching examples below can be used to get through the Full Cone, Restricted Cone and Port Restricted Cone NAT types. Symmetric NATs require more complex processes. However, this NAT type is more rare and can still be circumvented using a TURN server to relay traffic.

###### UDP hole punching

First establisch a local connection by listening using [`net.ListenUDP`](https://godoc.org/net#ListenUDP). Next use [`WriteTo`](https://godoc.org/net#UDPConn.WriteTo) and [`ReadFrom`](https://godoc.org/net#UDPConn.ReadFrom) to send and receive packets to and from the desired remote addresses.

###### TCP hole punching

TCP hole punching is a little more involved. In order to keep the NAT binding alive the same local TCP port should be used. This can be done by setting the SO_REUSEADDR and SO_REUSEPORT socket options on most operating systems. Sadly this isn't well supported until go1.11 as discussed in [golang/go#9661](https://github.com/golang/go/issues/9661). Starting from go1.11 the flag can be set using the [Dialer.Control](https://tip.golang.org/pkg/net/#Dialer.Control) function.

Example (dial.go):

```go
var d net.Dialer
d.Control = controlOnConnSetup

func controlOnConnSetup(network string, address string, c syscall.RawConn) error {
    return nil
}
```

For Unix (dial_unix.go):

```go
// +build darwin dragonfly freebsd linux netbsd openbsd solaris
func controlOnConnSetup(c syscall.RawConn, addr Addr) error {
    var operr error
    fn := func(s uintptr) {
        operr = syscall.SetsockoptInt(int(s), syscall.SOL_SOCKET, syscall.SO_REUSEADDR, 1)
        if operr != nil {
            return
        }
        operr = syscall.SetsockoptInt(int(s), syscall.SOL_SOCKET, syscall.SO_REUSEPORT, 1)
        if operr != nil {
            return
        }
    }
    if err := c.Control(fn); err != nil {
        return err
    }
    if operr != nil {
        return operr
    }
    return nil
}
```

For Windows (dial_windows.go):

```go
func controlOnConnSetup(network string, address string, c syscall.RawConn) error {
    var operr error
    fn := func(s uintptr) {
        handle := syscall.Handle(fd)
        operr = syscall.SetsockoptInt(handle, syscall.SOL_SOCKET, syscall.SO_REUSEADDR, 1)
        if operr != nil {
            return
        }
    }
    if err := c.Control(fn); err != nil {
        return err
    }
    if operr != nil {
        return operr
    }
    return nil
}
```

##### Candidate types and combinations of NAT types

Following chart summarises which types of candidates contribute to a successful NAT traversal in each combination of local and remote NAT types.

|           |      Open      |       F.Cone        |       R.Cone        |    PR.Cone     |      Symmetric      |
| :-------: | :------------: | :-----------------: | :-----------------: | :------------: | :-----------------: |
|   Open    |      host      |   srflx or prflx    |   srflx or prflx    | srflx or prflx |        prflx        |
|  F.Cone   | srflx or prflx |        srflx        |        srflx        |     srflx      | srflx **and** prflx |
|  R.Cone   | srflx or prflx |        srflx        |        srflx        |     srflx      | srflx **and** prflx |
|  PR.Cone  | srflx or prflx |        srflx        |        srflx        |     srflx      |        relay        |
| Symmetric |     prflx      | srflx **and** prflx | srflx **and** prflx |     relay      |        relay        |

- Open: Open to the Internet
- F.Cone: Full-cone NAT
- R.Cone: Restricted-cone NAT
- PR.Cone: Port restricted-cone NAT
- Symmetric: Symmetric NAT
- host: Local (host) address candidate
- srflx: Server reflexive candidate (a candidate derived from STUN)
- prflx: Peer reflexive candidate
- relay: Relay NAT (a candidate derived from TURN)

#### P.A.T. Port Address Translation

`> 1024`

| my local ip | my local port | my external ip | my external port | external ip |
| ----------- | ------------- | -------------- | ---------------- | ----------- |
| 192.168.3.1 | :1025         | 9.2.1.33       | :1025            | 188.1.3.15  |
| 192.168.3.2 | :1025         | 9.2.1.33       | :1026            | 188.1.3.15  |
| 192.168.3.3 | :1025         | 9.2.1.33       | :1027            | 188.1.3.15  |
