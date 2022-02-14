FROM python:3.10.2-alpine3.15


ENV PYTHONUNBUFFERED 1

RUN apk --update --no-cache add bash libffi-dev build-base \
    && rm -rf /var/cache/apk/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /src