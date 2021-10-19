# Webapp node type

## Synopsis

The "webapp" node type deploys the
[Senzing Entity Search Web app](https://github.com/Senzing/entity-search-web-app).
which can be used to visually inspect the Senzing Mode.

## Environment variables

1. :pencil2: Identify Senzing docker image versions.
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

1. :pencil2: Senzing API Server connectivity.
   **Note:** This may point to an ephemeral port for one of the senzing-api-server containers
   or may point to the service created by using a load-balancer or proxy server.
   Example:

    ```console
    export SENZING_API_SERVER_URL=http://10.0.0.3:8250
    ```

1. :pencil2: Senzing Web Server connectivity.
   Example:

    ```console
    export SENZING_WEB_SERVER_ADMIN_AUTH_PATH=http://10.0.0.4:8251
    export SENZING_WEB_SERVER_URL=http://10.0.0.4:8251
    ```

## Run docker formation

1. :pencil2: Identify directory having "webapp" node artifacts.
   Example:

    ```console
    export SENZING_DOCKER_COMPOSE_DIR=~/senzing.git/docker-compose-demo/resources/postgresql-kafka-multi-node/webapp
    ```

1. Bring up Senzing formation.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose \
        --file docker-compose-webapp.yaml \
        up
    ```
