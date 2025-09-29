from models.db import db

class Item(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     quantity= db.Column(db.Integer,nullable=False)
     unit_price= db.Column(db.Integer,nullable=False)
     design_id = db.Column(db.Integer, db.ForeignKey('design.id', ondelete = "CASCADE"), nullable=False)
     garment_variant_id= db.Column(db.Integer, db.ForeignKey('garment_variant.id', ondelete = "CASCADE"), nullable=False)
     order_id = db.Column(db.Integer, db.ForeignKey('order.id', ondelete= "CASCADE"),  nullable=False)

     design= db.relationship('Design', backref='items')
     garment_variant= db.relationship('GarmentVariant', backref='items')
     order= db.relationship(
         'Order',
         backref=db.backref('items', cascade='all, delete-orphan'),
         passive_deletes=True
         )
     
     def to_dict(self):
        return{
            "id" : self.id,
            "design_id" :self.design_id,
            "garment_variant_id":self.garment_variant_id ,
            "order_id" : self.order_id,
            "quantity":self.quantity,
            "unit_price":self.unit_price
        }



    


