---
### The title for the content.
title : "hcxtools"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "hcxtools"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Portable solution for conversion of cap/pcap/pcapng (gz compressed) WiFi dump files to hashcat/john formats."
### The datetime assigned to this page.
date : 2021-09-02T20:17:35+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "hcxtools"
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
tags : ["Tools","password-cracking"]
---

## hcxtools

### Installation

```bash
git clone https://github.com/ZerBea/hcxtools
cd hcxtools
sudo apt install libpcap-dev libcurl4-openssl-dev libssl-dev
make
sudo make install
```

### Usage

```bash
./hcxpcapngtool [OPTIONS]
```

### Flags

```bash
short options:
-o <file> : output WPA-PBKDF2-PMKID+EAPOL hash file (hashcat -m 22000)
            get full advantage of reuse of PBKDF2 on PMKID and EAPOL
-E <file> : output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
            retrieved from every frame that contain an ESSID
-R <file> : output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
            retrieved from PROBEREQUEST frames only
-I <file> : output unsorted identity list to use as input wordlist for cracker
-U <file> : output unsorted username list to use as input wordlist for cracker
-D <file> : output device information list
            format MAC MANUFACTURER MODELNAME SERIALNUMBER DEVICENAME
-h        : show this help
-v        : show version

long options:
--all                              : convert all possible hashes instead of only the best one
                                     that can lead to much overhead hashes
                                     use hcxhashtool to filter hashes
                                     need hashcat --nonce-error-corrections >= 8
--eapoltimeout=<digit>             : set EAPOL TIMEOUT (milliseconds)
                                   : default: 5000 ms
--nonce-error-corrections=<digit>  : set nonce error correction
                                     warning: values > 0 can lead to uncrackable handshakes
                                   : default: 0
--ignore-ie                        : do not use CIPHER and AKM information
                                     this will convert all frames regadless of
                                     CIPHER and/OR AKM information,
                                     and can lead to uncrackable hashes
--max-essids=<digit>               : maximum allowed ESSIDs
                                     default: 1 ESSID
                                     disregard ESSID changes and take ESSID with highest ranking
--eapmd5=<file>                    : output EAP MD5 CHALLENGE (hashcat -m 4800)
--eapmd5-john=<file>               : output EAP MD5 CHALLENGE (john chap)
--eapleap=<file>                   : output EAP LEAP and MSCHAPV2 CHALLENGE (hashcat -m 5500, john netntlm)
--tacacs-plus=<file>               : output TACACS PLUS (hashcat -m 16100, john tacacs-plus)
--nmea=<file>                      : output GPS data in NMEA format
                                     format: NMEA 0183 $GPGGA, $GPRMC, $GPWPL
                                     to convert it to gpx, use GPSBabel:
                                     gpsbabel -i nmea -f hcxdumptool.nmea -o gpx,gpxver=1.1 -F hcxdumptool.gpx
                                     to display the track, open file.gpx with viking
--csv=<file>                       : output ACCESS POINT information in CSV format
                                     delimiter: tabulator (0x08)
                                     columns:
                                     YYYY-MM-DD HH:MM:SS MAC_AP ESSID ENC_TYPE CIPHER AKM COUNTRY_INFO CHANNEL RSSI GPS(DM.m) GPS(D.d) GPSFIX SATCOUNT HDOP ALTITUDE UNIT
                                     to convert it to other formats, use bash tools or scripting languages
                                     GPS FIX:
                                     0 = fix not available or invalid
                                     1 = fix valid (GPS SPS mode)
                                     2 = fix valid (differential GPS SPS Mode)
                                     3 = not supported
                                     4 = not supported
                                     5 = not supported
                                     6 = fix valid (Dead Reckoning Mode)
--log=<file>                       : output logfile
--raw-out=<file>                   : output frames in HEX ASCII
                                   : format: TIMESTAMP*LINKTYPE*FRAME*CHECKSUM
--raw-in=<file>                    : input frames in HEX ASCII
                                   : format: TIMESTAMP*LINKTYPE*FRAME*CHECKSUM
--pmkid=<file>                     : output deprecated PMKID file (delimter *)
--hccapx=<file>                    : output deprecated hccapx v4 file
--hccap=<file>                     : output deprecated hccap file
--john=<file>                      : output deprecated PMKID/EAPOL (JtR wpapsk-opencl/wpapsk-pmk-opencl)
--prefix=<file>                    : convert everything to lists using this prefix (overrides single options):
                                      -o <file.22000>           : output PMKID/EAPOL hash file
                                      -E <file.essid>           : output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
                                      -I <file.identitiy>       : output unsorted identity list to use as input wordlist for cracker
                                      -U <file.username>        : output unsorted username list to use as input wordlist for cracker
                                     --eapmd5=<file.4800>       : output EAP MD5 CHALLENGE (hashcat -m 4800)
                                     --eapleap=<file.5500>      : output EAP LEAP and MSCHAPV2 CHALLENGE (hashcat -m 5500, john netntlm)
                                     --tacacs-plus=<file.16100> : output TACACS+ (hashcat -m 16100, john tacacs-plus)
                                     --nmea=<file.nmea>         : output GPS data in NMEA format
--help                             : show this help
--version                          : show version

bitmask for message pair field:
bit 0-2
 000 = M1+M2, EAPOL from M2 (challenge)
 001 = M1+M4, EAPOL from M4 if not zeroed (authorized)
 010 = M2+M3, EAPOL from M2 (authorized)
 011 = M2+M3, EAPOL from M3 (authorized) - unused
 100 = M3+M4, EAPOL from M3 (authorized) - unused
 101 = M3+M4, EAPOL from M4 if not zeroed (authorized)
3: reserved
4: ap-less attack (set to 1) - no nonce-error-corrections necessary
5: LE router detected (set to 1) - nonce-error-corrections only for LE necessary
6: BE router detected (set to 1) - nonce-error-corrections only for BE necessary
7: not replaycount checked (set to 1) - replaycount not checked, nonce-error-corrections definitely necessary
```

### Examples

```bash
./hcxpcapngtool -o output pwnagotchi.pcap 
```

### Related pages

{{< related_pages_table tag="password-cracking" >}}

### Also see

[Github Project](https://github.com/ZerBea/hcxtools)