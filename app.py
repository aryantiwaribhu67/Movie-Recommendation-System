import streamlit as st
from recommender import get_movie_titles, recommend_movies

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
    movies
)

if st.button("🎯 Recommend Movies"):
    with st.spinner("Finding similar movies..."):
        result = recommend_movies(selected_movie)

    st.success("Recommendations Found!")

    for name, score in result:
        with st.container():
            st.subheader(f"🎬 {name}")
            st.progress(score)
            st.write(f"⭐ Similarity: {score*100:.2f}%")
            st.divider()
