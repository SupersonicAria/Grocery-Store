from flask import Flask

# factory 
def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:Pink1023Heart!@localhost:5432/grocery_store'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             
