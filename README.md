# Encryptix-task-2

# IMDb Movie Rating Predictor

## 📌 Overview
This is a Streamlit-based web application that predicts the IMDb rating of a movie based on various input parameters such as release year, duration, total votes, and average ratings of the genre, director, and actors.

## 🚀 Features
- User-friendly Streamlit interface.
- Accepts movie-related inputs from users.
- Uses a trained machine learning model to predict IMDb ratings.
- Provides quick predictions with a single click.

## 🛠️ Installation

### Prerequisites
Ensure you have Python installed along with the required dependencies.

### Steps to Run the App
1. Clone the repository or download the project files.
2. Install the required Python libraries:
   ```bash
   pip install streamlit pandas pickle5
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📂 Project Structure
```
/IMDb-Rating-Predictor
│── app.py            # Streamlit application script
│── rf_pickle_model.pkl # Trained machine learning model (ensure this file is in the correct path)
│── README.md         # Project documentation
```

## 🔢 Inputs
- **Release Year**: Numeric input for the year of release.
- **Duration**: Numeric input for the movie's runtime in minutes.
- **Total Votes**: Number of votes the movie has received.
- **Genre Average Rating**: Average rating of the genre.
- **Director Average Rating**: Average rating of the movie's director.
- **Actor 1, 2, 3 Average Ratings**: Average ratings of the main actors.

## 🎯 Prediction Output
The model predicts the IMDb rating based on the given inputs and displays it on the Streamlit app.

## 🏗️ Model Details
- The trained model is loaded from `rf_pickle_model.pkl`.
- It takes in a set of numeric features and outputs the predicted IMDb rating.
- The model must be placed in the correct directory for the app to function properly.

## 🤖 Future Enhancements
- Add more features for improved prediction accuracy.
- Deploy the application online for public access.
- Improve the UI with better visuals and interactivity.

