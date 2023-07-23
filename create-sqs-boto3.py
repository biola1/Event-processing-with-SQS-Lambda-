import boto3

sqs = boto3.client('sqs')

sqs_blacksales = sqs.create_queue(QueueName='black-sqs')

print('The SQS has been created', sqs_blacksales['QueueUrl'])