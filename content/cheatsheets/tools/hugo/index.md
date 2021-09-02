---
### The title for the content.
title : "hugo"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "hugo"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "Hugo is a Fast and Flexible Static Site Generator."
### The datetime assigned to this page.
date : 2021-01-26T17:27:07+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "hugo"
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

## hugo

### Installation

```bash
snap install hugo --channel=extended
```

### Usage

```bash
hugo [command] [flags]
```

### Flags

```bash
Usage:
  hugo [flags]
  hugo [command]

Available Commands:
  config      Print the site configuration
  convert     Convert your content to different formats
  deploy      Deploy your site to a Cloud provider.
  env         Print Hugo version and environment info
  gen         A collection of several useful generators.
  help        Help about any command
  import      Import your site from others.
  list        Listing out various types of content
  mod         Various Hugo Modules helpers.
  new         Create new content for your site
  server      A high performance webserver
  version     Print the version number of Hugo

Flags:
  -b, --baseURL string             hostname (and path) to the root, e.g. http://spf13.com/
  -D, --buildDrafts                include content marked as draft
  -E, --buildExpired               include expired content
  -F, --buildFuture                include content with publishdate in the future
      --cacheDir string            filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
      --cleanDestinationDir        remove files from destination not found in static directories
      --config string              config file (default is path/config.yaml|json|toml)
      --configDir string           config dir (default "config")
  -c, --contentDir string          filesystem path to content directory
      --debug                      debug output
  -d, --destination string         filesystem path to write files to
      --disableKinds strings       disable different kind of pages (home, RSS etc.)
      --enableGitInfo              add Git revision, date and author info to the pages
  -e, --environment string         build environment
      --forceSyncStatic            copy all files when static is changed.
      --gc                         enable to run some cleanup tasks (remove unused cache files) after the build
  -h, --help                       help for hugo
      --i18n-warnings              print missing translations
      --ignoreCache                ignores the cache directory
      --ignoreVendor               ignores any _vendor directory
      --ignoreVendorPaths string   ignores any _vendor for module paths matching the given Glob pattern
  -l, --layoutDir string           filesystem path to layout directory
      --log                        enable Logging
      --logFile string             log File path (if set, logging enabled automatically)
      --minify                     minify any supported output format (HTML, XML etc.)
      --noChmod                    don't sync permission mode of files
      --noTimes                    don't sync modification time of files
      --path-warnings              print warnings on duplicate target paths etc.
      --print-mem                  print memory usage to screen at intervals
      --quiet                      build in quiet mode
      --renderToMemory             render to memory (only useful for benchmark testing)
  -s, --source string              filesystem path to read files relative from
      --templateMetrics            display metrics about template executions
      --templateMetricsHints       calculate some improvement hints when combined with --templateMetrics
  -t, --theme strings              themes to use (located in /themes/THEMENAME/)
      --themesDir string           filesystem path to themes directory
      --trace file                 write trace to file (not useful in general)
  -v, --verbose                    verbose output
      --verboseLog                 verbose logging
  -w, --watch                      watch filesystem for changes and recreate as needed

Additional help topics:
  hugo check   Contains some verification checks

Use "hugo [command] --help" for more information about a command.
```

### Examples

These examples are fine tuned to the theme used in this hugo instance.

#### Generate new site

```bash
hugo new site new-site-name
```

#### Generate new folder using directory based archetype

```bash
hugo new --kind cheatsheet-bundle cheatsheets/hugo
```

#### Generate new subfolder using new-folder archetype

```bash
hugo new --kind new-folder notes/hacking/External/_index.md
```

#### Run live debug server

```bash
hugo server
```

### Shortcodes

#### Attachments

    {{%/* attachments title="Related files" pattern=".*(pdf|mp4)"/*/%}}

#### Button

    {{%/* button href="https://getgrav.org/" icon="fas fa-download" icon-position="right" %}}Get Grav with icon right{{% /button %}}

#### Children

    {{% children style="h2" depth="3" description="true" %}}

#### Expand

    {{% expand "Is this learn theme rocks ?" %}}Yes !.{{% /expand%}}

#### Notice

##### Note (blue)

```
{{% notice note */%}}
A notice disclaimer
{{%/* /notice */%}}
```

##### Info (orange)

```
{{%/* notice info */%}}
An information disclaimer
{{%/* /notice */%}}
```

##### Tip (green)

```
{{%/* notice tip */%}}
A tip disclaimer
{{%/* /notice */%}}
```

##### Warning (red)

```
{{%/* notice warning */%}}
A warning disclaimer
{{%/* /notice */%}}
```

#### Releated pages

```
{ {< related_pages_table tag="password-cracking" >}}
```
