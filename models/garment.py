from models.db import db
import enum

class Size(enum.Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    XXXL = "3XL"

class Garment(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     description = db.Column(db.String(255), nullable=False)
     size = db.Column(db.Enum(Size),nullable=False)
     price = db.Column(db.Integer,nullable=False)
     stock = db.Column(db.Integer,nullable=False)

