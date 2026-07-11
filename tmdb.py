import os #module that let python to read environment variables
import requests  # for sending request to api and webservers
from dotenv import load_dotenv  #load load_dotenv function to read .env files

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

def get_movie_details(tmdb_id): 
   url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"  #url for request
   response=requests.get(url) #we get data in JSON format
   data=response.json()  #python converts it into dictionary
   return data

if __name__=="__main__":
    print(get_movie_details(862))
