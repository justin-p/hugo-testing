---
### The title for the content.
title: "Layer 3"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "osi model"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Layer 3 description."
### The datetime assigned to this page.
date: 2020-03-10T16:33:40+01:00
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
weight: 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
# tags : [""]
### a map of Front Matter keys whose values are passed down to the page’s descendants unless overwritten by self or a closer ancestor’s cascade.
cascade:
  tags: ["Layer 3"]
---

## Layer 3

{{< children style="card" depth="1" description="true" sort="Name" >}}

|                 |                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------ |
| Num             | 3                                                                                                |
| Name            | Network                                                                                          |
| Acronim         | Not                                                                                              |
| PDU             | Packet                                                                                           |
| What is 'on it' | Router                                                                                           |
| Function        | Structuring and managing a multi-node network, including addressing, routing and traffic control |

Network layer works for the transmission of data from one host to the other located in different networks. It also takes care of packet routing i.e. selection of the shortest path to transmit the packet, from the number of routes available. The sender & receiver’s IP address are placed in the header by network layer.

The functions of the Network layer are :

- Routing: The network layer protocols determine which route is suitable from source to destination. This function of network layer is known as routing.
- Logical Addressing: In order to identify each device on internetwork uniquely, network layer defines an addressing scheme. The sender & receiver’s IP address are placed in the header by network layer. Such an address distinguishes each device uniquely and universally.
