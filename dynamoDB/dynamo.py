import boto3

dynamodb = boto3.resource('dynamodb')


table = dynamodb.create_table(
    TableName = 'students',
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
        },
        {
            'AttributeName': 'student_fname',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'student_lname',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'student_lname',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'student_email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'student_address',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'student_gpa',
            'AttributeType': 'N'
        }
    ],

    ProvisionedThroughput = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }

)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName = 'students')

print(f'Table status: {table.item_count}')