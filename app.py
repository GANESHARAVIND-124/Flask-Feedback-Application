import os
from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo  # type: ignore

app = Flask(__name__)

# Set up MongoDB
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', 'mongodb://mongo:27017/my_flask_app_db')
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('feedback_form.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    number = request.form['number']
# /
    feedback = {
        'name': name,
        'email': email,
        'message': message,
        'number': number
    }
    
    mongo.db.feedback.insert_one(feedback)
    
    return redirect('/success')

@app.route('/success')
def show_success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
