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

1. **TL;DR** - A Simple example

   1. Prerequisites:
      1. [Docker compose]

   1. Download docker-compose file:

      ```console
      curl -O https://raw.githubusercontent.com/senzing-garage/docker-compose-demo/refs/heads/main/docker-compose/senzing-docker-compose-postgresql-truthset.yaml
      ```

      Alternatively, use a web browser to [download senzing-docker-compose-postgresql-truthset.yaml].

   1. Bring up the docker-compose formation:

      ```console
      docker compose --profile new --file senzing-docker-compose-postgresql-truthset.yaml up --pull always
      ```

   1. In a separate terminal, exec into the `senzingsdk-tools` container:

      ```console
      docker exec -it senzingsdk-tools /bin/bash
      ```

1. In addition to the **TL;DR**,
   this repository contains a multitude of docker-compose.yaml files in the [docker-compose directory].
   Variations:

      | Variation | Example filename                                          |
      |-----------|-----------------------------------------------------------|
      | database  | `senzing-docker-compose-<database>.yaml`                  |
      | truthset  | `senzing-docker-compose-<database>-truthset.yaml`         |
      | multi use | `senzing-docker-compose-<database>-<truthset>-multi.yaml` |

   For step-by-step instructions, see [Examples].

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

1. Bring up Docker compose formation.

   ```console
   docker-compose --profile new --file ${SENZING_TOOLS_DOCKER_COMPOSE_FILE} up --pull always
   ```

   *Note:* The optional [--pull always] parameter pulls the latest version of the Docker images before running.
   Omit the [--pull always] parameter if using the currently cached Docker images is preferred.

1. Work with Docker compose formation.
   See [Services] section.

1. Bring down Docker formation.

   ```console
   docker-compose --profile new --file ${SENZING_TOOLS_DOCKER_COMPOSE_FILE} down --volumes
   ```

   *Note:* The optional [--volumes] parameter cleans up the volumes.
   Omit the [--volumes] parameter if the data is to be reused via
   [--profile resume].

## Services

See [Services] for services rendered by each docker compose formation.

## References

- [Development]
- [Errors]
- [Examples]
- [Services]

[--profile resume]: https://docs.docker.com/reference/cli/docker/compose/up/#options
[--pull always]: https://docs.docker.com/reference/cli/docker/compose/up/#options
[--volumes]: https://docs.docker.com/reference/cli/docker/compose/down/#options
[Development]: docs/development.md
[Docker compose]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/docker-compose.md
[Docker is not supported in RHEL 8]: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#con_running-containers-without-docker_assembly_starting-with-containers
[docker-compose directory]: https://github.com/senzing-garage/docker-compose-demo/tree/main/docker-compose
[download senzing-docker-compose-postgresql-truthset.yaml]: https://raw.githubusercontent.com/senzing-garage/docker-compose-demo/refs/heads/main/docker-compose/senzing-docker-compose-postgresql-truthset.yaml
[Errors]: docs/errors.md
[Examples]: docs/examples.md
[Senzing Garage]: https://github.com/senzing-garage
[Senzing Quick Start guides]: https://docs.senzing.com/quickstart/
[Senzing]: https://senzing.com/
[Services]: docs/services.md
