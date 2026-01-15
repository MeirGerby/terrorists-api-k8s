from pymongo import MongoClient

client = MongoClient("mongodb+srv://meirg:HxDGLWDvLaLvgJBV@cluster0.a8kyzcd.mongodb.net/")
db = client["threats"]
collection = db["top_threats"]

# cursor = collection.find({"Quantity": {"$gt": 40}})
# print("The data having Quantity greater than 40 is:")
# for doc in cursor:
#     print(doc)

# cursor = collection.find({"Quantity": {"$lt": 40}})
# print("\nThe data having Quantity less than 40 is:")
# for doc in cursor:
#     print(doc)



data = {
"name": "Alpha",
"location": "Metropolis",
"danger_rate": 10
}

collection.insert_one(data)
print("Data inserted.")