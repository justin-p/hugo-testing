---
title: "Payloads"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---

## Non-staged

- Sends exploit shellcode all at once  
- Larger in size and won't always work

```bash
windows/meterpreter_reverse_tcp
                   ^
```

## Staged

- Sends payload in stages  
- Can be less stable

```bash
windows/meterpreter/reverse_tcp
                   ^
```
