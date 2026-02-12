# Within the decade that produced the highest number of movies, who were the top 5 contributing directors based on the number of movies they directed?
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

top_decade = movie["decade"].value_counts().idxmax()
print(top_decade)
decade_movies = movie[movie["decade"] == top_decade]
print(decade_movies)
top_directors = (
    decade_movies["director_id"]
    .value_counts()
    .head(5)
    .index
)
print(top_directors)
result = (
    decade_movies[decade_movies["director_id"].isin(top_directors)]
    .merge(
        directors,
        left_on="director_id",
        right_on="id"
    )
    [["director_name", "title"]]
    .sort_values(by="director_name")
)
print(result)
print(result.groupby("director_name")["title"].apply(list))