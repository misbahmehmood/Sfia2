#!/bin/bash

source ~/.bashrc

env PROJECT_URI="${PROJECT_URI}" docker stack deploy -c docker-compose.yaml fullapp
