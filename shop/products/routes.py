from flask import render_template, session, request, redirect, flash, url_for
from shop import app, db, photos
from .models import brands, fee
from .forms import Addmodel
from shop.user.models import User
from flask_bootstrap import Bootstrap
from datetime import datetime
import sqlite3
import os, secrets


# @app.route('/addbrand', methods = ['GET', 'POST'])
# def addbrand():
#     if request.method == "POST":
#         getBrand = request.form.get('company')
#         company = brands(company = getBrand)
#         flash(f'{getBrand} is added successfully', 'success')
#         return redirect(url_for('addbrand'))


#     return render_template('products/addbrand.html', title = "Add brand")


@app.route('/home')
def home():
    # sql = "SELECT \
    # * from brands \
    # inner join fee on brands.modelno = fee.modelno"
    z = User.query.get(session.get('phno'))
    y = fee.query.all()
    x = brands.query.all()
    return render_template('products/home.html', title = 'Homepage', models = x, fee = y, z=z)

@app.route('/addmodel', methods = ['GET', 'POST'])
def addmodel():
    form = Addmodel(request.form)
    brand = brands.query.all()
    if request.method == 'POST':
        data = brands(
            company = form.company.data,
            model = form.model.data,
            modelno = form.modelno.data,
            image = photos.save(request.files.get('image'), name = secrets.token_hex(10) + ".")
            # image = form.image.data
        )
        data1 = fee(
            modelno = form.modelno.data,
            fee = form.price.data
        )
        db.session.add(data)
        db.session.add(data1)
        db.session.commit()

        flash(f'Data is successfully added to the database', 'success')        
    return render_template('products/addmodel.html', title = 'Add model', form = form)

