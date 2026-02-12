#How many movies that are among top 10 popular movies are also among top 10 rated (vote_avg)?
import pandas as pd
import PATH

print('🕜 reading data from movie')
movie=pd.read_csv(PATH.MOVIE_PATH)
print('🎯 data loaded succesfully')
print('🟡 Movie dataframe information')
print(movie.info())
print('🚀 start 10 rows')
print(movie.head(10))
top_popular = (
    movie.sort_values(by="popularity", ascending=False)
      .head(10)["id"]
)
print(top_popular)
top_rated = (
    movie.sort_values(by="vote_average", ascending=False)
      .head(10)["id"]
)
print('🎯 TOP RATED MOVIE')
print(top_rated)
common_count = top_popular.isin(top_rated).sum()
print(common_count)

movie_popular=movie.sort_values("popularity", ascending=False).head(10)[["id","title"]] 
movie_top_rated=movie.sort_values("vote_average", ascending=False).head(10)[["id","title"]]

print('🎯 Popular movie')
print(movie_popular)
print('🎯 Top rated movie')
print(movie_top_rated)
print('🎯 Merge both the query')
movie_name=pd.merge(movie_popular,movie_top_rated,on='id')
print(movie_name)