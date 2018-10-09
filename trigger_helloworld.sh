#!/bin/bash
# Runs a hello world Python Flink script using a running Flink Docker container with flink libraries expanded
# Script is run from source folder mapped to /app in the container

docker exec -it flinkdockerpython_jobmanager_1 /app/src/trigger.sh
