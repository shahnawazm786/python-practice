# In which year did Christopher Nolan's directed films achieve their highest cumulative global box office revenue?

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
nolan_id = directors.loc[directors["director_name"] == "Christopher Nolan", "id"].iloc[0]
print(nolan_id)
nolan_movies = movie[movie["director_id"] == nolan_id]
print(nolan_movies)
yearly_revenue = (
    nolan_movies
    .groupby("year")["revenue"]
    .sum()
)
print(yearly_revenue)
print(yearly_revenue.idxmax())