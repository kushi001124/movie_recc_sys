import streamlit as st
import pickle

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

# Title and header
st.title("Movie Recommender System")
st.header('Get 5 similar movies based on your choice!')

# Load data
movies = pickle.load(open('movie_list_10k.pkl','rb'))
similarity = pickle.load(open('similarity_10k.pkl','rb'))

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    st.subheader("You might also like:")
    for name in recommended_movie_names:
        st.markdown(f"🎬 **{name}**")
