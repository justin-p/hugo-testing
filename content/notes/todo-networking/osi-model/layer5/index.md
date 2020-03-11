---
### The title for the content.
title: "Layer 5"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "layer5"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "layer5 description."
### The datetime assigned to this page.
date: 2020-03-10T16:43:49+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "layer5"
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

## Layer 5

|                 |                                                                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Num             | 5                                                                                                                                               |
| Name            | Session                                                                                                                                         |
| Acronim         | Sausage                                                                                                                                         |
| PDU             |                                                                                                                                                 |
| What is 'on it' | Session management (sockets)                                                                                                                    |
| Function        | Managing communication sessions, i.e. continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes |

This layer is responsible for establishment of connection, maintenance of sessions, authentication and also ensures security.
The functions of the session layer are:

- Session establishment, maintenance and termination: The layer allows the two processes to establish, use and terminate a connection.
- Synchronization: This layer allows a process to add checkpoints which are considered as synchronization points into the data. These synchronization point help to identify the error so that the data is re-synchronized properly, and ends of the messages are not cut prematurely and data loss is avoided.
- Dialog Controller: The session layer allows two systems to start communication with each other in half-duplex or full-duplex.
