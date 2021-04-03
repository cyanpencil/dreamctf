FROM ubuntu:latest
RUN apt update
RUN apt install -y python3-pip python3-dev gcc socat
RUN useradd -m poke
COPY pokectf/interactive_challs/crypto2 /home/poke/crypto2
RUN echo "poke{pr31m4ge_r3s1st4nce_4m1rite}" > /home/poke/crypto2/flag.txt
RUN chown poke -R /home/poke
EXPOSE 5000
CMD ["/bin/bash", "-c", "su poke bash -c 'cd ~/crypto2 && ./run.sh'"]