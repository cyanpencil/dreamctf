FROM php:7.2-apache

RUN apt-get update
RUN apt-get install -y sqlite3

ARG NAME=simple_blog
ARG FLAG="poke{fake_flag}"

WORKDIR /var/www/html

COPY ./docker_files/${NAME} .
RUN ./create_db.sh

EXPOSE 80