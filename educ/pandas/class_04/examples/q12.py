#In which decade, the most number of movies were produced?
import pandas as pd
import PATH

print('🕜 reading data from movie and director')
movie=pd.read_csv(PATH.MOVIE_PATH)
directors=pd.read_csv(PATH.DIRECTOR_PATH)
print('🎯 data loaded succesfully')
print('🟡 Movie dataframe information')
print(movie.info())
print('🚀 start 10 rows')
print(movie.head(10))
movie["decade"] = (movie["year"] // 10) * 10
print(movie)
movies_per_decade = movie["decade"].value_counts()
print(movies_per_decade)
print(movies_per_decade.idxmax())