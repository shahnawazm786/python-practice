import pymongo as mn
client=mn.MongoClient('mongodb://localhost:27017/')
mydb=client['demo']
mycol=mydb['customers']
mydict={'name':"Sarwar",'address':'Jameshedpur'}
rec=mycol.insert_one(mydict)
print(f"Insererted document id {rec.inserted_id}")
client.close()