# Defines help target logic
# Add help text after each target name starting with '\#\#'
# Inspired by <https://gist.github.com/prwhite/8168133>
DOCKER_COMPOSE_DEV = -f docker-compose.yml -f docker/docker-compose.dev.yml
DOCKER_COMPOSE_TEST = -f docker-compose.yml -f docker/docker-compose.test.yml
DOCKER_RUN = docker-compose $(DOCKER_COMPOSE_DEV) run --rm -e STANDALONE=true --no-deps -u root -w /code api

help:     ## Show this help.
	@$(DOCKER_RUN) make _help

_help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

# Primary active logic

run:      ## Run development server
	@docker-compose $(DOCKER_COMPOSE_DEV) up

db:       ## Run standalone postgres server; accessible at localhost:5432
	@docker-compose $(DOCKER_COMPOSE_DEV) run --service-ports --rm postgres

test:     ## Execute test suite
	@docker-compose $(DOCKER_COMPOSE_TEST) -p asheslive_tests run --rm -w /code api

shell:    ## Open a bash shell (as the root user!)
	@$(DOCKER_RUN) bash

db-shell: ## Open a bash shell with access to the database
	@docker-compose $(DOCKER_COMPOSE_DEV) run --rm -u root -w /code api bash

clean:    ## Clean up Docker containers, images, etc.
	@docker-compose $(DOCKER_COMPOSE_DEV) down --remove-orphans
	@docker-compose $(DOCKER_COMPOSE_TEST) -p asheslive_tests down --remove-orphans
	@echo 'All clean!'

# Occasional-use helpers

build:    ## Use docker compose to (re)build the main app container
	@docker-compose $(DOCKER_COMPOSE_DEV) build --no-cache api
