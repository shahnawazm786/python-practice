import pandas as pd

student={'marks': {0: 97,   1: 63,   2: 63,   3: 71,   4: 64,   5: 90,   6: 66,   7: 46,   8: 74,   9: 62,   10: 94,   11: 67},  'roll_no': {0: 1,   1: 2,   2: 1,   3: 3,   4: 1,   5: 3,   6: 3,   7: 3,   8: 2,   9: 2,   10: 1,   11: 2},  'subject': {0: 'NN',   1: 'DL',   2: 'ML',   3: 'Prob',   4: 'DL',   5: 'ML',   6: 'DL',   7: 'NN',   8: 'NN',   9: 'Prob',   10: 'Prob',   11: 'ML'}}
df=pd.DataFrame(student)
print(df)
# group by subject wise max 
max_marks=df.groupby('subject')['marks'].max()
print(max_marks)
print(max_marks.reset_index(drop=True))
max_marks.reset_index(drop=True)
result=pd.merge(df,max_marks, on="marks",how="inner")
result=result[['subject', 'marks', 'roll_no']]
print(result)