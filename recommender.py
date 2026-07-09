import joblib
movie_matrix=joblib.load("models/movie_matrix.joblib")
similarity=joblib.load("models/similarity.joblib")
matrix_titles=movie_matrix.index
matrix_dict={i.lower():i for i in matrix_titles}

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

usr_inpt=input("Enter Movie Name : ").lower()
matches=search(usr_inpt)
result=[]

if len(matches)==1:
   result=recommend(matches[0])
elif len(matches)==0:
  print("movie not found")
else:
  print("Choose one from below :")
  for i in range(len(matches)):
    print(i+1,matches[i])
  selected_indx=int(input("\nenter the choice : ")) 
  result=recommend(matches[selected_indx-1])

print("\n Recommended Movies:\n")
 
for name,score in result:
    print("Name : ",name,"    score : ", score)
    

  
