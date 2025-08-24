# Defines help target logic
# Add help text after each target name starting with '\#\#'
# Inspired by <https://gist.github.com/prwhite/8168133>

# Some systems only offer access to `docker-compose` (cannot access compose via `docker compose`)
#  but macOS Docker Desktop no longer provides that as an option. To enable our Make targets to run
#  on both platforms, we thus need to detect which style to use. This one-liner derived from:
#  https://stackoverflow.com/a/677212/38666
DOCKER_COMPOSE := $(shell if hash docker-compose 2>/dev/null; then echo docker-compose; else echo "docker compose"; fi)

DOCKER_RUN = $(DOCKER_COMPOSE) run --rm -e STANDALONE=true --no-deps -u root -w /code api
DOCKER_RUN_DB = $(DOCKER_COMPOSE) run --rm -u root -w /code api
DOCKER_COMPOSE_TESTS = $(DOCKER_COMPOSE) -p asheslive_tests -f docker-compose.yml -f docker-compose.test.yml

##=== Welcome to Ashes.live! ===

help:     ## Show this help.
	@$(DOCKER_RUN) make _help

_help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -E -e 's/:\s+\|?\s*[a-z_][ a-z_-]+?[a-z](\s+)##/:\1/' | sed -e 's/##//'

##
##=== Local development ===

up:          ## Run development server
	@$(DOCKER_COMPOSE) up

test:        ## Execute test suite; or specify target: `make test ARGS='api/tests/cards'`
	@$(DOCKER_COMPOSE_TESTS) run --rm -w /code -u root api \
		pytest --cov=api --cov-config=.coveragerc --cov-report=term:skip-covered --cov-report=html $(ARGS)

test-rm:     ## Cleans up test coverage artifacts; useful if coverage is innacurate
	@$(DOCKER_COMPOSE_TESTS) run --rm -w /code -u root api coverage erase
	@echo 'Test coverage cleaned up!'


# This ensures that even if they pass in an empty value, we default to "head"
ifndef REV
override REV = head
endif

migrate: clean-api     ## Run database migrations; or specify a revision: `make migrate REV='head'`
	@$(DOCKER_RUN_DB) alembic upgrade $(REV)

# These two is a bit frustrating; the default entrypoints cause inexplicable errors when trying to pass strings
#  (and just flat out fail for poetry commands), so we have to specify entrypoints with one-off commands
migrate-new: clean-api ## Autogenerate a new database migration: `make migrate-new ARGS='Description here'`
	$(DOCKER_COMPOSE) run --rm -u root -w /code --entrypoint alembic api revision --autogenerate -m "$(ARGS)"

poetry-add: clean-api  ## Add a poetry dependency: `make poetry-add ARGS='pytest --group dev'`
	$(DOCKER_COMPOSE) run --rm -e STANDALONE=true --no-deps -u root -w /code --entrypoint poetry api add $(ARGS)

# This ensures that even if they pass in an empty value, we default to parsing the "api" folder
ifndef FILEPATH
override FILEPATH = api
endif

format:      ## Format via isort and black; or specify a file: `make format FILEPATH='api/main.py'`
	@$(DOCKER_RUN) make _format FILEPATH="$(FILEPATH)"

_format:
	@black "$(FILEPATH)"
	@isort "$(FILEPATH)"

##
##=== Access internals ===

db:       ## Run standalone postgres server; accessible at localhost:5432
	@$(DOCKER_COMPOSE) run --service-ports --rm postgres

shell:    ## Open a bash shell to API (warning: root user!)
	@$(DOCKER_RUN) bash

shell-db: ## Open a bash shell to API with the database running
	@$(DOCKER_RUN_DB) bash

##
##=== Docker maintenance ===

build:    ## Rebuild the main app container
	@$(DOCKER_COMPOSE) build --no-cache api

clean-api:
	@$(DOCKER_COMPOSE) down --remove-orphans

clean-tests:
	@$(DOCKER_COMPOSE_TESTS) down --remove-orphans

clean: clean-api clean-tests    ## Clean up Docker containers, images, etc.
	@echo 'All clean!'

##

stack:    ## Rebuild the entire stack
	@$(DOCKER_COMPOSE) pull
	@$(DOCKER_COMPOSE) build

reset:    ## Completely remove all images, containers, and volumes (DANGER!)
	@$(DOCKER_COMPOSE) down --rmi all --remove-orphans --volumes
	@echo
	@echo 'You should now run `make stack`, `make db`, then populate your database!'

##
##=== First run ===

_pre-example-data:
	@$(DOCKER_RUN_DB) alembic upgrade 6b6df338dfc3

_populate-example-data: clean-api
	@$(DOCKER_COMPOSE) run -v `pwd`/docker/scripts:/scripts -u postgres --rm postgres /scripts/example_data.sh

_post-example-data:
	@$(DOCKER_RUN_DB) alembic upgrade head

# Pipe causes these to be executed in strict order
data: | _pre-example-data _populate-example-data _post-example-data     ## Populate example data (requires empty database!)
