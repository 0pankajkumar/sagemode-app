FROM python:3.9-bookworm AS app
LABEL maintainer="Yagami Light <805.bluebell@gmail.com>"

# setup environment variable
ENV DockerHOME=/home/app/webapp

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

COPY . $DockerHOME


RUN apt-get update && \
    apt-get install -y \
    curl

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

RUN python sagemode/manage.py makemigrations
RUN python sagemode/manage.py migrate
CMD python sagemode/manage.py runserver

