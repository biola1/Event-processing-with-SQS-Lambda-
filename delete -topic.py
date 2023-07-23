import boto3
sns=boto3.client('sns')
topicArn = 'arn:aws:sns:us-east-1:311855008889:black-message'
response = sns.delete_topic(
    TopicArn=topicArn
)
