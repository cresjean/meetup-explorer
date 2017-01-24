FROM ubuntu:latest
WORKDIR /opt/filebeat

# Prepare folder
RUN mkdir -p /opt/filebeat
RUN mkdir -p /var/log/rsvps

# Prepare installation
RUN apt-get update \
    && apt-get install -y \
    apt-transport-https wget curl vim

RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch |  apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" |  tee -a /etc/apt/sources.list.d/elastic-5.x.list

# Install filebeat and python
RUN apt-get update \
    && apt-get install -y filebeat python


# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install requests

# configure the beat to start automatically during boot
RUN service filebeat start
RUN update-rc.d filebeat defaults 95 10

RUN /etc/init.d/filebeat start
