#!/bin/bash

sudo apt install -y python 
sudo apt install -y python-pip

sudo mkdir -p ~/.local/bin
sudo touch ~/.bashrc
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc

sudo chown -R $(whoami):$(whoami) ~/*
source ~/.bashrc

pip3 install --user ansible

ansible --version