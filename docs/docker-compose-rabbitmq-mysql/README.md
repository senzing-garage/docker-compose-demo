# docker-compose-rabbitmq-mysql

## Overview

This repository illustrates a reference implementation of Senzing using
RabbitMQ as the queue and
MySQL as the underlying database.

The instructions show how to set up a system that:

1. Reads JSON lines from a file on the internet.
1. Sends each JSON line to a message queue.
    1. In this implementation, the queue is RabbitMQ.
1. Reads messages from the queue and inserts into Senzing.
    1. In this implementation, Senzing keeps its data in a MySQL database.
1. Reads information from Senzing via [Senzing REST API](https://github.com/Senzing/senzing-rest-api) server.

The following diagram shows the relationship of the docker containers in this docker composition.

![Image of architecture](architecture.png)

This docker formation brings up the following docker containers:

1. *[bitnami/rabbitmq](https://github.com/bitnami/bitnami-docker-rabbitmq)*
1. *[mysql](https://github.com/docker-library/mysql)*
1. *[phpmyadmin/phpmyadmin](https://github.com/phpmyadmin/docker)*
1. *[senzing/mock-data-generator](https://github.com/Senzing/mock-data-generator)*
1. *[senzing/mysql-init](https://github.com/Senzing/docker-mysql-init)*
1. *[senzing/senzing-base](https://github.com/Senzing/docker-senzing-base)*
1. *[senzing/stream-loader](https://github.com/Senzing/stream-loader)*
1. *[senzing/senzing-api-server](https://github.com/Senzing/senzing-api-server)*

### Contents

1. [Expectations](#expectations)
    1. [Space](#space)
    1. [Time](#time)
    1. [Background knowledge](#background-knowledge)
1. [Preparation](#preparation)
    1. [Prerequisite software](#prerequisite-software)
    1. [Clone repository](#clone-repository)
    1. [Create SENZING_DIR](#create-senzing_dir)
1. [Using docker-compose](#using-docker-compose)
    1. [Build docker images](#build-docker-images)
    1. [Configuration](#configuration)
    1. [Run docker formation](#run-docker-formation)
    1. [View data](#view-data)
    1. [Test Senzing API](#test-senzing-api)
1. [Cleanup](#cleanup)

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

### Clone repository

For more information on environment variables,
see [Environment Variables](https://github.com/Senzing/knowledge-base/blob/master/lists/environment-variables.md).

1. Set these environment variable values:

    ```console
    export GIT_ACCOUNT=senzing
    export GIT_REPOSITORY=docker-compose-demo
    ```

1. Follow steps in [clone-repository](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/clone-repository.md) to install the Git repository.

1. After the repository has been cloned, be sure the following are set:

    ```console
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"
    ```

### Create SENZING_DIR

If you do not already have an `/opt/senzing` directory on your local system, visit
[HOWTO - Create SENZING_DIR](https://github.com/Senzing/knowledge-base/blob/master/HOWTO/create-senzing-dir.md).

## Using docker-compose

### Build docker images

1. Build docker images.

    ```console
    sudo docker build \
      --tag senzing/mysql-init \
      https://github.com/senzing/docker-mysql-init.git
    ```

### Configuration

* **MYSQL_DATABASE** -
  Database name.
  Default: "G2"
* **MYSQL_PASSWORD** -
  Password for MYSQL_USERNAME.
  Default: "g2"
* **MYSQL_ROOT_PASSWORD** -
  The password for the the database "root" user name.
  Default: "root"
* **MYSQL_STORAGE** -
  Path on local system where the database files are stored.
  Default: "/storage/docker/senzing/docker-compose-rabbitmq-mysql/mysql"
* **MYSQL_USERNAME** -
  Non-root MySQL user.
  Default: "g2"
* **RABBITMQ_STORAGE** -
  Path on local system where RabbitMQ files are stored.
  Default: "/storage/docker/senzing/docker-compose-rabbitmq-mysql/rabbitmq"
* **SENZING_DIR** -
  Path on the local system where
  [Senzing_API.tgz](https://s3.amazonaws.com/public-read-access/SenzingComDownloads/Senzing_API.tgz)
  has been extracted.
  See [Create SENZING_DIR](#create-senzing_dir).
  No default.
  Usually set to "/opt/senzing".
* See [github.com/Senzing/docker-mysql](https://github.com/Senzing/docker-mysql)
  for more details on how to find values for other **MYSQL_** environment variables.

### Run docker formation

1. :pencil2: Set environment variables.  Example:

    ```console
    export MYSQL_DATABASE=G2
    export MYSQL_ROOT_PASSWORD=root
    export MYSQL_STORAGE=/storage/docker/senzing/docker-compose-rabbitmq-mysql/mysql
    export RABBITMQ_STORAGE=/storage/docker/senzing/docker-compose-rabbitmq-mysql/rabbitmq
    export SENZING_DIR=/opt/senzing
    ```

1. Create directories.  Example:

    ```console
    sudo mkdir -p ${RABBITMQ_STORAGE}
    sudo chmod 777 ${RABBITMQ_STORAGE}
    ```

1. Initialize database.  Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    sudo \
      MYSQL_DATABASE=${MYSQL_DATABASE} \
      MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
      MYSQL_STORAGE=${MYSQL_STORAGE} \
      SENZING_DIR=${SENZING_DIR} \
      docker-compose --file docker-compose-mysql-initialization.yaml up
    ```

1. Bring down database initialization.  Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    sudo docker-compose --file docker-compose-mysql-initialization.yaml down
    ```

1. Launch docker-compose formation.  Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    sudo \
      MYSQL_DATABASE=${MYSQL_DATABASE} \
      MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
      MYSQL_STORAGE=${MYSQL_STORAGE} \
      RABBITMQ_STORAGE=${RABBITMQ_STORAGE} \
      SENZING_DIR=${SENZING_DIR} \
      docker-compose --file docker-compose-rabbitmq-mysql.yaml up
    ```

### View data

1. Username and password for the following sites were either passed in as environment variables
   or are the default values seen in
   [docker-compose-rabbitmq-mysql.yaml](../../docker-compose-rabbitmq-mysql.yaml).
1. RabbitMQ is viewable at [localhost:15672](http://localhost:15672)
1. MySQL is viewable at [localhost:8080](http://localhost:8080).
    1. The records received from the queue can be viewed in the following Senzing tables:
        1. G2 > DSRC_RECORD
        1. G2 > OBS_ENT

### Test Senzing API

1. Wait for the following message in the terminal showing docker log.

    ```console
    senzing-api-server | Started Senzing REST API Server on port 8080.
    senzing-api-server |
    senzing-api-server | Server running at:
    senzing-api-server | http://0.0.0.0:8080/
    ```

1. Test Senzing REST API server.
   *Note:*  In
   [docker-compose-rabbitmq-mysql.yaml](../../docker-compose-rabbitmq-mysql.yaml)
   port 8889 on the localhost has been mapped to port 8080 in the docker container.
   Example:

    ```console
    export SENZING_API_SERVICE=http://localhost:8889

    curl -X GET ${SENZING_API_SERVICE}/heartbeat
    curl -X GET ${SENZING_API_SERVICE}/license
    curl -X GET ${SENZING_API_SERVICE}/entities/1
    ```

## Cleanup

In a separate (or reusable) terminal window:

1. Use environment variable describe in "[Clone repository](#clone-repository)" and "[Configuration](#configuration)".
1. Run `docker-compose` command.

    ```console
    cd ${GIT_REPOSITORY_DIR}
    sudo docker-compose --file docker-compose-rabbitmq-mysql.yaml down
    ```

1. Delete storage.

    ```console
    sudo rm -rf ${MYSQL_STORAGE}
    sudo rm -rf ${RABBITMQ_STORAGE}
    ```

1. Delete SENZING_DIR.

    ```console
    sudo rm -rf ${SENZING_DIR}
    ```

1. Delete git repository.

    ```console
    sudo rm -rf ${GIT_REPOSITORY_DIR}
    ```
