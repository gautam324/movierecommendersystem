# movierecommendersystem

https://youtu.be/AEwxP3VZ5lw?si=scQ62BJhdULy5-2S

Dataset Overview:

The IMDb 5000 Movies dataset contains information about thousands of movies, including attributes such as title, director, actors, genre, plot keywords, budget, gross earnings, and user ratings.
Each movie is represented by a set of features that describe various aspects of the movie.
Feature Extraction:

In a content-based recommender system, features are extracted from the dataset to represent the items (movies) and users' preferences.
Features extracted from the IMDb 5000 Movies dataset may include genres, plot keywords, director, actors, and other metadata associated with each movie.
Profile Creation:

A user profile is created based on the movies a user has liked or interacted with in the past.
The user profile consists of feature vectors representing the user's preferences derived from the features of the movies they have liked.
Similarity Calculation:

Similarity metrics such as cosine similarity or Pearson correlation coefficient are used to measure the similarity between the user profile and the features of other movies in the dataset.
The similarity score indicates how closely related each movie is to the user's preferences based on their past interactions.
Recommendation Generation:

Movies with the highest similarity scores to the user profile are recommended to the user.
The recommender system suggests movies that share similar attributes or characteristics with the movies the user has previously enjoyed.
User Interaction:

Users can interact with the recommender system by providing feedback on the recommended movies, such as liking or disliking them.
User feedback is used to update the user profile and refine future recommendations, creating a feedback loop for personalized recommendations.
Evaluation:

The performance of the content-based recommender system is evaluated using metrics such as precision, recall, and accuracy.
The effectiveness of the system is measured based on how well it predicts movies that the user is likely to enjoy, compared to their actual preferences.




The provided code implements a Movie Recommender System using Streamlit, allowing users to select a movie from a dropdown menu and receive recommendations based on their selection. Here's a detailed description of the code:

Imports:

The necessary libraries are imported, including Streamlit for building the user interface, requests for making HTTP requests, pandas for data manipulation, nltk for natural language processing tasks, and the SentimentIntensityAnalyzer from nltk.sentiment.vader for sentiment analysis.
NLTK Setup:

NLTK resources are downloaded using nltk.download to ensure that the VADER lexicon, used for sentiment analysis, is available.
Utility Functions:

Several functions are defined to fetch movie details, fetch movie reviews, perform sentiment analysis, and recommend movies based on a selected movie.
User Interface:

The Streamlit application title is set to "Movie Recommender System".
Movie data and similarity scores are loaded from pickle files.
A dropdown menu is provided for users to select a movie from the available options.
A slider button is added to toggle the display of movie recommendations. When set to "Show Recommendations", the system provides recommendations based on the selected movie.
Recommendation Display:

If the "Show Recommendations" slider is activated, the system displays recommended movies along with their details such as release date, overview, rating, genre, and poster image.
Additionally, reviews for recommended movies are displayed along with sentiment analysis results for each review.
Enhancements:

The code has been modified to include interactive elements such as sliders for better user interaction.
User interface segmentation is achieved by conditional display of recommendations based on the slider value.
The code retains its functionality for fetching movie data, performing sentiment analysis, and displaying recommendations while improving the user experience.
