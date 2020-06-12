#!/bin/bash

source ~/.bashrc

docker stack deploy -c docker-compose.yaml fullapp

echo $PROJECT_URI