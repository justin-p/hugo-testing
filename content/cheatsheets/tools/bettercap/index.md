---
### The title for the content.
title: "bettercap"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "bettercap"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "The Swiss Army knife for WiFi, Bluetooth Low Energy, wireless HID hijacking and IPv4 and IPv6 networks reconnaissance and MITM attacks."
### The datetime assigned to this page.
date: 2021-02-04T15:21:13+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "bettercap"
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

## Bettercap

### Installation

```bash
sudo apt update
sudo apt install golang git build-essential libpcap-dev libusb-1.0-0-dev libnetfilter-queue-dev

go get github.com/bettercap/bettercap
cd $GOPATH/src/github.com/bettercap/bettercap
make build
sudo make install
```

### Usage

```bash
Usage of /home/justin-p/go/bin/bettercap:
  -autostart string
        Comma separated list of modules to auto start. (default "events.stream")
  -caplet string
        Read commands from this file and execute them in the interactive session.
  -cpu-profile file
        Write cpu profile file.
  -debug
        Print debug messages.
  -env-file string
        Load environment variables from this file if found, set to empty to disable environment persistence.
  -eval string
        Run one or more commands separated by ; in the interactive session, used to set variables via command line.
  -gateway-override string
        Use the provided IP address instead of the default gateway. If not specified or invalid, the default gateway will be used.
  -iface string
        Network interface to bind to, if empty the default interface will be auto selected.
  -mem-profile file
        Write memory profile to file.
  -no-colors
        Disable output color effects.
  -no-history
        Disable interactive session history file.
  -silent
        Suppress all logs which are not errors.
  -version
        Print the version and exit.
```

### Examples

#### start and shutdown

```bash
# Before starting
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode monitor
sudo systemctl stop wpa_supplicant
sudo systemctl stop NetworkManager.service

# Start
sudo ~/go/bin/bettercap -iface eth0 -eval "set wifi.interface wlan0; wifi.recon on"

# After bettercap
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode managed
sudo systemctl restart wpa_supplicant
sudo systemctl restart NetworkManager.service
```

### WIFI Commands

#### `wifi.recon on`

Start 802.11 wireless base stations discovery and handshakes/PMKID capture.

#### `wifi.recon off`

Stop 802.11 wireless base stations discovery.

#### `wifi.clear`

Clear all access points collected by the WiFi discovery module.

#### `wifi.recon BSSID`

Set 802.11 base station address to filter for.

#### `wifi.recon clear`

Remove the 802.11 base station filter.

#### `wifi.assoc BSSID`

Send an association request to the selected BSSID in order to [receive a RSN PMKID](https://hashcat.net/forum/thread-7717.html) key (use `all`, `*` or `ff:ff:ff:ff:ff:ff` to iterate for every access point).

#### `wifi.deauth BSSID`

Start a 802.11 deauth attack, if an access point BSSID is provided, every client will be deauthenticated, otherwise only the selected client (**use `all`, `*` or `ff:ff:ff:ff:ff:ff` to deauth everything**).

#### `wifi.show`

Show current wireless stations list (default sorting by RSSI).

#### `wifi.show.wps BSSID`

Show WPS information about a given station (use `all`, `*` or `ff:ff:ff:ff:ff:ff` to select all).

#### `wifi.recon.channel CHANNEL`

Comma separated list of channels to hop on.

#### `wifi.recon.channel clear`

Enable channel hopping on all supported channels.

#### `wifi.ap`

Inject fake management beacons in order to create a rogue access point ( requires `wifi.recon` to run ).

#### Parameters

| parameter                | default                            | description                                                                                                                                                                                     |
| ------------------------ | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wifi.interface`         |                                    | If filled, the module will use this interface instead of the one provided by the `-iface` argument or detected automatically.                                                                   |
| `wifi.region`            | `BO`                               | Set the WiFi region to this value before activating the interface.                                                                                                                              |
| `wifi.txpower`           | `30`                               | Set WiFi transmission power to this value before activating the interface.                                                                                                                      |
| `wifi.rssi.min`          | `-200`                             | Minimum WiFi signal strength in dBm.                                                                                                                                                            |
| `wifi.show.manufacturer` | `false`                            | If true, wifi.show will also show the devices manufacturers.                                                                                                                                    |
| `wifi.show.filter`       |                                    | Defines a regular expression filter for `wifi.show`.                                                                                                                                            |
| `wifi.show.sort`         | `rssi asc`                         | Defines sorting field (`rssi`, `bssid`, `essid`, `channel`, `encryption`, `clients`, `seen`, `sent`, `rcvd`) and direction (`asc` or `desc`) for `wifi.show`.                                   |
| `wifi.show.sort`         | `asc`                              | Defines sorting direction for `wifi.show`.                                                                                                                                                      |
| `wifi.show.limit`        | `0`                                | If greater than zero, defines limit for `wifi.show`.                                                                                                                                            |
| `wifi.hop.period`        | `250`                              | If channel hopping is enabled (empty `wifi.recon.channel`), this is the time in millseconds the algorithm will hop on every channel (it'll be doubled if both 2.4 and 5.0 bands are available). |
| `wifi.handshakes.file`   | `~/bettercap-wifi-handshakes.pcap` | File path of the pcap file to save handshakes to.                                                                                                                                               |
| `wifi.source.file`       |                                    | If set, the wifi module will read from this pcap file instead of the hardware interface.                                                                                                        |
| `wifi.skip-broken`       | `true`                             | If true, dot11 packets with an invalid checksum will be skipped.                                                                                                                                |
| `wifi.assoc.skip`        |                                    | Comma separated list of BSSID to skip while sending association requests.                                                                                                                       |
| `wifi.assoc.silent`      | `false`                            | If true, messages from wifi.assoc will be suppressed.                                                                                                                                           |
| `wifi.assoc.open`        | `false`                            | Send association requests to open networks.                                                                                                                                                     |
| `wifi.deauth.skip`       |                                    | Comma separated list of BSSID to skip while sending deauth packets.                                                                                                                             |
| `wifi.deauth.silent`     | `false`                            | If true, messages from `wifi.deauth` will be suppressed.                                                                                                                                        |
| `wifi.deauth.open`       | `true`                             | Send wifi deauth packets to open networks.                                                                                                                                                      |
| `wifi.ap.ssid`           | `FreeWifi`                         | SSID of the fake access point.                                                                                                                                                                  |
| `wifi.ap.bssid`          | `<random mac>`                     | BSSID of the fake access point.                                                                                                                                                                 |
| `wifi.ap.channel`        | `1`                                | Channel of the fake access point.                                                                                                                                                               |
| `wifi.ap.encryption`     | `true`                             | If true, the fake access point will use WPA2, otherwise it'll result as an open AP.                                                                                                             |

##### Examples

Run bettercap using `eth0` as the main interface but start the wifi module on `wlan0` instead:

```sh
sudo bettercap -iface eth0 -eval "set wifi.interface wlan0; wifi.recon on"
```

Keep deauthing clients from the access point with BSSID `DE:AD:BE:EF:DE:AD` every five seconds:

```
> set ticker.period 5; set ticker.commands "wifi.deauth DE:AD:BE:EF:DE:AD"; ticker on
```

Use the [ticker](/modules/core/ticker/) and `wifi.recon` modules to create a WiFi scanner (performing channel hopping on every supported frequency):

```
> set ticker.commands "clear; wifi.show"; wifi.recon on; ticker on
```

Sort by BSSID and filter for BSSIDs starting with `F4`:

```
> set wifi.show.sort bssid asc
> set wifi.show.filter ^F4
> wifi.show
```

Only recon on channels 1, 2 and 3:

```
> wifi.recon.channel 1,2,3; wifi.recon on
```

Will send management beacons as the fake access point "Banana" with BSSID `DE:AD:BE:EF:DE:AD` on channel 5 without encryption:

```
> set wifi.ap.ssid Banana
> set wifi.ap.bssid DE:AD:BE:EF:DE:AD
> set wifi.ap.channel 5
> set wifi.ap.encryption false
> wifi.recon on; wifi.ap
```

### Also see

[Bettercap wiki](https://www.bettercap.org/)
