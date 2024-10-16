#!/bin/bash

# https://github.com/ansible/awx/blob/devel/tools/docker-compose/README.md

# Fedora 40
# 4 Cores, 8G Mem

dnf install git make ansible

dnf install dnf-plugins-core
dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
dnf install docker-ce docker-ce-cli containerd.io
systemctl start docker
systemctl enable docker

git clone https://github.com/ansible/awx.git
cd awx/

make clean/ui ui
make docker-compose-build
make docker-compose
