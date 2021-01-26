---
### The title for the content.
title : "showmount"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "finger"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "showmount"
### The datetime assigned to this page.
date : 2020-03-10T16:43:45+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "finger"
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

## showmount
Usefull when nfs is open.

```bash
111/tcp   open  rpcbind    2-4 (RPC #100000)
| rpcinfo:                
|   program version    port/proto  service                   
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind                   
|   100000  3,4          111/tcp6  rpcbind  
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs      
|   100003  2,3,4       2049/tcp6  nfs      
|   100003  2,3,4       2049/udp   nfs      
|   100003  2,3,4       2049/udp6  nfs      
|   100005  1,2,3      40412/udp   mountd
|   100005  1,2,3      51233/tcp6  mountd
|   100005  1,2,3      57722/tcp   mountd
|   100005  1,2,3      59004/udp6  mountd                        
|   100021  1,3,4      37539/tcp6  nlockmgr
|   100021  1,3,4      42654/udp   nlockmgr
|   100021  1,3,4      49656/udp6  nlockmgr                           
|   100021  1,3,4      54775/tcp   nlockmgr
|   100024  1          38568/tcp   status
|   100024  1          50138/udp   status        
|   100024  1          54698/udp6  status
|   100024  1          57281/tcp6  status
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl 
2049/tcp  open  nfs_acl    2-3 (RPC #100227)
```

```bash
showmount -e host
```