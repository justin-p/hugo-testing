---
### The title for the content.
title : "Dockerfile"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "dockerfile"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image."
### The datetime assigned to this page.
date : 2020-03-10T16:36:30+01:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "dockerfile"
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

## dockerfile

### Reference

#### Inheritance

```docker
FROM ruby:2.2.2
```

#### Variables

```docker
ENV APP_HOME /myapp
RUN mkdir $APP_HOME
```

#### Initialization

```docker
RUN bundle install
```

```docker
WORKDIR /myapp
```

```docker
VOLUME ["/data"]
# Specification for mount point
```

```docker
ADD file.xyz /file.xyz
COPY --chown=user:group host_file.xyz /path/container_file.xyz
```

#### Onbuild

```docker
ONBUILD RUN bundle install
# when used with another file
```

#### Commands

```docker
EXPOSE 5900
CMD    ["bundle", "exec", "rails", "server"]
```

#### Entrypoint

```docker
ENTRYPOINT ["executable", "param1", "param2"]
ENTRYPOINT command param1 param2
```

Configures a container that will run as an executable.

```docker
ENTRYPOINT exec top -b
```

This will use shell processing to substitute shell variables, and will ignore any `CMD` or `docker run` command line arguments.

#### Metadata

```docker
LABEL version="1.0"
```

```docker
LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
```

```docker
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

### See also

* [Docker Docs Builder](https://docs.docker.com/engine/reference/builder)
