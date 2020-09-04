---
### The title for the content.
title : "steal access tokens"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "sql injection"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "steal access tokens."
### The datetime assigned to this page.
date : 2020-03-10T16:43:45+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "sql-injection"
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

## steal access tokens

### GCP

Google JSON TOkens and credentials.db are saved to disk. 

JSON tokens are typically used for service account access to GCP. They can be used to authenticate with gcloud and/or ScouteSuite.

if a user authenticates with gcloud from a compute instance their creds are stored here: ~/.config/gcloud/credentials.db

`sudo find /home -name "credentials.db"`

### Azure

#### Azure Cloud Service Packages (.cspkg)

cspkg are deployment files created by Visual Studio. They offer possiablty to in intergrate to azure services such as SQL, Storage, etc.
These files use the zip file format. Look in these files for creds/certificates. They can be found in `<cloud project dir>\bin\debug\publish`

#### Azure Publish Settings files (.publishsettings)

Designed to make pushing code to azure easier. Search for these files in the Downloads folder or the VS projects folder.

They contain a Base64 encoded management certifiacte and sometimes clear test credentials.  Just open these files in a text editor and search them. To save the cert, save the cert copy the base64 encoded data and save it as a pfx file.

![Save the cert](images/management_cert.png)

#### Extract keys from storage explorers

Developers often use storage explorers to easily upload and download files to Azure. It may be possiable to extract storange credentials from these tools. Storage Explorers store credentials on disk (Windows Credential Manager) and use them to authenticate to services such as Azure. There are a number of different storage explorers that change frequently.  

Azure Storage Explorer has a built-in "Developer Tool" that allows you to set breakpoints while loading credentials allowing you to view them unencrypted.

#### web.config and app.config files

WebApps often need read/write access to cloud storage or DBs. These credentials can be saved in a web.config or app.config file.
Look for credentials or management certs (which can be saved to a PFX file). These files can often be found at the root folder of a WebApp.

#### Azure tools

When authenticating to Azure with something like the Az PowerShell module a file named TokenCache.dat is saved in `%USERPROFILE%\.azure\`. This file can be combined with the 'AzureRmContext.json' file, creating the equivalent of the output from the Save-AzContext command. Use [AzStealContext](https://github.com/justin-p/AzStealContext) to abuse this.

### Command history

May contain creds or tokens or other commands indicating where to look.

`~/.bash_history`
`%USERPROFILE%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`

### Internal Code Repositores

G O L D  M I N E for keys.

Find internal repos

- portscanning webservices and then using something like EyeWitmess to screenshot each result.
- Query AD for all hostnames, look for subdomains such as git, code, repo, bitbucket, gitlab, etc.

If you find these (and have access to repos) you can use automated tools (gitleak, trufflehog, gitrob) or use the built-in search features.

Search for string such as:

- AccessKey
- AKIA
- id_rsa
- credentials
- secret
- password
- token
