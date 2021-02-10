#!/usr/bin/env python

"""Example of using the Compute Engine API to create and delete instances.

Creates a new compute engine instance and uses it to apply a caption to
an image.

    https://cloud.google.com/compute/docs/tutorials/python-guide

For more information, see the README.md under /compute.
"""

import argparse
import os , json
import time
from pprint import pprint
import googleapiclient.discovery
import google.auth
import google.oauth2.service_account as service_account
# Access the project
project = os.getenv('GOOGLE_CLOUD_PROJECT') or 'datacenter-lab-5'
# Get the credentials using service-credentials.json file
credentials = service_account.Credentials.from_service_account_file(filename='service-credentials.json')
service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)

def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()
        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result
        time.sleep(1)

# [START create_instance]
def create_instance(compute, project, zone, name, bucket):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(
        project='ubuntu-os-cloud', family='ubuntu-1804-lts').execute()
    source_disk_image = image_response['selfLink']
    # Configure the machine
    machine_type = "zones/%s/machineTypes/f1-micro" % zone
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script-2.sh'), 'r').read()
    config = {
        'name': name,
        'machineType': machine_type,
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image
                }
            }
        ],
        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],
        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],
        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            }, {
                'key': 'bucket',
                'value': bucket
            }]
        }
    }
    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()
# [END create_instance]

project,zone,instance_name_template = "datacenter-lab-5","us-west1-b","instance-2"
# Create an instance by specifying the bucket name and instance name
create_instance(service,project,zone,instance_name_template,"nisc")
# Set the tag
data = service.instances().get(project="datacenter-lab-5",zone="us-west1-b",instance="instance-2").execute()
fingerprintOfData = data ['tags']['fingerprint']
body = {'items':['allow-5000'],'fingerprint': fingerprintOfData}   
request = service.instances().setTags(project="datacenter-lab-5", zone="us-west1-b", instance="instance-2", body=body).execute()