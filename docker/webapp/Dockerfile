FROM python:3.10

WORKDIR /app/src/webapp

COPY docker/webapp/requirements.txt /app/

RUN pip install -r /app/requirements.txt

ENV DEBUG 1
