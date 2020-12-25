import csv
import json

## csv to json classifier
csvfile = open('../csvfile/data.csv', 'r')
jsonfile = open('../json_file/file.json', 'w')

def dataProcessing():
    doc=""
    lines=csvfile.readlines()
    commastack=0
    for line in lines:
        name=""
        phone=""
        address=""
        gender=""
        doc='{"name" :'
        if line[0]=='C':
            for i in range(2,len(line)-1):
                if line[i]==',':
                    commastack+=1
                elif line[i-1]==',':
                    continue
                elif line[i]!=',' and commastack==0:
                    name+=line[i]
                elif line[i]!=',' and commastack==1:
                    phone+=line[i]
                elif line[i]!=',' and commastack==2:
                    address+=line[i]
                elif line[i]!=',' and commastack==3:
                    gender+=line[i]
            doc+='"'+name+'"'+' , "phone" : "'+phone+'", "address" : "'+address+'", "gender" : "'+gender+'"}'
            doc+='\n'
        elif line[0]=='T':
            transactionNumber=""
            productID=""
            price=""
            date=""
            customerName=""
            doc='{"transactionNumber" :'
            for i in range(2,len(line)-1):
                if line[i]==',':
                    commastack+=1
                    i=i+3
                elif line[i-1]==',':
                    continue
                elif line[i]!=',' and commastack==0:
                    transactionNumber+=line[i]
                elif line[i]!=',' and commastack==1:
                    productID+=line[i]
                elif line[i]!=',' and commastack==2:
                    price+=line[i]
                elif line[i]!=',' and commastack==3:
                    date+=line[i]
                elif line[i]!=',' and commastack==4:
                    customerName+=line[i]
            doc+='"'+transactionNumber+'"'+' , "productID" : "'+productID+'", "price" : "'+ price +'", "date" : "'+date+'", "customerName" : "'+customerName+'"}'
            doc+='\n'
        elif line[0]=='P':
            name=""
            productID=""
            SupplierName=""
            doc='{"name" :'
            for i in range(2,len(line)-1):
                if line[i]==',':
                    commastack+=1
                    i=i+3
                elif line[i-1]==',':
                    continue
                elif line[i]!=',' and commastack==0:
                    name+=line[i]
                elif line[i]!=',' and commastack==1:
                    productID+=line[i]
                elif line[i]!=',' and commastack==2:
                    SupplierName+=line[i]
            doc+='"'+name+'"'+' , "productID" : "'+productID+'", "SupplierName" : "'+ SupplierName+'"}'
            doc+='\n'
        jsonfile.write(doc)
        commastack=0
    jsonfile.close()
    

if __name__ == "__main__":
    dataProcessing()