FROM python:3.9-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.12 \
  POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
  && apt-get install -y \
     binutils \
     libpq-dev \
     build-essential \
     netcat-openbsd \
     libcairo2 \
     libpango-1.0-0 \
     libpangocairo-1.0-0 \
     libgdk-pixbuf2.0-0 \
     libffi-dev \
     shared-mime-info \
     curl \
  && pip install "poetry==$POETRY_VERSION"

WORKDIR /app
ARG DJANGO_ENV

COPY poetry.lock pyproject.toml /app/

RUN poetry export -f requirements.txt $(test "$DJANGO_ENV" != production && echo "--dev") --without-hashes | pip install -r /dev/stdin

RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www
COPY --chown=www:www src /app/
COPY --chown=www:www entrypoint.sh /

ARG BUILD
ENV BUILD ${BUILD}

ENTRYPOINT ["/entrypoint.sh"]
