from datetime import datetime,timezone
from flaskblog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Post', backref='author', lazy=True)# this line defines a one-to-many relationship between the current model and the 'Post' model, indicating that an instance of the current model can be associated with multiple 'Post' instances. n this context, 'author' means that on the 'Post' model, there will be an attribute named author that refers back to the instance of the current model associated with a particular post.

    def __repr__(self):
        return f"User('{self.username}',{self.email}'. '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), unique=True, nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    title=db.Column(db.Text, unique=True, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}',{self.date_posted}')"