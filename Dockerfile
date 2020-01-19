FROM python:3.7-alpine
MAINTAINER Lucky Adogun

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev
RUN pip install psycopg2
RUN apk del .build-deps

# copy entrypoint.sh
COPY ./entrypoint.sh /entrypoint.sh

RUN mkdir /timberr
WORKDIR /timberr
COPY ./timberr /timberr

RUN adduser -D user
USER user

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]