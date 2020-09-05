from shop import db

class User(db.Model):
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    licenseNo = db.Column(db.String(10), unique=True, nullable=False)
    phno = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False, default = 'profile.jpg')

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()