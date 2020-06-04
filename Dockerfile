FROM python:3

RUN wget -q -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN pip3 install coverage flask flask-restful

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD [ "python", "-m", "app" ]

