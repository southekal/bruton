import json
import os

import boto3
from botocore.exceptions import ClientError


AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
REGION_NAME = "us-east-1"
BASEPATH = "dummy"


def write_json_to_s3(key_name, json_data):
    s3 = boto3.resource("s3",
                        aws_access_key_id=AWS_ACCESS_KEY,
                        aws_secret_access_key=AWS_SECRET_KEY,
                        region_name=REGION_NAME)

    obj = s3.Object(BUCKET, f"{BASE_PATH}/public/{key_name}.json")
    obj.put(Body=json.dumps(json_data))


def read_json_from_s3(key_name):
    s3 = boto3.resource("s3",
                        aws_access_key_id=AWS_ACCESS_KEY,
                        aws_secret_access_key=AWS_SECRET_KEY,
                        region_name=REGION_NAME)

    try:
        obj = s3.Object(BUCKET, f"{BASE_PATH}/public/{key_name}.json")
        data = obj.get()['Body'].read()
        return json.loads(data)
    except ClientError as e:
        print(e)
        return None

