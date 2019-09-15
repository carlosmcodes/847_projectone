import boto3, json
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')

table = dynamodb.Table('student')
print(f'table status: {table.table_status}')


response = table.put_item(
    Item={
        'studentid': 99977776,
        'email': 'finaltest@yahoo.com',
        'address': 'ilovecelina way',
        'gpa': '2.5',

    },
    ReturnValues='ALL_OLD',
)
response = table.scan()
# Wait until the table exists.
# table.meta.client.get_waiter('table_exists').wait(TableName = 'student')
# table = table.delete_table(TableName='student')
print(f'item count:{table.item_count}')
print(f'table name: {table.table_name}')
print(response)
# print(json.dumps(response, indent=4))