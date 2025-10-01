import boto3

s3 = boto3.client('s3')

# Fixed destination bucket name
DESTINATION_BUCKET = "outputbucket123450"

def handler(event, context):
    print("Event:", event)

    # Extract source info from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Copy file from source to destination
    s3.copy_object(
        Bucket=DESTINATION_BUCKET,
        CopySource={'Bucket': source_bucket, 'Key': file_key},
        Key=file_key
    )

    print(f"Copied {file_key} from {source_bucket} to {DESTINATION_BUCKET}")
    return {"status": "success", "file": file_key}

