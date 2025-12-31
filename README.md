<<<<<<< HEAD
Spam Email Detection using Logistic Regression
Project Overview

Spam email detection is a classic Natural Language Processing (NLP) problem.
This project implements a binary classification system that identifies whether an email or SMS message is Spam or Not Spam (Ham) using Logistic Regression and TF-IDF vectorization.

A Streamlit web application is also built to allow users to interactively test messages in real time.

Objective

To preprocess email/SMS text data

To convert text into numerical features using TF-IDF

To train a Logistic Regression classifier

To evaluate model performance using standard metrics

To deploy the trained model using Streamlit

Machine Learning Workflow
Raw Text → Preprocessing → TF-IDF Vectorization → Logistic Regression → Prediction

Project Structure
spam_detection_app/
│
├── app.py                    # Streamlit application
├── spam_model.pkl            # Trained Logistic Regression model
├── tfidf_vectorizer.pkl      # Trained TF-IDF vectorizer
├── requirements.txt          # Required Python libraries
└── README.md                 # Project documentation

Dataset

SMS Spam Collection Dataset

Source: UCI Machine Learning Repository / Kaggle

Total messages: 5,572

Labels:

spam → Unwanted messages

ham → Legitimate messages

Tools & Libraries Used

Python 3.x

pandas, numpy

scikit-learn

nltk

joblib

Streamlit

matplotlib, seaborn

Text Preprocessing Steps

Convert text to lowercase

Remove punctuation and special characters

Remove stopwords using NLTK

Tokenization

TF-IDF vectorization (unigrams + optional bigrams)

Model Used
Logistic Regression

Efficient and interpretable

Suitable baseline for text classification

Outputs probability scores using predict_proba()

Model Evaluation Metrics

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

Typical Performance:

Accuracy: ~95–98%

High precision for spam detection

Streamlit Web Application
Features:

Text input for email/SMS

Real-time spam prediction

Spam probability confidence score

User-friendly interface

Run the App Locally
pip install -r requirements.txt
streamlit run app.py

Sample Test Messages

Spam Example:

Congratulations! You have won a free prize.
Claim your reward now!


Not Spam Example:

Hi, are we meeting tomorrow for the project discussion?
=======
# MiniProject_Email_Spam_detection
>>>>>>> 35c04dd82d8af911955767c6875b75b2a452d6eb
