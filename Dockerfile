# syntax=docker/dockerfile:1

FROM python:3.11-slim

WORKDIR /app

EXPOSE 5001

COPY requirements.txt requirements.txt

COPY main.py main.py
COPY finalized_model.sav finalized_model.sav


RUN pip install -r requirements.txt

#RUN mkdir -p /app/data


CMD python main.py
