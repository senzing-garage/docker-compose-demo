# docker-compose-api-app-swagger

## Overview

This repository illustrates how to package a few docker artifacts for use
in an air-gapped environment.

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
1. [Air-gapped](#air-gapped)
    1. [Save docker images](#save-docker-images)
    1. [Copy artifacts to air-gapped system](#copy-artifacts-to-air-gapped-system)
    1. [Load docker images](#load-docker-images)
1. [Using docker-compose](#using-docker-compose)
    1. [Volumes](#volumes)
    1. [Databases](#databases)
    1. [SwaggerUI](#swaggerui)
    1. [Run docker formation](#run-docker-formation)
1. [View data](#view-data)
    1. [View docker containers](#view-docker-containers)
    1. [View Senzing API](#view-senzing-api)
    1. [View Senzing Entity Search WebApp](#view-senzing-entity-search-webapp)
    1. [View SwaggerUI](#view-swaggerui)
1. [Cleanup](#cleanup)
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

The following instructions need to be performed on an internet-connected system.

1. :pencil2: Identify a new output directory.
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
   Latest versions are listed in
   [versions-latest.sh](https://github.com/Senzing/knowledge-base/blob/master/lists/versions-latest.sh)
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

1. Capture docker image versions into a file that can be `sourced`.
   Example:

    ```console
    cat > ${SENZING_OUTPUT_DIR}/docker-versions.sh <<EOF
    #!/usr/bin/env bash

    export SENZING_DOCKER_IMAGE_VERSION_ENTITY_SEARCH_WEB_APP=${SENZING_DOCKER_IMAGE_VERSION_ENTITY_SEARCH_WEB_APP}
    export SENZING_DOCKER_IMAGE_VERSION_SENZING_API_SERVER=${SENZING_DOCKER_IMAGE_VERSION_SENZING_API_SERVER}
    export SENZING_DOCKER_IMAGE_VERSION_SWAGGERAPI_SWAGGER_UI=${SENZING_DOCKER_IMAGE_VERSION_SWAGGERAPI_SWAGGER_UI}
    EOF
    ```

1. Create single compressed file.
   Example:

    ```console
    tar \
      --create \
      --directory=${SENZING_OUTPUT_DIR} \
      --file=senzing-package.tar.gz \
      --gzip \
      --verbose \
      .
    ```

### Copy artifacts to air-gapped system

Copy the `senzing-package.tar.gz` file to the air-gapped system.

### Load docker images

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

The following instructions are performed on the air-gapped system.

### Identify docker versions

1. Set environment variables for docker image versions used.
   Example:

    ```console
    source ${SENZING_INPUT_DIR}/docker-versions.sh
    ```

### Volumes

1. :pencil2: Identify Senzing directories on the local host.
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

### SwaggerUI

1. :pencil2: Identify directory holding Senzing OpenAPI specification (i.e. `senzing-rest-api.yaml`).
   Example:

    ```console
    export SENZING_SWAGGERUI_DIR=${SENZING_INPUT_DIR}
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

### View SwaggerUI

1. Swagger's UI is viewable at
   [localhost:9180](http://localhost:9180).

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

- **[SENZING_DATA_VERSION_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_data_version_dir)**
- **[SENZING_ETC_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_etc_dir)**
- **[SENZING_G2_DIR](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md#senzing_g2_dir)**
