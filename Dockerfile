FROM python:3.9.12

WORKDIR /app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


# install psycopg2


# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# add and run as non-root user
#RUN adduser -D suporte
#USER suporte
COPY . .
# running migrations
# RUN python manage.py migrate


# gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT

