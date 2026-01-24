import re
import requests

resp=requests.get('http://books.toscrape.com/index.html')
if resp.status_code==200:
    print(resp.content)
    
    remove_leading_space=str(resp.content).replace(" ","").replace(" ","")
    #remove_new_line=remove_leading_space.replace("\n","").replace("\n","")
    #remove_new_line=re.sub(r"[\n]+","",remove_leading_space)
    remove_new_line=remove_leading_space.replace("\\n","").replace('\\n','')
    print(remove_new_line)
    FILE_PATH='.\\regex\\book.html'
    with open(FILE_PATH, 'w') as f:
        #f.write(data_cleaning)
        f.close()
    
    

