import pandas as pd

data = {
    'name': ['Mark', 'Ramilla', 'Deb', 'Laxman'],
    'profession': ['dev', 'mle', 'mle', 'hr'],
    'gender': ['male', 'female', 'male', 'male'],
    'age': [21, 20, 30, 27],
    'review': ['need improvement', 'Can be improved', 'Scope of improvement', 'Great'],
    'rating': [10, 5, 7, 9]
}

df = pd.DataFrame(data)

df_new=df[df['gender']=='male']
print(df_new)
print(df_new[(df_new['age'] >= 23) & (df_new['age'] <= 30)])
#df_new=df_new[df_new['age']>=23 and df_new['age']<=30]
#print(df_new)