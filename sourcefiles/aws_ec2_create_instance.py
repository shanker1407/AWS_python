# Lets Create EC2 Instance Using Python Boto3

import boto3


def create_ec2_instance():
    """To Create EC2 Instance In AWS Account
    """

    try:
        print("creating ec2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-011c99152163a87ae",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="my newkey"
        ),
    except Exception as e:
        print(e)


def describe_ec2_instance():
    """"To List Out All EC2 Instances In AWS Account
    """

    try:
        print("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)


def stop_ec2_instance():
    """To Stop EC2 Instances
    """
    try:

        print("Stop EC2 Instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def start_ec2_instance():
    """To Start EC2 Instances
    """

    try:
        print("Start EC2 Instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def terminate_ec2_instance():
    """To Stop EC2 Instances
    """

    try:
        print("Terminate EC2 Instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


# create_ec2_instance()
# describe_ec2_instance()
stop_ec2_instance()
#start_ec2_instance()
#terminate_ec2_instance()

