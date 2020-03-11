---
title: "Dockerfile"
date: 2020-03-06T11:09:11+01:00
draft: false
---

### Reference

#### Inheritance

```bash
FROM ruby:2.2.2
```

#### Variables

```bash
ENV APP_HOME /myapp
RUN mkdir $APP_HOME
```

#### Initialization

```bash
RUN bundle install
```

```bash
WORKDIR /myapp
```

```bash
VOLUME ["/data"]
# Specification for mount point
```

```bash
ADD file.xyz /file.xyz
COPY --chown=user:group host_file.xyz /path/container_file.xyz
```

#### Onbuild

```bash
ONBUILD RUN bundle install
# when used with another file
```

#### Commands

```bash
EXPOSE 5900
CMD    ["bundle", "exec", "rails", "server"]
```

#### Entrypoint

```bash
ENTRYPOINT ["executable", "param1", "param2"]
ENTRYPOINT command param1 param2
```

Configures a container that will run as an executable.

```bash
ENTRYPOINT exec top -b
```

This will use shell processing to substitute shell variables, and will ignore any `CMD` or `docker run` command line arguments.

#### Metadata

```bash
LABEL version="1.0"
```

```bash
LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
```

```bash
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

### See also

* [Docker Docs Builder](https://docs.docker.com/engine/reference/builder)
* [DevHints](https://devhints.io/dockerfile)
