
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://leonardorivero:15FBq5jqCly2gAq8@cluster0.vwn5qfs.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     t = client.list_database_names()
#     db = client["DBTest"]
#     f = db.CollectionTest
#     data = {"name": 'Milena', 'last_name': 'Fonseca'}
#     post_id = f.insert_one(data)
#     print(post_id)

#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

# # leonardorivero
# # 15FBq5jqCly2gAq8
