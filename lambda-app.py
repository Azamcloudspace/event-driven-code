import boto3
import json

def handler(event, context):
    s3_record = event['Records'][0]['s3']
    bucket_name = s3_record['bucket']['name']
    file_key = s3_record['object']['key']

    print(f"Processing file: {file_key} from bucket: {bucket_name}")

    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:975050225555:FileProcessedTopic',
        Subject='File Processed Successfully',
        Message=f"File {file_key} has been processed successfully."
    )

    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully.')
    }

