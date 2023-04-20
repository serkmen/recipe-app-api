FROM python:3.9-alpine3.13
LABEL maintainer="serkmen"

# Suggested for python projects:see python logs immediately
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app∏
# Path that commands run
WORKDIR /app
EXPOSE 8000

# Single run commands mean single layer.

# Creates new python virtual environment
ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Add dependency packages for Psycopg2 PG adapter for Django
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    # Install Python Requirements
    /py/bin/pip install -r /tmp/requirements.txt &&  \
    # Include dev requirements if it is DEV
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # Keep your image lightweight. Clean temporary files as building image
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    # Add a new user. Do not user default root user (security!)
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user

