import boto3

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')

table = dynamodb.create_table(
    TableName = 'student',
    KeySchema =[
        
        {
        'AttributeName': 'studentid',
        'KeyType': 'HASH'
        },
        {
        'AttributeName': 'email',
        'KeyType': 'RANGE'
        },
        
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'studentid',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName = 'student')
print(f'table status: {table.table_status}')