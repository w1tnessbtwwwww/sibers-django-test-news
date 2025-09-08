FROM python:3.13-slim-bullseye AS prod

RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry==1.8.2

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

COPY . /app

RUN useradd -m -r django && \
    chown -R django /app
USER django

EXPOSE 8000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]