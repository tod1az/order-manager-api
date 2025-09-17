from models.db import db

class Design(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     description = db.Column(db.String(255), nullable=False)
     price = db.Column(db.Integer,nullable=False)
 
