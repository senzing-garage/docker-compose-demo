# docker-compose-demo

## Overview

This repository illustrates reference implementations of Senzing using docker-compose.

The instructions show how to set up a system that:

1. Reads JSON lines from a file on the internet.
1. Sends each JSON line as a message to a queue.
1. Reads messages from the queue and inserts into Senzing.
1. Reads information from Senzing via [Senzing REST API](https://github.com/Senzing/senzing-rest-api) server.
1. Views resolved entities in a web app.

The following diagram shows the relationship of the docker containers in this docker composition.
Arrows represent data flow.

![Image of architecture](docs/img-architecture/architecture.png)

## Implementation

The following table indicates the instructions for variations in components.

1. Component variants:
    1. Queue
        1. RabbitMQ
        1. Kafka
    1. Database
        1. Postgres
        1. MySQL
        1. Db2
        1. SQLite
1. Implementations of the docker formation:

    | Queue    | Database   | Instructions | docker-compose.yaml |
    |----------|------------|:------------:|---------------------|
    | Kafka    | Db2        | [:page_facing_up:](docs/docker-compose-kafka-db2/README.md)           | [docker-compose-kafka-db2.yaml](resources/db2/docker-compose-kafka-db2.yaml) |
    | Kafka    | MySQL      | [:page_facing_up:](docs/docker-compose-kafka-mysql/README.md)         | [docker-compose-kafka-mysql.yaml](resources/mysql/docker-compose-kafka-mysql.yaml) |
    | Kafka    | PostgreSQL | [:page_facing_up:](docs/docker-compose-kafka-postgresql/README.md)    | [docker-compose-kafka-postgresql.yaml](resources/postgresql/docker-compose-kafka-postgresql.yaml) |
    | Kafka    | SQLite     | [:page_facing_up:](docs/docker-compose-kafka-sqlite/README.md)        | [docker-compose-kafka-sqlite.yaml](resources/sqlite/docker-compose-kafka-sqlite.yaml) |
    | RabbitMQ | Db2        | [:page_facing_up:](docs/docker-compose-rabbitmq-db2/README.md)        | [docker-compose-rabbitmq-db2.yaml](resources/db2/docker-compose-rabbitmq-db2.yaml) |
    | RabbitMQ | MySQL      | [:page_facing_up:](docs/docker-compose-rabbitmq-mysql/README.md)      | [docker-compose-rabbitmq-mysql.yaml](resources/mysql/docker-compose-rabbitmq-mysql.yaml) |
    | RabbitMQ | PostgreSQL | [:page_facing_up:](docs/docker-compose-rabbitmq-postgresql/README.md) | [docker-compose-rabbitmq-postgresql.yaml](resources/postgresql/docker-compose-rabbitmq-postgresql.yaml) |
    | RabbitMQ | SQLite     | [:page_facing_up:](docs/docker-compose-rabbitmq-sqlite/README.md)     | [docker-compose-rabbitmq-sqlite.yaml](resources/sqlite/docker-compose-rabbitmq-sqlite.yaml) |
