import boto3
import os
from src.constants import AWS_SECRET_ACCESS_KEY_ENV_KEY, AWS_ACCESS_KEY_ID_ENV_KEY, ENDPOINT_URL

class S3Client:
    """
    S3Client for Backblaze B2 using boto3.

    This class gets credentials from environment variables and creates a connection
    with a Backblaze B2 bucket.
    """

    s3_client = None
    s3_resource = None

    def __init__(self):
        # Only initialize if not already done (singleton pattern)
        if S3Client.s3_resource is None or S3Client.s3_client is None:
            access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
            secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

            if access_key_id is None:
                raise Exception(f"Environment variable {AWS_ACCESS_KEY_ID_ENV_KEY} is not set.")
            if secret_access_key is None:
                raise Exception(f"Environment variable {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set.")

            # Create Backblaze S3 resource and client using endpoint_url
            S3Client.s3_resource = boto3.resource(
                's3',
                endpoint_url=ENDPOINT_URL,
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key
            )
            S3Client.s3_client = boto3.client(
                's3',
                endpoint_url=ENDPOINT_URL,
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key
            )

        # Assign instance variables
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
