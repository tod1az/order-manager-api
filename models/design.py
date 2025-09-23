from models.db import db

class Design(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     name = db.Column(db.String(255), nullable=False)
     image= db.Column(db.String(255), nullable=False)
     price = db.Column(db.Integer,nullable=False)

     def to_dict(self):
        return {
            "id":self.id,
            "description":self.name,
            "price":self.price
        }

 
