from datetime import datetime
import json
from typing import Any, Dict, List

import boto3
from botocore.exceptions import ClientError

# Initialize a Boto3 session and create a Bedrock runtime client
session = boto3.Session()
region = "us-east-1" # us-west-2 has better runtime quota
bedrock_client = session.client(service_name = 'bedrock-runtime', region_name = region)