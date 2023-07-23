![image](https://github.com/biola1/Event-processing-with-SQS-using-CDK/assets/90300917/581506ac-5eaa-4bc6-8f9e-8d5931500f65)# Event-processing-with-SQS-using-CDK
Sereverless architecture using sqs 
I will walk you through how I will to create a system that can track customer orders and send notifications when orders have been shipped. They want to use AWS services to build the system. They have decided to use SQS, Lambda, and Python for the project. For this project I will be using boto3 documentation for reference. 
This is a very simple serverless architecture and for this is project we will be using 
	1) AWS lambda : AWS Lambda is a serverless compute service provided by Amazon Web Services (AWS) that allows you to run code without provisioning or managing servers. With Lambda, you can upload your code, specify the runtime environment, and AWS takes care of the rest, automatically scaling and managing the infrastructure required to run your code.
	2)AWS SQS : this is a fully managed message queuing service provided by Amazon Web Services (AWS)
	2) Amazon API Gateway: Amazon API Gateway is a fully managed service provided by Amazon Web Services (AWS) that allows you to create, publish, maintain, monitor, and secure APIs (Application Programming Interfaces) at any scale
	3) Boto 3 documentation: Boto3 provides a Python API for AWS infrastructure services. Using the SDK for Python, you can directly create, update and delete AWS resources using Python scripts.
	4) IAM : This is AWS account to generate AWS access key and secret keys
	5) Python programming language

We need to set up our environment: 
	1. Create a cloud9 IDE by going to AWS console and search cloud9 and create an environment 
	2. Make sure your VPC is also set up before creating your cloud9 IDE because you will use it to create your IDE 
	3. Go to your GitHub account and create a repo. 
	4. Copy your repo url and clone your GitHub repo on your cloud9 
	5. Next is to install boto3 'pip install boto3'
	6. Also install aws using ' aws configure ' 
	7. This will ask you for your access key and secret keys .  
	8. You can set us-east-1. 
	9. For force update that will pop up cancel and and disable it. 
Now on our cloud 9 environment is ready. 
1. Create a Standard SQS Queue using Python: This involves using the Boto3 library (AWS SDK for Python) to programmatically create an SQS queue.
Create a python file on your cloud 9 
I will go to my boto3 documentation and search for sqs 
I created my sqs file name it black-sqs using script below which can also be found on my github page;

import boto3

sqs = boto3.client('sqs')

sqs_blacksales = sqs.create_queue(QueueName='black-sqs')

print('The SQS has been created', sqs_blacksales['QueueUrl'])


2. Create a Lambda function in the console with a Python 3.7 or higher runtime: In the AWS Lambda console, create a new function and configure it to use Python 3.7 or a higher version.
Go to AWS console and search lambda 
Create a function . Black-sqs-lambda
In the exectuion role, select existing role and create a policy 
On the policy, select the AmazonSQSFullAccess
Create a role call it black-sqs-lamba-role and create
Go back to your lambda and refresh the execution role and select the role you created 
Create your function 
3. Modify the Lambda to send a message to the SQS queue: Update the Lambda function code to send a message to the SQS queue. You can use the current time or a random number as the message content. Make sure to use the Boto3 library to interact with SQS.
I will create a script from my cloud9 using send message from boto3 documentation and paste on my lambda  code 

import json
import boto3
from datetime import datetime

date_time = datetime.now()

# Create SQS client
sqs = boto3.client('sqs')

queue_url_sales = 'https://sqs.us-east-1.amazonaws.com/311855008889/black-sqs'

def lambda_handler(event, context):
#using current time as a message 
    sales_date_time = date_time.strftime("%d/%m/%Y %H:%M:%S") 
    message_time = ("This trigger will be executed at date and time: " + str(sales_date_time) + ".")

# Send message to SQS queue
    response = sqs.send_message(
    QueueUrl= queue_url_sales,
    MessageBody=(message_time)
    )

    return {
        "statusCode": 200,
        'body': json.dumps(message_time)
    }

Select deploy , Next is to test then Select shareable and for the template option select 
API gateway Proxy .Save the changes and test
It will return a 200 

4. Create an API Gateway HTTP API type trigger: Set up an HTTP API trigger for the Lambda function in the API Gateway console. This allows you to invoke the Lambda function through an API endpoint.
On the lambda page click Trigger and from add trigger select API gateway and select create new API and API select  HTTP API , for security select open. For additional setting add  a name 'black-sqs-lambda-API' and for environment set default. click Add 
We will go back to our role to add another policy that will grant permission for API gateway, so we will add API gateway administrator  permission to  the black-sqs-lambda-role 
Go to IAM  and click the role and click  add permission then attach policies search amazon api gateway administrator
Then add permissions ant the policy is added.
5. Test the trigger to verify the message was sent: Use a tool like curl or a web browser to send a request to the API endpoint and verify that the Lambda function sends a message to the SQS queue.
6.  Go to your terminal,  copy your API enpoint from your lambda function and type: $ curl -X POST https://9ad2opyay4.execute-api.us-east-1.amazonaws.com/default/black-sqs-lambda
7. The trigger message will appear 
8. You can also use
Go to “Configuration” tab of your Lambda function, select  Triggers, then click on the url API endpoint and a webpage will be opened and you will get the message in your message. 
Go to the sqs created earlier black-sqs. Then click send and receive messages and scroll down to receive messages and I will see 2 messassages and I click poll messages  
Then on the message you will see the message ' This trigger will be executed at date and time: 22/07/2023 20:47:11.'

I will push my code to my github repo and this is the end of this project. Thank you. Don’t forget to like and follow me on linkedln : www.linkedin.com/in/abiola-majekodunmi-
Github : 



