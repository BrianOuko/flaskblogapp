#python code used on the terminal
#changing the structure to packages
python3
from flaskblog.models import User, Post
from flaskblog import app, db
app.app_context().push()
db.create_all()
User.query.all()