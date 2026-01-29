
'''
mport pandas as pd

data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000, 28000, 25000, 44000]
}

df = pd.DataFrame(data)
'''
import pandas as pd

data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000, 28000, 25000, 44000]
}

df = pd.DataFrame(data)
print(df)

row=df[df['income']==max(df['income'])]
print(row)
print(row['name'][0])