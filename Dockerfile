FROM python:3.7-alpine
MAINTAINER Lucky Adogun

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /timberr
WORKDIR /timberr
COPY ./timberr /timberr

RUN adduser -D user
USER user
