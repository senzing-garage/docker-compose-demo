# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
[markdownlint](https://dlaa.me/markdownlint/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.6.1] - 2021-05-04

### Changed in 1.6.1

- Change default senzing/sshd port from 22 to 9181

## [1.6.0] - 2021-04-19

### Changed in 1.6.0

- Migration to `senzingdata-2.0.0`
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

### Changed in 1.5.3

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
