FROM ubuntu:latest
ARG NAME=deadbeef

RUN apt update
RUN apt install -y python3-pip python3-dev socat

RUN useradd -m ${NAME}
WORKDIR /home/${NAME}

COPY . .
RUN echo "poke{sh0uld_h4ve_writt3n_it_1n_rust}" > /home/${NAME}/flag.txt
RUN chown ${NAME} -R /home/${NAME}
RUN chmod 333 -R /home/${NAME}

USER ${NAME}

EXPOSE 5000
CMD ["./run.sh"]