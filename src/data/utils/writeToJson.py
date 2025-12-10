import json

'''
@jsonFilePath - json file location
@data - need data from the file
'''
def write_into_json_file(jsonFilePath,data):
    print('🟣 Start writing data into json file')
    with open(jsonFilePath,mode='a+',encoding='utf-8') as json:
        #Dump the list dictionaries to the JSON file
        json.dump(data,jsonFilePath,indent=4) #indent for pretty printing
        
        print(f'✅ Data is inserted successfully into {jsonFilePath} ')
        json.close()
        print(f'{jsonFilePath} closed successfully ✅')
