FROM ubuntu:latest
RUN apt update
RUN apt install -y python3-pip
RUN pip3 install Flask Pygments flask_security tornado nord-pygments requests
RUN useradd -m poke
COPY pokectf/interactive_challs/web1 /home/poke/web1
RUN echo "poke{th1s_w3b_w4s_fun?}" > /home/poke/flag
RUN chown poke -R /home/poke
EXPOSE 5000
CMD ["/bin/bash", "-c", "su poke bash -c 'cd ~/web1 && python3 main.py'"]