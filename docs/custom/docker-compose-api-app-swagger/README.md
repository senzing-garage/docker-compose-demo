# docker-compose-api-app-swagger

## Overview

This repository illustrates a reference implementation of Senzing using
RabbitMQ as the queue and
PostgreSQL as the underlying database.

The instructions show how to set up a system that:

1. Reads JSON lines from a file on the internet.
1. Sends each JSON line to a message queue.
    1. In this implementation, the queue is RabbitMQ.
1. Reads messages from the queue and inserts into Senzing.
    1. In this implementation, Senzing keeps its data in a PostgreSQL database.
1. Reads information from Senzing via [Senzing REST API](https://github.com/Senzing/senzing-rest-api-specification) server.
1. Views resolved entities in a [web app](https://github.com/Senzing/entity-search-web-app).

The following diagram shows the relationship of the docker containers in this docker composition.
Arrows represent data flow.


This docker formation brings up the following docker containers:

1. *[senzing/entity-web-search-app](https://github.com/Senzing/entity-search-web-app)*
1. *[senzing/stream-loader](https://github.com/Senzing/stream-loader)*
1. *[swaggerapi/swagger-ui](https://hub.docker.com/r/swaggerapi/swagger-ui)*

### Contents

1. [Expectations](#expectations)
    1. [Space](#space)
    1. [Time](#time)
    1. [Background knowledge](#background-knowledge)
1. [Preparation](#preparation)
    1. [Prerequisite software](#prerequisite-software)
    1. [Clone repository](#clone-repository)
1. [Using docker-compose](#using-docker-compose)
    1. [Volumes](#volumes)
    6. [Run docker formation](#run-docker-formation)
1. [View data](#view-data)
    1. [View docker containers](#view-docker-containers)
    2. [Use SSH](#use-ssh)
    3. [View RabbitMQ](#view-rabbitmq)
    4. [View PostgreSQL](#view-postgresql)
    5. [View Senzing API](#view-senzing-api)
    6. [View Senzing Entity Search WebApp](#view-senzing-entity-search-webapp)
    7. [View Jupyter notebooks](#view-jupyter-notebooks)
    8. [View X-Term](#view-x-term)
1. [Cleanup](#cleanup)
1. [Advanced](#advanced)
    1. [Re-run docker formation](#re-run-docker-formation)
    1. [Configuration](#configuration)

### Legend

1. :thinking: - A "thinker" icon means that a little extra thinking may be required.
   Perhaps you'll need to make some choices.
   Perhaps it's an optional step.
1. :pencil2: - A "pencil" icon means that the instructions may need modification before performing.
1. :warning: - A "warning" icon means that something tricky is happening, so pay attention.

## Expectations

### Space

This repository and demonstration require 7 GB free disk space.

### Time

Budget 2 hours to get the demonstration up-and-running, depending on CPU and network speeds.

### Background knowledge

This repository assumes a working knowledge of:

1. [Docker](https://github.com/Senzing/knowledge-base/blob/master/WHATIS/docker.md)
1. [Docker-compose](https://github.com/Senzing/knowledge-base/blob/master/WHATIS/docker-compose.md)

## Preparation

### Prerequisite software

The following software programs need to be installed:

1. [docker](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/install-docker.md)
1. [docker-compose](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/install-docker-compose.md)

## Air-gapped

### Save docker images

The following instructions need to be performed on an internet connected system.

1. :pencil2: Identify output directory.
   Example:

    ```console
    export SENZING_OUTPUT_DIR=~/senzing-package
    ```

1. Make output directory.
   Example:

    ```console
    mkdir -p ${SENZING_OUTPUT_DIR}/docker-images
    ```

1. :pencil2: Identify docker image versions.
   Example:

    ```console
    export SENZING_DOCKER_IMAGE_VERSION_ENTITY_SEARCH_WEB_APP=2.2.3
    export SENZING_DOCKER_IMAGE_VERSION_SENZING_API_SERVER=2.6.1
    export SENZING_DOCKER_IMAGE_VERSION_SWAGGERAPI_SWAGGER_UI=v3.50.0
    ```

1. Pull docker images.
   Example:

    ```console
    docker pull senzing/entity-search-web-app:${SENZING_DOCKER_IMAGE_VERSION_ENTITY_SEARCH_WEB_APP}
    docker pull senzing/senzing-api-server:${SENZING_DOCKER_IMAGE_VERSION_SENZING_API_SERVER}
    docker pull swaggerapi/swagger-ui:${SENZING_DOCKER_IMAGE_VERSION_SWAGGERAPI_SWAGGER_UI}
    ```

1. Save docker images to output directory.
   Example:

    ```console
    docker save senzing/entity-search-web-app:${SENZING_DOCKER_IMAGE_VERSION_ENTITY_SEARCH_WEB_APP} \
      | gzip \
      > ${SENZING_OUTPUT_DIR}/docker-images/senzing-entity-search-web-app-${SENZING_DOCKER_IMAGE_VERSION_ENTITY_SEARCH_WEB_APP}.tar.gz

    docker save senzing/senzing-api-server:${SENZING_DOCKER_IMAGE_VERSION_SENZING_API_SERVER} \
      | gzip \
      > ${SENZING_OUTPUT_DIR}/docker-images/senzing-senzing-api-server-${SENZING_DOCKER_IMAGE_VERSION_SENZING_API_SERVER}.tar.gz

    docker save swaggerapi/swagger-ui:${SENZING_DOCKER_IMAGE_VERSION_SWAGGERAPI_SWAGGER_UI} \
      | gzip \
      > ${SENZING_OUTPUT_DIR}/docker-images/swaggerapi-swagger-ui-${SENZING_DOCKER_IMAGE_VERSION_SWAGGERAPI_SWAGGER_UI}.tar.gz
    ```

1. Add Senzing OpenAPI specification.
   Example:

    ```console
    curl -X GET \
      --output ${SENZING_OUTPUT_DIR}/senzing-rest-api.yaml \
      https://raw.githubusercontent.com/Senzing/senzing-rest-api-specification/master/senzing-rest-api.yaml
    ```

1. Add docker-compose.yaml.
   Example:

    ```console
    curl -X GET \
      --output ${SENZING_OUTPUT_DIR}/docker-compose.yaml \
      https://raw.githubusercontent.com/Senzing/docker-compose-demo/master/resources/custom/docker-compose-api-app-swagger.yaml
    ```

1. Create single compressed file.
   Example:

    ```console
    tar \
      --create \
      --file=~/senzing-package.tar.gz \
      --gzip \
      --verbose \
      ${SENZING_OUTPUT_DIR}
    ```

### Copy artifacts to air-gapped system.

Copy the `senzing-package.tar.gz` file to the air-gapped system.

### Load

The following instructions are performed on the air-gapped system.

1. :pencil2: Identify a new input directory and the location of the compressed file.
   Example:

    ```console
    export SENZING_INPUT_DIR=~/senzing-package
    export SENZING_INPUT_FILE=~/senzing-package.tar.gz
    ```

1. Make new input directory.
   Example:

    ```console
    mkdir -p ${SENZING_INPUT_DIR}
    ```

1. Extract package.
   Example:

    ```console
    tar \
      --directory=${SENZING_INPUT_DIR} \
      --extract \
      --verbose \
      --file=${SENZING_INPUT_FILE}
    ```

1. Load docker images into local repository.
   Example:

    ```console
    for DOCKER_IMAGE_NAME in ${SENZING_INPUT_DIR}/docker-images/*;
    do
      echo "Loading ${DOCKER_IMAGE_NAME}"
      docker load --input ${DOCKER_IMAGE_NAME}
    done
    ```

1. Verify docker images are in local docker repository.
   Example:

    ```console
    docker images
    ```

## Using docker-compose

### Volumes

1. :pencil2: Identify directories on the local host.
   Example:

    ```console
    export SENZING_DATA_VERSION_DIR=/opt/my-senzing/data/2.0.0
    export SENZING_ETC_DIR=/opt/my-senzing/etc
    export SENZING_G2_DIR=/opt/my-senzing/g2
    ```

### Databases

1. :pencil2: Identify database connection information.
   Connection format: `postgresql://Username:Password@Host:Port:Name`
   Example:

    ```console
    export SENZING_DATABASE_CONNECTION_CORE="postgresql://postgres:postgres@10.1.1.20:5432:G2"
    export SENZING_DATABASE_CONNECTION_RES="postgresql://postgres:postgres@10.1.1.21:5432:G2"
    export SENZING_DATABASE_CONNECTION_LIBFEAT="postgresql://postgres:postgres@10.1.1.22:5432:G2"
    ```

### Run docker formation

1. Launch docker-compose formation.
   Example:

    ```console
    cd ${SENZING_INPUT_DIR}
    sudo \
      --preserve-env \
      docker-compose --file docker-compose.yaml up
    ```

1. Allow time for the components to come up and initialize.
    1. There will be errors in some docker logs as they wait for dependent services to become available.
       `docker-compose` isn't the best at orchestrating docker container dependencies.

## View data

### View docker containers

1. A good tool to monitor individual docker logs is
   [Portainer](https://github.com/Senzing/knowledge-base/blob/master/WHATIS/portainer.md).
   When running, Portainer is viewable at
   [localhost:9170](http://localhost:9170).

### View Senzing API

View results from Senzing REST API server.
The server supports the
[Senzing REST API](https://github.com/Senzing/senzing-rest-api-specification).

1. OpenApi Editor is viewable at
   [localhost:9180](http://localhost:9180).
1. Example Senzing REST API request:
   [localhost:8250/heartbeat](http://localhost:8250/heartbeat)
1. See
   [additional tips](https://github.com/Senzing/knowledge-base/blob/master/lists/docker-compose-demo-tips.md#senzing-api-server)
   for working with Senzing API server.

### View Senzing Entity Search WebApp

1. Senzing Entity Search WebApp is viewable at
   [localhost:8251](http://localhost:8251).
1. See
   [additional tips](https://github.com/Senzing/knowledge-base/blob/master/lists/docker-compose-demo-tips.md#senzing-entity-search-webapp)
   for working with Senzing Entity Search WebApp.


## Cleanup

When the docker-compose formation is no longer needed,
it can be brought down and directories can be deleted.

1. Bring down docker formation.
   Example:

    ```console
    cd ${SENZING_INPUT_DIR}
    sudo docker-compose --file docker-compose.yaml down
    ```

1. Remove directories from host system.
   The following directories were created during the demonstration:
    1. `${SENZING_INPUT_DIR}`

   They may be safely deleted.


### Configuration

Configuration values specified by environment variable or command line parameter.

- **[POSTGRES_DB](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#postgres_db)**
- **[POSTGRES_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#postgres_dir)**
- **[POSTGRES_PASSWORD](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#postgres_password)**
- **[POSTGRES_USERNAME](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#postgres_username)**
- **[RABBITMQ_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#rabbitmq_dir)**
- **[RABBITMQ_PASSWORD](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#rabbitmq_password)**
- **[RABBITMQ_USERNAME](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#rabbitmq_username)**
- **[SENZING_ACCEPT_EULA](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_accept_eula)**
- **[SENZING_DATA_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_data_dir)**
- **[SENZING_DATA_SOURCE](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_data_source)**
- **[SENZING_DATA_VERSION_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_data_version_dir)**
- **[SENZING_ENTITY_TYPE](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_entity_type)**
- **[SENZING_ETC_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_etc_dir)**
- **[SENZING_G2_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_g2_dir)**
- **[SENZING_VAR_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_var_dir)**
