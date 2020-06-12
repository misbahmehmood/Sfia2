#!/bin/bash

source ~/.bashrc

docker-compose build
docker push misbahmehmood/service_1
docker push misbahmehmood/service_2
docker push misbahmehmood/service_3
docker push misbahmehmood/service_4

env PROJECT_URI="${PROJECT_URI}" docker stack deploy -c docker-compose.yaml fullapp
