from pymongo import MongoClient


class DBConnection:
    @staticmethod
    def get_connection():
        client = MongoClient("mongodb+srv://meirg:HxDGLWDvLaLvgJBV@cluster0.a8kyzcd.mongodb.net/")
        db = client["threats"]
        collection = db["top_threats"]
        return collection


class DBCrud:
    _collection = DBConnection.get_connection()

    @staticmethod
    def insert_data(top: list[dict]):
        DBCrud._collection.insert_many(top)
        print("Data inserted.")

