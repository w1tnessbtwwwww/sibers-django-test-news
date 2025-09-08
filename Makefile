migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

build:
	docker-compose --env-file .env --project-directory . up --build