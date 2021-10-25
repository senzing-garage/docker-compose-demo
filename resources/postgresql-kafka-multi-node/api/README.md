# Api node type

## Synopsis

The "api" node type is responsible for
creating a [RESTful HTTP API](https://github.com/Senzing/senzing-rest-api-specification)
on top of the Senzing Engine.

It uses the
[Senzing API Server](https://github.com/Senzing/senzing-api-server).

## Environment variables

1. :pencil2: Identify Senzing docker image versions.
   See [latest versions](https://github.com/Senzing/knowledge-base/blob/master/lists/docker-versions-latest.sh).
   Example:

    ```console
    export SENZING_DOCKER_IMAGE_VERSION_INIT_CONTAINER=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_SENZING_API_SERVER=0.0.0
    ```

   :thinking: **Alternative method:**
   This method identifies the latest versions of each Docker image.

    ```console
    source <(curl -X GET https://raw.githubusercontent.com/Senzing/knowledge-base/master/lists/docker-versions-latest.sh)
    ```

1. :pencil2: Identify location of Senzing binary folders on host system.
   Example:

    ```console
    export SENZING_DATA_VERSION_DIR=/opt/senzing/data/2.0.0
    export SENZING_ETC_DIR=/etc/opt/senzing
    export SENZING_G2_DIR=/opt/senzing/g2
    ```

1. :pencil2: Database connectivity.
   This is used in a "single-database" configuration.
   For multi-database configuration, construct `SENZING_ENGINE_CONFIGURATION_JSON`
   to reflect multi-database configuration.
   Example:

    ```console
    export POSTGRES_DB=G2
    export POSTGRES_HOST=10.0.0.1
    export POSTGRES_PASSWORD=my-password
    export POSTGRES_PORT=5432
    export POSTGRES_USERNAME=my-username
    ```

1. Senzing Engine configuration.
   This is a "single-database" example.
   Using "bash shell parameter expansion",
   the database connectivity information is used
   to construct `SENZING_ENGINE_CONFIGURATION_JSON`.

   Condensed example:

    ```console
    export SENZING_ENGINE_CONFIGURATION_JSON="{\"PIPELINE\":{\"CONFIGPATH\":\"/etc/opt/senzing\",\"RESOURCEPATH\":\"/opt/senzing/g2/resources\",\"SUPPORTPATH\":\"/opt/senzing/data\"},\"SQL\":{\"CONNECTION\":\"postgresql://${POSTGRES_USERNAME}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}:${POSTGRES_DB}/\"}}"
    ```

   Formatted example;

    ```console
    export SENZING_ENGINE_CONFIGURATION_JSON=" \
        {\
            \"PIPELINE\":{\
                \"CONFIGPATH\":\"/etc/opt/senzing\",\
                \"RESOURCEPATH\":\"/opt/senzing/g2/resources\",\
                \"SUPPORTPATH\":\"/opt/senzing/data\"\
            },\
            \"SQL\":{\
              \"CONNECTION\":\"postgresql://${POSTGRES_USERNAME}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}:${POSTGRES_DB}/\"}\
        }"
    ```

### One-time initialization

1. :pencil2: Identify directory having "api" node artifacts.
   Example:

    ```console
    export SENZING_DOCKER_COMPOSE_DIR=~/senzing.git/docker-compose-demo/resources/postgresql-kafka-multi-node/api
    ```

1. Initialize Senzing.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose --file docker-compose-api-init.yaml up
    ```

1. After completion, bring down initialization formation.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose --file docker-compose-api-init.yaml down
    ```

1. :pencil2: Install Senzing license.
   Example:

    ```console
    cp /path/to/g2.lic ${SENZING_ETC_DIR}/g2.lic
    ```

## Run docker formation

1. :pencil2: Specify number of "senzing-api-server" containers to run.
   Example:

    ```console
    export SENZING_DOCKER_COMPOSE_SCALE_SENZING_API_SERVER=3
    ```

1. :pencil2: Specify the port range for the set of "senzing-api-servers".
   The number of ports must be equal to or larger than the value of
   `SENZING_DOCKER_COMPOSE_SCALE_SENZING_API_SERVER`.
   Example:

    ```console
    export SENZING_DOCKER_COMPOSE_PORT_RANGE_SENZING_API_SERVER="10000-10002"
    ```

1. Bring up Senzing formation.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose \
        --file docker-compose-api.yaml \
        up \
          --scale api=${SENZING_DOCKER_COMPOSE_SCALE_SENZING_API_SERVER}
    ```

1. **Note:** Each "senzing-api-container" will be given a different "ephemeral host port".
   A load-balancer or proxy is needed to aggregate the individual containers into a service
   having a single host:port.
