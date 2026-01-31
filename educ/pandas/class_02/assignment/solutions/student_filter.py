'''
Problem Description:

Given a dataframe containing records of some college students, with columns "Name", "Age", "Percentage" and "Stream".

Return the name of the students belonging to either Commerce or Arts Stream and with a Percentage greater than or equal to 75.

Input Format (No need to take the input explicitly):

First line of the input contains the dataframe, in the form of a dictionary.
Output Format:

The selected student names in a Series.
'''

import pandas as pd

data = {
    'Name': ['Himanshu', 'Robert', 'Karie', 'Rohan', 'John'],
    'Age': [15, 14, 15, 16, 17],
    'Percentage': [80, 77, 83, 45, 70],
    'Stream': ['Commerce', 'Science', 'Arts', 'Commerce', 'Science']
}

df = pd.DataFrame(data)
print(df)
print(df['Stream'].isin(['Commerce','Arts']))
mask=df['Stream'].isin(['Commerce','Arts'])
print(mask)
print(df[mask])
new_df=df[mask].copy(deep=True)
print(new_df)

#print(df[(df['Percentage']>=75) and df['Stream'].isin(['Commerce','Arts'])]['Name'])
print(new_df[new_df['Percentage']>=75]['Name'])