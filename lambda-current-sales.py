import json
import boto3
from datetime import datetime

date_time = datetime.now()

# Create SQS client
sqs = boto3.client('sqs')

queue_url_sales = 'SQS_QUEUE_URL'

def lambda_handler(event, context):
#using current time as a message 
    sales_date_time = date_time.strftime("%d/%m/%Y %H:%M:%S") 
    message_time = ("This trigger will be executed at date and time: " + str(sales_date_time) + ".")

# Send message to SQS queue
    sqs_blacksales = sqs.send_message(
    QueueUrl=queue_url_sales,
    MessageBody=(message_time)
    )

    return {
        "statusCode": 200,
        'body': json.dumps(message)
    }