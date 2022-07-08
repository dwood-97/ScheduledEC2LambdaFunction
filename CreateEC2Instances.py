import boto3

ec2_resource = boto3.resource("ec2")

x = ec2_resource.create_instances(ImageId = 'ami-0cff7528ff583bf9a',
      InstanceType = 't2.micro',
      MaxCount = 3,
      MinCount = 3,#change counts to add multiple
      TagSpecifications = [
                           {
                               'ResourceType': 'instance',
                               'Tags': [{'Key': 'Test1','Value': 'Test1pair'}],
                           },
                       ],
                       )

print(x)
