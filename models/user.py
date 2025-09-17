from models.db import db

class User(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     email = db.Column(db.String(255), nullable=False)
     role = db.Column(db.String(255), nullable=False)
     password  =db.Column(db.String(255),nullable=False)

