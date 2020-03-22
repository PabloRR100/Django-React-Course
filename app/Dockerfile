FROM python:3.8.1-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY foo
ENV DJANGO_ALLOWED_HOSTS localhost 127.0.0.1 [::1]

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./requirements-dev.txt /usr/src/app/requirements-dev.txt
RUN pip install -r requirements-dev.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app/

# RUN python manage.py createsuperuser --noinput

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
