# Redoer node type

## Synopsis

The "redoer" node type is responsible for
receiving "redo" records from the Senzing Engine,
putting the records into a RabbitMQ queue
reading the "redo" records from the queue,
and having the records processed by the Senzing Engine.
The use of a queue is to support scale up of redo loaders.

It uses the
[redoer](https://github.com/Senzing/redoer).

## Environment variables

1. :pencil2: Identify Senzing docker image versions.
   See [latest versions](https://github.com/Senzing/knowledge-base/blob/master/lists/docker-versions-latest.sh).
   Example:

    ```console
    export SENZING_DOCKER_IMAGE_VERSION_BITNAMI_RABBITMQ=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_INIT_CONTAINER=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_REDOER=0.0.0
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

1. :pencil2: Identify directory having "redoer" node artifacts.
   Example:

    ```console
    export SENZING_DOCKER_COMPOSE_DIR=~/senzing.git/docker-compose-demo/resources/postgresql-kafka-multi-node/redoer
    ```

1. Initialize Senzing.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose --file docker-compose-redoer-init.yaml up
    ```

1. After completion, bring down initialization formation.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose --file docker-compose-redoer-init.yaml down
    ```

1. :pencil2: Install Senzing license.
   Example:

    ```console
    cp /path/to/g2.lic ${SENZING_ETC_DIR}/g2.lic
    ```

## Run docker formation

1. :pencil2: Specify number of "redoer" containers to run.
   Example:

    ```console
    export SENZING_STREAM_REDOER_SCALE=5
    ```

1. Bring up Senzing formation.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose \
        --file docker-compose-redoer.yaml \
        up \
          --scale redoerqueuereader=${SENZING_STREAM_REDOER_SCALE}
    ```
