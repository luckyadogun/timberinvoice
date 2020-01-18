FROM python:3.7-alpine
MAINTAINER Lucky Adogun

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBUG 0

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev
RUN pip install psycopg2
RUN apk del .build-deps

RUN mkdir /timberr
WORKDIR /timberr
COPY ./timberr /timberr

RUN adduser -D user
USER user

EXPOSE "8000"

CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT