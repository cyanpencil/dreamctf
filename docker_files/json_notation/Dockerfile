FROM node:14
ARG NAME=json_notation

RUN useradd -m ${NAME}
WORKDIR /home/${NAME}

COPY . .
RUN npm install
RUN echo "poke{S4V3_T3H_P0T0TYP3_WH4L3S}" > /home/${NAME}/flag.txt
RUN chown ${NAME} -R /home/${NAME}
RUN chmod 555 -R /home/${NAME}

USER ${NAME}

EXPOSE 3000
CMD ["node", "index.js"]