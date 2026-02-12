import pandas as pd
import PATH
movie=pd.read_csv(PATH.MOVIE_PATH)
print(movie)
print(movie.columns)
movie_director=movie[movie['year']>=2010]['director_id']
print(movie_director)
print(movie_director.nunique())