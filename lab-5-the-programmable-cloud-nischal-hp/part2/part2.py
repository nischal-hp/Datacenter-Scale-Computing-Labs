#!/usr/bin/env python

import argparse
import os
import time
import googleapiclient.discovery
from six.moves import input
from googleapiclient import discovery
import google.auth
from oauth2client.client import GoogleCredentials

"""Example of using the Compute Engine API to create and delete instances.

Creates a new compute engine instance and uses it to apply a caption to
an image.

    https://cloud.google.com/compute/docs/tutorials/python-guide

For more information, see the README.md under /compute.
"""

credentials, project = google.auth.default()
service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)
project,zone,disk,bucket = 'datacenter-lab-5','us-west1-b','instance','nisc'
snapshot_body = {
    'name' : 'base-snapshot-instance'
}
def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation['name']).execute()
        print(result)

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)


def create_instance(compute,project,zone,name,bucket,snapshotname): 
    getsourceSnapshot = compute.snapshots().get(project = project , snapshot = snapshotname).execute()
    source_snapshot = getsourceSnapshot['selfLink']
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    config = {
            'name': name,
            'machineType': machine_type,
            # Specify the source snapshot to be used as a source.
            'disks': [
                {                    
                    'boot': True,
                    'autoDelete': True,
                    'initializeParams': {
                        'sourceSnapshot': source_snapshot                        
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
response = service.disks().createSnapshot(project = project, zone = zone , disk = disk , body = snapshot_body).execute()
# List to store each of the required times
allTimes = []
# Compute the time taken to create instance-1
time0 = time.time()
operation_1 = create_instance(service,project,zone,'instance-1',bucket,snapshot_body['name'])
wait_for_operation(service,project,zone,operation_1)
time1 = time.time()
allTimes.append(time1 - time0)
# Compute the time taken to create instance-2
time2 = time.time()
operation_2 = create_instance(service,project,zone,'instance-2',bucket,snapshot_body['name'])
wait_for_operation(service,project,zone,operation_2)
time3 = time.time()
allTimes.append(time3 - time2)
# Compute the time taken to create instance-3
time4 = time.time()
operation_3 = create_instance(service,project,zone,'instance-3',bucket,snapshot_body['name'])
wait_for_operation(service,project,zone,operation_3)
time5 = time.time()
allTimes.append(time5 - time4)
# Finally print out all the times
print(allTimes)
