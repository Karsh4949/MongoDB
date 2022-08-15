from pymongo import MongoClient

client = MongoClient("mongodb+srv://karsh:karshgabani@cluster0.ncuxbt4.mongodb.net/?retryWrites=true&w=majority")
db = client.todo_application

collection_name = db["todos_app"]