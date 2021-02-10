#!/bin/bash
#!/usr/bin/python
# [START startup_script]
sudo apt-get update
sudo apt-get install -y python3 python3-pip git
mkdir lab5
sudo pip3 install --upgrade google-api-python-client
sudo pip3 install --upgrade google-api-python-client oauth2client
cd /lab5
curl http://metadata/computeMetadata/v1/instance/attributes/startup-script-2 -H "Metadata-Flavor: Google" > startup-script-2.sh
curl http://metadata/computeMetadata/v1/instance/attributes/service-credentials -H "Metadata-Flavor: Google" > service-credentials.json
curl http://metadata/computeMetadata/v1/instance/attributes/part3-2 -H "Metadata-Flavor: Google" > part3-2.py
sudo python3 part3-2.py 'datacenter-lab-5' 'nisc'

mkdir flask
# [END startup_script]
