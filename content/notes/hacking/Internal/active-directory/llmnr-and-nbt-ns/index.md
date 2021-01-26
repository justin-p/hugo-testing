---
### The title for the content.
title : "LLMNR and NBT-NS"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "llmnr_nbt ns"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "LLMNR and NBT-NS."
### The datetime assigned to this page.
date : 2020-03-10T16:43:45+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "llmnr_nbt-ns"
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

## LLMNR and NBT-NS

By default when a DNS lookup fails windows tries to use 2 other components as a fallback. Link-Local Multicast Name Resolution (LLMNR) and Netbios Name Service (NBT-NS). LLLMNR was introduced in Windows Vista and is the successor to NBT-NS.

These protocols help machines on the network identify hosts when DNS fails. So if one machine tries to resolve a particular host, but DNS resolution fails, the machine will then attempt to ask all other machines on the local network for the correct address via LLMNR or NBT-NS.

An attacker can listen on a network for these LLMNR (UDP/5355) or NBT-NS (UDP/137) broadcasts and respond to them, thus pretending that the attacker knows the location of the requested host.  

![example of LLMNR Poisoning](stern-llmnr_poison1.jpg)

### Attacking

[responder](https://github.com/lgandx/Responder) + [ntlmrelayx](https://github.com/SecureAuthCorp/impacket)

### Defence

1. Disable LLMNR and NBT-NS
2. Enable Network Access Control
3. Strong password policy (e.g., 14 characters and limit common word usage)

#### LLMNR GPO

`Computer Configuration -> Administrative Templates -> Network -> DNS Client -> Turn Off Multicast Name Resolution -> Enabled`

#### NBT-NS GPO (startup script)

```powershell
$regkey = "HKLM:SYSTEM\CurrentControlSet\services\NetBT\Parameters\Interfaces"
Get-ChildItem $regkey | ForEach { 
    Set-ItemProperty -Path "$regkey\$($_.pschildname)" -Name NetbiosOptions -Value 2 -Verbose
}
```
