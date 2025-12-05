# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `docker-compose-demo`, a collection of Docker Compose files for demonstrating Senzing entity resolution. It's part of the Senzing Garage (experimental/demo projects, not production-ready).

## Repository Structure

- `docker-compose/` - Docker Compose YAML files for different database backends:
  - `senzing-docker-compose-postgresql.yaml` - PostgreSQL (primary example)
  - `senzing-docker-compose-postgresql-multi.yaml` - PostgreSQL multi-instance for version comparison
  - `senzing-docker-compose-mysql.yaml` - MySQL
  - `senzing-docker-compose-mssql.yaml` - MS SQL Server
  - `senzing-docker-compose-sqlite.yaml` - SQLite
- `docs/` - Documentation (services.md, examples.md, development.md, errors.md)

## Docker Compose Profiles

All compose files use profiles to control formation behavior:

- `new` - Fresh database with Senzing schema and config, no data
- `resume` - Bring up existing formation with preserved data
- `truthset` - Fresh database with Senzing TruthSets pre-loaded

## Common Commands

Start a formation (example with PostgreSQL):

```bash
docker compose --profile truthset --file docker-compose/senzing-docker-compose-postgresql.yaml up --pull always
```

Stop formation (preserving data):

```bash
docker compose --profile truthset --file docker-compose/senzing-docker-compose-postgresql.yaml down
```

Stop formation and delete volumes:

```bash
docker compose --profile truthset --file docker-compose/senzing-docker-compose-postgresql.yaml down --volumes
```

Access the Senzing tools container:

```bash
docker exec -it senzingsdk-tools /bin/bash
```

## Architecture

Each compose file defines a self-contained formation with:

1. **Database service** - The backend database (postgres, mysql, mssql, or sqlite)
2. **Database init service** - Initializes Senzing schema/config (profile: `new`) or loads TruthSets (profile: `truthset`)
3. **DB admin tool** - Web UI for database administration (PgAdmin, PhpMyAdmin, Adminer, or Sqlite-Web)
4. **senzingsdk-tools** - Container with Senzing CLI tools (sz_explorer, etc.)
5. **makefile service** - Creates configuration files for DB admin tools

Key environment variables:

- `SENZING_DOCKER_IMAGE_VERSION_*` - Override image versions
- `SENZING_LICENSE_BASE64_ENCODED` - Senzing license
- `SENZING_UID`/`SENZING_GID` - Container user/group IDs
- `SENZING_DOCKER_NETWORK` - Docker network name (default: senzing-network)

## DB Admin Ports

- PgAdmin (PostgreSQL): <http://localhost:9171>
- PhpMyAdmin (MySQL): <http://localhost:9173>
- Adminer (MSSQL): <http://localhost:9177>
- Sqlite-Web (SQLite): <http://localhost:9174>

## Development Prerequisites

- Docker with `docker compose` command
- Git
