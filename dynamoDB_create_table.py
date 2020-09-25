
import boto3
# Get the service resource.


import key_config as keys

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=keys.aws_access_key_id,
                          aws_secret_access_key=keys.aws_secret_access_key,
                          aws_session_token=keys.aws_session_token
                          )


#dynamodb = boto3.resource('dynamodb')
'''
# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'
        }

    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')

# Print out some data about the table.
print(table.item_count)
'''

table = dynamodb.Table('users')
print(table.creation_date_time)
table.put_item(
            Item={
                'name': 'mausam',
                'email': 'mausam@mausam.com',
                'password': 'password'
            }
        )
