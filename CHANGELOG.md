# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
[markdownlint](https://dlaa.me/markdownlint/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.13.0] - 2023-03-15

### Changed in 1.13.0

- Move from database specific initializers to `senzing/senzing-tools initdatabase`

## [1.12.1] - 2023-01-16

### Changed in 1.12.1

- Updated README.md documentation
- Migrate from Juypter notebook to Jupyter lab
- Updated location of pgAdmin `servers.json` file
- Refactor how data sources are added for "Truth Set"

## [1.12.0] - 2022-09-12

### Changed in 1.12.0

- Moved to "Truth Set" demonstration data
- Changed directory permissions
- Improved documentation
- Information on ELK stack
- Add `LICENSESTRINGBASE64`
- Remove `ENTITY_TYPE` support

## [1.11.1] - 2022-05-31

### Changed in 1.11.1

- Move from `yum` to `apt` based installation.

## [1.11.0] - 2022-05-11

### Changed in 1.11.0

- Move from senzing data 2.0.0 to 3.0.0

## [1.10.0] - 2022-03-22

### Changed in 1.10.0

- Changed network to `senzing-network` as default name.

## [1.9.0] - 2021-10-28

### Changed in 1.9.0

- Migrate from `senzing-api-server` to `senzing-poc-server`

## [1.8.0] - 2021-10-01

### Changed in 1.8.0

- Improved docker image version management
- Updated documentation
- Moved demonstrations into "advanced" instructions

## [1.7.0] - 2021-08-04

### Changed in 1.7.0

- Add SENZING_ENGINE_CONFIGURATION_JSON to services

## [1.6.1] - 2021-07-22

### Changed in 1.6.1

- Updated README.md files
  - Add information on SSH port
- Change senzing-api-server parameters from command-line to environment variables
- Update docker image version defaults
  - bitnami/kafka:2.4.0 to bitnami/kafka:2.8.0-debian-10-r55
  - bitnami/rabbitmq:3.8.2 to bitnami/rabbitmq:3.8.19-debian-10-r6
  - bitnami/zookeeper:3.5.6 to bitnami/zookeeper:3.7.0-debian-10-r87
  - ibmcom/db2:11.5.0.0a to ibmcom/db2:11.5.5.1
  - mysql:5.7 to bitnami/mysql:5.7.34-debian-10-r70
  - obsidiandynamics/kafdrop:3.23.0 to obsidiandynamics/kafdrop:3.27.0
  - phpmyadmin/phpmyadmin:4.9 to bitnami/phpmyadmin:5.1.1-debian-10-r29
  - postgres:11.6 to bitnami/postgresql:11.12.0-debian-10-r50
  - senzing/console:1.0.1 to senzing/console:1.0.3
  - senzing/init-container:1.6.9 to senzing/init-container:1.6.12
  - senzing/jupyter:1.2.0 to senzing/jupyter:1.3.0
  - senzing/redoer:1.3.5 to senzing/redoer:1.3.9
  - senzing/resolver:1.3.1 to senzing/resolver:1.3.2
  - senzing/senzing-api-server:2.5.0 to senzing/senzing-api-server:2.6.2
  - senzing/sshd:1.1.0 to senzing/sshd:1.2.3
  - senzing/stream-loader:1.7.5 to senzing/stream-loader:1.8.2
  - senzing/stream-producer:1.4.0 to senzing/stream-producer:1.5.1
  - senzing/xterm:1.1.0 to senzing/xterm:1.1.2
  - swaggerapi/swagger-ui to swaggerapi/swagger-ui:v3.51.0

## [1.6.0] - 2021-05-04

### Changed in 1.6.0

- Migration to `senzingdata-2.0.0`
- Change default senzing/sshd port from 22 to 9181
- Update docker image versions
  - senzing/console:1.0.0 to senzing/console:1.0.1
  - senzing/entity-search-web-app:2.2.1 to senzing/entity-search-web-app:2.2.3
  - senzing/init-container:1.6.6 to senzing/init-container:1.6.9
  - senzing/senzing-api-server:2.3.2 to senzing/senzing-api-server:2.5.0
  - senzing/sshd:1.0.3 to senzing/sshd:1.1.0
  - senzing/stream-loader:1.7.2 to senzing/stream-loader:1.7.5
  - senzing/stream-producer:1.3.3 to senzing/stream-producer:1.4.0
  - senzing/yum:1.1.3 to senzing/yum:1.1.4

## [1.5.3] - 2021-04-15

### Added in 1.5.3

- `senzing/jupyter` added to cluster databases
- `senzing/sshd` added for ssh/scp access
- `KAFKA_ADVERTISED_LISTENERS` for Kafka

### Changed in 1.5.3

- Removed `senzing/debug` and added `senzing/console` in its place
- Update docker image versions
  - senzing/stream-producer:1.3.1 to senzing/stream-producer:1.3.3
  - senzing/stream-loader:1.7.0 to senzing/stream-loader:1.7.2
  - senzing/redoer:1.3.4 to senzing/redoer:1.3.5
  - senzing/senzing-api-server:2.3.1 to senzing/senzing-api-server:2.3.2
  - senzing/xterm:1.0.5 to senzing/xterm:1.1.0
- Migrated from `senzing/debug` to `senzing/console`

## [1.5.2] - 2021-02-10

### Added in 1.5.2

- `swaggerapi/swagger-ui` container

### Changed in 1.5.2

- Documentation improvements
- Updated versions of containers

## [1.5.1] - 2020-08-05

### Changed in 1.5.1

- Update invocation to `webapp:`
- Fix database connectivity issues with `redoer:` for Db2 and MS SQL.
- Update docker image versions
  - senzing/jupyter 1.5.5 to 1.2.0

## [1.5.0] - 2020-07-31

### Changed in 1.5.0

- Works with senzing version 2.0.0 and above
- Added "senzing/redoer:1.3.1" to formations
- Update docker image versions
  - senzing/entity-search-web-app:1.2.1 to senzing/entity-search-web-app:2.0.0
  - senzing/init-container:1.5.4 to senzing/init-container:1.5.6
  - senzing/redoer:1.3.0 to senzing/redoer:1.3.1
  - senzing/resolver:1.2.0 to senzing/resolver:1.3.0
  - senzing/senzing-api-server:1.8.3 to senzing/senzing-api-server:2.0.0
  - senzing/senzing-debug:1.3.4 to senzing/senzing-debug:1.3.5
  - senzing/stream-loader:1.5.4 to senzing/stream-loader:1.5.5
  - senzing/stream-producer: 1.1.1 to senzing/stream-producer:1.2.2
  - senzing/xterm:1.0.2 to senzing/xterm:1.0.3

## [1.4.0] - 2020-07-07

### Changed in 1.4.0

- Works with senzing versions up to 1.15.6
- Not supported for senzing version 2.0.0 and above

## [1.3.4] - 2020-03-21

### Added in 1.3.4

- Added advanced scenarios for PostgreSQL, RabbitMQ, and Kafka

### Changed in 1.3.4

- Rename "With-info" to "Withinfo"
- Update docker image versions
  - postgres:11.5 to postgres:11.6
  - senzing/init-container 1.3.3 to 1.5.0
  - senzing/debug 1.2.1 to 1.3.0
  - senzing/stream-loader 1.4.0 to 1.5.3
  - senzing/stream-logger 1.0.0 to 1.0.1
  - senzing/redoer 1.1.0 to 1.2.1

## [1.3.3] - 2020-02-27

### Changed in 1.3.3

- Added `kafdrop`; removed kafka-manager
- Simplified localhost storage ("volumes:")
- Simplified `README.md`
  - Moved "advanced" topics into knowledge-base and linked to them.
  - Using `sudo --preserve-env`

## [1.3.2] - 2020-02-27

### Changed in 1.3.2

- Update versions of docker images
- Senzing docker images updated from `debian:9` to `debian:10.2`
- Added simplified `docker-compose-getting-started`
- Added `docker-compose-rabbitmq-sqlite-governor` example.
- Added `docker-compose-rabbitmq-sqlite-jupyter` example.
- Added spike for "withInfo"

## [1.3.1] - 2020-01-13

### Changed in 1.3.1

- Added demonstration using SQLite Senzing cluster.

## [1.3.0] - 2019-11-13

### Changed in 1.3.0

- Added demonstrations using MSSQL.

## [1.2.0] - 2019-11-01

### Changed in 1.2.0

- Updated versions of underlying docker images.

## [1.1.0] - 2019-08-20

### Changed in 1.1.0

- Moved to RPM-based Senzing installation

## [1.0.1] - 2019-07-18

### Changed in 1.0.1

- Separated "database initialization" into separate docker-compose formation.
  - MySQL
  - PostgreSQL
  - SQLite
- Added tags to images
- Cleaned YAML
- Standardized on `TEST` datasource

## [1.0.0] - 2019-06-05

### Added in 1.0.0

- Initial release.
