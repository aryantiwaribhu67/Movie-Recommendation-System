import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

#read csv files using pandas
movies=pd.read_csv("data/movies.csv")  
ratings=pd.read_csv("data/ratings.csv")

#delete timestamp column
ratings=ratings.drop(columns=["timestamp"])

#movie and ratings size
print("\n movies size:",movies.shape)
print("\n rating size:",ratings.shape)

#columns in movies and ratings
print("\n movies columns :")
print(movies.columns)
print("\n ratings columns:")
print(ratings.columns)

#missing values
print("\nnull values in movies:",movies.isnull().sum())
print("\n null values in ratings:",ratings.isnull().sum())

#remove null values(if any)
movies=movies.dropna()
ratings=ratings.dropna()

#duplicate rows
print("\n duplicate rows in movies:",movies.duplicated().sum())
print("\n duplicate rows in ratings",ratings.duplicated().sum())

#delete duplicates (if any)
movies=movies.drop_duplicates()
ratings=ratings.drop_duplicates()

#datatypes
print("\n movie datatypes:")
print(movies.dtypes)
print("\n rating datatypes:")
print(ratings.dtypes)

#merge tables on same column
merged=pd.merge(movies,ratings,on="movieId")

print("\nmerged successfully")
print(merged.shape)
print("\n merged dataset:")
print(merged.head().to_string())

#make pivot table
movie_matrix=merged.pivot_table(index="title",columns="userId",values="rating")

#fill NaN as 0
movie_matrix=movie_matrix.fillna(0)
print(movie_matrix.shape)
print(movie_matrix.head())

movie_titles=movie_matrix.index

#make similarity matrix
similarity=cosine_similarity(movie_matrix)
print(similarity.shape)
print("done")
joblib.dump(similarity,"models/similarity.joblib")
joblib.dump(movie_matrix,"models/movie_matrix.joblib")
joblib.dump(movie_titles,"models/movie_titles.joblib")
print("models saved successfully")

