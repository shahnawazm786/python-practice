import csv 
import json
'''
@csvFilePath - CSV file location
@jsonFilePath - JSON file location
'''
def read_from_csv_add_into_json(csvFilePath):
    data=[]
    with open(csvFilePath,'r',newline='',encoding='utf-8') as file:
        csvReader=csv.DictReader(file)
        for row in csvReader:
            data.append(row)
    return data
    

#read_from_csv_add_into_json('src/data/csv/customer_data.csv','')
