---
title: "Docker Compose"
date: 2020-03-06T11:09:37+01:00
draft: false
weight: 20
---

### Basic example

```yaml
version: "2"

services:
  # define a new container called web
  web:
    build: .
    # build from local Dockerfile
    context: ./Path
    dockerfile: Dockerfile
    # open port 5000 from the inside to the outside (guest:host)
    ports:
      - "5000:5000"
    # mount the local folder as /code
    volumes:
      - .:/code
  # define a new container called redis
  redis:
    image: redis
```

### Commands

```bash
docker-compose start
docker-compose stop
```

```bash
docker-compose pause
docker-compose unpause
```

```bash
docker-compose ps
docker-compose up
docker-compose down
```

### Reference

#### Building

```yaml
web:
  # build from Dockerfile
  build: .
```

```yaml
# build from custom Dockerfile
build:
  context: ./dir
  dockerfile: Dockerfile.dev
```

```yaml
  # build from image
  image: ubuntu
  image: ubuntu:14.04
  image: tutum/influxdb
  image: example-registry:4000/postgresql
  image: a4bc65fd
```

#### Ports

```yaml
ports:
  - "3000"
  - "8000:80" # guest:host
```

```yaml
# expose ports to linked services (not to host)
expose: ["3000"]
```

#### File Commands

```yaml
  # command to execute
  command: bundle exec thin -p 3000
  command: [bundle, exec, thin, -p, 3000]
```

```yaml
  # override the entrypoint
  entrypoint: /app/start.sh
  entrypoint: [php, -d, vendor/bin/phpunit]
```

#### Environment variables

```yaml
  # environment vars
  environment:
    RACK_ENV: development
  environment:
    - RACK_ENV=development
```

```yaml
  # environment vars from file
  env_file: .env
  env_file: [.env, .development.env]
```

#### Dependencies

```yaml
# makes the `db` service available as the hostname `database`
# (implies depends_on)
links:
  - db:database
  - redis
```

```yaml
# make sure `db` is alive before starting
depends_on:
  - db
```

#### Other options

```yaml
# make this service extend another
extends:
  file: common.yml # optional
  service: webapp
```

```yaml
volumes:
  - /var/lib/mysql
  - ./_data:/var/lib/mysql
```

### Advanced features

#### Labels

```yaml
services:
  web:
    labels:
      com.example.description: "Accounting web app"
```

#### DNS servers

```yaml
services:
  web:
    dns: 8.8.8.8
    dns:
      - 8.8.8.8
      - 8.8.4.4
```

#### Devices

```yaml
services:
  web:
    devices:
      - "/dev/ttyUSB0:/dev/ttyUSB0"
```

#### External links

```yaml
services:
  web:
    external_links:
      - redis_1
      - project_db_1:mysql
```

#### Hosts

```yaml
services:
  web:
    extra_hosts:
      - "somehost:192.168.1.100"
```

#### Network

```yaml
# creates a custom network called `frontend`
networks:
  frontend:
```

#### External network

```yaml
# join a pre-existing network
networks:
  default:
    external:
      name: frontend
```

### Also see

- [DevHints](https://devhints.io/docker-compose)
