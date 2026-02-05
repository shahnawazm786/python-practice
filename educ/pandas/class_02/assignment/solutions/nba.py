import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

team = df.groupby('Team')
print(team)

print(df)
print(team.first())
print(team['Salary'].max())