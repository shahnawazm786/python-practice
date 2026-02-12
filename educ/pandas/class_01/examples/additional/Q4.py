# merge
import pandas as pd
d={'Names':['Jack','Roman','Steph'],
   'Profession':['Accounting','Engineering','Engineering']
   }
e={'Profession':['Accounting','Accounting','Engineering','Engineering','HR','HR'],
   'skill_required':['math','spreadsheet','coding','linux','spreadsheets','organization']
   }
df=pd.DataFrame(d)
df1=pd.DataFrame(e)
print(df.merge(df1))