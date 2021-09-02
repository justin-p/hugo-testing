---
### The title for the content.
title: "E-Mail Gathering"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "email"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "If you know e-mail addresses you know naming conventions and possible even passwords."
### The datetime assigned to this page.
date: 2020-03-10T16:43:44+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "email"
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
tags: ["user-enumeration"]
---

## User enumeration

When you want to infiltrate an organization gaining some form of credentials will be key. One of the ways to gain these credentials would be to preform brute-force techniques, such as password spraying. But in order to preform these you would first need to have a list of potential usernames. This is where user enumeration comes in.

### Username schema

If the target organisation is Microsoft based you will most likely be able to use 2 usernames for each account. This is because Active Directory has 2 options for valid usernames. sAMAccountName (DOMAIN\user) and UserPrincipalNames (user.name@domain.tld). Most of the times the UPN will match the e-mailadres of the user. In the case where these dont match, or you need to know the username schemas for sAMAccountName document meta data may be able to help you.

### Meta data

If an organization  publishes office files (word, excel, pdf, etc) on the internet there is a high chance that it will contain some form of metadata, one of which can be the Author and Creator fields.
These field can contain internal usernames which you can use to guesse there naming schema.

Tools: PowerMeta, FOCA # MOVE TO OWN TOOLS PAGE

### Users lists

After finding out the user naming schema you can start to generate a user list. One of the ways todo is is to scrape employee names from linked in and generate a userlist based of the user naming schema.
A tool called [CrossLinked](https://github.com/m8r0wn/CrossLinked) can help you with this.

### Validation endpoints

Once you have generated user list you should try to validate if these are actually valid. The graph below shows some options you can use.

| What       | Where                                           | With what  |
| ---------- | ----------------------------------------------- | ---------- |
| Azure/O365 | https://login.microsoft.com/common/oauth2/token | [MSOLSpray](https://github.com/dafthack/MSOLSpray)  |
| Onprem     | https://webmail.domain.com/owa/ or /ews/        | [MailSniper](https://github.com/dafthack/MailSniper) |

### External services

| Service                               | info                     |
| ------------------------------------- | ------------------------ |
| [hunter.io](https://hunter.io)        | find email addresses     |
| [emailrep](https://emailrep.io/)      | get e-mail 'reputation'  |
| [linkedin](https://www.linkedin.com/) | LinkedIn is your friend. |

### Related pages

{{< related_pages_table tag="user-enumeration" >}}
