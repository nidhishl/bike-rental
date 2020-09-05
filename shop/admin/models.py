from shop import db

class Admin(db.Model):
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    phno = db.Column(db.Integer, primary_key=True, nullable=False)

    def __repr__(self):
        return '<Admin %r>' % self.phno

db.create_all()