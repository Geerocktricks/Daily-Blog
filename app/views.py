from flask import render_template,Flask , flash , redirect, url_for ,request, session , logging
from app import app
from .data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

Articles = Articles()

# config MySQL
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = '1921'
app.config['MySQL_DB'] = 'DailyBlog'
app.config['MySQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

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

# ________________________**____________Validation_________**_____________________________

class RegisterForm(Form):
    name = StringField('Name' , [validators.Length(min=1, max=50)])
    username = StringField('Username' , [validators.Length(min = 4 ,max = 25)])
    email = StringField('Email' , [validators.Length(min = 6, max = 50)])
    password = PasswordField('password' , [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register' , methods = ['GET' , 'POST'])
def register():
    '''
    Register root page for registration
    '''
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, username, password)VALUES(%s,%s,%s,%s)", (name , email, username, password))

        #  commit to DB
        mysql.connection.commit()

        #  close connection
        cur.close()

        flash('Succesfully Registered!!' , 'success')
        return redirect(url_for('login'))
    return render_template('register.html' , form = form)

#user login
@app.route('/login', methods = ['GET' , 'POST'])
def login():
    '''
    Login root page for registration
    '''
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password_candidate = request.form['password']

    #     cur = mysql.connection.cursor()

    #     result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

    #     if result > 0:
    #         data = cur.fetchone()
    #         password = data['password']

    #         if sha256_crypt.verify(password_candidate, password):
    #             session['logged_in'] = True
    #             session['username'] = username

    #             flash('You are now logged in', 'success')
    #             return redirect(url_for('dashboard'))
    #         else:
    #             error = 'Invalid Login'
    #             return render_template( 'login.html' , error = error )
    #     else:
    #         error = 'usernanme not found'
    #         return render_template( 'login.html' , error = error )
        
    #     cur.close()
    return render_template( 'login.html' )

    

# logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out ', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard') 
def dashboard():
    return render_template('dashboard.html')

# app.secret_key = '1921'