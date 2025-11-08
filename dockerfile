FROM php:8.2-fpm-alpine
RUN apk add --no-cache mysql-client \
 && docker-php-ext-install mysqli pdo_mysql
