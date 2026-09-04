import streamlit as st
import pickle
import requests

api_key = st.secrets["TMDB_API_KEY"]

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    movie_index = int(movies_df[movies_df['title'] == movie].index[0])
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        index = i[0]
        movie_id = movies_df.iloc[index].id
        recommended_movies.append(movies_df.iloc[index].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


similarity = pickle.load(open("similarity.pkl", "rb"))
movies_df = pickle.load(open("movies.pkl", "rb"))
movies_list = movies_df['title'].values

st.set_page_config(
        page_title="Movie Recommender System",
)

st.header("Movie Recommender System", divider=True)
st.write("Model trained on tmdb_5000_movies dataset. (1990s - 2010s)")

selected_movie_name = st.selectbox("Enter Movie",
                                   movies_list,
                                   index= None,
                                   placeholder="Enter movie name")

if st.button("Recommend"):
    st.write("Showing Recommendations for:", selected_movie_name)
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.text(names[0])

    with col2:
        st.image(posters[1])
        st.text(names[1])

    with col3:
        st.image(posters[2])
        st.text(names[2])

    with col4:
        st.image(posters[3])
        st.text(names[3])

    with col5:
        st.image(posters[4])
        st.text(names[4])
