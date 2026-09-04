import streamlit as st
import pickle

def recommend(movie):
    movie_index = int(movies_df[movies_df['title'] == movie].index[0])
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)

    return recommended_movies


similarity = pickle.load(open("similarity.pkl", "rb"))
movies_df = pickle.load(open("movies.pkl", "rb"))
movies_list = movies_df['title'].values

st.header("Movie Recommender System", divider=True)
st.write("Model trained on tmdb_5000_movies dataset.")
st.write("The tmdb_5000_movies dataset covers movies from 1916 to 2017,with the vast majority being modern releases and a strong skew toward U.S. productions as the dataset contains detailed information about roughly 5,000 movies, mainly from the United States over the past 100 years (1916-2017).")

selected_movie_name = st.selectbox("Enter Movie",
                                   movies_list,
                                   index= None,
                                   placeholder="Enter movie name")

if st.button("Recommend"):
    st.write("Showing Recommendations for:", selected_movie_name)
    recommendations = recommend(selected_movie_name)

    for movie in recommendations:
        st.write(movie)

