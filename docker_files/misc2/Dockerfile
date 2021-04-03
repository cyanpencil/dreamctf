FROM ubuntu:latest
RUN apt update
RUN apt install -y python3-pip python3-dev gcc socat
RUN useradd -m poke
COPY pokectf/interactive_challs/misc2 /home/poke/misc2
RUN echo "poke{y0u_mu\$t_r34l1ze_th3r3_1\$_n0_b0x}" > /home/poke/misc2/flag.txt
RUN chown poke -R /home/poke
EXPOSE 5000
CMD ["/bin/bash", "-c", "su poke bash -c 'cd ~/misc2 && ./run.sh'"]