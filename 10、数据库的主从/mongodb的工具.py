import pymongo

class db(object):
    def __init__(self,dbname, collname, ip = '127.0.0.1', port = 27017):
        self.ip = ip
        self.port = port
        self.dbname = dbname
        self.collname = collname
        pass
    
    def opendb(self):
        mongoClient = pymongo.MongoClient(self.ip,self.port)
        db = mongoClient[self.dbname]
        coll = db[self.collname]

        return coll
    # 添加
    def add_db(self,list):
        coll = self.opendb()
        result = coll.insert(list)
        for i in result:
            print('添加成功  数据id:%s'%i)
    
    # 删除
    def deldb(self,list):
        coll = self.opendb()
        for i in list:
            reslut = coll.remove(i)
            print('删除成功')
        print(reslut)
        pass
    
    # 修改
    def update(self,dict1,dict2):
        coll = self.opendb()
        reslut = coll.update_many(dict1,{'$set':dict2})
        print('修改成功')
        print(reslut)
        pass
    
    # 查询
    def finddb(self):
        coll = self.opendb()
        soult = coll.find()
        list = []
        for i in soult:
            list.append(i)
        return list
        pass
    # 查询单个
    def find_one(self):
        coll = self.opendb()
        text = coll.find_one()
        return text
    # 排序查询
    def find_sort(self,str,numb):
        coll = self.opendb()
        list = coll.find().sort(str,numb)
        return list
    # 分页的查询
    def paging(self,n):
        coll = self.opendb()
        list = coll.find().limit(2).skip((n-1)*2)
        return list

# 添加
list = [{'aa':'df','sort':1},{'aa1':'df','sort':3},{'aa2':'df','sort':2},{'aa':'df','sort':4},{'aa3':'df','sort':6},{'aa4':'df','sort':5}]
db = db(dbname = 'aadb',collname = 'aacoll')
db.add_db(list)


# 删除
list = [
    {'aa':'aaaaaaaaaaaaaaaa'},
]
db.deldb(list)

# 查询

list = db.finddb()
print('查询成功')
for i in list:
    print(i)


# 修改
dict1 = {'aa':'df'}
dict2 = {'aa':'aaaaaaaaaaaaaaaa'}
db.update(dict1,dict2)

# 查询单条
text = db.find_one()
print('单个查询成功')
print(text)

# 排序查询
list = db.find_sort('sort',-1)
print('排序成功')
for i in list:
    print(i)

# 分页查询
print('第三页的内容是：')
list = db.paging(3)
for i in list:
    print(i)