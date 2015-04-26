from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.login import LoginManager
from app import app, lm
from app.database import db_session
from forms import RegistrationForm, LoginForm, UploadForm
from models import User, ROLE_USER, ROLE_ADMIN

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/', methods = ['GET', 'POST'])
@app.route('/start', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        if User.query.filter(User.username == form.username.data).first():
            flash("user already registered!")
            return redirect(url_for('login'))
        user = User(username=form.username.data, email=form.email.data)
        user.hash_password(form.password.data)
        db_session.add(user)
        db_session.commit()
        flash("user added")
        return redirect(url_for('login'))
    else:
        flash("Nothing")
        return render_template('registration.html', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.username == form.username.data).first()
        if user is None:
            return redirect(url_for('register'))
        
        if user.verify_password(form.password.data):
            flash("Login successful!")
            session['remember_me'] = form.remember_me.data
            login_user(user)
            return redirect(request.args.get("next") or url_for('home', username = g.user.username))
        
        else:
            return redirect(url_for('login', form=form))
        
        
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')
    
@app.route('/home/<username>')
@login_required
def home(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('register'))
    else:
        return render_template('user.html', user=user)

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if request.method == 'POST' and form.validate():
        g.user.avatar = form.uri.data
        db_session.add(g.user.avatar)
        db_session.commit()
        return redirect(url_for("home", username=g.user.username))
    return render_template("upload.html", form=form, user=g.user)
    
