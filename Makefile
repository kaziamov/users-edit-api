up:
	docker-compose up

dev: freeze
	docker-compose up --force-recreate

logs:
	docker-compose logs -f -t

run-server:
	poetry run uvicorn users_edit_api:app --host 0.0.0.0 --port 8000 --reload

start-db:
	docker-compose -f docker-compose.db.yml up

freeze:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

rm:
	docker-compose stop && \
	docker-compose rm && \
	sudo rm -rf pgdata/

rm-venv:
	rm -rf `poetry env info -p`

automigrate:
	poetry run alembic revision --autogenerate -m 'init'

migrate:
	poetry run alembic upgrade head

s:
	git status

lint:
	poetry run flake8 users_edit_api

push: lint
	git push
