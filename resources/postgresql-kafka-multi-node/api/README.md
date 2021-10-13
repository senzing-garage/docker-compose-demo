# Api node type

## Synopsis

The "api" node type is responsible for
creating a [RESTful HTTP API](https://github.com/Senzing/senzing-rest-api-specification)
on top of the Senzing Engine.

## Environment variables

1. :pencil2: Location of Senzing binary folders on host system.
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
    export SENZING_DOCKER_IMAGE_VERSION_SENZING_API_SERVER=0.0.0
    ```

1. :pencil2: Database connectivity.
   This is used in a "single-database" configuration.
   For multi-database configuration, construct `SENZING_ENGINE_CONFIGURATION_JSON`
   to reflect multi-database configuration.
   Example:

    ```console
    export POSTGRES_DB=G2
    export POSTGRES_HOST=localhost
    export POSTGRES_PASSWORD=my-password
    export POSTGRES_PORT=5432
    export POSTGRES_USERNAME=my-username
    ```

1. Senzing Engine configuration.
   This is a "single-database" example.
   Using "bash shell parameter expansion",
   the database connectivity information is used
   to construct `SENZING_ENGINE_CONFIGURATION_JSON`.
   Example:

    ```console
    export SENZING_ENGINE_CONFIGURATION_JSON="{\"PIPELINE\":{\"CONFIGPATH\":\"/etc/opt/senzing\",\"RESOURCEPATH\":\"/opt/senzing/g2/resources\",\"SUPPORTPATH\":\"/opt/senzing/data\"},\"SQL\":{\"CONNECTION\":\"postgresql://${POSTGRES_USERNAME}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}:${POSTGRES_DB}/\"}}"
    ```
