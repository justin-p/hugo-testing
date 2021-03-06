---
### The title for the content.
title: "10. Sysctl Optimization"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "10 sysctl optimization"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Linux sysctl.conf parameter tweaking to improve memory management, network security, network performance."
### The datetime assigned to this page.
date : 2020-03-10T16:37:55+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "10-sysctl-optimization"
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

## Sysctl Optimization

Linux sysctl.conf parameter tweaking to improve memory management, network security, network performance.

### Configuration

Open /etc/sysctl.conf in an editor

`sudo vim /etc/sysctl.conf`

Add the following lines to the end of the file:

```bash
# Do not accept ICMP redirects (prevent MITM attacks)
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
# Do not send ICMP redirects (we are not a router)
net.ipv4.conf.all.send_redirects = 0
# Log Martian Packets
net.ipv4.conf.all.log_martians = 1
# Controls IP packet forwarding
net.ipv4.ip_forward = 0
# Controls source route verification
net.ipv4.conf.default.rp_filter = 1
# Do not accept source routing
net.ipv4.conf.default.accept_source_route = 0
# Controls the System Request debugging functionality of the kernel
kernel.sysrq = 0
# Controls whether core dumps will append the PID to the core filename
# Useful for debugging multi-threaded applications
kernel.core_uses_pid = 1
 # Controls the use of TCP syncookies
net.ipv4.tcp_synack_retries = 2
######## IPv4 networking start ###########
# Send redirects, if router, but this is just server
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0
# Accept packets with SRR option? No
net.ipv4.conf.all.accept_source_route = 0
# Accept Redirects? No, this is not router
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.secure_redirects = 0
# Log packets with impossible addresses to kernel log? Yes
net.ipv4.conf.all.log_martians = 1
net.ipv4.conf.default.accept_source_route = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.default.secure_redirects = 0
# Ignore all ICMP ECHO and TIMESTAMP requests sent to it via broadcast/multicast
net.ipv4.icmp_echo_ignore_broadcasts = 1
# Prevent against the common 'syn flood attack'
net.ipv4.tcp_syncookies = 1
# Enable source validation by reversed path, as specified in RFC1812
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
######## IPv6 networking start ###########
# Number of Router Solicitations to send until assuming no routers are present.
# This is host and not router
net.ipv6.conf.default.router_solicitations = 0
# Accept Router Preference in RA?
net.ipv6.conf.default.accept_ra_rtr_pref = 0
# Learn Prefix Information in Router Advertisement
net.ipv6.conf.default.accept_ra_pinfo = 0
# Setting controls whether the system will accept Hop Limit settings from a router advertisement
net.ipv6.conf.default.accept_ra_defrtr = 0
#router advertisements can cause the system to assign a global unicast address to an interface
net.ipv6.conf.default.autoconf = 0
#how many neighbor solicitations to send out per address?
net.ipv6.conf.default.dad_transmits = 0
# How many global unicast IPv6 addresses can be assigned to each interface?
net.ipv6.conf.default.max_addresses = 1
######## IPv6 networking ends ###########
# Disabled, not used anymore
#Enable ExecShield protection |
#kernel.exec-shield = 1
#kernel.randomize_va_space = 1
# TCP and memory optimization
# increase TCP max buffer size setable using setsockopt()
#net.ipv4.tcp_rmem = 4096 87380 8388608
#net.ipv4.tcp_wmem = 4096 87380 8388608
# increase Linux auto tuning TCP buffer limits
#net.core.rmem_max = 8388608
#net.core.wmem_max = 8388608
#net.core.netdev_max_backlog = 5000
#net.ipv4.tcp_window_scaling = 1
# increase system file descriptor limit
fs.file-max = 65535
#Allow for more PIDs
kernel.pid_max = 65536
#Increase system IP port limits
net.ipv4.ip_local_port_range = 2000 65000
# Disable IPv6 autoconf
#net.ipv6.conf.all.autoconf = 0
#net.ipv6.conf.default.autoconf = 0
#net.ipv6.conf.eth0.autoconf = 0
#net.ipv6.conf.all.accept_ra = 0
#net.ipv6.conf.default.accept_ra = 0
#net.ipv6.conf.eth0.accept_ra = 0
```

Save the configuration file and process the changes using the command below

`sudo sysctl -p`
