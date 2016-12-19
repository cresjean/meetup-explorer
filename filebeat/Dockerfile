FROM ubuntu:latest
WORKDIR /opt/filebeat

# Prepare folder
RUN mkdir -p /opt/filebeat
RUN mkdir -p /var/log/rsvps
RUN touch /var/log/rsvps.log

# Prepare installation
RUN apt-get update \
    && apt-get install -y \
    apt-transport-https wget curl vim

RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch |  apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" |  tee -a /etc/apt/sources.list.d/elastic-5.x.list

# Install filebeat
RUN apt-get update \
    && apt-get install -y filebeat


# configure the beat to start automatically during boot
RUN update-rc.d filebeat defaults 95 10
