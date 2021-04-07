FROM ubuntu:latest
ARG NAME=go_fast

RUN apt update
RUN apt install -y python3-pip python3-dev socat

RUN useradd -m ${NAME}
WORKDIR /home/${NAME}

COPY . .
RUN echo "poke{s4n1c_w1ns_th3_hung3r_G4M3S!}" > /home/${NAME}/flag.txt
RUN chown ${NAME} -R /home/${NAME}
RUN chmod 333 -R /home/${NAME}

USER ${NAME}

EXPOSE 5000
CMD ["./run.sh"]