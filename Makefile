# Defines help target logic
# Add help text after each target name starting with '\#\#'
# Inspired by <https://gist.github.com/prwhite/8168133>
DOCKER_COMPOSE_DEV = -f docker-compose.yml -f docker/docker-compose.dev.yml
DOCKER_COMPOSE_TEST = -f docker-compose.yml -f docker/docker-compose.test.yml
DOCKER_RUN = docker-compose $(DOCKER_COMPOSE_DEV) run --rm -e STANDALONE=true --no-deps -u root -w /code api
DOCKER_RUN_DB = docker-compose $(DOCKER_COMPOSE_DEV) run --rm -u root -w /code api

##=== Welcome to Ashes.live! ===

help:     ## Show this help.
	@$(DOCKER_RUN) make _help

_help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

##
##=== Local development ===

run:      ## Run development server
	@docker-compose $(DOCKER_COMPOSE_DEV) up

test:     ## Execute test suite
	@docker-compose $(DOCKER_COMPOSE_TEST) -p asheslive_tests run --rm -w /code api


# This ensures that even if they pass in an empty value, we default to "head"
ifndef REV
override REV = head
endif

migrate:  ## Run database migrations; or specify a revision: `make migrate REV='head'`
	@$(DOCKER_RUN_DB) alembic upgrade $(REV)

##
##=== Access internals ===

db:       ## Run standalone postgres server; accessible at localhost:5432
	@docker-compose $(DOCKER_COMPOSE_DEV) run --service-ports --rm postgres

shell:    ## Open a bash shell to API (warning: root user!)
	@$(DOCKER_RUN) bash

shell-db: ## Open a bash shell to API with the database running
	@$(DOCKER_RUN_DB) bash

##
##=== Docker maintenance ===

build:    ## Rebuild the main app container
	@docker-compose $(DOCKER_COMPOSE_DEV) build --no-cache api

clean:    ## Clean up Docker containers, images, etc.
	@docker-compose $(DOCKER_COMPOSE_DEV) down --remove-orphans
	@docker-compose $(DOCKER_COMPOSE_TEST) -p asheslive_tests down --remove-orphans
	@echo 'All clean!'

##
##=== Rarely used ===

example-data: ## Populate an empty database with example data (requires first revision!)
	@docker-compose $(DOCKER_COMPOSE_DEV) run -v `pwd`/docker/scripts:/scripts -u postgres --rm postgres /scripts/example_data.sh
