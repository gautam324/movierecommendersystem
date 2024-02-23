import pickle
import streamlit as st
import requests
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK resources (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MDJjNmIyM2QwOTdlMjllYTQzZTg5M2RhYTQxOGZiZCIsInN1YiI6IjY1ZDc0MjM0ZTZkM2NjMDE2MmMwYWY0ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dJ3o1dMmGeJCSu2_cmIOAsqQGM0AxKaXi9zN85R-ZOQ"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for unsuccessful requests
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching movie details: {str(e)}")
        return None

def fetch_movie_reviews(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MDJjNmIyM2QwOTdlMjllYTQzZTg5M2RhYTQxOGZiZCIsInN1YiI6IjY1ZDc0MjM0ZTZkM2NjMDE2MmMwYWY0ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dJ3o1dMmGeJCSu2_cmIOAsqQGM0AxKaXi9zN85R-ZOQ"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for unsuccessful requests
        data = response.json()
        return data['results']
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching movie reviews: {str(e)}")
        return None

def perform_sentiment_analysis(text):
    sentiment_scores = sia.polarity_scores(text)
    sentiment = ''
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return sentiment

def recommend_with_details(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies_info = []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].get('movie_id')
            if movie_id:
                movie_details = fetch_movie_details(movie_id)
                if movie_details:
                    reviews = fetch_movie_reviews(movie_id)
                    movie_details['reviews'] = reviews
                    recommended_movies_info.append(movie_details)
                else:
                    st.warning("No details found for recommended movie: {}".format(movies.iloc[i[0]].get('title')))
            else:
                st.warning("No movie ID found for recommended movie: {}".format(movies.iloc[i[0]].get('title')))
        return recommended_movies_info
    except IndexError:
        st.error("Selected movie '{}' not found in the dataset.".format(movie))
        return []

st.title('Movie Recommender System')

# Load data
with open(r'C:\Users\gauta\Downloads\movie_list.pkl','rb') as f:
    movies = pickle.load(f)
with open(r'C:\Users\gauta\Downloads\similarity.pkl','rb') as f:
    similarity = pickle.load(f)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select a movie from the dropdown",
    movie_list
)

show_recommendations = st.slider("Show Recommendations", 0, 1, 0)
if show_recommendations:
    st.markdown('## Recommendations')
    recommended_movies_info = recommend_with_details(selected_movie)
    if recommended_movies_info:
        for movie_info in recommended_movies_info:
            st.write("###", movie_info['title'])
            st.write("**Release Date:**", movie_info['release_date'])
            st.write("**Overview:**", movie_info['overview'])
            st.write("**Rating:**", movie_info['vote_average'])
            st.write("**Genre:**", ", ".join([genre['name'] for genre in movie_info['genres']]))
            poster_url = "https://image.tmdb.org/t/p/w500/" + movie_info['poster_path']
            st.image(poster_url, caption=movie_info['title'], use_column_width=True)
            st.write("### Reviews:")
            if movie_info.get('reviews'):
                for review in movie_info['reviews']:
                    st.write(review['content'])
                    sentiment = perform_sentiment_analysis(review['content'])
                    st.write("**Sentiment:**", sentiment)
                    st.write("---")
            else:
                st.write("No reviews available.")
            st.markdown("---")
    else:
        st.warning("No recommendations found for selected movie.")
