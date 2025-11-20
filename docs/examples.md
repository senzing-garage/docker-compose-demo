# docker-compose-demo examples

## Truthset on Postgresql

This is a one-and-done set of instructions for bringing up a tool in the
`senzing/senzingsdk-tools` Docker image.
The database is deleted when the docker-compose formation is brought down.

1. Prerequisites:
    1. `docker compose` or `docker-compose`.

        ```console
        docker compose version
        ```

        ```console
        docker-compose version
        ```

        If neither is installed, visit [What is Docker-Compose].

        If only `docker-compose` is installed, the instructions will need to use `docker-compose` instead of `docker compose`.

1. Download docker-compose file.

    ```console
    curl -O https://raw.githubusercontent.com/senzing-garage/docker-compose-demo/refs/heads/main/docker-compose/senzing-docker-compose-postgresql.yaml
    ```

1. Bring up docker-compose formation.

    ```console
    docker compose --profile new --file senzing-docker-compose-postgresql-truthset.yaml up --pull always
    ```

1. In a separate terminal, exec into the `senzing/senzingsdk-tools` container.

    ```console
    docker exec -it senzingsdk-tools /bin/bash
    ```

    1. Tips for importing/exporting files from
    *Note:* To import/export data from the Docker container, use the `/var/opt/senzing` directory.
    This may be mapped to one of the following locations on localhost:

        - Linux: `/var/lib/docker/volumes`
        - macOS: Use Docker.Desktop > Volumes > senzing-docker-compose-postgresql-truthset_user-data-volume
        - Alternatives:

            Export from container:

            ```console
            docker cp senzingsdk-tools:/var/opt/senzing/* /tmp/from-container/
            ```

            Import into container:

            ```console
            docker cp /tmp/to-container/* senzingsdk-tools:/var/opt/senzing
            ```

1. In the `senzingsdk-tools` docker container, run the `sz_explorer` tool.

    ```console
    sz_explorer
    ```

1. In `sz_explorer`, run `quick_look`.

    ```console
    quick_look
    ```

1. To view database in a web browser, visit [PgAdmin4] at [localhost:9171]
    1. Username and password are in dialog box.
    1. Password for postgres database: postgres

1. Bring docker-compose formation down and delete the attached volumes.

    ```console
    docker compose --profile new --file senzing-docker-compose-postgresql-truthset.yaml down --volumes
    ```

## Reusable Truthset on Postgresql

This is a set of instructions for repeatedly bringing and down a docker-compose formation.
It demonstrates using a tool in the `senzing/senzingsdk-tools` Docker image.

1. Prerequisites:
    1. `docker compose` or `docker-compose`.

        ```console
        docker compose version
        ```

        ```console
        docker-compose version
        ```

        If neither is installed, visit [What is Docker-Compose].

        If only `docker-compose` is installed, the instructions will need to use `docker-compose` instead of `docker compose`.

1. Download docker-compose file.

    ```console
    curl -O https://raw.githubusercontent.com/senzing-garage/docker-compose-demo/refs/heads/main/docker-compose/senzing-docker-compose-postgresql.yaml
    ```

1. Bring up the initial docker-compose formation.

    1. Bring up docker-compose formation using `--profile new`.

        ```console
        docker compose --profile new --file senzing-docker-compose-postgresql-truthset.yaml up --pull always
        ```

    1. In a separate terminal, exec into the `senzing/senzingsdk-tools` container.

        ```console
        docker exec -it senzingsdk-tools /bin/bash
        ```

    1. In the `senzingsdk-tools` docker container, run the `sz_explorer` tool.

        ```console
        sz_explorer
        ```

    1. In `sz_explorer`, run `quick_look`

        ```console
        quick_look
        ```

    1. To view database in a web browser, visit [PgAdmin4] at [localhost:9171]
        1. Username and password are in dialog box.
        1. Password for postgres database: postgres

    1. Bring docker-compose formation down, but leave the attached volumes intact so the formation can be reused.

        ```console
        docker compose --profile new --file senzing-docker-compose-postgresql-truthset.yaml down
        ```

1. Bring up the same docker-compose formation again.

    1. Bring up docker-compose formation using `--profile resume`.

        ```console
        docker compose --profile resume --file senzing-docker-compose-postgresql-truthset.yaml up
        ```

    1. In a separate terminal, exec into the `senzing/senzingsdk-tools` image.

        ```console
        docker exec -it senzingsdk-tools /bin/bash
        ```

    1. In the `senzingsdk-tools` docker container, run the `sz_explorer` tool.

        ```console
        sz_explorer
        ```

    1. In `sz_explorer`, run `quick_look`

        ```console
        quick_look
        ```

    1. Bring docker-compose formation down, but leave the attached volumes intact so the formation can be reused.

        ```console
        docker compose --profile new --file senzing-docker-compose-postgresql-truthset.yaml down
        ```

1. Cleanup.  When the database is not longer needed, the docker-compose formation is brought down with the
   `--volumes` command option.

    1. Bring docker-compose formation down and delete the attached volumes.

        ```console
        docker compose --profile resume --file senzing-docker-compose-postgresql-truthset.yaml down --volumes
        ```

## Compare different versions

Bring up separate docker compose formations
by modifying the [--project-name] commandline option
and specifying the version of `senzing/senzingsdk-tools` via
the `SENZING_DOCKER_IMAGE_VERSION_SENZING_SENZINGSDK_TOOLS` environment variable.

1. Prerequisites:
    1. `docker compose` or `docker-compose`.

        ```console
        docker compose version
        ```

        ```console
        docker-compose version
        ```

        If neither is installed, visit [What is Docker-Compose].

        If only `docker-compose` is installed, the instructions will need to use `docker-compose` instead of `docker compose`.

1. Download docker-compose file.

    ```console
    curl -O https://raw.githubusercontent.com/senzing-garage/docker-compose-demo/refs/heads/main/docker-compose/senzing-docker-compose-postgresql-multi.yaml
    ```

1. Bring up first Senzing version.

    1. Bring up docker-compose formation with Senzing version 4.0.0.

       :pencil2: Replace `4.0.0` and `senzing-4_0_0` with desired Senzing version.

        ```console
        export SENZING_DOCKER_IMAGE_VERSION_SENZING_SENZINGSDK_TOOLS=4.0.0
        docker compose --project-name senzing-4_0_0 --profile new --file senzing-docker-compose-postgresql-truthset-multi.yaml up --pull always
        ```

    1. In a separate terminal, exec into the `senzing/senzingsdk-tools` container.

       :pencil2: Replace `senzing-4_0_0` with desired Senzing version.

        ```console
        docker exec -it senzing-4_0_0-senzingsdk-tools /bin/bash
        ```

    1. In the `senzingsdk-tools` docker container, verify Senzing version.

        ```console
        cat /opt/senzing/er/szBuildVersion.json
        ```

    1. In the `senzingsdk-tools` docker container, run the `sz_explorer` tool.

        ```console
        sz_explorer
        ```

    1. In `sz_explorer`, run `quick_look`.

        ```console
        quick_look
        ```

1. Bring up second Senzing version.

    1. In a separate terminal, bring up docker-compose formation with Senzing version 4.1.0.

       :pencil2: Replace `4.1.0` and `senzing-4_1_0` with desired Senzing version.

        ```console
        export SENZING_DOCKER_IMAGE_VERSION_SENZING_SENZINGSDK_TOOLS=4.1.0
        docker compose --project-name senzing-4_1_0 --profile new --file senzing-docker-compose-postgresql-truthset-multi.yaml up --pull always
        ```

    1. In a separate terminal, exec into the `senzing/senzingsdk-tools` container.

       :pencil2: Replace `senzing-4_1_0` with desired Senzing version.

        ```console
        docker exec -it senzing-4_1_0-senzingsdk-tools /bin/bash
        ```

    1. In the `senzingsdk-tools` docker container, verify Senzing version.

        ```console
        cat /opt/senzing/er/szBuildVersion.json
        ```

    1. In the `senzingsdk-tools` docker container, run the `sz_explorer` tool.

        ```console
        sz_explorer
        ```

    1. In `sz_explorer`, run `quick_look`.

        ```console
        quick_look
        ```

1. Bring docker-compose formations down and delete the attached volumes.

    :pencil2: Replace `senzing-4_0_0` and `senzing-4_1_0` with desired Senzing versions.

    ```console
    docker compose --project-name senzing-4_0_0 --profile new --file senzing-docker-compose-postgresql-truthset-multi.yaml down --volumes
    docker compose --project-name senzing-4_1_0 --profile new --file senzing-docker-compose-postgresql-truthset-multi.yaml down --volumes
    ```

[localhost:9171]: http://localhost:9171
[PgAdmin4]: https://www.pgadmin.org/
[What is Docker-Compose]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/docker-compose.md
