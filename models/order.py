from models.db import db
import enum
from datetime import datetime

class OrderStatus(enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Order(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     status = db.Column(db.Enum(OrderStatus), default=OrderStatus.pending)
     receipt = db.Column(db.String(255))
     created_at = db.Column(db.DateTime, default=datetime.now().timestamp(), nullable=False)
     updated_at = db.Column(db.DateTime, default=datetime.now().timestamp(), onupdate=datetime.now().timestamp(), nullable=False)
     user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     user = db.relationship('User', backref='orders')
     
     def to_dict(self):
        return{
            "id" :self.id,
            "status" :self.status,
            "receipt" :self.receipt,
            "created_at" :self.created_at,
            "user_id":self.user_id
        }

