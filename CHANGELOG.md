# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
[markdownlint](https://dlaa.me/markdownlint/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
