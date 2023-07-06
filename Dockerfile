FROM postgres
ARG user=postgres
ARG password=postgres
ARG db=postgres

ENV POSTGRES_USER=${user}
ENV POSTGRES_PASSWORD=${password}
ENV POSTGRES_DB=${db}

