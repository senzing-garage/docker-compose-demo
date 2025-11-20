# docker-compose-demo examples

## Truthset on Postgresql

1. Download docker-compose file.

    ```console
    curl -O https://raw.githubusercontent.com/senzing-garage/docker-compose-demo/refs/heads/main/docker-compose/senzing-docker-compose-postgresql.yaml
    ```

1. Bring up docker-compose formation.

    ```console
    docker-compose --profile new --file senzing-docker-compose-postgresql-truthset.yaml up --pull always
    ```

1. In a separate terminal, exec into the `senzing/senzingsdk-tools` image.

    ```console
    docker exec -it senzingsdk-tools /bin/bash
    ```

1. In the `senzingsdk-tools` docker container, run `sz_explorer`.

    ```console
    sz_explorer
    ```

1. In `sz_explorer`, run `quick_look`

    ```console
    quick_look
    ```

1. Bring docker-compose formation down, but leave the attached volumes intact.

    ```console
    docker-compose --profile new --file senzing-docker-compose-postgresql-truthset.yaml down
    ```

1. Re-start the docker-compose formation with the prior database.
   Notice that the `--profile` value is now `resume`.

    ```console
    docker-compose --profile resume --file senzing-docker-compose-postgresql-truthset.yaml up
    ```

1. In a separate terminal, exec into the `senzing/senzingsdk-tools` image.

    ```console
    docker exec -it senzingsdk-tools /bin/bash
    ```

1. In the `senzingsdk-tools` docker container, run `sz_explorer`.

    ```console
    sz_explorer
    ```

1. In `sz_explorer`, run `quick_look`

    ```console
    quick_look
    ```

1. Bring docker-compose formation down and delete the attached volumes.

    ```console
    docker-compose --profile resume --file senzing-docker-compose-postgresql-truthset.yaml down --volumes
    ```
