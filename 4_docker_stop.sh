#!/bin/bash
## docker stop -t 10  eplodn_container
docker exec eplodn_container pkill -SIGINT python

sudo chown -R "$USER":"$USER" coverage

sleep 2
