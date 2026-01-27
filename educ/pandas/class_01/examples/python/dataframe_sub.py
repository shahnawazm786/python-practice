import pandas as pd
dict={'name':["Sam","Roma","Mark"], "profession":['dev','mle','Data scientist'],"gender":['male','female','male'], "age":[21,20,25],"review":['No comments','hardworker','need improvement'],"rating":[10,5,7]}

df=pd.DataFrame(dict)
print(df)
