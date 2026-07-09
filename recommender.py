import joblib
movie_matrix=joblib.load("models/movie_matrix.joblib")
similarity=joblib.load("models/similarity.joblib")
def recommend(movie_name):
    index=movie_matrix.index.get_loc(movie_name)
    movie_list=similarity[index]
    movie_list=list(enumerate(movie_list))
    movie_list=sorted(movie_list,key=lambda x:x[1],reverse=True)
    movie_list=movie_list[1:6]
    recommendations=[]
    for movie in movie_list:
       recommendations.append(movie_matrix.index[movie[0]])
    return recommendations
movie_name=input("Enter Movie Name : ")

try: 
 result=recommend(movie_name)
 print("\n Recommended Movies:\n")
 
 for i in result:
    print(i)
except KeyError:
   print("Movie not found")
  
