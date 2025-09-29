from sqlalchemy import ARRAY
from models.db import db

class Design(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     name = db.Column(db.String(255), nullable=False)
     images= db.Column(ARRAY(db.String),nullable=True, default=[])
     description= db.Column(db.Text)
     features= db.Column(ARRAY(db.Text),nullable=True, default=[])
     price = db.Column(db.Integer,nullable=False)

     def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "description":self.description,
            "price":self.price,
            "images":self.images,
            "features":self.features
        }
     def to_dict_for_item(self):
      return{
         "images":self.images,
         "name":self.name,
      }

 
