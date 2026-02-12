import pandas as pd

dict={'name':["Jim","Carrie","Chris","Moris"],
      'Gender':['M','F','M','M'],
      'Profession':['Athelete','Tech','Cricketer','Actor']
      }

df=pd.DataFrame(dict)
#print(df)
print(df.iloc[:2,:2])
print(df.loc[:2,"Name":"Profession"] )