from . import db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title= db.Column(db.String(255), nullable=False)
    done= db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done
        }

    __all__=["Task"] 
