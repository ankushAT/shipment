FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /shipment-api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
