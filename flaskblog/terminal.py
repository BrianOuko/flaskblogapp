#python code used on the terminal -starting from database init onwards
#changing the structure to packages
python3
>>> from flaskblog.models import User, Post
>>> from flaskblog import app, db
>>> app.app_context().push()
>>> db.create_all()
>>> User.query.all()

pip install flask-bcrypt

>>> python3
>>> from flask_bcrypt import Bcrypt
>>> bycrypt_pw=Bcrypt()
>>> bycrypt_pw.generate_password_hash('testing') #result =b'$2b$12$r7ultaMlmzmcPF4LVWnzduSxo9U3nljQDE1tYm47u6jhKpOhun8je'
>>> bycrypt_pw.generate_password_hash('testing').decode('utf-8')# result='$2b$12$DpqSj7YXcKTg0P89e0j9cepZafKqNQjYLhDF6DmubWiaqsf.1BoW2'

>>> hashed_pw=bycrypt_pw.generate_password_hash('testing').decode('utf-8')# save hashed pw as a variable
>>> bycrypt_pw.check_password_hash(hashed_pw, 'colour')
False
>>> bycrypt_pw.check_password_hash(hashed_pw, 'testing')
True
>>> 

#Checking out our db
# user is first added to the db using register function on routes
#def register ():
    #form=RegistrationForm()
    #if form.validate_on_submit():
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()

#on the terminal..
>>> from flaskblog import app, db
>>> app.app_context().push()
>>> from flaskblog.models import User, Post
>>> user=User.query.first()
>>> post=Post.query.first()
>>>db.create_all()
>>> user
User('briano',briano@hotmail.com'. 'default.jpg')
>>> user.password
'$2b$12$QonMK26ZmE1uwjLYKjJ5FOIi2Ax2B1qk/MBQ4XoWE2d6Q4B4SCwOO'

#to prevent adding the same user twice import and use ValidationError and validate_field fn from wtf forms on forms.py

#to create a login system after the registration system use the Flask login extension to manager user sessions
#on the terminal..
>>> pip install flask-login

#to restrict access to specific routescdap