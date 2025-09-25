from models.db import db
import enum
from datetime import datetime

class OrderStatus(enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    sent = "sent"  

class Order(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     status = db.Column(db.Enum(OrderStatus), default=OrderStatus.pending)
     receipt = db.Column(db.String(255), default="")
     created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

     user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     user = db.relationship('User', backref='orders')
     
     def to_dict(self):
        return{
            "id" :self.id,
            "status" :self.status.value,
            "receipt" :self.receipt,
            "created_at" :self.created_at,
            "user_id":self.user_id,
            "items":[ item.to_dict() for item in self.items] 
        }

