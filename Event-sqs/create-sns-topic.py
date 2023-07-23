import boto3

#create a sns topic
sns = boto3.client('sns')

black_sns = sns.create_topic(
    Name='black-message',
)
print(black_sns['TopicArn'])
