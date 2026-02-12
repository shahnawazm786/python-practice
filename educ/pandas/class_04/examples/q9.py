#Among the top 10 most popular movies, which movie has the 2nd highest vote_average?
import pandas as pd
import PATH

#load movie file
movie=pd.read_csv(PATH.MOVIE_PATH,index_col=False)
print(movie.head())
print(movie.columns)
print(movie[['vote_average','title']])
# sort the vote_average
sort_by_popularity=movie.sort_values(by='popularity',ascending=False)
print(sort_by_popularity.head(10))
sort_by_vote_average=sort_by_popularity.head(10).sort_values(by="vote_average",ascending=False)
print(sort_by_vote_average.iloc[1]['title'])