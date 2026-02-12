import pandas as pd
import PATH
movie=pd.read_csv(PATH.MOVIE_PATH)
print(movie)
print(movie.info())
releaseDate=movie['day']+"-"+movie['month']+"-"+movie['year'].astype('str')
print(movie['day']+"-"+movie['month']+"-"+movie['year'].astype('str'))
print(releaseDate)