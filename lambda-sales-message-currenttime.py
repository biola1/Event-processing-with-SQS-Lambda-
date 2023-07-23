import json
import boto3

from datetime import datetime

date_time = datetime.now()
sqs = boto3.client('sqs')

def lambda_handler(event, content):
    
   black_queue = sqs.get_queue_by_name(QueueName ='black_sales_queue') 

    sales_date_time = date_time.strftime("%d/%m/%Y %H:%M:%S") 
    message = ("This trigger will be executed at date and time: " + str(sales_date_time) + ".") 
    
    response = black_queue.send_message(MessageBody = message) 

    return {
        "statusCode": 200,
        'body': json.dumps(message)
    }
