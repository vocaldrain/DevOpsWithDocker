FROM ubuntu:20.04
WORKDIR /usr/src/app
COPY hello.sh .
RUN apt-get update && apt-get install -y curl
CMD ./hello.sh
