build:
	docker-compose -f docker-compose.dev.yml --env-file .env.docker up --force-recreate --build

dev:
	docker-compose -f docker-compose.dev.yml --env-file .env.docker up

rm:
	sudo rm -rf ./pgdata

rebuild: rm build

new-build-and-migrate: rm
	docker-compose -f docker-compose.migrate.yml --env-file .env.docker up --force-recreate --build

migrate: rm
	docker-compose -f docker-compose.migrate.yml --env-file .env.docker up --build

makemigrate:
	poetry run alembic revision --autogenerate -m "migration"

#migrate:
#	poetry run alembic upgrade head
