FROM ubuntu:latest
ARG NAME=bland_rsa

RUN apt update
RUN apt install -y python3-pip python3-dev socat

RUN useradd -m ${NAME}
WORKDIR /home/${NAME}

COPY . .
RUN echo "poke{pr31m4ge_r3s1st4nce_4m1rite}" > /home/${NAME}/flag.txt
RUN chown ${NAME} -R /home/${NAME}
RUN chmod 333 -R /home/${NAME}

USER ${NAME}

EXPOSE 5000
CMD ["./run.sh"]