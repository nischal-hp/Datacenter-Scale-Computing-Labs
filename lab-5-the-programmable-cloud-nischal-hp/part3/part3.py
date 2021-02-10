#!/usr/bin/env python

"""Example of using the Compute Engine API to create and delete instances.

Creates a new compute engine instance and uses it to apply a caption to
an image.

    https://cloud.google.com/compute/docs/tutorials/python-guide

For more information, see the README.md under /compute.
"""

import argparse
import os
import time
import googleapiclient.discovery
from six.moves import input
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# [START create_instance]
def create_instance(compute, project, zone, name, bucket):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(
        project='ubuntu-os-cloud', family='ubuntu-1804-lts').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script.sh'), 'r').read()

    startup_script_2 = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script-2.sh'), 'r').read()

    part3_2 = open(
        os.path.join(
            os.path.dirname(__file__), 'part3-2.py'), 'r').read()

    server_credentials = open(
        os.path.join(
            os.path.dirname(__file__), 'service-credentials.json'), 'r').read()

    config = {
        'name': name,
        'machineType': machine_type,
        # Specify the boot disk and the image to use as a source.
        'disks': [
            {                
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,                                      
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
                'key': 'service-credentials',
                'value': server_credentials
                }, {
                'key': 'startup-script',
                'value': startup_script
            }, 
            {
                'key': 'startup-script-2',
                'value': startup_script_2
            },
            {
                'key': 'part3-2',
                'value': part3_2
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


# [START wait_for_operation]
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
# [END wait_for_operation]


# [START run]
def main(project, bucket, zone, instance_name, wait=True):
    compute = googleapiclient.discovery.build('compute', 'v1')
    operation = create_instance(compute, project, zone, instance_name, bucket)
    wait_for_operation(compute, project, zone, operation['name'])

    print("Instance created.")




if __name__ == '__main__':
    parser = argparse.ArgumentParser
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument(
        'bucket_name', help='Your Google Cloud Storage bucket name.')        
    parser.add_argument(
        '--zone',
        default='us-west1-b',
        help='Compute Engine zone to deploy to.')
    parser.add_argument(
        '--name', default='instance-1', help='New instance name.')
    args = parser.parse_args()
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)

    # Project ID, zone, instance name, firewall rules 
    project,zone,instance = 'datacenter-lab-5' ,'us-west1-b', 'instance-1'
    firewall_body = {"name": "allow-5000","allowed": [{"IPProtocol": "tcp","ports": ["5000"],"targetTags": ["allow-5000"],}],}
    # Get list of Firewalls and also check if allow-5000 is already in the list
    listOfAllFirewalls = service.firewalls().list(project=project).execute()
    listOfAllFirewallsNames = []
    for eachFirewall in listOfAllFirewalls['items']:
        listOfAllFirewallsNames.append(eachFirewall['name'])
    if("allow-5000" not in listOfAllFirewallsNames):
        response = service.firewalls().insert(project=project, body=firewall_body).execute()
    else:
        print("Just Continue")
    main(args.project_id, args.bucket_name, args.zone, args.name)
    # Get the response of the instance and extract out the fingerprint
    responseOfInstance = service.instances().get(project=project, zone=zone, instance=instance).execute()
    fingerprintOfResponse = responseOfInstance['tags']['fingerprint']
    # Mention the body tags
    tags_body = {"items": ["allow-5000"],"fingerprint" : fingerprintOfResponse}
    set_tags = service.instances().setTags(project=project, zone=zone, instance=instance,body = tags_body).execute()
#[END run]
