# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    category = db.Column(db.String(50))

def __init__(self, name, price, description=None, image=None, category=None):
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.category = category

