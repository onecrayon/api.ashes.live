#!/usr/bin/env sh

set -o errexit
set -o nounset

cmd="$*"

postgres_ready () {
	# Check that postgres is up and running on port `5432`:
	dockerize -wait 'tcp://postgres:5432' -timeout 5s
}

# We need this line to make sure that this container is started
# after the ones with postgres and redis:
until [ -n "${STANDALONE:-''}" ] || { postgres_ready; }; do
	>&2 echo 'Postgres unavailable - sleeping...'
done

if [ -n "${STANDALONE:-''}" ]; then
	>&2 echo ''
else
	>&2 echo 'All services up - continuing...'
fi

# Evaluating passed command (do not touch):
# shellcheck disable=SC2086
exec $cmd
