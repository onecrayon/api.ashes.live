#!/usr/bin/env bash

echo 'Populating example data...'

# Source the functions we need to get the database up and running
source /docker-entrypoint.sh

# Launch the temporary server using the same logic as the entrypoint
export PGPASSWORD="${PGPASSWORD:-$POSTGRES_PASSWORD}"
docker_temp_server_start "$@" > /dev/null

# Process our SQL
docker_process_sql -f /scripts/2020-09-10-example_data.sql  > /dev/null

# Teardown the server and exit
docker_temp_server_stop > /dev/null
unset PGPASSWORD

echo 'Example data has been populated!'
