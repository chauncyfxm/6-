import pymongo

mogoClient = pymongo.MongoClient('127.0.0.1',27017)

db = mogoClient.student

info = db.info

document = {
    'name':'张三',
    'gender':1,
    'age':20
}

document1 = {
    'name':'李四',
    'gender':1,
    'age':20
}
document2 = {
    'name':'王五',
    'gender':1,
    'age':20
}
document3 = {
    'name':'赵六',
    'gender':1,
    'age':20
}

reslut = info.insert(document)

reslut = info.insert([document,document1,document2])