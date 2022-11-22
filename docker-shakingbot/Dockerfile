FROM python:3.9-alpine

WORKDIR /opt/shakingbot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY shakingbot/ /opt/shakingbot/