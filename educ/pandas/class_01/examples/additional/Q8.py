import pandas as pd

data = {
    'name': ['Bruno', 'Ariana', 'Harry', 'Selena', 'Weeknd'],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'income': ['low', 'high', 'medium', 'medium', 'medium']
}

df = pd.DataFrame(data)
print(df)
medium_income=df[df['income']=='medium']
print(medium_income)
#count the medium income employee
medium_income_count=medium_income.shape[0]
print(medium_income_count)
#percentage
precentage_income=(medium_income_count/df.shape[0])/100
print(precentage_income)