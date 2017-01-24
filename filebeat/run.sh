#!/bin/bash

python /opt/filebeat/stream.py /var/log/rsvps/rsvps-`date +'%Y%m%d'`.log
