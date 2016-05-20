

import pymongo
from bson import ObjectId

client = pymongo.MongoClient()

db = client.books
coll = db.Book

result = coll.find({"Ratings.UserId": ObjectId('525867733a93bb219814602c')})
for b in result:
    print(b.get("Title"))
