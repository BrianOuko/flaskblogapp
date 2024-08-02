from flask import Flask
from flask_sqlalchemy import SQLAlchemy #alchemy is an ORM for .py

app = Flask (__name__)
app.config['SECRET_KEY']='0346d7a54607eab673efb17f6eab633fc3c8cafcc2d53cec5ae80379947e0482'#secret key above generated from python using import secrets|secrets.token_hex(32).Setting a secret key to prevent modifying cookies, cross-siterequests and forgery attacks
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app) #creating a db instance

from flaskblog import routes # we import routes after initializing the app because the routes file imports the app variable itself
