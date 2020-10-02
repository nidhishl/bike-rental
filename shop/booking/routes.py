from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db, bcrypt
from .models import Booking, Temp_booking
from shop.user.models import User
from shop.products.models import brands, fee
from .forms import Addbooking
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user   
from datetime import datetime
# from wtforms.fields.html5 import DateField

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def first():
    form = Addbooking(request.form)
    if 'phno' and 'modelno' in session:
        return redirect(url_for('billing'))
    else:
        if request.method == "POST":
            dates = Temp_booking(
                startTime = form.startTime.data,
                endTime = form.endTime.data
            )
            session['startTime'] = form.startTime.data
            session['endTime'] = form.endTime.data

            db.session.add(dates)
            db.session.commit()

            flash(f'Successfully stored in the database', 'success')
            return redirect(url_for('home'))
    return render_template('products/index.html', title = 'Home Page', form=form)

@app.route('/billing')
def billing():
    # print(session.get("phno"))
    a = request.args.get('modelno')
    x = User.query.get(session.get('phno'))
    d = session.get("startTime")
    c = session.get("endTime")
    z = brands.query.get(a)
    b = fee.query.get(a)
    # m = session.get("endTime")
    # print(m)
    # print (d[6])
    m=""
    n=""
    for p in range(5,7):
        m = m+d[p]
        n = n+c[p]
    p=int(n)-int(m)
    m=""
    n=""
    for p in range(0,16):
        m=m+d[p]
        n=n+c[p]
    if x and c and d:
        return render_template('booking/temp.html', title = 'Billing Page', x=x, z=z, b=b, p=p, m=m, n=n)
    else:
        # flash('StartTime and endTime are missing')        
        # if c and d:
        return redirect(url_for('login'))

