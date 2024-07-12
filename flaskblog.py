from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy #alchemy is a ORM for .py
from forms import RegistrationForm, LoginForm
app = Flask (__name__)

#setting a secret key to prevent modifying cookies, cross-siterequests and forgery attacks
app.config['SECRET_KEY']='0346d7a54607eab673efb17f6eab633fc3c8cafcc2d53cec5ae80379947e0482'#secret key above generated from python using import secrets|secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

posts= [
    {
        'author': 'Brian O',
        'title': 'Blog 1',
        'content' : 'First post content',
        'date_posted' : 'June 27 2024'
    },
    {
        'author': 'Brian O',
        'title': 'Blog 2',
        'content' : 'First post content',
        'date_posted' : 'June 27 2024'
    },
]
@app.route("/")
def home ():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about ():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register ():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'sucesss')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login ():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash(f"You have been logged in!", 'sucess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check your username and password','danger')
    return render_template('login.html', title='Login', form=form)

if __name__== '__main__':
    app.run(debug=True)

