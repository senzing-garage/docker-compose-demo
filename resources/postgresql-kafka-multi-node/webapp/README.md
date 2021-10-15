# Webapp node type

## Synopsis

The "loader" node type is responsible for
reading messages from a Kafka Topic
and sending the messages to the Senzing Engine.

## Environment variables

1. :pencil2: Senzing API Server connectivity.
   Example:

    ```console
    export SENZING_API_SERVER_URL=http://localhost:8250
    ```

1. :pencil2: Senzing API Server connectivity.
   Example:

    ```console
    export SENZING_WEB_SERVER_ADMIN_AUTH_PATH=http://localhost:8251
    export SENZING_WEB_SERVER_URL: http://senzing-webapp:8251

    ```

1. :pencil2: Senzing docker image versions.
   See [latest versions](https://github.com/Senzing/knowledge-base/blob/master/lists/docker-versions-latest.sh).
   Example:

    ```console
    export SENZING_DOCKER_IMAGE_VERSION_ENTITY_SEARCH_WEB_APP=0.0.0
    ```

   :thinking: **Alternative method:**
   This method identifies the latest versions of each Docker image.

    ```console
    source <(curl -X GET https://raw.githubusercontent.com/Senzing/knowledge-base/master/lists/docker-versions-latest.sh)
    ```

## Run docker formation

1. :pencil2: Identify directory having "webapp" node artifacts.
   Example:

    ```console
    export SENZING_DOCKER_COMPOSE_DIR=~/senzing.git/docker-compose-demo/resources/postgresql-kafka-multi-node/webapp
    ```

1. Bring Senzing formation.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose --file docker-compose-webapp.yaml up
    ```
