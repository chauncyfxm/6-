import pymongo

client = pymongo.MongoClient('127.0.0.1',27017)

ku = client.ku
collection = ku.collection

docment = {
    'name':'张三',
    'age':22,
    'class':'202',
    'hight':165
}
result = collection.insert(docment)
