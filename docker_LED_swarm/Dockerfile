FROM armhf/debian

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN apt-get update \
    && apt-get -y install python3 \
    python3-pip \
    python3-dev \
    python-software-properties

RUN pip3 install RPi.GPIO

CMD [ "python3", "app.py" ]

COPY blinking.py /data