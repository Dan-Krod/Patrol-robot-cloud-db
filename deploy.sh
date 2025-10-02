#!/usr/bin/env bash
set -e

cd /home/ubuntu/Patrol-robot-cloud-db

git fetch --all
git reset --hard origin/main

source venv/bin/activate
pip install --upgrade pip
pip install -r app/patrul_robot_project/requirements.txt
deactivate

sudo systemctl daemon-reload
sudo systemctl restart patrol.service

echo "Deploy finished: $(date)"