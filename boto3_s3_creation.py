import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: String - Bucket to create (make the name unique because S3 bucket names are shared across all AWS accounts)
    :param region: String - aws region to create bucket in
    :return: True if bucket created, else False
    """
    try:
        if region is None:

            # if no region is specified, use the default 'us-east-1' region
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        
        else:
            # If a region is specified, set that as the bucket region in creation
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location,
            )

            print(f'A new bucket called {bucket_name} was created in the {region} region.')
    # Handle errors if any occur
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'BucketAlreadyExists':
            print(f"Error: The bucket name '{bucket_name}' is already taken. Please choose a different name.")
        else:
            print(e)

    return True

create_bucket('testing-script-ksm-auto-1', 'eu-west-1')
