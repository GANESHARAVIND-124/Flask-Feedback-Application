# Flask-Feedback-Application

# Flask Feedback Application

This is a simple Flask application that allows users to submit feedback. The application uses MongoDB as the database to store the feedback data. 

## Features

- Feedback form with fields for name, email, message, and number.
- Admin interface to view feedback entries.
- Data stored in MongoDB.

## Requirements

- Python 3.8+
- Docker
- Docker Compose

## Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install Dependencies

You can use pip to install the necessary dependencies:

bash

pip install -r requirements.txt

Environment Variables

Create a .env file in the project root with the following content:

env

SQLALCHEMY_DATABASE_URI=mongodb://myuser:mypassword@db:27017/my_flask_app_db
FLASK_APP=app.py
FLASK_ENV=development

Docker Setup

Ensure Docker and Docker Compose are installed on your system. Then, you can use the provided docker-compose.yml to set up the services:

yaml

version: '3.8'

services:
  db:
    image: mongo:latest
    environment:
      MONGO_INITDB_ROOT_USERNAME: myuser
      MONGO_INITDB_ROOT_PASSWORD: mypassword
      MONGO_INITDB_DATABASE: my_flask_app_db
    volumes:
      - mongo_data:/data/db
    ports:
      - "27017:27017"

  web:
    build: .
    command: flask run --host=0.0.0.0
    volumes:
      - .:/app
    ports:
      - "5000:5000"
    environment:
      FLASK_APP: app.py
      FLASK_ENV: development
      SQLALCHEMY_DATABASE_URI: mongodb://myuser:mypassword@db:27017/my_flask_app_db
    depends_on:
      - db

volumes:
  mongo_data:

Running the Application

Start the application using Docker Compose:

bash

docker-compose up --build

The application will be accessible at http://localhost:5000.
Accessing MongoDB

You can access MongoDB using MongoDB Compass or the MongoDB shell:

bash

docker exec -it your-repo-name_db_1 mongo

Admin Interface

The admin interface is available at http://localhost:5000/admin.
Viewing Data

To view data in MongoDB, you can use the MongoDB shell or MongoDB Compass.
MongoDB Shell

bash

docker exec -it your-repo-name_db_1 mongo

Switch to your database:

shell

use my_flask_app_db

Show collections:

shell

show collections

View data in the feedback collection:

shell

db.feedback.find().pretty()

MongoDB Compass

    Download and install MongoDB Compass.
    Connect using the connection string mongodb://localhost:27017.
    Navigate to your database my_flask_app_db.
    Explore the feedback collection.

License

This project is licensed under the MIT License. See the LICENSE file for details.

python


### Feedback

If you have any questions or suggestions, please feel free to open an issue or submit a pull request.

Happy coding!
