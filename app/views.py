from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Carlos'}  # fake user
    posts = [  # fake array of posts
        { 'author': {'nickname': 'John'}, 
            'body': 'It\'s a beautiful day!' },
        { 'author': {'nickname': 'Susan'}, 
            'body': 'It\'s okay I guess.' }
    ]
    return render_template("index.html",
                           title = 'Victor',
                           user = user,
                           posts = posts)
