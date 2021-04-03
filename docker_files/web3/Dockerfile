FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y socat frotz npm 
RUN useradd -m poke
COPY pokectf/interactive_challs/web3 /home/poke/web3
RUN echo "poke{S4V3_T3H_P0T0TYP3_WH4L3S}" > /home/poke/web3/flag.txt
RUN chown poke -R /home/poke/web3
EXPOSE 3000
CMD su poke /bin/bash -c "cd /home/poke/web3 && npm install && npm start"
