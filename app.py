import os
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from urllib.parse import quote_plus  # Import quote_plus

app = Flask(__name__, static_url_path='/static')

# Replace these with your actual MongoDB username and password
username = "ganesharavind124"
password = "19cs031@Ga"  # Replace with your actual password

# URL-encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Construct the MongoDB URI
mongo_uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.ukf6c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Set up MongoDB connection using PyMongo
client = MongoClient(mongo_uri)

# Specify the database name you want to use
db = client.get_database('my_flask_app_db')  # Replace 'my_flask_app_db' with your actual database name

@app.route('/')
def index():
    return render_template('feedback_form.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    number = request.form['number']

    feedback = {
        'name': name,
        'email': email,
        'message': message,
        'number': number
    }
    
    # Insert feedback into the MongoDB collection
    db.feedback.insert_one(feedback)
    
    return redirect('/success')

@app.route('/success')
def show_success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
