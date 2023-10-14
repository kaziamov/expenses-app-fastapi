build:
	docker-compose -f docker-compose.dev.yml --env-file .env.docker up --force-recreate

dev:
	docker-compose -f docker-compose.dev.yml --env-file .env.docker up

rm:
	sudo rm -rf ./pgdata

rebuild: rm build

makemigrate:
	poetry run alembic revision --autogenerate -m "migration"

migrate:
	poetry run alembic upgrade head
