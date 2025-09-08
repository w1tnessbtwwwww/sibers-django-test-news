# Инструкция по запуску


## Docker
1. Заполнить .env (cp .env.example .env)
2. make build (на Linux или Windows с утилитой make установленной из choco)
3. Если нет make, команда из правила build в Makefile

--
1. Fill .env (cp .env.example .env)
2. make build (on Linux or Windows with the make utility installed from choco)
3. If there is no make, the command from the build rule in the Makefile

## Source
1. Поднять базу данных PostgreSQL в Docker
```bash
    docker run -e POSTGRES_PASSWORD=пароль -e POSTGRES_DB=название_бд -p внешние_подключения:5432 --name имя_контейнера postgres:16.4 -d
```
2. Заполнить .env (cp .env.example .env)
3. poetry run python manage.py runserver