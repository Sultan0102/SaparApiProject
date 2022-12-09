FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /django_web_api

WORKDIR /django_web_api

COPY ./Core ./Core
COPY ./requirements.txt ./requirements.txt
COPY ./manage.py ./manage.py

# install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements.txt
