---
### The title for the content.
title : "encrypted password protected pdf"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "encrypted password protected pdf"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "encrypted password protected pdf description."
### The datetime assigned to this page.
date : 2020-03-10T16:43:47+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "encrypted-password-protected-pdf"
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

## encrypted password protected pdf


[source](https://blog.didierstevens.com/2017/12/26/cracking-encrypted-pdfs-part-1/)

## pdfid

check if pdf is encrypted (/Encrypt)

```
root@kali:/mnt/hgfs/_shared_folder# pdfid -n "0ld is g0ld.pdf" 
PDFiD 0.2.7 0ld is g0ld.pdf
 PDF Header: %PDF-1.6
 obj                   15
 endobj                15
 stream                 5
 endstream              5
 xref                   2
 trailer                2
 startxref              2
 /Page                  1
 /Encrypt               2
 /ObjStm                1
```

## pdf-parser

Where is /Encrypt (object 43)

```
root@kali:/mnt/hgfs/_shared_folder# pdf-parser -s /Encrypt "0ld is g0ld.pdf" 
trailer
  <<
    /Size 45
    /Root 1 0 R
    /Info 10 0 R
    /ID [<5C8F37D2A45EB64E9DBBF71CA3E86861><5C8F37D2A45EB64E9DBBF71CA3E86861>]
    /Encrypt 43 0 R
  >>

trailer
  <<
    /Size 45
    /Root 1 0 R
    /Info 10 0 R
    /ID [<5C8F37D2A45EB64E9DBBF71CA3E86861><5C8F37D2A45EB64E9DBBF71CA3E86861>]
    /Encrypt 43 0 R
    /Prev 196676
    /XRefStm 196344
  >>
```

show object 43

```
root@kali:/mnt/hgfs/_shared_folder# pdf-parser -o 43 "0ld is g0ld.pdf" 
obj 43 0
 Type: 
 Referencing: 

  <<
    /CF
      <<
        /StdCF
          <<
            /AuthEvent /DocOpen
            /CFM /AESV2
            /Length 16
          >>
      >>
    /Filter /Standard
    /Length 128
    /O <702CC7CED92B595274B7918DCB6DC74BEDEF6EF851B4B4B5B8C88732BA4DAC0C>
    /P -1060
    /R 4
    /StmF /StdCF
    /StrF /StdCF
    /U <9CBA5CFB1C536F1384BBA7458AAE3F8100000000000000000000000000000000>
    /V 4
  >>
```

Uses `RC4 128-bit` `/Filter /Standard /Length 128`

## qpdf

check if its a user or system password.

```
root@kali:/mnt/hgfs/_shared_folder# qpdf --show-encryption "0ld is g0ld.pdf"
0ld is g0ld.pdf: invalid password
```

## pdf2john

Get password hash from pdf

```
root@kali:/mnt/hgfs/_shared_folder# /usr/share/john/pdf2john.pl "0ld is g0ld.pdf" 
0ld is g0ld.pdf:$pdf$4*4*128*-1060*1*16*5c8f37d2a45eb64e9dbbf71ca3e86861*32*9cba5cfb1c536f1384bba7458aae3f8100000000000000000000000000000000*32*702cc7ced92b595274b7918dcb6dc74bedef6ef851b4b4b5b8c88732ba4dac0c
```

### hashcat format

hashcat just needs the hash, not the pdf name.

```
root@kali:/mnt/hgfs/_shared_folder# /usr/share/john/pdf2john.pl "0ld is g0ld.pdf" | cut -d : -f 2
$pdf$4*4*128*-1060*1*16*5c8f37d2a45eb64e9dbbf71ca3e86861*32*9cba5cfb1c536f1384bba7458aae3f8100000000000000000000000000000000*32*702cc7ced92b595274b7918dcb6dc74bedef6ef851b4b4b5b8c88732ba4dac0c
```


see hashcat for examplesto crack