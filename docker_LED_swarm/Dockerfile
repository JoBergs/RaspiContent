FROM armhf/debian

RUN apt-get update \
    && apt-get -y install python3 \
    python3-pip \
    python3-dev \
    python-software-properties

RUN pip3 install RPi.GPIO

CMD [ "python3", "blinking.py" ]

COPY blinking.py /data