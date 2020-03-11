---
### The title for the content.
title : "OSI Model"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "osi model"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "OSI Model description."
### The datetime assigned to this page.
date : 2020-03-10T16:33:40+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "osi-model"
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
### a map of Front Matter keys whose values are passed down to the page’s descendants unless overwritten by self or a closer ancestor’s cascade. 
cascade:
    tags: ['OSI Model']
---

## OSI Model - Open Systems Interconnecting Model

Please Do Not Throw Sausage Pizza Away

| Layer number | layer name   | Protocol data unit (PDU)       | What runs 'on it'            | Function of layer                                                                                                                               |
| ------------ | ------------ | ------------------------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 7            | Application  |                                | HTTP, SMTP, SMB              | High-level APIs, including resource sharing, remote file access                                                                                 |
| 6            | Presentation | Data                           | AVI, GIF ,JPEG, MKV          | Translation of data between a networking service and an application; including character encoding, data compression and encryption/decryption   |
| 5            | Session      |                                | Session management (sockets) | Managing communication sessions, i.e. continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes |
| 4            | Transport    | Segment (TCP) / Datagram (UDP) |                              | Reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing                    |
| 3            | Network      | Packet                         | IP addresses, Routing        | Structuring and managing a multi-node network, including addressing, routing and traffic control                                                |
| 2            | Data link    | Frame                          | Switching, MAC addresses     | Reliable transmission of data frames between two nodes connected by a physical layer                                                            |
| 1            | Physical     | Bit                            | Data cables, CAT5e, CAT6     | Transmission and reception of raw bit streams over a physical medium                                                                            |

### Protocol data unit

Stands for "Protocol Data Unit." A PDU is a specific block of information transferred over a network. It is often used in reference to the OSI model, since it describes the different types of data that are transferred from each layer.

{{< children style="card" depth="1" description="true" sort="Name" >}}
