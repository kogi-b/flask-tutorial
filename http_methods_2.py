from flask import Flask

app = Flask(__name__)

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

def do_the_login():
    return "this is from do_the_login, **htttp_methods_2**"

def show_the_login_form():
    return "this is from show the login form, **htttp_methods_2**"