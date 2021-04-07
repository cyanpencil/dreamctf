FROM ubuntu:latest
ARG NAME=liars

RUN apt update
RUN apt install -y python3-pip python3-dev socat

RUN useradd -m ${NAME}
WORKDIR /home/${NAME}

COPY . .
RUN echo "poke{0h_y0ur_p4rents_d0nt_h4v3_4_fl4g?}" > /home/${NAME}/flag.txt
RUN chown ${NAME} -R /home/${NAME}
RUN chmod 333 -R /home/${NAME}

USER ${NAME}

EXPOSE 5000
CMD ["python3", "main.py"]