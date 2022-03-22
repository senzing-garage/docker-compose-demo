#!/usr/bin/env bash

# Check docker-compose.yaml files.

# Get absolute path.

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"

# Identify subdirectories in .../docker-compose-demo/resources.

RESOURCES_DIRECTORIES=(
    "custom"
    "db2"
    "mssql"
    "mysql"
    "postgresql"
    "sqlite"
)

# For each subdirectory in "resources":

for RESOURCES_DIRECTORY in ${RESOURCES_DIRECTORIES[@]}; do

    # Verify each docker-compose.yaml file.

    for DOCKER_COMPOSE_FILE in ${SCRIPT_DIR}/../resources/${RESOURCES_DIRECTORY}/* ; do
        echo "Processing:  ${DOCKER_COMPOSE_FILE}"
        docker-compose -f ${DOCKER_COMPOSE_FILE} config > /dev/null
    done
done
