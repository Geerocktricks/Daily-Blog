from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - my personal blog'
    intro = 'Daily Blog'
    return render_template('index.html', title = title , intro = intro)

@app.route('/about')
def about():
    '''
    about root page that returns its data
    '''
    return render_template('about.html')