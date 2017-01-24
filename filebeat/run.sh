#!/bin/bash
/etc/init.d/filebeat start && python /opt/filebeat/stream.py /var/log/rsvps/rsvps-`date +'%Y%m%d'`.log
