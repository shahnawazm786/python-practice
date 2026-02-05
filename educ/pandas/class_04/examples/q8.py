#How many different movies have been directed by James Cameron between 2005 to 2010?
import pandas as pd
import PATH

movie=pd.read_csv(PATH.MOVIE_PATH,index_col=False)
director=pd.read_csv(PATH.DIRECTOR_PATH,index_col=False)
movie.drop('Unnamed: 0',axis=1,inplace=True)
director.drop('Unnamed: 0',axis=1,inplace=True)
print(movie.columns)
print(director.columns)
df=pd.merge(movie,director,left_on='director_id',right_on='id',how='inner')
print(df.columns)
df.drop(columns=['id_x','id_y'],axis=1,inplace=True)
print(df.columns)
#How many different movies have been directed by James Cameron between 2005 to 2010?
#data=df[(df['director_name']=='James  Cameron')]
#print(movie_count)
print(df['director_name'])
#print(data)
james_data=df[df['director_name']=='James Cameron']
print(james_data)
print(james_data.info())
#between_2005_and_2010=james_data[james_data['year']>=2005 and james_data['year']<=2010]
#print(between_2005_and_2010)
print(james_data[(james_data['year']>=2005) & (james_data['year']<=2010)])
