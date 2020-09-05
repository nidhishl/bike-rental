from shop import db

class brands(db.Model):
    company = db.Column(db.String(255), nullable = False)
    model = db.Column(db.String(255), unique = True, nullable = False)
    modelno = db.Column(db.Integer, primary_key=True, nullable = False)
    image = db.Column(db.String(100), nullable = False)
    # fee = db.relationship('fee', backref = 'price')
    def __repr__(self):
        return '<Brand %r>' % self.modelno

class fee(db.Model):
    fee = db.Column(db.Integer, nullable = False)
    modelno = db.Column(db.Integer, db.ForeignKey(brands.modelno),primary_key=True, nullable = False)


db.create_all()

# create table fee(
#    ...> modelno int primary key,
#    ...> fee int
#    ...> ,
#    ...> FOREIGN KEY(modelno) REFERENCES brands(modelno)
#    ...> );