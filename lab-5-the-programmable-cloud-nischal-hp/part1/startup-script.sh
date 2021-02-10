#!/bin/bash
# # [START startup_script]
sudo apt-get update
sudo apt-get install -y python3 python3-pip git
mkdir flask
git clone https://github.com/pallets/flask.git flask
cd /flask/examples/tutorial
sudo python3 setup.py install
sudo pip3 install -e .

export FLASK_APP=flaskr
flask init-db
nohup flask run -h 0.0.0.0 &
# [END startup_script]
