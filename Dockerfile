# pull the official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt install -y python3.9-dev python3-wheel 
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app


RUN echo "SECRET_KEY = 'django-insecure-_^39%)wfp910i*)2!2+ihrxbnrv$&44nm#pv-yf!7&mqhbgnkz'" > .env
RUN echo "SECRET_KEY = 'django-insecure-_^39%)wfp910i*)2!2+ihrxbnrv$&44nm#pv-yf!7&mqhbgnkz'" >> .env 
RUN echo "DB_NAME = 'wickedpark'" >> .env
RUN echo "DB_USER = 'postgres'" >> .env
RUN echo "DB_PASSWORD = 'Thomas2018'"  >> .env
RUN echo "DB_HOST = 'wickedpark.cxvo6tyuitau.eu-west-1.rds.amazonaws.com'" >> .env
RUN echo "DB_PORT = '5432'" >> .env


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
