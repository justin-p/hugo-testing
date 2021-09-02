---
### The title for the content.
title: "public key disclosure"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "public key disclosure"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description: "Sharing is caring, but this may be a but to much."
### The datetime assigned to this page.
date: 2020-03-10T16:43:46+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "public key disclosure"
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
tags : ["public key disclosure"]
---

## public key disclosure

Very often keys are pushed to code repositories such as Github, Bitbucket or Gitlab. You want to identify a target code repo and search all commit history to discover secrets that might have been pushed.

Tools to search git repos

- [gitleaks](https://github.com/zricethezav/gitleaks) # MOVE TO OWN TOOLS PAGE

- [gitrob](https://github.com/michenriksen/gitrob) # MOVE TO OWN TOOLS PAGE

- [truffleHog](https://github.com/dxa4481/truffleHog) # MOVE TO OWN TOOLS PAGE

### Example

```txt
docker pull zricethezav/gitleaks
docker run --rm --name=gitleaks zricethezav/gitleaks -v -r https://github.com/name/repo.git
```

When it returns a match it will also include a git commit which you can use to view it in a browser or use git to 'check it out'.

```txt
git checkout commit
```

### External services

| Service                           | info                        |
| --------------------------------- | --------------------------- |
| [shhgit](https://www.shhgit.com/) | Monitors github for secrets |

### Related pages

{{< related_pages_table tag="public key disclosure" >}}
