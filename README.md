# Flask-Feedback-Application

This is a simple Flask application that allows users to submit feedback. The application uses MongoDB as the database to store the feedback data and is Dockerized for easy setup and deployment.

## Features

- **Feedback Form**: Users can submit their feedback through a simple form with fields for name, email, message, and phone number.
- **Admin Interface**: An admin interface allows administrators to view and manage feedback submissions.
- **MongoDB Integration**: Feedback data is stored in a MongoDB database.
- **Dockerized Setup**: The application can be easily set up and run using Docker and Docker Compose.

## Requirements

- Docker
- Docker Compose

## Setup

### Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Environment Variables

Create a .env file in the project root with the following content:

env

SQLALCHEMY_DATABASE_URI=mongodb://myuser:mypassword@db:27017/my_flask_app_db
FLASK_APP=app.py
FLASK_ENV=development

Docker Setup

Ensure Docker and Docker Compose are installed on your system. Use the provided docker-compose.yml file to set up the services.
Running the Application

Start the application using Docker Compose:

bash

docker-compose up --build

The application will be accessible at http://localhost:5000.
Accessing MongoDB

You can access MongoDB using MongoDB Compass or the MongoDB shell.

    MongoDB Compass: Connect using the connection string mongodb://localhost:27017.

    MongoDB Shell: Use the following command:

    bash

    docker exec -it your-repo-name_db_1 mongo

Admin Interface

The admin interface is available at http://localhost:5000/admin.

Screenshots

Feedback Form
![Screenshot from 2024-06-14 12-12-12](https://github.com/GANESHARAVIND-124/PFlask-Feedback-Application/assets/70093284/16dfa8ec-e779-480f-9ca0-423c5133e532)

Success Page

![Screenshot from 2024-06-14 12-12-50](https://github.com/GANESHARAVIND-124/PFlask-Feedback-Application/assets/70093284/d14800c4-3b90-467b-ab6d-26b7d42ad032)

Admin Interface

License

This project is licensed under the MIT License. See the LICENSE file for details.
Feedback

If you have any questions or suggestions, please feel free to open an issue or submit a pull request.

Happy coding!

'''bash


### Commit your changes and push them to GitHub:


git add .
git commit -m "Add README and images"
git push origin main


### Feedback

If you have any questions or suggestions, please feel free to open an issue or submit a pull request.

Happy coding!
