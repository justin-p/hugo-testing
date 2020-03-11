---
title: "steganography"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
tags: ['Steganography']
---

| tools    | |
|----------|-|
| steghide | |
| binwalk  | |
| foremost | |

### NTFS Alternate Data Streams

[info](https://www.secjuice.com/ntfs-steganography-hiding-in-plain-sight/)

| tool       | commands |
|------------|----------|
| cmd        | `dir /r` |
| powershell | `gci -recurse | % { gi $_.FullName -stream * } | where stream -ne ':$Data' | select filename,stream,@{'name'='identifier';"e"={"$($_.filename)$($_.stream)"}}` |

### Also see

https://0xrick.github.io/lists/stego/