FROM ubuntu:latest

RUN apt update
RUN apt install -y python3-pip python3-dev socat

ARG NAME=real_fun
ARG FLAG="poke{fake_flag}"

RUN useradd -m ${NAME}
WORKDIR /home/${NAME}

COPY ./docker_files/${NAME} .
RUN echo ${FLAG} > /home/${NAME}/flag.txt
RUN pip3 install -r requirements.txt
RUN chown ${NAME} -R /home/${NAME}
RUN chmod 555 -R /home/${NAME}
RUN chmod 666 /home/${NAME}

USER ${NAME}

EXPOSE 5000
CMD ["./run.sh"]