from models.db import db
from datetime import datetime

class Order(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     status= db.Column(db.String(255), default="pending")
     receipt = db.Column(db.String(255), default="")
     created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

     user_id= db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
     user = db.relationship(
         'User',
          backref=db.backref('orders', cascade='all, delete-orphan'),
          passive_deletes=True
          )
     
     def to_dict(self):
        return{
            "id" :self.id,
            "status" :self.status,
            "receipt" :self.receipt,
            "created_at" :self.created_at,
            "items":[ item.to_dict() for item in self.items] ,
            "user": self.user.to_dict() if self.user else None
        }

