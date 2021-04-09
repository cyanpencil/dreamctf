FROM node:14
ARG NAME=json_notation

RUN useradd -m ${NAME}
WORKDIR /home/${NAME}

COPY . .
RUN npm install
RUN echo "poke{save_teh_prototype_whales}" > /home/${NAME}/flag.txt
RUN chown ${NAME} -R /home/${NAME}
RUN chmod 555 -R /home/${NAME}

USER ${NAME}

EXPOSE 3000
CMD ["node", "index.js"]