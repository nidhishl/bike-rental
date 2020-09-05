from shop import db
from datetime import datetime

class Booking(db.Model):
    startTime = db.Column(db.Date, nullable=False)
    endTime = db.Column(db.Date, nullable=False)
    pickup = db.Column(db.String)
    phno = db.Column(db.Integer, db.ForeignKey('user.phno'), primary_key=True)
    modelno = db.Column(db.Integer, db.ForeignKey('brands.modelno'), primary_key=True) 

class Temp_booking(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    startTime = db.Column(db.Date, nullable=False)
    endTime = db.Column(db.Date, nullable=False)


db.create_all()