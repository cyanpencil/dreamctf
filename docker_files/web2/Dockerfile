FROM ubuntu:latest
RUN apt update
RUN apt install -y python3-pip
RUN pip3 install Flask Pygments flask_security tornado nord-pygments requests
RUN useradd -m poke
COPY pokectf/interactive_challs/web2 /home/poke/web2
RUN echo "poke{0h_y0ur_p4rents_d0nt_h4v3_4_fl4g?}" > /home/poke/web2/flag.txt
RUN chown poke -R /home/poke
EXPOSE 5000
CMD ["/bin/bash", "-c", "su poke bash -c 'cd ~/web2 && python3 main.py'"]