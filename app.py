from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField
from wtforms.validators import input_required, email, length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user   
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Code/flask/project_v2/test.db'
db = SQLAlchemy(app)
Bootstrap(app)

class usr(UserMixin, db.Model):
    name = db.Column(db.String(255))
    phno = db.Column(db.Integer, primary_key=True)
    licenseNo = db.Column(db.String(10))
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    licenseNo = db.Column(db.String(10), unique=True, nullable=False)
    phno = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    profile = db.Column(db.String(180), unique=False, nullable=False, default = 'profile.jpg')

    # name VARCHAR(255),
    # phno INT,
    # licenseNo VARCHAR(255),
    # PRIMARY key(phno)

class booking(UserMixin, db.Model):
    startTime = db.Column(db.DateTime, default=datetime.utcnow)
    endTime = db.Column(db.DateTime)
    d = db.Column(db.Date, primary_key=True)
    pickup = db.Column(db.String)
    phno = db.Column(db.Integer, db.ForeignKey('usr.phno'), primary_key=True)
    modelno = db.Column(db.Integer, db.ForeignKey('brands.modelno'), primary_key=True) 
    # startTime DATETIME,
    # endTime DATETIME,                 db.ForeignKey('')
    # d DATE,
    # pickup VARCHAR(255),
    # phno int,
    # modelno VARCHAR(3),
    # PRIMARY key (d, modelno, phno),
    # foreign key (phno) REFERENCES usr(phno),
    # FOREIGN key (modelno) REFERENCES brands(modelno)

class brands(UserMixin, db.Model):
    company = db.Column(db.String(255))
    model = db.Column(db.String(255))
    modelno = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(255), nullable = False)
    model = db.Column(db.String(255), unique = True, nullable = False)
    modelno = db.Column(db.Integer, primary_key=True, nullable = False)
    image = db.Column(db.String(100), nullable = False)

    # company VARCHAR(255),
    # model VARCHAR(255),
    # modelno VARCHAR (3),
    # PRIMARY key (modelno)


class riderInfo(UserMixin, db.Model):
    totaltrips = db.Column(db.Integer)
    totalFee = db.Column(db.Integer)
    phno = db.Column(db.Integer, db.ForeignKey('usr.phno'),  primary_key = True)
    # totalTrips int,
    # totalFee int,
    # phno int,
    # FOREIGN key (phno) REFERENCES usr(phno)

class payments(UserMixin, db.Model):
    phno = db.Column(db.Integer, db.ForeignKey('usr.phno'), primary_key = True)
    pay = db.Column(db.Float)
    # phno int,
    # pay VARCHAR(6),
    # primary key (phno),
    # FOREIGN key (phno) REFERENCES usr(phno)

class fee(UserMixin, db.Model):
    modelno = db.Column(db.Integer, db.ForeignKey('brands.modelno'), primary_key = True)
    fee = db.Column(db.Integer)
    # modelno VARCHAR(255),
    # fee int,  -- hourly fee 
    # primary KEY (modelno),
    # FOREIGN KEY (modelno) REFERENCES brands (modelno)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

# @app.route('/signup')
# def signup():


# @app.route('/homepage')
# def homepage():

# @app.route('/payment')
# def payment():

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)