import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('student')

table.put_item(
    Item={
        'student_id': 111,
        'lname':'lopez',
        # 'fname': 'carlos',
        # 'email': 'a@a.com',
        # 'address': 'ilovecelina way',
        # 'gpa': '2.5',

    }
)

print(f'item count:{table.item_count}')

