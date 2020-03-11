---
### The title for the content.
title: "00. Introduction"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "00 intro"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Introduction to this guide."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "00-intro"
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

## Introduction

This guide helps first timers to setup a Ubuntu server through the command-line interface \(CLI\). This was initially written by a old friend of mine to help me setup my first 'publicly accessible' server. Over the years I build/updated his work and still use it as a reference for a basic baseline when ever I need to setup a VPS. There is a bunch of things you can do yourself to improve, finetune and further secure your VPS, but this should get you at least setup with the \(imo\) bare minimums.

This is also the main reason why this guide its aimed at people who are new to Linux and have little to no experience or sysadmins that have no experience with Linux/Linux headless servers and want to get a server up and running. This is by no means a guide on _all you need to know about server management_.

_This guide has last been tested on Ubuntu 18.04LTS._
