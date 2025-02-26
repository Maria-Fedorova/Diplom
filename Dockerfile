FROM python:3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .
