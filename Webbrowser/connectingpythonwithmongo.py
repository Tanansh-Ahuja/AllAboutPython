import pymongo

def enterdata(client,db):
    x = db["sample"]
    # d = {'name':'tanansh','age':20}
    # x.insert_one(d)
    x.insert_many([{"name":"bhavya","marks":30},
    {"name":"sajal","marks":20},
    {"name":"utkarsh","marks":35},
    {"name":"shrsihti","marks":50}])

def fetchdata(client,db):
    x = db["sample"]
    # one = x.find_one({"name":"sajal"})
    # print(one['name'])

    alldoc = x.find({'name':'tanansh'},{'_id':0,'age':1})
    for data in alldoc:
        print(data)
    
    


if __name__=="__main__":
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client["tanansh"]
    #enterdata(client,db)
    fetchdata(client,db)
