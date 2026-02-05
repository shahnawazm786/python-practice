import pandas as pd
import PATH
movie=pd.read_csv(PATH.MOVIE_PATH)
print(movie)
print(movie.columns)
movie_in_2010=movie[movie['year']==2010]['title']
print(movie_in_2010)
print(movie_in_2010.count())