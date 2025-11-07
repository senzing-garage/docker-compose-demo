# docker-compose-demo

If you are beginning your journey with [Senzing],
please start with [Senzing Quick Start guides].

You are in the [Senzing Garage] where projects are "tinkered" on.
Although this GitHub repository may help you understand an approach to using Senzing,
it's not considered to be "production ready" and is not considered to be part of the Senzing product.
Heck, it may not even be appropriate for your application of Senzing!

## Synopsis

Using `docker-compose`, bring up a Docker compose formation for demonstrating Senzing.

## Overview

## Caveat

This demonstration runs on platforms that support `docker` and `docker-compose`.

:warning: RedHat has explicitly stated that [Docker is not supported in RHEL 8].
As such, these demonstrations of Senzing using `docker` and `docker-compose`
do not run in a RedHat Enterprise Linux 8 environment natively.
Likewise, `docker` is not a CentOS 8 supported project.
Although with user-modification it has been shown that docker and docker-compose can run in these environments,
the onus is on the user for proper operation of docker and docker networking.

## Usage

1. :pencil2: Identify the file to be downloaded.
   Choose from the files in the [docker-compose directory].

   Example:

    ```console
    export SENZING_TOOLS_DOCKER_COMPOSE_FILE=senzing-docker-compose-postgresql.yaml
    ```

1. Download the docker-compose file.

   ```console
   curl -O https://raw.githubusercontent.com/senzing-garage/docker-compose-demo/refs/heads/main/docker-compose/${SENZING_TOOLS_DOCKER_COMPOSE_FILE}
   ```

1. :thinking: **Optional:** Pull Docker image versions.

   ```console
   docker-compose --file ${SENZING_TOOLS_DOCKER_COMPOSE_FILE} pull
   ```

1. Bring up Docker compose formation.

   ```console
   docker-compose --file ${SENZING_TOOLS_DOCKER_COMPOSE_FILE} up
   ```

1. Work with Docker compose formation.
   See [Services] section.

1. Bring down Docker formation.

   ```console
   docker-compose --file ${SENZING_TOOLS_DOCKER_COMPOSE_FILE} down --volumes
   ```

   *Note:* The optional [--volumes] parameter cleans up the volumes.
   Omit the [--volumes] parameter if the data is to be reused.

## Services

All Docker Compose formations include:

- [senzingsdk-tools]

Services offered by specific Docker Compose formations:

| Docker compose file                      | DB Admin     |
|------------------------------------------|--------------|
| [senzing-docker-compose-postgresql.yaml] | [PgAdmin]    |
| [senzing-docker-compose-sqlite.yaml]     | [Sqlite-Web] |

### senzingsdk-tools

The [senzing/senzingsdk-tools] Docker image contains Senzing tools for analyzing Senzing information.

1. In a separate terminal, use `docker exec` to enter the `senzing/senzingsdk-tools` Docker container.

   ```console
   docker exec -it senzingsdk-tools /bin/bash
   ```

### PgAdmin

A Postgres database administration tool.

1. View at [localhost:9171](http://localhost:9171)
   1. When prompted for PgAdmin credentials, read the information in the "Senzing demonstration" section.
   1. When prompted for the *database* (not PgAdmin) password, enter `postgres`.
1. Pgadmin4 homepage: [github.com/dpage/pgadmin4]

### PhpMyAdmin

A MySQL database administration tool.

1. View at [localhost:9173](http://localhost:9173)
   1. Username: mysql
   1. Password: mysql
1. PhpMyAdmin homepage: []

### Sqlite-Web

An SQLite database administration tool.

1. View at [localhost:9174](http://localhost:9174)
1. Sqlite-web homepage: [github.com/coleifer/sqlite-web]

[--volumes]: https://docs.docker.com/reference/cli/docker/compose/down/#options
[Docker is not supported in RHEL 8]: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#con_running-containers-without-docker_assembly_starting-with-containers
[docker-compose directory]: https://github.com/senzing-garage/docker-compose-demo/tree/main/docker-compose
[github.com/coleifer/sqlite-web]: https://github.com/coleifer/sqlite-web
[github.com/dpage/pgadmin4]: https://github.com/dpage/pgadmin4
[PgAdmin]: #pgadmin
[Senzing Garage]: https://github.com/senzing-garage
[Senzing Quick Start guides]: https://docs.senzing.com/quickstart/
[senzing-docker-compose-postgresql.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/352-dockter-2/docker-compose/senzing-docker-compose-postgresql.yaml
[senzing-docker-compose-sqlite.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/352-dockter-2/docker-compose/senzing-docker-compose-sqlite.yaml
[Senzing]: https://senzing.com/
[senzing/senzingsdk-tools]: https://github.com/Senzing/senzingsdk-tools
[senzingsdk-tools]: #senzingsdk-tools
[Services]: #services
[Sqlite-Web]: #sqlite-web
