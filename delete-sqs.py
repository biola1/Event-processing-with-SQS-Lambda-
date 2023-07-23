
import boto3
sqs=boto3.client('sqs')
queue_url_sales = 'https://sqs.us-east-1.amazonaws.com/311855008889/black-sqs'
response = sqs.delete_queue(
    QueueUrl=queue_url_sales
)