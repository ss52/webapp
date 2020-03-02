from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sasha'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'test phrase John'
        },
        {
            'author': {'username': 'Mike'},
            'body': 'test phrase Mike'
        }
    ]
    return render_template('index.html', title="test", user=user, posts=posts)
