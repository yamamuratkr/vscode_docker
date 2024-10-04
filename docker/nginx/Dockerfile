FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY docker/nginx/default.conf /etc/nginx/conf.d
COPY docker/nginx/nginx.conf /etc/nginx

WORKDIR /app

RUN mkdir /app/static