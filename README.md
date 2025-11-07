# docker-compose-demo

If you are beginning your journey with [Senzing],
please start with [Senzing Quick Start guides].

You are in the [Senzing Garage] where projects are "tinkered" on.
Although this GitHub repository may help you understand an approach to using Senzing,
it's not considered to be "production ready" and is not considered to be part of the Senzing product.
Heck, it may not even be appropriate for your application of Senzing!

## Synopsis

Using `docker-compose`, bring up a Senzing stack.

## Overview

1. :pencil2: Identify the file to be downloaded.

    ```console
    export SENZING_TOOLS_DOCKER_COMPOSE_FILE=senzing-docker-compose-postgresql.yaml
    ```

1. Download the docker-compose file.

   ```console
   curl -O https://raw.githubusercontent.com/senzing-garage/docker-compose-demo/refs/heads/352-dockter-2/docker-compose/${SENZING_TOOLS_DOCKER_COMPOSE_FILE}
   ```

1. :thinking: **Optional:** Pull Docker image versions.

   ```console
   docker --file ${SENZING_TOOLS_DOCKER_COMPOSE_FILE} pull
   ```

1. Bring up Docker compose formation.

   ```console
   docker --file ${SENZING_TOOLS_DOCKER_COMPOSE_FILE} up
   ```

1.

## Services

### senzing/senzingsdk-tools

1. xx

   ```console
   docker exec -it senzingsdk-tools /bin/bash
   ```

### PgAdmin

A Postgres database administration tool.

- View at [localhost:8171](http://localhost:9171)
- Homepage: [github.com/dpage/pgadmin4](https://github.com/dpage/pgadmin4)

## Caveat

This demonstration runs on platforms that support `docker` and `docker-compose`.

:warning: RedHat has explicitly stated that [Docker is not supported in RHEL 8].
As such, these demonstrations of Senzing using `docker` and `docker-compose`
do not run in a RedHat Enterprise Linux 8 environment natively.
Likewise, `docker` is not a CentOS 8 supported project.
Although with user-modification it has been shown that docker and docker-compose can run in these environments,
the onus is on the user for proper operation of docker and docker networking.

## Implementation
