---
### The title for the content.
title : "docker"
### If set, this will be used for the page's menu entry (instead of the `title` attribute)
# menuTitle : "docker"
### The title of the page in menu will be prefixed by this HTML content
# pre : ""
### The title of the page in menu will be postfixed by this HTML content
# post : ""
### The description for the content.
description : "A self-sufficient runtime for containers."
### The datetime assigned to this page.
date : 2021-09-02T14:13:26+02:00
### Appears as the tail of the output URL. A value specified in front matter will override the segment of the URL based on the filename.
# slug : "docker"
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
tags : ["Tools","docker"]
---

## docker

### Installation

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### Usage

```bash
Usage:  docker [OPTIONS] COMMAND
```

### Flags

```bash
Options:
      --config string      Location of client config files (default "/home/justin-p/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST
                           env var and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/home/justin-p/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/home/justin-p/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/home/justin-p/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  engine      Manage the docker engine
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes
```

### Examples

#### Create a container (without starting it)

```bash
docker create [IMAGE]
```

#### Rename an existing container

```bash
docker rename [CONTAINER_NAME] [NEW_CONTAINER_NAME]
```

#### Run a command in a new container

```bash
docker run [IMAGE] [COMMAND]
```

#### Start a container

```bash
docker start [CONTAINER]
```

#### Stop a running container

```bash
docker stop [CONTAINER]
```

#### Stop a running container and start it up again

```bash
docker restart [CONTAINER]
```

#### Pause processes in a running container

```bash
docker pause [CONTAINER]
```

#### Unpause processes in a running container

```bash
docker unpause [CONTAINER]
```

#### Block a container until others stop (after which it prints their exit codes)

```bash
docker wait [CONTAINER]
```

#### kill a container by sending a SIGKILL to a running container

```bash
docker kill [CONTAINER]
```

#### Attach local standard input, output, and error streams to a running container

```bash
docker attach [CONTAINER]
```

#### Stop and remove all running containers

```bash
docker rm -f $(docker ps -a -q)
```

#### Execute a command in container

```bash
docker exec -it <container name> <command>
```

#### Clean up all things docker related (excluding volumes)

```bash
docker system prune -a
```

### Related pages

{{< related_pages_table tag="docker" >}}

### Also see

[docs.docker.com](https://docs.docker.com/engine/reference/commandline/docker/)