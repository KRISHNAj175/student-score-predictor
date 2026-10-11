# Student Score Predictor
A machine learning web application that predicts a student's final exam score based on academic and lifestyle factors.

## Project Overview

The Student Score Predictor uses a Linear Regression model built with Scikit-learn to estimate a student's final score using five input features. 

## Features

- Predicts final exam scores using machine learning.
- Interactive web interface built with Streamlit.
- Adjustable sliders for student details.
- Displays the predicted score with a visual progress bar.

## Input Features

- Study Hours per Day
- Attendance Percentage
- Previous Exam Score
- Assignment Score
- Sleep Hours per Day

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib

## Project Structure

```text
student-score-predictor/
├── app.py
├── student_model.pkl
├── requirements.txt
└── README.md
```
## Installation and Setup

1. Clone this repository:
   
   git clone https://github.com/KRISHNAj175/student-score-predictor.git
   
3. Navigate to the project directory:
   
   cd student-score-predictor
   
5. Install the required libraries:
   
   pip install -r requirements.txt
   
7. Run the application:
   
   python -m streamlit run app.py

## Machine Learning Model
- Algorithm: Linear Regression
- Library: Scikit-learn
- Evaluation Metrics: MAE, MSE, RMSE, and R² Score
- Model Storage: Joblib

## Disclaimer

The predicted scores are estimates based on the training data and are not guaranteed exam results.

## Author

Created as a machine learning project to learn model development and deployment using Python and Streamlit.
