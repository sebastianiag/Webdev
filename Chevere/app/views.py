from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.login import LoginManager
from app import app, db, lm, auth
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN



@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    
@app.route('/', methods = ['GET','POST'])
def signup():
    username =  request.form['username']
    password =  request.form['password']
    email = request.form['email']
    if username is None or password is None or email is None:
        abort(400) #missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) #existing user
    user = User(username = username, email = email)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))
    
@app.route('/home')
@login_required
def home():
    user = g.user
    return render_template('home.html',
        user = user)    
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    username =  request.form['username']
    password =  request.form['password']
    user = User.query.filter_by(username = username).first()
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    if not user:
        return redirect(url_for('home'))
    else if user.verify_password(password):
        login_user(user, remember = remember_me)
        return redirect(request.args.get('next') or url_for('home'))
    else:
        return redirect(url_for('login'))
        
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user =  User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User' + nickname + ' not found.')
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]

    return render_template('user.html', user= user, posts=posts)
