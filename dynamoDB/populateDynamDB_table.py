import boto3

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')

table = dynamodb.create_table(
    TableName = 'student',
    KeySchema =[
        
        {
        'AttributeName': 'student_id',
        'KeyType': 'HASH'
        },
        
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'student_id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName = 'student')