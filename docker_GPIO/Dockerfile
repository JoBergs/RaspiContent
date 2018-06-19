# Use an official Python runtime as a parent image
FROM raspbian/stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
#RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update \
    && apt-get -y install python3 \
    python3-pip \
    python3-dev \
    python3-rpi.gpio

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "app.py"]