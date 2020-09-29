---
### The title for the content.
title : "cyborg"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "cyborg"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "cyborg description."
### The datetime assigned to this page.
date : 2020-09-29T14:47:17+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "cyborg"
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
    tags: ['cyborg']
---

## cyborg

### cyborg 00 -> 01

#### Goal

The goal of this level is to log into the game.

#### Solution

sign up and get the creds.

```PowerShell
$ ssh cyborg1@cyborg.underthewire.tech:cyborg1

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg1\desktop>
```

### cyborg 01 -> 02

#### Goal

```txt
The password for cyborg2 is the state that the user Chris Rogers is from as stated within Active Directory.

NOTE:
- The password will be lowercase no matter how it appears on screen.
- "State" refers to the location within the country and NOT the "state" of the account (enabled/ disabled).

```

#### Solution

```PowerShell
PS C:\users\cyborg1\desktop> $users = Get-ADUser -Filter * -properties state
PS C:\users\cyborg1\desktop> $users | ? {$_.surname -eq "Rogers"} | ft name,state

name   state
----   -----
Rogers, Chris  kansas
PS C:\users\cyborg1\desktop> exit
Connection to cyborg.underthewire.tech closed.

$ ssh cyborg1@cyborg.underthewire.tech:kansas
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg2\desktop>  
```

### cyborg 02 -> 03

#### Goal

```txt
The password for cyborg3 is the host A record IP address for CYBORG718W100N PLUS the name of the file on the desktop.

NOTE:
- If the IP is "10.10.1.5" and the file on the desktop is called "_address", then the password is "10.10.1.5_address".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg2\desktop> $($(Resolve-DnsName CYBORG718W100N).IPAddress + $(ls).name)
172.31.45.167_ipv4  
PS C:\users\cyborg2\desktop> exit
Connection to cyborg.underthewire.tech closed.

$ ssh cyborg1@cyborg.underthewire.tech:172.31.45.167_ipv4
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg3\desktop> 
```

### cyborg 03 -> 04

#### Goal

```txt
The password for cyborg4 is the number of users in the Cyborg group within Active Directory PLUS the name of the file on the desktop.

NOTE:
- If the number of users is "20" and the file on the desktop is called "_users", then the password is "20_users".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg3\desktop> $("$((Get-ADGroup Cyborg | Get-ADGroupMember).count)" + $(ls).name)
88_objects
PS C:\users\cyborg3\desktop> exit
Connection to cyborg.underthewire.tech closed.  

$ ssh cyborg4@cyborg.underthewire.tech:88_objects
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg4\desktop>
```

### cyborg 04 -> 05

#### Goal

```txt
The password for cyborg5 is the PowerShell module name with a version number of 8.9.8.9 PLUS the name of the file on the desktop.

NOTE:
- If module name is "bob" and the file on the desktop is called "_settings", then the password is "bob_settings".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg4\desktop> $((Get-Module -ListAvailable | ? {$_.Version -eq "8.9.8.9"}).name + $(ls).name)
bacon_eggs
PS C:\users\cyborg4\desktop> exit
Connection to cyborg.underthewire.tech closed.

$ ssh cyborg5@cyborg.underthewire.tech:bacon_eggs

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg5\desktop> 
```

### cyborg 05 -> 06

#### Goal

```txt
The password for cyborg6 is the last name of the user who has logon hours set on their account PLUS the name of the file on the desktop.

NOTE:
- If the last name is "fields" and the file on the desktop is called "_address", then the password is "fields_address".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg5\desktop> $((Get-ADUser -filter * -Properties logonhours | ? {($null -ne $_.logonhours) -and ($null -ne $_.surname)}).surname + $(ls).name).ToLower()
rowray_timer
PS C:\users\cyborg5\desktop> exit
Connection to cyborg.underthewire.tech closed.

$ ssh cyborg6@cyborg.underthewire.tech:rowray_timer

Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg6\desktop>
```

### cyborg 06 -> 07

#### Goal

```txt
The password for cyborg7 is the decoded text of the string within the file on the desktop.

NOTE:
- The password is the last word of the string. For example, if it is "I like PowerShell", the password would be "powershell".
- The password will be lowercase no matter how it appears on screen.
- There are no spaces in the answer.
```

#### Solution

```PowerShell
PS C:\users\cyborg6\desktop> [System.Convert]::FromBase64String($(gc .\cypher.txt))
99 
0  
121
0  
98 
0  
101
0  
114
0  
103
0  
101
0  
100
0  
100
0  
111
0  
110
0  
PS C:\users\cyborg6\desktop> [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($(gc .\cypher.txt)))
cybergeddon
PS C:\users\cyborg6\desktop> exit

$ ssh cyborg7@cyborg.underthewire.tech:cybergeddon
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg7\desktop> 
```

### cyborg 07 -> 08

#### Goal

```txt
The password for cyborg8 is the executable name of a program that will start automatically when cyborg7 logs in.

NOTE:
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg7\desktop> $(gci HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\ | ? {$_.name -like '*run*'}).Property.ToLower()
skynet

$ ssh cyborg8@cyborg.underthewire.tech:skynet
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg8\desktop>
```

### cyborg 08 -> 09

#### Goal

```txt
The password for cyborg9 is the Internet zone that the picture on the desktop was downloaded from.

NOTE:
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/6e3f7352-d11c-4d76-8c39-2516a9df36e8

https://docs.microsoft.com/en-us/archive/blogs/askcore/alternate-data-streams-in-ntfs

```
0 My Computer
1 Local Intranet Zone
2 Trusted sites Zone
3 Internet Zone
4 Restricted Sites Zone
```

```PowerShell
PS C:\users\cyborg8\desktop> gi .\1_qs5nwlcl7f_-SwNlQvOrAw.png -Stream *


PSPath: Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png::$DATA
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop
PSChildName   : 1_qs5nwlcl7f_-SwNlQvOrAw.png::$DATA   
PSDrive       : C     
PSProvider    : Microsoft.PowerShell.Core\FileSystem  
PSIsContainer : False 
FileName      : C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png 
Stream: :$DATA
Length: 60113 

PSPath: Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\users\cyborg8\desktop
PSChildName   : 1_qs5nwlcl7f_-SwNlQvOrAw.png:Zone.Identifier  
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem  
PSIsContainer : False 
FileName      : C:\users\cyborg8\desktop\1_qs5nwlcl7f_-SwNlQvOrAw.png 
Stream        : Zone.Identifier
Length        : 26



PS C:\users\cyborg8\desktop> gc .\1_qs5nwlcl7f_-SwNlQvOrAw.png -Stream Zone.Identifier
[ZoneTransfer]
ZoneId=4
PS C:\users\cyborg8\desktop> exit
Connection to cyborg.underthewire.tech closed.

$ ssh cyborg8@cyborg.underthewire.tech:4
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg9\desktop> 
```

### cyborg 09 -> 10

#### Goal

```txt
The password for cyborg10 is the first name of the user with the phone number of 876-5309 listed in Active Directory PLUS the name of the file on the desktop.

NOTE:
- If the first name "chris" and the file on the desktop is called "23", then the password is "chris23".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg9\desktop> $($(Get-ADUser -Properties officephone -Filter * | ? {$_.officephone -eq "876-5309"}).GivenName + $(ls).name).ToLower()
onita99
PS C:\users\cyborg9\desktop> exit
Connection to cyborg.underthewire.tech closed.

$ ssh cyborg10@cyborg.underthewire.tech:onita99
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg10\desktop> 

```

### cyborg 10 -> 11

#### Goal

```txt
The password for cyborg11 is the description of the Applocker Executable deny policy for ill_be_back.exe PLUS the name of the file on the desktop.

NOTE:
- If the description is "green$" and the file on the desktop is called "28", then the password is "green$28".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg10\desktop> $($(Get-AppLockerPolicy -Effective).RuleCollections.Description + $(ls).name).ToLower()
terminated!99
PS C:\users\cyborg10\desktop> exit
Connection to cyborg.underthewire.tech clo

$ ssh cyborg11@cyborg.underthewire.tech:terminated!99
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg11\desktop> 
```

### cyborg 11 -> 12

#### Goal

```txt
The password for cyborg12 is located in the IIS log. The password is not Mozilla or Opera.

NOTE:
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg11\desktop> gc C:\inetpub\logs\logfiles\w3svc1\u_ex160413.log | sls pass

2016-04-13 04:14:12 W3SVC1 Century 172.31.45.65 GET / - 80 - 172.31.45.65 HTTP/1.1 LordHelmet/5.0+(CombTheDesert)+Password+is:spaceballs - - century.underthewire.tech 200 0 0 925 118 0 

PS C:\users\cyborg11\desktop> exit
Connection to cyborg.underthewire.tech closed.  

$ ssh cyborg12@cyborg.underthewire.tech:spaceballs
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg12\desktop> 

```

### cyborg 12 -> 13

#### Goal

```txt
The password for cyborg13 is the first four characters of the base64 encoded fullpath to the file that started the i_heart_robots service PLUS the name of the file on the desktop.

NOTE:
- An example of a fullpath would be 'c:\some_folder\test.exe'.
- Be sure to use 'UTF8' in your encoding.
- If the encoded base64 is "rwmed2fdreewrt34t" and the file on the desktop is called "_address", then the password is "rwme_address".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
PS C:\users\cyborg12\desktop> $((([Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($(Get-WmiObject win32_service | where {$_.Name -eq "i_heart_robots"}).PathName))[0..3]) -join "") + $(ls).name).ToLower()
yzpc_heart
PS C:\users\cyborg12\desktop> exit

$ ssh cyborg13@cyborg.underthewire.tech:QwA6_heart
Under the Wire... PowerShell Training for the People!
PS C:\users\cyborg13\desktop> 

```

### cyborg 13 -> 14

#### Goal

```txt
The password cyborg14 is the number of days the refresh interval is set to for DNS aging for the underthewire.tech zone PLUS the name of the file on the desktop.

NOTE:
- If the days is set to "08:00:00:00" and the file on the desktop is called "_tuesday", then the password is "8_tuesday".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
$($($(Get-DnsServerZoneAging -Name underthewire.tech).RefreshInterval).ToString().Split(".")[0] + $(ls).name)
22_days
```

### cyborg 14 -> 15

#### Goal

```txt
The password for cyborg15 is the caption for the DCOM application setting for application ID {59B8AFA0-229E-46D9-B980-DDA2C817EC7E} PLUS the name of the file on the desktop.

NOTE:
- If the caption is "dcom" and the file on the desktop is called "_address", then the password is "dcom_address".
- The password will be lowercase no matter how it appears on screen.
```

#### Solution

```PowerShell
$((Get-CimInstance -ClassName Win32_DCOMApplicationSetting -Property * | ? {$_.AppID -eq "{59B8AFA0-229E-46D9-B980-DDA2C817EC7E}"}).Caption + $(ls).name)
propshts_objects
```
