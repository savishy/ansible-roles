#!/usr/bin/python

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances
import boto3
import os
# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g., 'us-east-1'
region = os.environ['EC2_REGION']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
    response = ec2.describe_instances(Filters=filters)
    instanceIds = []
    for res in response['Reservations']:
        for inst in res['Instances']:
            instanceIds.append(inst.id)
    print 'running instances: ' + str(instanceIds)
    if len(instanceIds) > 0:
        ec2.stop_instances(InstanceIds=instanceIds)
        print 'stopped your instances: ' + str(instanceIds)
