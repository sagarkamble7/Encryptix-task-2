import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open(r'D:\Encryptix task 2\rf_pickle_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app
st.title("🎬 IMDb Movie Rating Predictor")

st.write("## Enter Movie Details for Prediction")

year = st.number_input("Release Year", min_value=1900, max_value=2025, value=2020)
duration = st.number_input("Duration (minutes)", min_value=30, max_value=300, value=120)
votes = st.number_input("Total Votes", min_value=0, value=100, step=10)
genre_avg_rating = st.number_input("Genre Average Rating", min_value=0.0, max_value=10.0, value=6.0, step=0.1)
director_avg_rating = st.number_input("Director Average Rating", min_value=0.0, max_value=10.0, value=6.5, step=0.1)
actor1_avg_rating = st.number_input("Actor 1 Average Rating", min_value=0.0, max_value=10.0, value=5.5, step=0.1)
actor2_avg_rating = st.number_input("Actor 2 Average Rating", min_value=0.0, max_value=10.0, value=5.8, step=0.1)
actor3_avg_rating = st.number_input("Actor 3 Average Rating", min_value=0.0, max_value=10.0, value=5.3, step=0.1)

if st.button("Predict IMDb Rating"):
    input_data = pd.DataFrame({
        'Year': [year],
        'Votes': [votes],
        'Duration': [duration],
        'Genre_Average_Rating': [genre_avg_rating],
        'Director_Average_Rating': [director_avg_rating],
        'Actor1_Average_Rating': [actor1_avg_rating],
        'Actor2_Average_Rating': [actor2_avg_rating],
        'Actor3_Average_Rating': [actor3_avg_rating]
    })
    prediction = model.predict(input_data)
    st.success(f"Predicted IMDb Rating: {prediction[0]:.2f}")