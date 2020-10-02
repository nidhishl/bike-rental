from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
from shop.products.models import brands
import os

# @app.route('/admin')
# def admin():
#     if 'phno' not in session:
#         return redirect(url_for('admin.login'))
#     models = brands.query.all()
#     return render_template('admin/index.html', title = 'Admin', models = models)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
            
        user = User(
            name = form.name.data, 
            licenseNo = form.licenseNo.data,
            phno = form.phno.data,
            username = form.username.data, 
            email = form.email.data,
            password = hash_password)
        db.session.add(user)
        db.session.commit()

        flash(f'Welcome {form.name.data}, Thank for registering')
        a = request.args.get('modelno')
        if a:
            return redirect(url_for('billing'))
        else:
            return redirect(url_for('home'))
    return render_template('user/register.html', form=form, title = "Registration Page")



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(phno = form.phno.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['phno'] = form.phno.data
            flash(f'You have successfully logged in' , 'success')
            a = request.args.get('modelno')
            if a:
                return redirect(request.args.get('next') or url_for('billing'))
            else:
                return redirect(request.args.get('next') or url_for('home'))


        else:
            flash('wrong password', 'danger ')
            return redirect(url_for('login'))
    return render_template('user/login.html', form = form, title = 'Login Page')

@app.route('/logout')
def logout():
    del session["phno"]
    return redirect('/home')