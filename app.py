import streamlit as st
from recommender import get_movie_titles, recommend_movies,get_tmdb_id
from tmdb import get_movie_details

movies = get_movie_titles()
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")
st.markdown(
    "Discover movies similar to your favorites using **Machine Learning** and **Cosine Similarity**."
)
st.divider()

selected_movie = st.selectbox(
    "🔍 Select a Movie",
    movies,index=None,placeholder="Select and search a movie"
)

if st.button("🎯 Recommend Movies"):
 if not selected_movie:
   st.warning("Please select a movie")
 else:
   with st.spinner("Finding similar movies..."):
       result = recommend_movies(selected_movie)

   st.success("Recommendations Found!")

   for name, score in result:
       tmdb_id=get_tmdb_id(name)
       
       if tmdb_id:
         details=get_movie_details(int(tmdb_id))
       else:
         details=None
       with st.container():
          #  st.subheader(f"🎬 {name}")
           # st.progress(score)
          #  st.write(f"⭐ Similarity: {score*100:.2f}%")
           # st.divider()
         col1,col2=st.columns([1,3])
           
         if details:  
         
           with col1: 
              if details["poster"]:
                poster_url = "https://image.tmdb.org/t/p/w500" + details["poster"]
                st.image(poster_url,width=220)
              else:
                 st.warning("Unable to load image")
           
           with col2:
             
                   st.subheader(details["title"])
                   st.write(f"⭐ Rating: {details['rating']:.1f}/10")
                   st.write(f"🎯 Similarity: {score*100:.2f}%")
                   st.write(f"📅 Release Date: {details['release_date']}")
                   st.write(f"🎭 Genres: {details['genres']}")
                   st.write(details["overview"])
           
         else:
             st.warning("TMDB request failed")
         st.divider()

