FROM python:3.10 as development_build

# This is only available at build, and is a required variable
ARG ENV

# These provide default environment variable definitions; can be overridden at runtime through
#  `-e` commandline argument or env_file
ENV ENV=${ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONPATH="${PYTHONPATH}:/code" \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # dockerize:
  DOCKERIZE_VERSION=v0.6.1 \
  # poetry:
  POETRY_VERSION=1.2.2 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

# System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
    make \
  # Cleaning cache:
  && apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* \
  # Installing `dockerize` utility:
  # https://github.com/jwilder/dockerize
  && wget "https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  && tar -C /usr/local/bin -xzvf "dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" \
  && rm "dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz" && dockerize --version \
  # Update setuptools so that pytest-cov works
  && pip install --upgrade setuptools \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && pip install "poetry==$POETRY_VERSION" && poetry --version

# Copy only requirements, to cache them in docker layer (volume is not available on build)
WORKDIR /code
COPY ./poetry.lock ./pyproject.toml /code/

# Project initialization:
RUN echo "$ENV" \
  && poetry install \
    $(if [ "$ENV" = 'production' ]; then echo '--only main'; fi) \
    --no-interaction --no-ansi \
  # Cleaning poetry installation's cache for production:
  && if [ "$ENV" = 'production' ]; then rm -rf "$POETRY_CACHE_DIR"; fi

# These are special cases used as code entrypoints:
COPY ./docker/entrypoint.sh ./docker/gunicorn.sh /

# Setting up proper permissions:
RUN chmod +x '/entrypoint.sh' \
  && chmod +x '/gunicorn.sh' \
  && groupadd -r web && mkdir -p /home/web \
  && useradd -d /home/web -r -g web web \
  && chown web:web -R /code && chown web:web -R /home/web

# Running as non-root user:
USER web

# Custom entrypoint ensures that full stack is up and running in local development environment:
ENTRYPOINT ["/entrypoint.sh"]


# The following stage is only for production deployments.
# (The development_build sets things up for a full local stack; this step
# copies in the code so we don't need volumes)
FROM development_build as production_build
COPY --chown=web:web ./alembic.ini /code/
COPY --chown=web:web ./api /code/api
COPY --chown=web:web ./migrations /code/migrations
