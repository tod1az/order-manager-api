from models.db import db

class Item(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     design_id = db.Column(db.Integer, db.ForeignKey('design.id'), nullable=False)
     garment_id= db.Column(db.Integer, db.ForeignKey('garment.id'), nullable=False)
     order_id = db.Column(db.Integer, db.ForeignKey('order.id'),  nullable=False)

     design= db.relationship('Design', backref='items')
     garment= db.relationship('Garment', backref='items')
     order= db.relationship('Order', backref='items')

    


