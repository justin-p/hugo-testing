---
title: "Remove_default_db"
date: 2020-03-06T11:13:07+01:00
draft: false
---

```powershell
Get-Mailbox –Database “Mailbox Database 0923333700”
Get-Mailbox –Database “Mailbox Database 0923333700” |New-MoveRequest –TargetDatabase “DAG”  -BatchName "DB01toDB02"

Get-Mailbox -Database “Mailbox Database 0923333700” | New-MoveRequest -TargetDatabase “DAG” -BatchName "DB01toDB02"

Get-Mailbox –Arbitration
Get-Mailbox –Arbitration | New-MoveRequest –TargetDatabase "TargetDatabaseName"
```
