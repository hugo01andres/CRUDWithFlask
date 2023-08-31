from flask import Flask
from routes.Contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load .env file
load_dotenv('.env') 

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print('SQLALCHEMY_DATABASE_URI: ', os.environ.get('DATABASE_URL'))
migrate = Migrate(app, db)




# Register blueprint
app.register_blueprint(contacts, url_prefix='/contacts')



