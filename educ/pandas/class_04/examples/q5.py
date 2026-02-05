import pandas as pd
import PATH
movie=pd.read_csv(PATH.MOVIE_PATH)
print(movie)
print(movie.columns)