# Mocks

## Synopsis

"mocks" are used for localized testing.
They are not part of a production environment.

The mock services provisioned are:

- Zookeeper
- Kafka
- KafDrop
- PostgreSQL
- Senzing Stream-producer
- PhpPgAdmin

## Environment variables

1. :pencil2: Identify location of Senzing binary folders on host system.
   Example:

    ```console
    export SENZING_DATA_VERSION_DIR=/opt/senzing/data/2.0.0
    export SENZING_ETC_DIR=/etc/opt/senzing
    export SENZING_G2_DIR=/opt/senzing/g2
    ```

1. :pencil2: Identify Senzing docker image versions.
   See [latest versions](https://github.com/Senzing/knowledge-base/blob/master/lists/docker-versions-latest.sh).
   Example:

    ```console
    export SENZING_DOCKER_IMAGE_VERSION_BITNAMI_KAFKA=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_BITNAMI_PHPPGADMIN=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_BITNAMI_POSTGRESQL=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_BITNAMI_ZOOKEEPER=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_INIT_CONTAINER=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_OBSIDIANDYNAMICS_KAFDROP=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_POSTGRESQL_CLIENT=0.0.0
    export SENZING_DOCKER_IMAGE_VERSION_STREAM_PRODUCER=0.0.0
    ```

   :thinking: **Alternative method:**
   This method identifies the latest versions of each Docker image.

    ```console
    source <(curl -X GET https://raw.githubusercontent.com/Senzing/knowledge-base/master/lists/docker-versions-latest.sh)
    ```

## Run docker formation

1. :pencil2: Identify directory having mock artifacts.
   Example:

    ```console
    export SENZING_DOCKER_COMPOSE_DIR=~/senzing.git/docker-compose-demo/resources/postgresql-kafka-multi-node/mocks
    ```

1. Bring Senzing formation.
   Example:

    ```console
    cd ${SENZING_DOCKER_COMPOSE_DIR}
    sudo \
      --preserve-env \
      docker-compose --file docker-compose-mocks.yaml up
    ```

## View data

Once the docker-compose formation is running,
different aspects of the formation can be viewed.

### View docker containers

1. A good tool to monitor individual docker logs is
   [Portainer](https://github.com/Senzing/knowledge-base/blob/master/WHATIS/portainer.md).
   When running, Portainer is viewable at
   [localhost:9170](http://localhost:9170).

### View Kafka

1. Kafdrop is viewable at
   [localhost:9179](http://localhost:9179).

### View PostgreSQL

1. PostgreSQL is viewable at
   [localhost:9171](http://localhost:9171).
    1. **Defaults:** username: `postgres` password: `postgres`
