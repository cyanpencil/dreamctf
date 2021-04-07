FROM ubuntu:latest
ARG NAME=printer

RUN apt update
RUN apt install -y python3-pip python3-dev socat

RUN useradd -m ${NAME}
WORKDIR /home/${NAME}

COPY . .
RUN echo "poke{s0_th4t's_why_th3y_alw4ys_br34k}" > /home/${NAME}/flag.txt
RUN chown ${NAME} -R /home/${NAME}
RUN chmod 333 -R /home/${NAME}

USER ${NAME}

EXPOSE 5000
CMD ["./run.sh"]