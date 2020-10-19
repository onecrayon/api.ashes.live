#!/usr/bin/env sh

set -o errexit
set -o nounset

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $ENV is set to "production",
# fail otherwise, since it may break things:
echo "ENV is $ENV"
if [ "$ENV" != 'production' ]; then
  echo 'Error: ENV is not set to "production".'
  echo 'Application will not start.'
  exit 1
fi

export ENV

# TODO: implement automatic migrations on startup (needs to support multiple concurrently launched nodes)

# Start gunicorn:
# Docs: http://docs.gunicorn.org/en/stable/settings.html
# Concerning `workers` setting see:
# https://github.com/wemake-services/wemake-django-template/issues/1022
/usr/local/bin/gunicorn api:app \
  -k uvicorn.workers.UvicornWorker `# Establish Uvicorn as our worker class` \
  --workers=3 `# Workers generally should be (2 x $num_cores) + 1` \
  --bind='0.0.0.0:10000' `# Run API on 10000 port (Render's default)` \
  --chdir='/code'       `# Locations` \
  --log-file=- \
  --worker-tmp-dir='/dev/shm'
