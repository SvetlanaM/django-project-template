FROM postgres:12.3

COPY ./compose/local/postgres/postgresql.conf /etc/postgresql/

CMD ["-c", "config_file=/etc/postgresql/postgresql.conf"]
