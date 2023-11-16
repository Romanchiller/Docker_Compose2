FROM nginx:1.19.0

RUN mkdir /app

RUN rm /etc/nginx/conf.d/default.conf

COPY project.conf /etc/nginx/conf.d/default.conf

WORKDIR /app
