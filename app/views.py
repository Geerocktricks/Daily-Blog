from flask import render_template
from app import app
from .data import Articles

Articles = Articles()

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

@app.route('/articles')
def articles():
    '''
    articles root page that returns its data
    '''
    return render_template('articles.html' , articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    '''
    articles root page that returns its data
    '''
    return render_template('article.html' , id = id)