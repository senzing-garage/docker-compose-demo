# docker-compose-demo services

All Docker Compose formations include:

- [senzingsdk-tools]

Services offered by specific Docker Compose formations:

| Docker compose file                                     | [DB Admin]   | [TruthSet]         |
|---------------------------------------------------------|--------------|:------------------:|
| [senzing-docker-compose-mssql.yaml]                     | [Adminer]    |                    |
| [senzing-docker-compose-mysql.yaml]                     | [PhpMyAdmin] |                    |
| [senzing-docker-compose-postgresql-truthset-multi.yaml] | [PgAdmin]    | :white_check_mark: |
| [senzing-docker-compose-postgresql-truthset.yaml]       | [PgAdmin]    | :white_check_mark: |
| [senzing-docker-compose-postgresql.yaml]                | [PgAdmin]    |                    |
| [senzing-docker-compose-sqlite-truthset.yaml]           | [Sqlite-Web] | :white_check_mark: |
| [senzing-docker-compose-sqlite.yaml]                    | [Sqlite-Web] |                    |

## senzingsdk-tools

The [senzing/senzingsdk-tools] Docker image contains Senzing tools for analyzing Senzing information.

1. In a separate terminal, use `docker exec` to enter the `senzing/senzingsdk-tools` Docker container.

   ```console
   docker exec -it senzingsdk-tools /bin/bash
   ```

   *Note:* In docker-compose files ending with `-multi.yaml`, the name of the docker container may differ.

## DB Admin

The database administration tools are for the following databases:

- [Adminer] MS SQL
- [PgAdmin] Postgres
- [PhpMyAdmin] MySQL
- [Sqlite-Web] SQLite

### Adminer

A MS SQL database administration tool.

1. View at [localhost:9177](http://localhost:9177)
   1. *System:* MS SQL (beta)
   1. *Server:* senzing-mssql
   1. *Username:* sa
   1. *Password:* Passw0rd
   1. *Database:* G2
1. Adminer homepage: [https://www.adminer.org/en/]

### PgAdmin

A Postgres database administration tool.

1. View at [localhost:9171](http://localhost:9171)
   1. When prompted for PgAdmin credentials, read the information in the "Senzing demonstration" section.
   1. When prompted for the *database* (not PgAdmin) password, enter `postgres`.
1. Pgadmin4 homepage: [github.com/dpage/pgadmin4]

### PhpMyAdmin

A MySQL database administration tool.

1. View at [localhost:9173](http://localhost:9173)
   1. Username: mysql
   1. Password: mysql
1. PhpMyAdmin homepage: [https://www.phpmyadmin.net/]

### Sqlite-Web

An SQLite database administration tool.

1. View at [localhost:9174](http://localhost:9174)
1. Sqlite-web homepage: [github.com/coleifer/sqlite-web]

## TruthSet

The [Senzing Truthsets] are a curated set of data sources and records to illustrate
principles of Entity Resolution.

[Adminer]: #adminer
[DB Admin]: #db-admin
[github.com/coleifer/sqlite-web]: https://github.com/coleifer/sqlite-web
[github.com/dpage/pgadmin4]: https://github.com/dpage/pgadmin4
[https://www.adminer.org/en/]: https://www.adminer.org/en/
[https://www.phpmyadmin.net/]: https://www.phpmyadmin.net
[PgAdmin]: #pgadmin
[PhpMyAdmin]: #phpmyadmin
[Senzing Truthsets]: https://github.com/Senzing/truth-sets
[senzing-docker-compose-mssql.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/main/docker-compose/senzing-docker-compose-mssql.yaml
[senzing-docker-compose-mysql.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/main/docker-compose/senzing-docker-compose-mysql.yaml
[senzing-docker-compose-postgresql-truthset-multi.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/main/docker-compose/senzing-docker-compose-postgresql-truthset-multi.yaml
[senzing-docker-compose-postgresql-truthset.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/main/docker-compose/senzing-docker-compose-postgresql-truthset.yaml
[senzing-docker-compose-postgresql.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/main/docker-compose/senzing-docker-compose-postgresql.yaml
[senzing-docker-compose-sqlite-truthset.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/main/docker-compose/senzing-docker-compose-sqlite-truthset.yaml
[senzing-docker-compose-sqlite.yaml]: https://github.com/senzing-garage/docker-compose-demo/blob/main/docker-compose/senzing-docker-compose-sqlite.yaml
[senzing/senzingsdk-tools]: https://github.com/Senzing/senzingsdk-tools
[senzingsdk-tools]: #senzingsdk-tools
[Sqlite-Web]: #sqlite-web
[TruthSet]: #truthset
