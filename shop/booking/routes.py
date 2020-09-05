from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db, bcrypt
from .models import Booking, Temp_booking
from shop.user.models import User
from shop.products.models import brands
from .forms import Addbooking
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user   
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
    if request.method == "POST":
        dates = Temp_booking(
            startTime = form.startTime.data,
            endTime = form.endTime.data
        )
        
        db.session.add(dates)
        db.session.commit()

        flash(f'Successfully stored in the database', 'success')
        return redirect(url_for('home'))
    return render_template('products/index.html', title = 'Home Page', form=form)

@app.route('/billing')
def billing():
    # print(session.get("phno"))
    a = request.args.get('modelno')
    # print(a)
    x = User.query.get(session.get('phno'))
    y = Temp_booking.query.all()
    z = brands.query.get(a)
    return render_template('booking/billing.html', title = 'Billing Page', x=x, y=y, z=z, a=a)