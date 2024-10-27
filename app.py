import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
from textblob import TextBlob
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MongoDB setup using environment variable for the URI
mongo_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongo_uri)
db = client['sentiment_db']  # Change to your database name if different
collection = db['sentiments']  # Change to your collection name if different

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        if not text.strip():
            return render_template('index.html', error="Please enter valid text.")
        
        # Perform sentiment analysis with TextBlob
        blob = TextBlob(text)
        sentiment_polarity = blob.sentiment.polarity

        # Determine sentiment based on polarity
        if sentiment_polarity > 0:
            sentiment = 'Positive'
        elif sentiment_polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        
        # Store in MongoDB
        collection.insert_one({'text': text, 'sentiment': sentiment, 'polarity': sentiment_polarity})
        
        return redirect(url_for('results'))

    return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
    sentiments = list(collection.find())
    
    # Add emojis based on the sentiment
    for sentiment in sentiments:
        if sentiment['sentiment'] == 'Positive':
            sentiment['emoji'] = '😊'
        elif sentiment['sentiment'] == 'Negative':
            sentiment['emoji'] = '😞'
        else:
            sentiment['emoji'] = '😐'
    
    sentiment_counts = {
        'Positive': sum(1 for s in sentiments if s['sentiment'] == 'Positive'),
        'Negative': sum(1 for s in sentiments if s['sentiment'] == 'Negative'),
        'Neutral': sum(1 for s in sentiments if s['sentiment'] == 'Neutral'),
    }

    return render_template('results.html', sentiments=sentiments, sentiment_counts=sentiment_counts)

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    collection.delete_one({'_id': ObjectId(id)})  # Convert id to ObjectId
    return redirect(url_for('results'))

@app.route('/clear', methods=['POST'])
def clear():
    collection.delete_many({})  # Deletes all records in the collection
    return redirect(url_for('results'))

if __name__ == '__main__':
    app.run(debug=True)
