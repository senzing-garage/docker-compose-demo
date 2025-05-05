# docker-compose-demo

If you are beginning your journey with [Senzing],
please start with [Senzing Quick Start guides].

You are in the [Senzing Garage] where projects are "tinkered" on.
Although this GitHub repository may help you understand an approach to using Senzing,
it's not considered to be "production ready" and is not considered to be part of the Senzing product.
Heck, it may not even be appropriate for your application of Senzing!

## Synopsis

Using `docker-compose`, bring up a Senzing stack.

## Overview

This repository illustrates reference implementations of Senzing using docker-compose.

The instructions show how to set up a system that:

1. Reads JSON lines from a file on the internet and sends each JSON line to a message queue via the Senzing
   [stream-producer].
1. Reads messages from the queue and inserts into Senzing via the Senzing
   [stream-loader].
1. Reads information from Senzing via [Senzing API Server] server.
1. Views resolved entities in a [web app].

The following diagram shows the relationship of the docker containers in this docker composition.
Arrows represent data flow.

![Image of architecture]

## Caveat

This demonstration runs on platforms that support `docker` and `docker-compose`.

:warning: RedHat has explicitly stated that [Docker is not supported in RHEL 8].
As such, these demonstrations of Senzing using `docker` and `docker-compose`
do not run in a RedHat Enterprise Linux 8 environment natively.
Likewise, `docker` is not a CentOS 8 supported project.
Although with user-modification it has been shown that docker and docker-compose can run in these environments,
the onus is on the user for proper operation of docker and docker networking.

## Implementation

The following tables indicate the instructions for variations in components.

1. Component variants:
   1. Queue
      1. RabbitMQ
      1. Kafka
      1. AWS SQS
   1. Database
      1. Postgres
      1. MySQL
      1. MS SQL
1. Implementations of the docker formation:

   | Queue    | Database   |            Instructions            | docker-compose.yaml                       |
   | -------- | ---------- | :--------------------------------: | ----------------------------------------- |
   | RabbitMQ | PostgreSQL | [rabbitmq postgresql instructions] | [docker-compose-rabbitmq-postgresql.yaml] |
   | RabbitMQ | MySQL      |   [rabbitmq mysql instructions]    | [docker-compose-rabbitmq-mysql.yaml]      |
   | RabbitMQ | MSSQL      |   [rabbitmq mssql instructions]    | [docker-compose-rabbitmq-mssql.yaml]      |
   | Kafka    | PostgreSQL |  [kafka postgresql instructions]   | [docker-compose-kafka-postgresql.yaml]    |
   | Kafka    | MySQL      |     [kafka mysql instructions]     | [docker-compose-kafka-mysql.yaml]         |
   | Kafka    | MSSQL      |     [kafka mssql instructions]     | [docker-compose-kafka-mssql.yaml]         |
   | AWS SQS  | PostgreSQL | [aws sqs postgresql instructions]  | [docker-compose-sqs-postgresql.yaml]      |

1. Advanced docker formations:

   | Description                                      |      Instructions       |
   | ------------------------------------------------ | :---------------------: |
   | Enhancements built upon PostgreSQL and RabbitMQ. | [rabbitmq instructions] |
   | Enhancements built upon PostgreSQL and Kafka.    |  [kafka instructions]   |
   | Enhancements built upon PostgreSQL and AWS SQS.  | [aws sqs instructions]  |

[aws sqs instructions]: docs/docker-compose-sqs-postgresql-advanced/README.md
[aws sqs postgresql instructions]: docs/docker-compose-sqs-postgresql/README.md
[Docker is not supported in RHEL 8]: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index#con_running-containers-without-docker_assembly_starting-with-containers
[docker-compose-kafka-mssql.yaml]: resources/mssql/docker-compose-kafka-mssql.yaml
[docker-compose-kafka-mysql.yaml]: resources/mysql/docker-compose-kafka-mysql.yaml
[docker-compose-kafka-postgresql.yaml]: resources/postgresql/docker-compose-kafka-postgresql.yaml
[docker-compose-rabbitmq-mssql.yaml]: resources/mssql/docker-compose-rabbitmq-mssql.yaml
[docker-compose-rabbitmq-mysql.yaml]: resources/mysql/docker-compose-rabbitmq-mysql.yaml
[docker-compose-rabbitmq-postgresql.yaml]: resources/postgresql/docker-compose-rabbitmq-postgresql.yaml
[docker-compose-sqs-postgresql.yaml]: resources/postgresql/docker-compose-sqs-postgresql.yaml
[Image of architecture]: docs/img-architecture/architecture.png
[kafka instructions]: docs/docker-compose-kafka-postgresql-advanced/README.md
[kafka mssql instructions]: docs/docker-compose-kafka-mssql/README.md
[kafka mysql instructions]: docs/docker-compose-kafka-mysql/README.md
[kafka postgresql instructions]: docs/docker-compose-kafka-postgresql/README.md
[rabbitmq instructions]: docs/docker-compose-rabbitmq-postgresql-advanced/README.md
[rabbitmq mssql instructions]: docs/docker-compose-rabbitmq-mssql/README.md
[rabbitmq mysql instructions]: docs/docker-compose-rabbitmq-mysql/README.md
[rabbitmq postgresql instructions]: docs/docker-compose-rabbitmq-postgresql/README.md
[Senzing API Server]: https://github.com/senzing-garage/senzing-api-server
[Senzing Garage]: https://github.com/senzing-garage
[Senzing Quick Start guides]: https://docs.senzing.com/quickstart/
[Senzing]: https://senzing.com/
[stream-loader]: https://github.com/senzing-garage/stream-loader
[stream-producer]: https://github.com/senzing-garage/stream-producer
[web app]: https://github.com/senzing-garage/entity-search-web-app
