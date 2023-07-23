import json
import boto3


def lambda_handler(event, context):

    # Create SQS client
    sqs = boto3.client('sqs')
    sns = boto3.client('sns')

    queue_url_sales = 'https://sqs.us-east-1.amazonaws.com/311855008889/black-sqs'
    topicArn = 'arn:aws:sns:us-east-1:311855008889:black-message'

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url_sales,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )

    # Check if any messages were received
    if 'Messages' in response:
        message = response['Messages'][0]['Body']
        receipt_handle = response['Messages'][0]['ReceiptHandle']

        # Publish message to SNS topic
        sns.publish(
            TopicArn=topicArn,
            Message='Order received: ' + message,
        )

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url_sales,
            ReceiptHandle=receipt_handle
        )

        return {
            "statusCode": 200,
            'body': json.dumps('Order has been Received and deleted message: %s' % message)
        }
    else:
        return {
            "statusCode": 200,
            'body': json.dumps('No messages received from the queue.')
        }
