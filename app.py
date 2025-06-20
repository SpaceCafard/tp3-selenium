from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users_db = {"user": "password"}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if users_db.get(username) == password:
        return redirect(url_for('dashboard'))
    else:
        return 'Invalid credentials, please try again.'

@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'

if __name__ == '__main__':
    app.run(debug=True)
