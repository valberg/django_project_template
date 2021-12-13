#!/bin/sh

if [ -z "$POSTGRES_HOST" ]; then
  echo "POSTGRES_HOST not set"

else
  echo "Waiting for postgres..."

  while ! nc -z "$POSTGRES_HOST" "$POSTGRES_HOST"; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

exec "$@"
