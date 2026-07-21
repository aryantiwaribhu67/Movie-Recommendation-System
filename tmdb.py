import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

def get_movie_details(tmdb_id):
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Connection": "close"
    }

    for attempt in range(3):  # Try up to 3 times
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=15
            )

            response.raise_for_status()

            data = response.json()

            return {
                "title": data.get("title"),
                "rating": data.get("vote_average"),
                "overview": data.get("overview"),
                "release_date": data.get("release_date"),
                "poster": data.get("poster_path"),
                "genres": ", ".join(
                    genre["name"] for genre in data.get("genres", [])
                )
            }

        except requests.exceptions.RequestException:
            if attempt < 2:
                time.sleep(1)   # Wait 1 second before retrying
            else:
                return None
    
if __name__ == "__main__":
    data =get_movie_details(862)

    if data:
        print(data)
