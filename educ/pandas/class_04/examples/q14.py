# Display only those years where the number of movies produced are more than 70.
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

movies_per_year = movie.groupby("year").size()
movies_70=movies_per_year[movies_per_year > 70]
print(movies_70)
