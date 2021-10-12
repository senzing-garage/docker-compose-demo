# Loader node type

## Synopsis

The "loader" node type is responsible for reading messages from a Kafka Topic
and sending the messages to the Senzing Engine

## Environment variables

1. :pencil2: Database connectivity.
   Example:

    ```console
    export POSTGRES_DB=G2
    export POSTGRES_HOST=localhost
    export POSTGRES_PASSWORD=my-password
    export POSTGRES_PORT=5432
    export POSTGRES_USERNAME=my-username
    ```

1. :pencil2: Kafka connectivity.
   Example:

    ```console
    export SENZING_KAFKA_BOOTSTRAP_SERVER=localhost:9092
    export SENZING_KAFKA_TOPIC=senzing-kafka-topic
    ```

1. :pencil2: Senzing binary folders.
   Example:

    ```console
    export SENZING_DATA_VERSION_DIR=/opt/senzing/data/2.0.0
    export SENZING_ETC_DIR=/etc/opt/senzing
    export SENZING_G2_DIR=/opt/senzing/g2
    ```

1. :pencil2: Senzing docker image versions.
   See [latest versions](https://github.com/Senzing/knowledge-base/blob/master/lists/docker-versions-latest.sh).
   Example:

    ```console
    export SENZING_DOCKER_IMAGE_VERSION_INIT_CONTAINER=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_STREAM_LOADER=0.0.0
    ```

2. Synthesized variables.
   Example:

    ```console
    export SENZING_DATABASE_URL="postgresql://${POSTGRES_USERNAME:-postgres}:${POSTGRES_PASSWORD:-postgres}@${POSTGRES_HOST:-senzing-postgres}:${POSTGRES_PORT:-5432}/${POSTGRES_DB:-G2}"

    export SENZING_ENGINE_CONFIGURATION_JSON="{\"PIPELINE\":{\"CONFIGPATH\":\"/etc/opt/senzing\",\"RESOURCEPATH\":\"/opt/senzing/g2/resources\",\"SUPPORTPATH\":\"/opt/senzing/data\"},\"SQL\":{\"CONNECTION\":\"postgresql://${POSTGRES_USERNAME}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}:${POSTGRES_DB}/\"}}"
    ```
