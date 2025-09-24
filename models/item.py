from models.db import db

class Item(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     design_id = db.Column(db.Integer, db.ForeignKey('design.id'), nullable=False)
     garment_variant_id= db.Column(db.Integer, db.ForeignKey('garment_variant.id'), nullable=False)
     order_id = db.Column(db.Integer, db.ForeignKey('order.id'),  nullable=False)

     design= db.relationship('Design', backref='items')
     garment_variant= db.relationship('GarmentVariant', backref='items')
     order= db.relationship('Order', backref='items')
     
     def to_dict(self):
        return{
            "id" : self.id,
            "design_id" :self.design_id,
            "garment_variant_id":self.garment_variant_id ,
            "order_id" : self.order_id
        }



    


