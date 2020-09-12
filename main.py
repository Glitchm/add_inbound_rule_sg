import boto3
import argparse
from botocore.exceptions import ClientError


def add_ip(ipaddr, rule_description):
    ec2_session = boto3.session.Session()
    ec2_client = ec2_session.client('ec2')

    try:
        ec2_client.authorize_security_group_ingress(
            GroupId='group_id',  # *Add your own groupID
            IpPermissions=[
                {
                    'FromPort': 443,
                    'IpProtocol': 'tcp',
                    'IpRanges': [
                        {
                            'CidrIp': ipaddr,
                            'Description': rule_description
                        },
                    ],
                    'ToPort': 443,
                },
            ],
            DryRun=False
        )
        print(f"Ip Address: {ipaddr} added for {rule_description}")
    except ClientError as e:
        print(e)


def main(ipaddr, desc):
    add_ip(ipaddr, desc)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ipaddr", required=True,
                    help="Enter the IP address you want added for https access. Example: 10.0.0.5/32")
    ap.add_argument("-d", "--desc", required=True,
                    help="enter a description")
    args = vars(ap.parse_args())
    main(args['ipaddr'], args['desc'])
