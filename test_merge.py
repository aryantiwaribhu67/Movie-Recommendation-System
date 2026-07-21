import pandas as pd
movies=pd.read_csv("data/movies.csv")
links=pd.read_csv("data/links.csv")
merged=pd.merge(movies,links,on="movieId")
print(merged.head())
print(merged.columns)
print(merged.shape)
