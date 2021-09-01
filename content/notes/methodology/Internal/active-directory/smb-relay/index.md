---
### The title for the content.
title : "SMB Relay"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "smb relay"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "SMB Relay."
### The datetime assigned to this page.
date : 2020-03-10T16:43:46+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "smb-relay"
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

## SMB Relay

Use a captures hash to authenticated against a PC.

1. SMB signing has to be disabled. (nmap --script smb2-security-mode.nse -p 445 CIDR/HOST)
2. User credentials must have remote login access

### Attacking

Setup responder to not start a SMB and HTTP server. (vim /usr/share/responder/Responder.conf)

[responder](https://github.com/lgandx/Responder) + [ntlmrelayx](https://github.com/SecureAuthCorp/impacket)

### Defences

1. Enable SMB signing
   - pro: fixes attack
   - con: may cause slow down with file copies
2. Disable NTLM auth.
   - pro: fixes attack
   - con: if kerberos goes down windows falls back to NTLM
3. Account tiering.
    - Pro: Limits domain admins to specific task, setup multiple tiered accounts. (only login into servers with need of DA).
    - Con: may be difficult to implement/enforce.
4. Restrict local admin access.
    - Pro: Can prevent a lot of lateral movement
    - Con: May increase load on SD/IT admins.

#### SMB signing GPO

`Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options`

##### Servers

Microsoft network server: Digitally sign communications (always) -> Enabled

If SMBv1 is needed: Microsoft network server: Digitally sign communications (if client agrees) -> Enabled

#### Clients

Microsoft network client: Digitally sign communications (always) -> Enabled

If SMBv1 is needed: Microsoft network client: Digitally sign communications (if server agrees) -> Enabled

### Restrict/Deny NTLM in Active Directory

`Computer Configurations -> Policies -> Windows Settings -> Security Settings -> Local Policies -> Security Options -> Network Security: Restrict NTLM: NTLM authentication in this domain`

`Deny all`

### Account tiering

See [this](https://www.petri.com/use-microsofts-active-directory-tier-administrative-model) and [this](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material)

### Restrict local admin access

[Try looking into LAPS.](https://blog.stealthbits.com/running-laps-in-the-race-to-security/)