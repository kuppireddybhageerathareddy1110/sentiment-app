# Sentiment Analysis App

A web application that performs sentiment analysis on user-input text, identifying it as positive, negative, or neutral. This app is built using Flask, MongoDB, and TextBlob for sentiment analysis.

## Features
- **Sentiment Analysis**: Analyzes text input and categorizes it as positive, negative, or neutral.
- **Data Storage**: Stores text and sentiment results in a MongoDB database.
- **Interactive UI**: A simple user interface with results display and delete options.

## Tech Stack
- **Backend**: Flask, TextBlob for NLP sentiment analysis
- **Database**: MongoDB
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render

## Setup and Installation

### Prerequisites
- **Python 3.x** installed
- **MongoDB Atlas** account (or local MongoDB setup)
- **Render** account for deployment

### Local Development
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sentiment-app.git
   cd sentiment-app

### create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

## Install dependencies:
 ```bash
 pip install -r requirements.txt

Set up environment variables:

### Create a .env file in the project root with your MongoDB URI:
##plaintext
##Copy 
MONGODB_URI=your_mongodb_uri

##Run the application:

```bash

flask run
Access the app locally:

##Open your browser and navigate to http://127.0.0.1:5000.

###Deployment on Render

##Push the repository to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/sentiment-app.git
git push -u origin main

###Deploy to Render:

#Go to Render.
#Select "New Web Service" and connect your GitHub repo.
#Configure environment variables:
#MONGODB_URI: Your MongoDB connection string
#Deploy the service.
