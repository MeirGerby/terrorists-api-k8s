from pymongo import MongoClient


class DBConnection:
    @staticmethod
    def get_collection():
        client = MongoClient("mongodb+srv://meirg:HxDGLWDvLaLvgJBV@cluster0.a8kyzcd.mongodb.net/")
        db = client["threats"]
        collection = db["top_threats"]
        return collection


class DBCrud:
    _collection = DBConnection.get_collection()

    @staticmethod
    def insert_data(top):
        DBCrud._collection.insert_one(top)
        print("Data inserted.")




