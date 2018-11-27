from app import app

if __name__ == '__main__':
    app.secret_key = '1921'
    app.run(debug = True)