import pandas as pd
import PATH
director=pd.read_csv(PATH.DIRECTOR_PATH)
#What is the % of male directors in the given data?
#male_percent=movie.value_counts()
#print(male_percent)
print(director.columns)
print(director['gender'].value_counts(normalize=True))


