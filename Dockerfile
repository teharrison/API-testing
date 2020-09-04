# MG-RAST API-testing

# docker build -t mgrast/api-testing .

#FROM debian:stretch
FROM alpine:3.9

#RUN apt-get update && apt-get install -y make curl python3 python3-pip
RUN apk update ; apk add make curl python3


RUN pip3 install --upgrade pip

RUN pip3 install pytest pytest-json

# ensure backwards compatibility
RUN apk add --no-cache bash
RUN ln -s /usr/bin/python3 /usr/bin/python


COPY . /root/

WORKDIR /root
