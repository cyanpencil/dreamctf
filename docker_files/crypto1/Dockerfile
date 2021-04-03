FROM ubuntu:latest
RUN apt update
RUN apt install -y python3-pip python3-dev gcc socat
RUN useradd -m poke
COPY pokectf/interactive_challs/crypto1 /home/poke/crypto1
RUN echo "poke{th4t's_4ffine_c1ph3r_y0u_g0t_th3r3?}" > /home/poke/crypto1/flag.txt
RUN chown poke -R /home/poke
EXPOSE 5000
CMD ["/bin/bash", "-c", "su poke bash -c 'cd ~/crypto1 && ./run.sh'"]