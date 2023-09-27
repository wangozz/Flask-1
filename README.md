
# Flask Pizza Restaurant App

This is a simple Flask web application for managing a pizza restaurant. It allows you to add restaurants, pizzas, and associate pizzas with restaurants.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need the following software installed on your system to run this project:

- Python 3
- Flask
- Flask-SQLAlchemy
- Faker (for generating fake data)
- [Add any other dependencies]

### Installing

1. Clone the repository to your local machine:

```bash
git clone https://github.com/wangozz/Flask-1
Set up a virtual environment and activate it:

bash

cd Flask-Pizza-Restaurant
python3 -m venv env
source env/bin/activate
Install the required dependencies:

bash

pip install -r requirements.txt
Set up the database:

bash

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Running the Application
To run the application, use the following command:

bash


python app.py
The app will be accessible at http://localhost:5000.

Usage
Navigate to the home page to view a list of restaurants.
Click on a restaurant to view its details, including associated pizzas.
Similarly, you can view pizza details.
Seeding Data
If you want to populate the database with some initial data, you can run the seed.py script:

bash

python seed.py
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Faker for providing fake data for testing.
Flask for the web framework.
SQLAlchemy for database management


