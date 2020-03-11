---
### The title for the content.
title : "layer2"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "layer2"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "layer2 description."
### The datetime assigned to this page.
date : 2020-03-10T16:43:48+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "layer2"
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

## Layer 2

|                 | |
|-----------------|-|
| Num             | 2 |
| Name            | Data link |
| Acronim         | Do |
| PDU             | Frame |
| What is 'on it' | NIC, Switch, Bridge |
| Function        |	Reliable transmission of data frames between two nodes connected by a physical layer |

The data link layer is responsible for the node to node delivery of the message. The main function of this layer is to make sure data transfer is error free from one node to another, over the physical layer. When a packet arrives in a network, it is the responsibility of the data link layer to transmit it to the Host using its MAC address.
Data Link Layer is divided into two sub layers :
 - Logical Link Control (LLC)
 - Media Access Control (MAC)

The packet received from Network layer (layer 3) is further divided into frames depending on the frame size of NIC (Network Interface Card). The data link layer also encapsulates Sender and Receiver's MAC address in the header.

The Receiver’s MAC address is obtained by placing an ARP(Address Resolution Protocol) request onto the wire asking "Who has that IP address?" and the destination host will reply with its MAC address.

The functions of the data Link layer are :

- Framing: Framing is a function of the data link layer. It provides a way for a sender to transmit a set of bits that are meaningful to the receiver. This can be accomplished by attaching special bit patterns to the beginning and end of the frame.
- Physical addressing: After creating frames, Data link layer adds physical addresses (MAC address) of sender and/or receiver in the header of each frame.
- Error control: Data link layer provides the mechanism of error control in which it detects and retransmits damaged or lost frames.
- Flow Control: The data rate must be constant on both sides else the data may get corrupted thus, flow control coordinates that amount of data that can be sent before receiving acknowledgement.
- Access control: When a single communication channel is shared by multiple devices, MAC sub-layer of data link layer helps to determine which device has control over the channel at a given time.

## MAC Addresses

First 3 pairs of MAC = Vendor.  

Also called OUI.

[OUI list](http://standards-oui.ieee.org/oui/oui.txt)  
[Online lookup - macvendors](https://macvendors.com/)  
