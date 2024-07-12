from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask (__name__)

#setting a secret key to prevent modifying cookies, cross-siterequests and forgery attacks
app.config['SECRET_KEY']='0346d7a54607eab673efb17f6eab633fc3c8cafcc2d53cec5ae80379947e0482'
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

@app.route("/register")
def register ():
    form=RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login ():
    form=LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__== '__main__':
    app.run(debug=True)

