FROM python:3.9-alpine3.13
LABEL maintainer="serkmen"

#suggested for python projects:see python logs immediately
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app  /app
#path that commands run
WORKDIR /app
EXPOSE 8000

#single run commands mean single layer.

#creates new python virtual environment
RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt &&  \
    #keep your image lightweight. Clean temporary files as building image
    rm -rf /tmp/ && \
    #add a new user. Do not user default root user (security!)
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user

