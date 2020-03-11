---
title: "Legacy"
description: "Notes from the Legacy machine on HTB."

date: 2020-03-06T13:18:23+01:00
draft: false
weight: 700
---

### where you at

10.10.10.4

### what you got

```bash
# Nmap 7.80 scan initiated Thu Jan 23 14:44:54 2020 as: nmap -oX - -A -T4 -p- -oN /mnt/hgfs/_shared_folder/htb/boxes/legacy/scans/full_tcp.nmap -oG /mnt/hgfs/_shared_folder/htb/boxes/legacy/scans/full_tcp.gnmap 10.10.10.4
Nmap scan report for 10.10.10.4
Host is up (0.020s latency).
Not shown: 65532 filtered ports
PORT     STATE  SERVICE       VERSION
139/tcp  open   netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open   microsoft-ds  Windows XP microsoft-ds
3389/tcp closed ms-wbt-server
Device type: general purpose|specialized
Running (JUST GUESSING): Microsoft Windows XP|2003|2000|2008 (94%), General Dynamics embedded (87%)
OS CPE: cpe:/o:microsoft:windows_xp::sp3 cpe:/o:microsoft:windows_server_2003::sp1 cpe:/o:microsoft:windows_server_2003::sp2 cpe:/o:microsoft:windows_2000::sp4 cpe:/o:microsoft:windows_server_2008::sp2
Aggressive OS guesses: Microsoft Windows XP SP3 (94%), Microsoft Windows Server 2003 SP1 or SP2 (92%), Microsoft Windows XP (92%), Microsoft Windows Server 2003 SP2 (91%), Microsoft Windows 2003 SP2 (90%), Microsoft Windows XP SP2 or Windows Server 2003 (90%), Microsoft Windows 2000 SP4 (90%), Microsoft Windows XP SP2 or SP3 (90%), Microsoft Windows XP SP2 or Windows Small Business Server 2003 (90%), Microsoft Windows 2000 SP4 or Windows XP SP2 or SP3 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

Host script results:
|_clock-skew: mean: 5d00h58m20s, deviation: 1h24m51s, median: 4d23h58m20s
|_nbstat: NetBIOS name: LEGACY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:3e:dd (VMware)
| smb-os-discovery:
|   OS: Windows XP (Windows 2000 LAN Manager)
|   OS CPE: cpe:/o:microsoft:windows_xp::-
|   Computer name: legacy
|   NetBIOS computer name: LEGACY\x00
|   Workgroup: HTB\x00
|_  System time: 2020-01-28T17:44:54+02:00
| smb-security-mode:
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)

TRACEROUTE (using port 3389/tcp)
HOP RTT      ADDRESS
1   19.92 ms 10.10.14.1
2   19.82 ms 10.10.10.4

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jan 23 14:47:24 2020 -- 1 IP address (1 host up) scanned in 150.89 seconds
```

### Exploit

#### SMB

`ms08_067_netapi`
