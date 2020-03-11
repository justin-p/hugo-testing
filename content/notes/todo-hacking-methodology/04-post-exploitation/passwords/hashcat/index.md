---
### The title for the content.
title : "hashcat"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "hashcat"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "hashcat description."
### The datetime assigned to this page.
date : 2020-03-10T16:43:46+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "hashcat"
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

## hashcat


## basic wordlist

Attack NTLM hashes using wordlist, enable custom kernels (limits lenght of pass to 27, better speed), use workload 3 and save in cracked_hashes

```
hashcat -a 0 -m 1000 -O -w 3 hashfile wordlist -o cracked_hashes
```

## wordlist + rulelist

```
hashcat -a 0 -m 1000 -O -w 3 hashfile wordlist -o cracked_hashes -r rule
```

### one-rule-to-rule-them-all

https://www.notsosecure.com/one-rule-to-rule-them-all/  
https://github.com/NotSoSecure/password_cracking_rules  

## bruteforcing 

```
predefined charsets
?l = abcdefghijklmnopqrstuvwxyz
?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
?d = 0123456789
?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
?a = ?l?u?d?s
?b = 0x00 - 0xff
```

?l?d?u is the same as:  
?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789  
  
### Brute force all passwords length 1-8 with possible characters A-Z a-z 0-9   

`hashcat64 -m 500 hashes.txt -a  3  ?1?1?1?1?1?1?1?1 --increment -1 ?l?d?u`  

## username:hash format

hashfile

```
user:b4b9b02e6f09a9bd760f388b67351e2b
```

command

```
hashcat64.exe -a 0 -m 1000 -O hashfile wordlist -o cracked_hashes --username
```

### show username:hash:password

ones cracked use --show --username to show username:hash:password (it uses the potfile for this).

```
hashcat -m 1000 hashfile --show --username

user:b4b9b02e6f09a9bd760f388b67351e2b:hashcat
```

### output username:hash:password

output to file in format

```
hashcat -m 1000 hashfile --show --username -o user_hash_pass

user:b4b9b02e6f09a9bd760f388b67351e2b:hashcat
```

## [PRINCE Password Generation](https://github.com/hashcat/princeprocessor)

PRINCE (PRobability INfinite Chained Elements) is a hashcat utility for randomly generating probable passwords:

```
pp64.bin --pw-min=8 < dict.txt | head -20 shuf dict.txt | pp64.bin --pw-min=8 | head -20
```

## [Purple Rain](https://www.netmux.com/blog/purple-rain-attack)

Purple Rain attack uses a combination of Prince, a dictionary and random Mutation rules to dynamicaly create infinite combinations of passwords.

```
shuf dict.txt | pp64.bin --pw-min=8 | hashcat -a 0 -m 1000 -w 3 -O hashes.txt -g 300000
```
