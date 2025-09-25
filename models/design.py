from sqlalchemy import ARRAY
from models.db import db

class Design(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     name = db.Column(db.String(255), nullable=False)
     images= db.Column(ARRAY(db.String),nullable=True, default=[])
     price = db.Column(db.Integer,nullable=False)

     def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "images":self.images
        }

 
