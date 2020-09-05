from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import Admin
import os

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = Admin.query.filter_by(phno = form.phno.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['phno'] = form.phno.data
            flash(f'You have successfully logged in' , 'success')
            return redirect(request.args.get('next') or url_for('billing'))
        else:
            flash('wrong password', 'danger ')
            return redirect(url_for('login'))
    return render_template('', form = form, title = 'Admin Access')

