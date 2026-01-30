import pandas as pd

data = {
    'name': ['Jim', 'Clarke', 'Kent', 'Mark'],
    'username': ['itsjimhere', 'clark002', 'itskentment', 'markyoumustknow'],
    'userid': [20, 10, 86, 21]
}

df = pd.DataFrame(data)
def check(name,username):
    return name.lower() in username

#df[~(df.apply(lambda x:check(x['name'],x['username']), axis=0))]['userid']
df[~(df.apply(lambda x:check(x['name'],x['username']), axis=1))]['userid']
print(df)