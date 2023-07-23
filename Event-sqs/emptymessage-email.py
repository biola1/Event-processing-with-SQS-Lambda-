import json
import boto3


def lambda_handler(event, context):

        # Create SQS client
        sqs = boto3.client('sqs')
        
        queue_url_sales = 'https://sqs.us-east-1.amazonaws.com/311855008889/black-sqs'
        
        # Receive message from SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url_sales,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20
        )
        
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        
        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url_sales,
            ReceiptHandle=receipt_handle
        )
        
        return {
        "statusCode": 200,
        'body': json.dumps('Order has been Received and deleted message: %s' % message)
    }
 

