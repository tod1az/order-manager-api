from models.db import db

class Garment(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     name = db.Column(db.String(255), nullable=False)
     price = db.Column(db.Integer,nullable=False)

     def to_dict(self):
        return{
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "variants":[v.to_dict() for v in self.garment_variants]
       }

     def to_dict_for_item(self):
         return{
          "name":self.name
      }

