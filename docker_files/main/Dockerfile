FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

COPY /pokectf/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY /pokectf/ /usr/src/app/

EXPOSE 5000
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "manage:app" ]