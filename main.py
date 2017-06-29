from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    if len(username) < 3 or len(username) > 20:
        username_error = "Invalid username. Username must be 3-20 characters."
        return render_template('index.html', username_error=username_error)
    if username == '':
        username_error = "Please enter a username."
        return render_template('index.html', username_error=username_error)

    if len(password) < 3 or len(password) > 20:
        password_error = "Invalid password. Password must be 3-20 characters."
        return render_template('index.html', password_error=password_error)
    if password == '':
        password_error = "Please enter a password."
        return render_template('index.html', password_error=password_error)

    if password != verify:
        verify_error = "Passwords do not match."
        return render_template('index.html', verify_error=verify_error)

    if email == '':
        pass
    else:
        if len(email) < 3 or len(email) > 20:
            email_error = "Please enter a valid email."
            return render_template('index.html', email_error=email_error)
        if '@' and '.' not in email:
            email_error = "Please enter a valid email."
            return render_template('index.html', email_error=email_error)

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)

    return render_template('index.html', username=username, password=password, verify=verify, email=email)

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

app.run()
