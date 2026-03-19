
FROM postgres:15-alpine

ENV POSTGRES_USER=shreya
ENV POSTGRES_PASSWORD=shreya123
ENV POSTGRES_DB=appdb

COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 5432
