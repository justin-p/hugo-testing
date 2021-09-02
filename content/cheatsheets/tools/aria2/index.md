---
### The title for the content.
title : "aria2"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "aria2"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "aria2 description."
### The datetime assigned to this page.
date : 2021-09-02T20:40:45+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "aria2"
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

## aria2

### Installation

```bash
apt install aria2
```

### Usage

```bash
aria2c [OPTIONS] [URI | MAGNET | TORRENT_FILE | METALINK_FILE]...
```

### Flags

```bash
-v, --version                Print the version number and exit.
                             Tags: #basic
-h, --help[=TAG|KEYWORD]     Print usage and exit.
                             The help messages are classified with tags. A tag
                             starts with "#". For example, type "--help=#http"
                             to get the usage for the options tagged with
                             "#http". If non-tag word is given, print the usage
                             for the options whose name includes that word.
                             Possible Values: #basic, #advanced, #http, #https, #ftp, #metalink, #bittorrent, #cookie, #hook, file, #rpc, #checksum, #experimental, #deprecated, #help, #all
                             Default: #basic
                             Tags: #basic, #help
-l, --log=LOG                The file name of the log file. If '-' is
                             specified, log is written to stdout.
                             Possible Values: /path/to/file, -
                             Tags: #basic
-d, --dir=DIR                The directory to store the downloaded file.
                             Possible Values: /path/to/directory
                             Default: /root/
                             Tags: #basic, #file
-o, --out=FILE               The file name of the downloaded file. It is
                             always relative to the directory given in -d
                             option. When the -Z option is used, this option
                             will be ignored.
                             Possible Values: /path/to/file
                             Tags: #basic, #http, #ftp, #file
-s, --split=N                Download a file using N connections. If more
                             than N URIs are given, first N URIs are used and
                             remaining URLs are used for backup. If less than
                             N URIs are given, those URLs are used more than
                             once so that N connections total are made
                             simultaneously. The number of connections to the
                             same host is restricted by the 
                             --max-connection-per-server option. See also the
                             --min-split-size option.
                             Possible Values: 1-*
                             Default: 5
                             Tags: #basic, #http, #ftp
--file-allocation=METHOD     Specify file allocation method.
                             'none' doesn't pre-allocate file space. 'prealloc'
                             pre-allocates file space before download begins.
                             This may take some time depending on the size of
                             the file.
                             If you are using newer file systems such as ext4
                             (with extents support), btrfs, xfs or NTFS
                             (MinGW build only), 'falloc' is your best
                             choice. It allocates large(few GiB) files
                             almost instantly. Don't use 'falloc' with legacy
                             file systems such as ext3 and FAT32 because it
                             takes almost same time as 'prealloc' and it
                             blocks aria2 entirely until allocation finishes.
                             'falloc' may not be available if your system
                             doesn't have posix_fallocate() function.
                             'trunc' uses ftruncate() system call or
                             platform-specific counterpart to truncate a file
                             to a specified length.
                             Possible Values: none, prealloc, trunc, falloc
                             Default: prealloc
                             Tags: #basic, #file
-V, --check-integrity[=true|false] Check file integrity by validating piece
                             hashes or a hash of entire file. This option has
                             effect only in BitTorrent, Metalink downloads
                             with checksums or HTTP(S)/FTP downloads with
                             --checksum option. If piece hashes are provided,
                             this option can detect damaged portions of a file
                             and re-download them. If a hash of entire file is
                             provided, hash check is only done when file has
                             been already download. This is determined by file
                             length. If hash check fails, file is
                             re-downloaded from scratch. If both piece hashes
                             and a hash of entire file are provided, only
                             piece hashes are used.
                             Possible Values: true, false
                             Default: false
                             Tags: #basic, #metalink, #bittorrent, #file, #checksum
-c, --continue[=true|false]  Continue downloading a partially downloaded
                             file. Use this option to resume a download
                             started by a web browser or another program
                             which downloads files sequentially from the
                             beginning. Currently this option is only
                             applicable to http(s)/ftp downloads.
                             Possible Values: true, false
                             Default: false
                             Tags: #basic, #http, #ftp
-i, --input-file=FILE        Downloads URIs found in FILE. You can specify
                             multiple URIs for a single entity: separate
                             URIs on a single line using the TAB character.
                             Reads input from stdin when '-' is specified.
                             Additionally, options can be specified after each
                             line of URI. This optional line must start with
                             one or more white spaces and have one option per
                             single line. See INPUT FILE section of man page
                             for details. See also --deferred-input option.
                             Possible Values: /path/to/file, -
                             Tags: #basic
-j, --max-concurrent-downloads=N Set maximum number of parallel downloads for
                             every static (HTTP/FTP) URL, torrent and metalink.
                             See also --split and --optimize-concurrent-downloads options.
                             Possible Values: 1-*
                             Default: 5
                             Tags: #basic
-Z, --force-sequential[=true|false] Fetch URIs in the command-line sequentially
                             and download each URI in a separate session, like
                             the usual command-line download utilities.
                             Possible Values: true, false
                             Default: false
                             Tags: #basic
-x, --max-connection-per-server=NUM The maximum number of connections to one
                             server for each download.
                             Possible Values: 1-16
                             Default: 1
                             Tags: #basic, #http, #ftp
-k, --min-split-size=SIZE    aria2 does not split less than 2*SIZE byte range.
                             For example, let's consider downloading 20MiB
                             file. If SIZE is 10M, aria2 can split file into 2
                             range [0-10MiB) and [10MiB-20MiB) and download it
                             using 2 sources(if --split >= 2, of course).
                             If SIZE is 15M, since 2*15M > 20MiB, aria2 does
                             not split file and download it using 1 source.
                             You can append K or M(1K = 1024, 1M = 1024K).
                             Possible Values: 1048576-1073741824
                             Default: 20M
                             Tags: #basic, #http, #ftp
--ftp-user=USER              Set FTP user. This affects all URLs.
                             Tags: #basic, #ftp
--ftp-passwd=PASSWD          Set FTP password. This affects all URLs.
                             Tags: #basic, #ftp
--http-user=USER             Set HTTP user. This affects all URLs.
                             Tags: #basic, #http
--http-passwd=PASSWD         Set HTTP password. This affects all URLs.
                             Tags: #basic, #http
--load-cookies=FILE          Load Cookies from FILE using the Firefox3 format
                             and Mozilla/Firefox(1.x/2.x)/Netscape format.
                             Possible Values: /path/to/file
                             Tags: #basic, #http, #cookie
-S, --show-files[=true|false] Print file listing of .torrent, .meta4 and
                             .metalink file and exit. More detailed
                             information will be listed in case of torrent
                             file.
                             Possible Values: true, false
                             Default: false
                             Tags: #basic, #metalink, #bittorrent
--max-overall-upload-limit=SPEED Set max overall upload speed in bytes/sec.
                             0 means unrestricted.
                             You can append K or M(1K = 1024, 1M = 1024K).
                             To limit the upload speed per torrent, use
                             --max-upload-limit option.
                             Possible Values: 0-*
                             Default: 0
                             Tags: #basic, #bittorrent
-u, --max-upload-limit=SPEED Set max upload speed per each torrent in
                             bytes/sec. 0 means unrestricted.
                             You can append K or M(1K = 1024, 1M = 1024K).
                             To limit the overall upload speed, use
                             --max-overall-upload-limit option.
                             Possible Values: 0-*
                             Default: 0
                             Tags: #basic, #bittorrent
-T, --torrent-file=TORRENT_FILE  The path to the .torrent file.
                             Possible Values: /path/to/file
                             Tags: #basic, #bittorrent
--listen-port=PORT...        Set TCP port number for BitTorrent downloads.
                             Multiple ports can be specified by using ',',
                             for example: "6881,6885". You can also use '-'
                             to specify a range: "6881-6999". ',' and '-' can
                             be used together.
                             Possible Values: 1024-65535
                             Default: 6881-6999
                             Tags: #basic, #bittorrent
--enable-dht[=true|false]    Enable IPv4 DHT functionality. It also enables
                             UDP tracker support. If a private flag is set
                             in a torrent, aria2 doesn't use DHT for that
                             download even if ``true`` is given.
                             Possible Values: true, false
                             Default: true
                             Tags: #basic, #bittorrent
--dht-listen-port=PORT...    Set UDP listening port used by DHT(IPv4, IPv6)
                             and UDP tracker. Multiple ports can be specified
                             by using ',', for example: "6881,6885". You can
                             also use '-' to specify a range: "6881-6999".
                             ',' and '-' can be used together.
                             Possible Values: 1024-65535
                             Default: 6881-6999
                             Tags: #basic, #bittorrent
--enable-dht6[=true|false]   Enable IPv6 DHT functionality.
                             Use --dht-listen-port option to specify port
                             number to listen on. See also --dht-listen-addr6
                             option.
                             Possible Values: true, false
                             Default: false
                             Tags: #basic, #bittorrent
--dht-listen-addr6=ADDR      Specify address to bind socket for IPv6 DHT. 
                             It should be a global unicast IPv6 address of the
                             host.
                             Tags: #basic, #bittorrent
-M, --metalink-file=METALINK_FILE The file path to the .meta4 and .metalink
                             file. Reads input from stdin when '-' is
                             specified.
                             Possible Values: /path/to/file, -
                             Tags: #basic, #metalink
```

### Examples

#### Download a file over http/s

```bash
aria2c https://domain.tld/file.txt
```

#### Use multiple mirrors of bottlenecked 

```bash
aria2c https://domain.tld/file.txt https://domain2.tld/file.txt
```

#### Download a file over ftp

```bash
aria2c ftp://domain.tld/file.txt
```

#### Download a torrent

```bash
aria2c file.torrent
```

```bash
aria2c https://domain.tld/file.torrent --follow-torrent=mem
```

```bash
aria2c magnet:?xt=urn:btih:JEQMEEFTBXT35RJ3GUTGXU7HP3HBU5P6&dn=rockyou2021.txt%20dictionary%20from%20kys234%20on%20RaidForums&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce
```

### Related pages

{{< related_pages_table tag="" >}}

### Also see

[aria2](https://aria2.github.io/)
