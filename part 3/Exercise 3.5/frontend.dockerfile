FROM node:16
WORKDIR ./app
EXPOSE 5000
RUN useradd -m frontend
USER frontend 
COPY ./example-frontend .
RUN npm install
CMD ["npm","start"]