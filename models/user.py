from models.db import db

class User(db.Model):
     id = db.Column(db.Integer, primary_key= True, autoincrement=True)
     email = db.Column(db.String(255), nullable=False)
     name = db.Column(db.String(255), nullable=False)
     role = db.Column(db.String(255), nullable=False)
     password  =db.Column(db.String(255),nullable=False)
     
     def to_dict(self):
        return{
            "id":self.id,
            "email":self.email,
            "name":self.name,
            "role":self.role,
            "password":self.password,
        }

