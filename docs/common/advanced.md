# Advanced

## SSH port

:thinking: **Optional:**
If you do not plan on using the senzing/sshd container then these ssh sections can be ignored.
Normally port 22 is already in use for `ssh`.
So a different port may be needed by the running docker container.

1. :thinking: See if port 22 is already in use.
   If it is not in use, the next 2 steps are optional.
   Example:

    ```console
    sudo lsof -i -P -n | grep LISTEN | grep :22

    ````

1. :pencil2: Choose port for docker container.
   Example:

    ```console
    export SENZING_SSHD_PORT=9181

    ```

1. Construct parameter for `docker run`.
   Example:

    ```console
    export SENZING_SSHD_PORT_PARAMETER="--publish ${SENZING_SSHD_PORT:-9181}:22"

    ```

## Set sshd password

:thinking: **Optional:** The default password set for the sshd containers is `senzingsshdpassword`.
However, this can be changed.

1. :pencil2: Set the `SENZING_SSHD_PASSWORD` variable to change the password to access the sshd container.
   Example:

    ```console
    export SENZING_SSHD_PASSWORD=<Pass_You_Want>
    ```
