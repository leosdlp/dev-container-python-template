FROM mysql:8.0

ENV MYSQL_DATABASE=cours_data \
    MYSQL_ROOT_USER=root \
    MYSQL_ROOT_PASSWORD=root

EXPOSE 3306

COPY ./init.sql /docker-entrypoint-initdb.d/

RUN echo "alias ll='ls -al'" >> /root/.bashrc

CMD ["mysqld"]