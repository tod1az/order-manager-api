from models.db import db

class Garment(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     name = db.Column(db.String(255), nullable=False)

     def to_dict(self):
        return{
            "id":self.id,
            "name":self.name,
       }

