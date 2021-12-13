DOCKER_COMPOSE = COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose
DOCKER_RUN = ${DOCKER_COMPOSE} run -u `id -u`
DOCKER_BUILD = DOCKER_BUILDKIT=1 docker build
DOCKER_CONTAINER_NAME = app
MANAGE_EXEC = python /app/src/manage.py
MANAGE_COMMAND = ${DOCKER_RUN} ${DOCKER_CONTAINER_NAME} ${MANAGE_EXEC}

ARGS = $(filter-out $@,$(MAKECMDGOALS))
%:
  @:

run:
	${DOCKER_COMPOSE} up

makemigrations:
	${MANAGE_COMMAND} makemigrations ${EXTRA_ARGS}

migrate:
	${MANAGE_COMMAND} migrate ${EXTRA_ARGS}

createsuperuser:
	${MANAGE_COMMAND} createsuperuser

shell:
	${MANAGE_COMMAND} shell

manage_command:
	${MANAGE_COMMAND} ${ARGS}

test:
	${DOCKER_RUN} ${DOCKER_CONTAINER_NAME} pytest src/

add_dependency:
	${DOCKER_RUN} ${DOCKER_CONTAINER_NAME} poetry add --lock ${DEPENDENCY}

add_dev_dependency:
	${DOCKER_RUN} ${DOCKER_CONTAINER_NAME} poetry add -D --lock ${DEPENDENCY}

poetry_lock:
	${DOCKER_RUN} ${DOCKER_CONTAINER_NAME} poetry lock --no-update

poetry_command:
	${DOCKER_RUN} ${DOCKER_CONTAINER_NAME} poetry ${ARGS}

build_dev_docker_image:
	${DOCKER_COMPOSE} build ${DOCKER_CONTAINER_NAME}
