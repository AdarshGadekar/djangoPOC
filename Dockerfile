FROM python:3.8.10
LABEL maintainer = "adarsh"

ENV PYTHONBUFFERED 1

COPY ./app /app
WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

EXPOSE 8000

# RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo

RUN pip3 install pipx && pipx ensurepath

RUN pipx install  poetry

RUN /root/.local/bin/poetry install