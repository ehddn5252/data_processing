import pymongo
import traceback
import json


def main():
    try:
        client = pymongo.MongoClient("mongodb+srv://user1:start3we@cluster0.mqlrz.mongodb.net/<dbAs>?retryWrites=true&w=majority")
        #client = pymongo.MongoClient("mongodb+srv://user1:start3we@cluster0.mqlrz.mongodb.net/<TEST2>?retryWrites=true&w=majority")
        db = client.dbAs ## db name 
        print('MongoDB Connected.')

        inputfile="../json_file/file.json"
        f = open(inputfile, 'r',encoding='UTF8')
        lines = f.readlines()
        for i in lines:
            print(i)
            i=json.loads(i)
            db.mycollection.insert_one(i)

    except Exception as e:
        print(traceback.format_exc())
    finally:
        client.close()
        print('MongoDB Closed.')
 
if __name__ == "__main__":
    main()