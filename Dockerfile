FROM python:3.6
ENV PYTHONUNBUFFERED 1

ADD . /dajngo-chat-app
WORKDIR /dajngo-chat-app

RUN pip install -r requirements.txt
