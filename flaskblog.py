from flask import Flask, render_template, url_for
app = Flask (__name__)

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

if __name__== '__main__':
    app.run(debug=True)

