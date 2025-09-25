from models.db import db

class GarmentVariant(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     size = db.Column(db.String(255),nullable=False)
     price = db.Column(db.Integer,nullable=False)
     stock = db.Column(db.Integer,nullable=False)

     garment_id= db.Column(db.Integer, db.ForeignKey('garment.id', ondelete = "CASCADE"), nullable=False )
     garment = db.relationship('Garment', backref='garment_variants')
 

     def to_dict(self):
        return{
            "id":self.id,
            "price":self.price ,
            "size":self.size,
            "stock":self.stock,
            "garment_id":self.garment_id
        }

