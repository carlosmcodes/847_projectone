from dynamodb_mapper.model import DynamoDBModel, ConnectionBorg

class studentDB(DynamoDBModel):
    __table__ = u"studentDB"
    __hash_key__ = u"studentid"
    __range_key__= u"email"
    __schema__ = {
        u"studentid": int,
        u"fname": str,
        u"lname": str,
        u"email": str,
        u"address": str,
        u"gpa": float,
        
    }

# connection = ConnectionBorg()
# # connection.get_table("studentDB").delete()
# connection.create_table(studentDB, 10, 10, wait_for_active=True)
# studentDB.delete()


# exampledb = studentDB()
# exampledb.studentid = 968
# exampledb.fname = 'mackenzie'
# exampledb.lname = 'hoeckley'
# exampledb.email = 'mackenz@yahoo.com'
# exampledb.gpa = 3.96
# exampledb.address = '2 laurel lane'
# exampledb.save()

# response = exampledb.scan()

# how to print generator
# for values in response:
#     print (f'generated:{values.studentid}')

# dblist = list(response)
# for i in dblist:
#     print(f'list: {i.studentid}')

# for i in dblist:
#     print(f'list: {i.studentid}')