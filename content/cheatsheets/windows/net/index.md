---
### The title for the content.
title : "NET"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "net"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "NET Command is used to manage network resources."
### The datetime assigned to this page.
date : 2021-09-01T17:53:39+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "net"
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

## NET

### ACCOUNTS / NET USER / NET GROUP

#### Usage

```bash
NET ACCOUNTS  [/FORCELOGOFF:{minutes | NO} ] [/MINPWLENGTH:length]
             [/MAXPWAGE:{days | UNLIMITED}] [/MINPWAGE:days] [/UNIQUEPW:number] [/DOMAIN]
```

#### Examples ACCOUNTS

##### View the local password & logon policy.

```bash
NET ACCOUNTS
```

##### View the domain password & logon policy.

```bash
NET ACCOUNTS /DOMAIN
```

##### Set passwords to never expire.

```bash
NET ACCOUNTS /MAXPWAGE:UNLIMITED /DOMAIN
```

#### Examples USER

##### View the password properties of user account 'Ella'

```bash
NET USER Ella
```

##### View user account details

```bash
NET USER [/DOMAIN]
```

##### Add a user account.

```bash
NET USER username {password | *} /ADD [options] [/DOMAIN]
```

##### Modify a user account.

```bash
NET USER [username [password | *] [options]] [/DOMAIN]
```

##### Delete a username

```bash
NET USER username /DELETE [/DOMAIN]
```

#### Examples GROUP

##### Add a group to domain

```bash
NET GROUP groupname /ADD /DOMAIN
```

##### Add a group to local

```bash
NET LOCALGROUP groupname /ADD 
```

##### Edit a domain group

```bash
NET GROUP groupname /DOMAIN
```

```bash
NET LOCALGROUP groupname
```

##### Delete a domain group

```bash
NET GROUP groupname /DELETE [/DOMAIN]
```

```bash
NET LOCALGROUP groupname /DELETE
```

##### Add a user to a group

```bash
NET GROUP groupname username [...] /ADD /DOMAIN
```

```bash
NET LOCALGROUP groupname username [...] /ADD
```

##### Delete a user from a group

```bash
NET GROUP groupname username [...] /DELETE /DOMAIN
```

```bash
NET LOCALGROUP groupname username [...] /DELETE
```

#### Examples FILE

##### Show all open shared files

```bash
NET FILE
```

#### Examples SESSION

##### List all sessions to this machine

```bash
NET SESSION
```

#### Examples services

##### List running services

```bash
NET START
```

##### Stop and start service

```bash
NET STOP <SERVICE> && NET START <SERVICE>
```

#### Examples SHARE

##### Display the details of all local shares

```bash
NET SHARE
```

##### Create a new share

```bash
NET SHARE <sharename>=C:\path\to\folder /REMARK:"comment" /CACHE:No
```

##### Limit the number of users who can connect to a share

```bash
NET SHARE <sharename> /USERS:15
```

##### Remove any limit on the number of users who can connect to a share

```bash
NET SHARE <sharename> /UNLIMITED
```

##### Delete a share

```bash
NET SHARE <sharename> /DELETE
```

#### Examples USE

##### Map a file share

```bash
NET USE J: \\MainServer\Users\
```

##### Disconnect from a share

```bash
NET USE J: /DELETE /Y
```

##### Map a drive using alternate credentials (PowerShell)

```PowerShell
PS C:\> $SecString = "s5QxXkwnOxt3MuNlgY6E" | ConvertTo-SecureString -AsPlainText -Force
PS C:\> $cred = New-Object System.Management.Automation.PsCredential('DOMAIN\user',$SecString)
PS C:\> New-PSDrive -name G -Root \\Server64\Share1 -Credential $cred -PSProvider filesystem -Persist
```

#### Examples VIEW

##### Display a list of computers in the current domain

```bash
NET VIEW
```

##### List the File/Printer shares on a remote computer

```bash
NET VIEW \\ComputerName
```

##### List all the shares in the domain

```bash
NET VIEW /DOMAIN
```

#### List of shares on a different domain

```bash
NET VIEW /DOMAIN:domainname
```

### Also see

N/A