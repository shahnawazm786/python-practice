import pandas as pd
#educ\pandas\class_04\data\movies.csv
MOVIE_PATH="educ/pandas/class_04/data/movies.csv"
DIRECTOR_PATH="educ/pandas/class_04/data/directors.csv"

movie=pd.read_csv(MOVIE_PATH)
print(movie)
print(movie['year'].nunique())
