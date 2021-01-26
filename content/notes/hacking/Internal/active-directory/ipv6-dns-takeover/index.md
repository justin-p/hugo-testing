---
### The title for the content.
title : "IPv6 DNS Takeover"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "ipv6 dns takeover"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "IPv6 DNS Takeover."
### The datetime assigned to this page.
date : 2020-03-10T16:43:46+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "ipv6-dns-takeover"
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

## IPv6 DNS Takeover

Windows prefers IPv6 over IPv4. This enables us to perform a DNS takeover using mitm6 if IPv6 is not already in use in the network. When this attack is performed, it is also possible to make computer accounts and users authenticate to us over HTTP by spoofing the WPAD location and requesting authentication to use our rogue proxy.

### Attacking

Combine with [mitm6](https://github.com/fox-it/mitm6) + [ntlmrelayx](https://github.com/SecureAuthCorp/impacket) + ([getSP.py](https://github.com/SecureAuthCorp/impacket) + ) [secretsdump.py](https://github.com/SecureAuthCorp/impacket)

### Defense

#### Mitigating mitm6

mitm6 abuses the fact that Windows queries for an IPv6 address even in IPv4-only environments. If you don't use IPv6 internally, the safest way to prevent mitm6 is to block DHCPv6 traffic and incoming router advertisements in Windows Firewall via Group Policy. Disabling IPv6 entirely may have unwanted side effects. Setting the following predefined rules to Block instead of Allow prevents the attack from working:

- (Inbound) Core Networking - Dynamic Host Configuration Protocol for IPv6(DHCPV6-In)
- (Inbound) Core Networking - Router Advertisement (ICMPv6-In)
- (Outbound) Core Networking - Dynamic Host Configuration Protocol for IPv6(DHCPV6-Out)

#### Mitigating WPAD abuse

If WPAD is not in use internally, disable it via Group Policy and by disabling the WinHttpAutoProxySvc service.

#### Mitigating relaying to LDAP

Relaying to LDAP and LDAPS can only be mitigated by enabling both LDAP signing and [LDAP channel binding.](https://support.microsoft.com/en-us/help/4034879/how-to-add-the-ldapenforcechannelbinding-registry-entry)

#### Protected users

Consider adding Administrative users to the Protected Users group or marking them as 'Account is sensitive and cannot be delegated', which will prevent any impersonation of that user via delegation.
