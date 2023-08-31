from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv('.env')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')

# Initialize SQLAlchemy instance
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)






# Register blueprint
from routes.Contacts import contacts
app.register_blueprint(contacts, url_prefix='/contacts')



