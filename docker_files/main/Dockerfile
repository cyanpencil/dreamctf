FROM ubuntu:latest
RUN apt update
RUN apt install -y python3-pip
RUN pip3 install Flask Flask-Login Flask-SQLAlchemy Flask-WTF email_validator SQLAlchemy==1.3.23 WTForms Werkzeug flask-admin flask_security tornado psycopg2-binary 
RUN useradd -m poke
EXPOSE 5000
CMD ["/bin/bash", "-c", "su poke bash -c 'cd ~/pokectf && python3 chals.py && python3 run.py'"]
