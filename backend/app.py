import flask
import flask_migrate

from flask import Flask
from flask_migrate import Migrate

# factory 
def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pink1023Heart!@localhost:5432/grocery_store'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             
    
    from utils import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    return app