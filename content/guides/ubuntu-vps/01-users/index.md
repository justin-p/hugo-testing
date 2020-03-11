---
### The title for the content.
title: "01. Adding users"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "01 users"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Adding users using the commandline."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "01-users"
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

## Adding users

Most likely if you are setting up a VPS with a cloud provider they gave you access to the machine with the root account. Using the root account for daily tasks is against best practices, so first things first, lets create a additional account for daily administrator tasks. If you are installing in VM you most likely already setup a additional account during the installation, if so you can skip to the next page.

In this guide we will be using a account named `beheer`. This is interchangeable between systems. I'd recommend choosing something that you like.

To setup this user follow the instructions below:

* Create new user with `adduser beheer`
* Change user to your new one to check whether it works `su beheer`
* Try doing something you should not be able to do, like `apt-get install ncdu`. You will probably see a Error message. This is because this user account currently does not have rights to run this command. This is because this user has not been added to the sudoers group.
* Go back to root `exit`
* Add the user to sudoers `sudo adduser beheer sudo`
* Try switching to the user and see if you are now able to install something.
