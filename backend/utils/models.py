from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class OrderDetails(db.Model):
    __tablename__ =  'order_details' 
    
    order_id = db.Column(db.Integer, primary_key = True) 
    product_id = db.Column(db.Integer) 
    quantity = db.Column(db.Float) 
    total_price = db.Column(db.Float)

class Orders(db.Model):
    __tablename__ =  'orders' 
    
    order_id = db.Column(db.Integer, primary_key = True) 
    customer_name = db.Column(db.String) 
    total = db.Column(db.Float) 
    datetime = db.Column(db.DateTime)

class Products(db.Model):
    __tablename__ =  'products' 
    
    product_id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String)  
    uom_id = db.Column(db.Integer) 
    price_per_unit = db.Column(db.Float) 

class UOM(db.Model):
    __tablename__ =  'uom' 
    
    uom_id = db.Column(db.Integer, primary_key = True) 
    uom_name = db.Column(db.String) 
