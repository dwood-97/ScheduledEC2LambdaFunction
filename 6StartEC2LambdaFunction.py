import json
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

def lambda_handler(event, context):
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']},{'Name': 'tag:Test1','Values':['Test1pair']}])#enter your EC2 tag key and id where I have "test1" and "test1pair"
    for instance in instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).start()
        print("Instance ID is started :- "+instance.id)
    return "success"
