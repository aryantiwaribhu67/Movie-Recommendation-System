import joblib
import pandas as pd
from tmdb import get_movie_details

movie_matrix=joblib.load("models/movie_matrix.joblib")
similarity=joblib.load("models/similarity.joblib")

movies=pd.read_csv("data/movies.csv")
movies=movies.dropna()
movies=movies.drop_duplicates()
links=pd.read_csv("data/links.csv")
links=links.dropna()
links=links.drop_duplicates()
merged=pd.merge(movies,links,on="movieId")
matrix_titles=movie_matrix.index
matrix_dict={i.lower():i for i in matrix_titles}

#movie titles function
def get_movie_titles():
  return matrix_titles.tolist()
  
#recommend function
def recommend(movie_name):
    index=movie_matrix.index.get_loc(movie_name)
    movie_list=similarity[index]
    movie_list=list(enumerate(movie_list))
    movie_list=sorted(movie_list,key=lambda x:x[1],reverse=True)
    movie_list=movie_list[1:6]
    recommendations=[]
    for movie in movie_list:
       recommendations.append((movie_matrix.index[movie[0]],movie[1]))
    return recommendations

#search function
def search(inpt):
    matches=[value for key,value in matrix_dict.items() if inpt in key]
    return matches   

#recommend_movie function
def recommend_movies(movie_name):
    return recommend(movie_name)
    
def get_tmdb_id(movie_name):
    result=merged[merged["title"]==movie_name]["tmdbId"]
    
    if result.empty:
      return None
    else:
      return result.iloc[0]



    

  
