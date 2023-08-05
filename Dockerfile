FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY static /app/static
COPY templates /app/templates
COPY manage.py /app/manage.py
COPY WiredWorldProject /app/WiredWorldProject