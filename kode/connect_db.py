from pymongo import MongoClient
from reader import kort

monogodb_URL = "mongodb+srv://admin:admin@clusterfms.pbcxras.mongodb.net/?retryWrites=true&w=majority"
user = []
username = {
    'name': 'null'
}
ok = {
    'access': 0
}

def user_lookup():
    client = MongoClient(monogodb_URL)
    db = client.get_database("harald")
    col_users = db.get_collection('users')

    dblist = client.list_database_names()
    if "harald" in dblist:
        print("The database exists.")

    if col_users.find_one({"id": {"$eq": kort.get('id')}}):
        print("Bruger fundet")
        query = col_users.find_one({"id": kort.get('id')})
        user.append(query)
        username['name'] = query['fornavn']
        ok['access'] = 1
    else:
        print("Ukendt Bruger")
        ok['access'] = 0

