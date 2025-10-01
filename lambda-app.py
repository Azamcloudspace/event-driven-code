import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Event:", event)
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Copy file to output bucket
    destination_bucket = os.environ.get("OUTPUT_BUCKET", "my-output-bucket-123")
    s3.copy_object(
        Bucket=destination_bucket,
        CopySource={'Bucket': source_bucket, 'Key': file_key},
        Key=file_key
    )

    return {"status": "File processed", "file": file_key}
