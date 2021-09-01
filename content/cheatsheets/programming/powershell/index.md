---
### The title for the content.
title : "PowerShell"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "powershell"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "PowerShell tips."
### The datetime assigned to this page.
date : 2020-03-10T16:33:40+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "powershell"
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
hidden : false
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
    tags: ['PowerShell']
---

## PowerShell

### Base64 Encode DLL

```powershell
$Path = "$PSScriptRoot\TotallyNotMalware.dll"
$bytes = [System.IO.File]::ReadAllBytes($Path)
$string = [System.Convert]::ToBase64String($bytes)
```

### Copy something to clipboard

```PowerShell
$string | Set-Clipboard
```

### Load Base64 Encoded DLL

```PowerShell
$dll = 'TVqQAAMAAAAEAAAA//8AALgAAAAA...'
$bytes = [System.Convert]::FromBase64String($dll)
[System.Reflection.Assembly]::Load($bytes)
```

### Easy way to create an object

```PowerShell
function Add2Obj {
    param (
        $FirstName,
        $LastName
    )
    return (New-Object psobject -Property @{FirstName=$FirstName;LastName=$LastName;})
}

$Names  = @()
$Names += Add2Obj -FirstName "Justin" -LastName "Perdok"

<#
PS> $Names

LastName FirstName
-------- ---------
Perdok   Justin
#>
```

### Search NETLOGON/SYSVOL for cpassword

```PowerShell
Get-ChildItem | Where-Object {$_.name -ne 'Policydefinitions'} | Get-ChildItem -Recurse -File | ForEach-Object {$_.fullname; Get-Content $_.fullname | Select-String cpassword}
```

#### Alternative

https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Get-GPPPassword.ps1

### Ensure PowerShell uses TLS1.2

```PowerShell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

### Ignore invalid certs

```PowerShell
add-type @"
    using System.Net;
    using System.Security.Cryptography.X509Certificates;
    public class TrustAllCertsPolicy : ICertificatePolicy {
        public bool CheckValidationResult(
            ServicePoint srvPoint, X509Certificate certificate,
            WebRequest request, int certificateProblem) {
            return true;
        }
    }
"@
[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy
```

### Also see

N/A