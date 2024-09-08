
# Sentiment Analysis on Product Reviews


## Project Overview

Sentiment analysis on Product reviews aims to classify the sentiments or reviews given by a user as positive or negative , helping in analyzing the users opinion on a product and improve the feedback mechanism .

## Objectives

Correction of spellings in text Customers's reviews to improve the chance of words that might mismatch while training using the textblob library.

Breaking texts into tokens using tokenization will transform the data into a structured format that will be suitable for analysis.

Removing unwanted text like punctuation, symbols etc. doesn't very much affect the sentiment of the model.

Applying stemming will reduce the words to their root form, which will optimize the model to recognize different words having the same sentiment.

Training the model using logistic regression 

Deploying the model using Flask.

## Technologies Used

○ Python: The core programming language for implementing the data processing and web application.

○ Pandas : For data manipulation and analysis.

○ Scikit-learn: For training the model using Logistic Regression and visualizing the classification report and accuracy score.

○ Textblob - For correcting the spellings of words in reviews.

○ Stopword Removal - For removing unncessary words(Stopword) which play little role in deciding the sentiment.

○ Porter Stemmer - For converting words to their root form and hence recognizing the words having same meaning.

○ Flask: For building the web application to deploy the model.

○ HTML & CSS: For designing the front-end interface of the web application.
## Project Structure

data/: Contains the dataset used for analysis.

notebook/:  Jupyter notebooks with step-by-step explanations of the data processing, clustering, and model development.

app/: Flask application files, including templates and routes.

models/: Pre-trained models and pickled objects used in the application.

templates/: HTML templates for the web pages.

README.md: Project documentation (this file).
